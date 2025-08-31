
# To-Do List Manager — v2.0 (exceptions + JSON persistence)
# Scope: primitives, control flow, functions + robust exception handling + file operations
# Features: Bulletproof JSON persistence, backup/recovery, data validation, import/export

import json
import os
import shutil
from datetime import datetime


# ---- Global state and configuration ----
ERROR_LOG = []  # Track session errors
CONFIG = {
    "tasks_file": "tasks.json",
    "export_dir": "exports",
    "max_backups": 5,
    "auto_save": True
}

# -------------------------
# ERROR LOGGING AND SAFE INPUT FUNCTIONS
# -------------------------


def log_error(error_type, message):
    """Log errors for session statistics."""
    ERROR_LOG.append({
        "type": error_type,
        "message": message,
        "timestamp": datetime.now().isoformat()
    })


def recompute_next_id(tasks):
    """Recompute next_id to maintain monotonic sequence after imports/merges."""
    if tasks:
        return max(task.get("id", 0) for task in tasks) + 1
    return 1


def safe_get_int(prompt, min_val=1, max_val=None):
    """Get an integer with comprehensive validation."""
    while True:
        try:
            raw = input(prompt)
            value = int(raw)

            if value < min_val:
                print(f"❌ Value must be >= {min_val}")
                log_error("ValueError",
                          f"Integer below minimum: {value} < {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"❌ Value must be <= {max_val}")
                log_error("ValueError",
                          f"Integer above maximum: {value} > {max_val}")
                continue

            return value

        except ValueError:
            print("❌ Please enter a valid integer")
            log_error("ValueError", "Invalid integer input")
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Goodbye!")
            raise SystemExit(0)


def safe_get_menu_choice(min_choice=1, max_choice=9):
    """Get menu choice with comprehensive validation."""
    while True:
        try:
            choice = int(
                input(f"Choose an option ({min_choice}-{max_choice}): "))
        except ValueError:
            print("❌ Please enter a valid number")
            log_error("ValueError", "Invalid menu choice input")
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Goodbye!")
            raise SystemExit(0)
        else:
            if min_choice <= choice <= max_choice:
                return choice
            print(
                f"❌ Please choose a number between {min_choice}-{max_choice}")
            log_error("ValueError", f"Menu choice out of range: {choice}")


def safe_get_string(prompt, min_length=1, max_length=None, allow_empty=False):
    """Get a string with validation."""
    while True:
        try:
            value = input(prompt).strip()

            if not allow_empty and len(value) < min_length:
                print(f"❌ Input must be at least {min_length} characters")
                log_error("ValueError",
                          f"String too short: {len(value)} < {min_length}")
                continue
            if max_length is not None and len(value) > max_length:
                print(f"❌ Input must be at most {max_length} characters")
                log_error("ValueError",
                          f"String too long: {len(value)} > {max_length}")
                continue

            return value

        except (KeyboardInterrupt, EOFError):
            print("\n👋 Goodbye!")
            raise SystemExit(0)


# -------------------------
# JSON PERSISTENCE WITH BULLETPROOF ERROR HANDLING
# -------------------------

def validate_task_structure(task):
    """Validate that a task has the required structure."""
    required_fields = ["id", "title", "done"]

    if not isinstance(task, dict):
        return False, f"Task must be a dictionary, got {type(task)}"

    for field in required_fields:
        if field not in task:
            return False, f"Missing required field: {field}"

    # Validate field types
    if not isinstance(task["id"], int):
        return False, f"Task ID must be integer, got {type(task['id'])}"
    if not isinstance(task["title"], str):
        return False, f"Task title must be string, got {type(task['title'])}"
    if not isinstance(task["done"], bool):
        return False, f"Task done must be boolean, got {type(task['done'])}"

    # Additional validation
    if task["id"] < 1:
        return False, f"Task ID must be positive, got {task['id']}"
    if len(task["title"].strip()) == 0:
        return False, "Task title cannot be empty"

    return True, "Valid task structure"


def create_backup(filename):
    """Create a backup of the current tasks file."""
    try:
        if os.path.exists(filename):
            # Handle directory path correctly
            dir_path = os.path.dirname(filename) or "."
            base_name = os.path.basename(filename)
            backup_filename = os.path.join(
                dir_path, f"{base_name}.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}")

            shutil.copy2(filename, backup_filename)

            # Manage backup count in the same directory
            backup_pattern = f"{base_name}.backup."
            backup_files = [f for f in os.listdir(
                dir_path) if f.startswith(backup_pattern)]
            backup_files.sort()

            # Keep only the most recent backups
            max_backups = CONFIG.get("max_backups", 5)
            if len(backup_files) > max_backups:
                for old_backup in backup_files[:-max_backups]:
                    try:
                        os.remove(os.path.join(dir_path, old_backup))
                    except Exception as e:
                        log_error(
                            "BackupError", f"Failed to remove old backup {old_backup}: {e}")

            return True, f"Backup created: {backup_filename}"
        return True, "No existing file to backup"
    except Exception as e:
        log_error("BackupError", f"Backup creation failed: {e}")
        return False, f"Backup failed: {e}"


def save_tasks(tasks, filename=None):
    """Save tasks to JSON file with comprehensive error handling."""
    if filename is None:
        filename = CONFIG["tasks_file"]

    temp_filename = None
    try:
        # Validate all tasks before saving
        for i, task in enumerate(tasks):
            is_valid, message = validate_task_structure(task)
            if not is_valid:
                log_error("ValidationError", f"Task {i}: {message}")
                return False, f"Validation failed for task {i}: {message}"

        # Create backup first
        backup_success, backup_message = create_backup(filename)
        if not backup_success:
            print(f"⚠️ Warning: {backup_message}")

        # Ensure directory exists
        os.makedirs(os.path.dirname(filename) if os.path.dirname(
            filename) else ".", exist_ok=True)

        # Save to temporary file first, then replace (atomic operation)
        temp_filename = f"{filename}.tmp"
        with open(temp_filename, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)
            f.flush()
            os.fsync(f.fileno())  # Ensure bytes hit disk before replace

        # Atomic replace (cross-platform safe)
        os.replace(temp_filename, filename)

        # Fsync parent directory for durability (best-effort on POSIX)
        try:
            dir_fd = os.open(os.path.dirname(filename) or ".", os.O_DIRECTORY)
            try:
                os.fsync(dir_fd)
            finally:
                os.close(dir_fd)
        except Exception:
            pass  # Not supported on some platforms (Windows), safe to ignore

        print(f"✅ Saved {len(tasks)} tasks to {filename}")
        return True, f"Successfully saved {len(tasks)} tasks"

    except PermissionError:
        log_error("PermissionError", f"Cannot write to {filename}")
        return False, f"Permission denied writing to {filename}"
    except OSError as e:
        log_error("OSError", f"File system error saving tasks: {e}")
        return False, f"File system error: {e}"
    except Exception as e:
        log_error("SaveError", f"Unexpected error saving tasks: {e}")
        return False, f"Unexpected error: {e}"
    finally:
        # Clean up temporary file if it exists
        try:
            if temp_filename and os.path.exists(temp_filename):
                os.remove(temp_filename)
        except Exception as cleanup_err:
            log_error("SaveCleanupError",
                      f"Temp cleanup failed: {cleanup_err}")


def load_tasks(filename=None):
    """Load tasks from JSON file with error recovery."""
    if filename is None:
        filename = CONFIG["tasks_file"]

    try:
        with open(filename, "r", encoding="utf-8") as f:
            loaded_tasks = json.load(f)

        # Validate file format
        if not isinstance(loaded_tasks, list):
            log_error("ValidationError", "Tasks file must contain a list")

            # Try to recover from backup
            backup_tasks, backup_message = try_recover_from_backup(filename)
            if backup_tasks:
                # Normalize by persisting recovered data to replace corrupted file
                save_success, save_message = save_tasks(backup_tasks, filename)
                if save_success:
                    print(f"💾 Normalized recovered data to {filename}")
                return backup_tasks, f"Recovered from backup: {backup_message}"

            return [], "Tasks file format invalid, starting fresh"

        # Validate and clean tasks
        valid_tasks = []
        for i, task in enumerate(loaded_tasks):
            is_valid, message = validate_task_structure(task)
            if is_valid:
                valid_tasks.append(task)
            else:
                log_error("ValidationError",
                          f"Skipping invalid task {i}: {message}")

        print(f"✅ Loaded {len(valid_tasks)} tasks from {filename}")
        if len(valid_tasks) != len(loaded_tasks):
            skipped = len(loaded_tasks) - len(valid_tasks)
            print(f"⚠️ Skipped {skipped} invalid tasks")

        return valid_tasks, f"Successfully loaded {len(valid_tasks)} tasks"

    except FileNotFoundError:
        print(f"⚠️ Tasks file {filename} not found, starting fresh")
        log_error("FileNotFoundError", f"Tasks file not found: {filename}")
        return [], "No saved tasks found, starting fresh"
    except json.JSONDecodeError as e:
        print(f"❌ Tasks file corrupted: {e}")
        log_error("JSONDecodeError", f"Corrupted tasks file: {e}")

        # Try to recover from backup
        backup_tasks, backup_message = try_recover_from_backup(filename)
        if backup_tasks:
            # Normalize by persisting recovered data to replace corrupted file
            save_success, save_message = save_tasks(backup_tasks, filename)
            if save_success:
                print(f"💾 Normalized recovered data to {filename}")
            return backup_tasks, f"Recovered from backup: {backup_message}"

        return [], "Tasks file corrupted, starting fresh"
    except PermissionError:
        log_error("PermissionError", f"Cannot read {filename}")
        return [], f"Permission denied reading {filename}"
    except Exception as e:
        log_error("LoadError", f"Unexpected error loading tasks: {e}")
        return [], f"Unexpected error: {e}, starting fresh"


def try_recover_from_backup(filename):
    """Try to recover tasks from backup files."""
    try:
        # Handle directory path correctly
        dir_path = os.path.dirname(filename) or "."

        if not os.path.isdir(dir_path):
            return [], "No backup directory found"

        base_name = os.path.basename(filename)
        backup_pattern = f"{base_name}.backup."
        backup_files = [f for f in os.listdir(
            dir_path) if f.startswith(backup_pattern)]

        if not backup_files:
            return [], "No backup files found"

        # Try the most recent backup
        backup_files.sort(reverse=True)
        for backup_file in backup_files:
            try:
                backup_path = os.path.join(dir_path, backup_file)
                with open(backup_path, "r", encoding="utf-8") as f:
                    backup_tasks = json.load(f)

                if isinstance(backup_tasks, list):
                    # Validate each recovered task
                    valid_tasks = []
                    for i, task in enumerate(backup_tasks):
                        is_valid, message = validate_task_structure(task)
                        if is_valid:
                            valid_tasks.append(task)
                        else:
                            log_error(
                                "RecoveryError", f"Invalid task in backup {backup_file} idx {i}: {message}")

                    if valid_tasks:
                        print(
                            f"✅ Recovered {len(valid_tasks)} tasks from {backup_file}")
                        return valid_tasks, f"Recovered from {backup_file}"
                    else:
                        log_error(
                            "RecoveryError", f"No valid tasks found in backup {backup_file}")
                        continue
            except Exception as e:
                log_error("RecoveryError",
                          f"Failed to recover from {backup_file}: {e}")
                continue

        return [], "All backup files corrupted or invalid"
    except Exception as e:
        log_error("RecoveryError", f"Backup recovery failed: {e}")
        return [], f"Recovery failed: {e}"


# -------------------------
# CLI INTERFACE
# -------------------------

def display_menu():
    """Display enhanced menu with persistence operations."""
    print("\n" + "=" * 60)
    print("📝 To-Do List Manager v2.0 - Bulletproof Edition 🛡️")
    print("=" * 60)
    print("1) Add task")
    print("2) List tasks")
    print("3) Toggle done by ID")
    print("4) Delete by ID")
    print("5) Clear all tasks")
    print("6) Save/Load operations")
    print("7) Import/Export")
    print("8) Statistics & Recovery")
    print("9) Quit")
    print("=" * 60)


def display_save_load_menu():
    """Display save/load operations menu."""
    print("\n💾 Save/Load Operations:")
    print("1) Save tasks now")
    print("2) Load tasks from file")
    print("3) Auto-save toggle")
    print("4) Back to main menu")

    return safe_get_menu_choice(1, 4)


def display_import_export_menu():
    """Display import/export operations menu."""
    print("\n📤 Import/Export Operations:")
    print("1) Export tasks to file")
    print("2) Import tasks from file")
    print("3) Export completed tasks only")
    print("4) Export pending tasks only")
    print("5) Back to main menu")

    return safe_get_menu_choice(1, 5)


def display_statistics():
    """Display comprehensive session statistics."""
    print("\n📊 Session Statistics:")
    print(f"Total errors logged: {len(ERROR_LOG)}")

    if ERROR_LOG:
        print("\n❌ Error Summary:")
        error_types = {}
        for error in ERROR_LOG:
            error_type = error["type"]
            error_types[error_type] = error_types.get(error_type, 0) + 1

        for error_type, count in error_types.items():
            print(f"  {error_type}: {count} occurrence(s)")

        print("\n📝 Recent Errors (last 3):")
        for error in ERROR_LOG[-3:]:
            timestamp = error.get("timestamp", "unknown")[:19]
            print(f"  {timestamp} | {error['type']}: {error['message']}")
    else:
        print("🎉 No errors recorded this session!")


def export_tasks(tasks, filename=None, filter_func=None):
    """Export tasks to file with optional filtering."""
    try:
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"tasks_export_{timestamp}.json"

        # Apply filter if provided
        if filter_func:
            filtered_tasks = [task for task in tasks if filter_func(task)]
        else:
            filtered_tasks = tasks

        # Ensure export directory exists
        export_dir = CONFIG.get("export_dir", "exports")
        os.makedirs(export_dir, exist_ok=True)

        export_path = os.path.join(export_dir, filename)

        with open(export_path, "w", encoding="utf-8") as f:
            json.dump(filtered_tasks, f, indent=2, ensure_ascii=False)

        print(f"✅ Exported {len(filtered_tasks)} tasks to {export_path}")
        return True, f"Successfully exported {len(filtered_tasks)} tasks"

    except Exception as e:
        log_error("ExportError", f"Export failed: {e}")
        return False, f"Export failed: {e}"


def import_tasks(filename):
    """Import tasks from file with validation."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            imported_tasks = json.load(f)

        # Validate file format
        if not isinstance(imported_tasks, list):
            log_error("ImportError", "Import file must contain a list of tasks")
            return [], "Import file format invalid"

        # Validate and clean imported tasks
        valid_tasks = []
        for i, task in enumerate(imported_tasks):
            is_valid, message = validate_task_structure(task)
            if is_valid:
                valid_tasks.append(task)
            else:
                log_error("ImportError",
                          f"Skipping invalid task {i}: {message}")

        print(f"✅ Imported {len(valid_tasks)} valid tasks from {filename}")
        if len(valid_tasks) != len(imported_tasks):
            skipped = len(imported_tasks) - len(valid_tasks)
            print(f"⚠️ Skipped {skipped} invalid tasks")

        return valid_tasks, f"Successfully imported {len(valid_tasks)} tasks"

    except FileNotFoundError:
        log_error("ImportError", f"Import file not found: {filename}")
        return [], f"Import file {filename} not found"
    except IsADirectoryError:
        log_error("ImportError", f"Cannot import from directory: {filename}")
        return [], f"Cannot import from directory {filename} (need a file)"
    except json.JSONDecodeError as e:
        log_error("ImportError", f"Invalid JSON in import file: {e}")
        return [], f"Invalid JSON in import file: {e}"
    except Exception as e:
        log_error("ImportError", f"Import failed: {e}")
        return [], f"Import failed: {e}"


def add_task(tasks, next_id):
    """Add a new task with comprehensive validation."""
    try:
        title = safe_get_string("Enter your task title: ",
                                min_length=1, max_length=200)

        # Create task with validation
        task = {"id": next_id, "title": title, "done": False}
        is_valid, message = validate_task_structure(task)

        if not is_valid:
            log_error("ValidationError", f"Task validation failed: {message}")
            print(f"❌ Task validation failed: {message}")
            return next_id

        tasks.append(task)
        print(f"✅ Added task #{next_id}: {title}")

        # Auto-save if enabled
        if CONFIG.get("auto_save", True):
            save_success, save_message = save_tasks(tasks)
            if save_success:
                print("💾 autosaved")
            else:
                print(f"⚠️ Auto-save failed: {save_message}")

        return next_id + 1

    except Exception as e:
        log_error("AddTaskError", f"Failed to add task: {e}")
        print(f"❌ Failed to add task: {e}")
        return next_id


def list_tasks(tasks):
    """Display tasks with enhanced formatting and statistics."""
    if not tasks:
        print("📭 No tasks yet!")
        return

    completed = sum(1 for task in tasks if task.get("done", False))
    pending = len(tasks) - completed

    print(
        f"\n📋 Task Summary: {len(tasks)} total, {completed} completed, {pending} pending")
    print("=" * 60)

    for task in tasks:
        try:
            status = "✅" if task.get("done", False) else "⏳"
            task_id = task.get("id")
            id_str = str(task_id) if task_id is not None else "?"
            title = task.get("title", "No title")
            print(f"[{id_str:>3}] {status} {title}")
        except Exception as e:
            log_error("DisplayError", f"Error displaying task: {e}")
            print(f"[???] ❌ Error displaying task: {e}")


def toggle_by_id(tasks):
    """Toggle task completion status by ID with validation."""
    try:
        if not tasks:
            print("📭 No tasks to toggle!")
            return False

        task_id = safe_get_int("Choose a task ID to toggle: ", min_val=1)

        for task in tasks:
            if task.get("id") == task_id:
                old_status = task.get("done", False)
                task["done"] = not old_status
                status_text = "completed" if task["done"] else "pending"
                print(f"✅ Task #{task_id} marked as {status_text}")

                # Auto-save if enabled
                if CONFIG.get("auto_save", True):
                    save_success, save_message = save_tasks(tasks)
                    if save_success:
                        print("💾 autosaved")
                    else:
                        print(f"⚠️ Auto-save failed: {save_message}")

                return True

        print(f"❌ Task with ID {task_id} not found")
        log_error("TaskNotFound", f"Task ID {task_id} not found")
        return False

    except Exception as e:
        log_error("ToggleError", f"Failed to toggle task: {e}")
        print(f"❌ Failed to toggle task: {e}")
        return False


def delete_by_id(tasks):
    """Delete task by ID with confirmation and validation."""
    try:
        if not tasks:
            print("📭 No tasks to delete!")
            return False

        task_id = safe_get_int("Choose a task ID to delete: ", min_val=1)

        for i, task in enumerate(tasks):
            if task.get("id") == task_id:
                title = task.get("title", "No title")

                # Confirmation prompt
                try:
                    confirm = input(
                        f"Delete task '{title}'? (y/N): ").lower().strip()
                except (KeyboardInterrupt, EOFError):
                    print("\n👋 Goodbye!")
                    raise SystemExit(0)

                if confirm in ('y', 'yes'):
                    tasks.pop(i)
                    print(f"✅ Deleted task #{task_id}: {title}")

                    # Auto-save if enabled
                    if CONFIG.get("auto_save", True):
                        save_success, save_message = save_tasks(tasks)
                        if save_success:
                            print("💾 autosaved")
                        else:
                            print(f"⚠️ Auto-save failed: {save_message}")

                    return True
                else:
                    print("❌ Delete cancelled")
                    return False

        print(f"❌ Task with ID {task_id} not found")
        log_error("TaskNotFound", f"Task ID {task_id} not found")
        return False

    except Exception as e:
        log_error("DeleteError", f"Failed to delete task: {e}")
        print(f"❌ Failed to delete task: {e}")
        return False


def clear_all(tasks):
    """Clear all tasks with confirmation and backup."""
    try:
        if not tasks:
            print("📭 No tasks to clear!")
            return False

        count = len(tasks)

        # Confirmation prompt
        try:
            confirm = input(
                f"Clear all {count} tasks? This cannot be undone! (y/N): ").lower().strip()
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Goodbye!")
            raise SystemExit(0)

        if confirm in ('y', 'yes'):
            # Create backup before clearing
            backup_success, backup_message = create_backup(
                CONFIG["tasks_file"])
            if backup_success:
                print(f"💾 {backup_message}")

            tasks.clear()
            print(f"✅ Cleared {count} tasks")

            # Auto-save if enabled
            if CONFIG.get("auto_save", True):
                save_success, save_message = save_tasks(tasks)
                if save_success:
                    print("💾 autosaved")
                else:
                    print(f"⚠️ Auto-save failed: {save_message}")

            return True
        else:
            print("❌ Clear cancelled")
            return False

    except Exception as e:
        log_error("ClearError", f"Failed to clear tasks: {e}")
        print(f"❌ Failed to clear tasks: {e}")
        return False


def run_todo_manager():
    """Main application loop with bulletproof exception handling."""
    # Welcome banner and initialization
    print("🎉 Welcome to To-Do List Manager v2.0!")
    print("🛡️ Now with bulletproof JSON persistence and comprehensive error handling!")
    print("📝 All your tasks are automatically saved and backed up!")

    # Initialize tasks and load from file
    tasks = []
    next_id = 1

    # Load existing tasks
    loaded_tasks, load_message = load_tasks()
    if loaded_tasks:
        tasks = loaded_tasks
        # Find the next ID
        next_id = recompute_next_id(tasks)

    try:
        while True:
            try:
                display_menu()
                choice = safe_get_menu_choice(1, 9)

                if choice == 9:  # Quit
                    print("\n👋 Thank you for using To-Do List Manager v2.0!")
                    print(
                        f"📊 Session summary: {len(tasks)} tasks, {len(ERROR_LOG)} errors handled")

                    # Offer to save before quitting
                    if tasks and not CONFIG.get("auto_save", True):
                        try:
                            save_choice = input(
                                "💾 Save tasks before quitting? (Y/n): ").lower().strip()
                        except (KeyboardInterrupt, EOFError):
                            save_choice = "y"  # Default to save on interrupt

                        if save_choice not in ('n', 'no'):
                            save_tasks(tasks)

                    print("🎯 No crashes occurred - bulletproof success! 🛡️")
                    break

                elif choice == 1:  # Add task
                    next_id = add_task(tasks, next_id)

                elif choice == 2:  # List tasks
                    list_tasks(tasks)

                elif choice == 3:  # Toggle task by ID
                    toggle_by_id(tasks)

                elif choice == 4:  # Delete task by ID
                    delete_by_id(tasks)

                elif choice == 5:  # Clear all tasks
                    clear_all(tasks)

                elif choice == 6:  # Save/Load operations
                    try:
                        save_load_choice = display_save_load_menu()

                        if save_load_choice == 1:  # Save now
                            save_success, save_message = save_tasks(tasks)
                            if save_success:
                                print(f"✅ {save_message}")
                            else:
                                print(f"❌ {save_message}")

                        elif save_load_choice == 2:  # Load from file
                            try:
                                filename = input(
                                    "Enter filename to load from (or press Enter for default): ").strip()
                                if not filename:
                                    filename = None

                                loaded_tasks, load_message = load_tasks(
                                    filename)
                                if loaded_tasks:
                                    # Ask to merge or replace
                                    if tasks:
                                        try:
                                            merge_choice = input(
                                                "Merge with current tasks? (Y/n): ").lower().strip()
                                        except (KeyboardInterrupt, EOFError):
                                            merge_choice = "y"

                                        if merge_choice not in ('n', 'no'):
                                            # Merge tasks, handling ID conflicts
                                            existing_ids = {
                                                task.get("id", 0) for task in tasks}
                                            for loaded_task in loaded_tasks:
                                                if loaded_task.get("id", 0) not in existing_ids:
                                                    tasks.append(loaded_task)
                                                else:
                                                    # Assign new ID to avoid conflicts
                                                    loaded_task["id"] = next_id
                                                    tasks.append(loaded_task)
                                                    next_id += 1
                                            print(
                                                f"✅ Merged {len(loaded_tasks)} tasks")
                                        else:
                                            tasks.clear()
                                            tasks.extend(loaded_tasks)
                                            print(
                                                f"✅ Replaced with {len(loaded_tasks)} tasks")
                                    else:
                                        tasks.extend(loaded_tasks)
                                        print(
                                            f"✅ Loaded {len(loaded_tasks)} tasks")

                                    # Update next_id
                                    next_id = recompute_next_id(tasks)
                                else:
                                    print(f"⚠️ {load_message}")

                            except (KeyboardInterrupt, EOFError):
                                print("\n👋 Goodbye!")
                                raise SystemExit(0)

                        elif save_load_choice == 3:  # Toggle auto-save
                            CONFIG["auto_save"] = not CONFIG.get(
                                "auto_save", True)
                            status = "enabled" if CONFIG["auto_save"] else "disabled"
                            print(f"✅ Auto-save {status}")

                        elif save_load_choice == 4:  # Back
                            continue

                    except Exception as e:
                        print(f"❌ Save/Load operation failed: {e}")
                        log_error("FileIOError",
                                  f"Save/Load operation failed: {e}")

                elif choice == 7:  # Import/Export
                    try:
                        import_export_choice = display_import_export_menu()

                        if import_export_choice == 1:  # Export all tasks
                            export_success, export_message = export_tasks(
                                tasks)
                            if export_success:
                                print(f"✅ {export_message}")
                            else:
                                print(f"❌ {export_message}")

                        elif import_export_choice == 2:  # Import tasks
                            try:
                                filename = input(
                                    "Enter filename to import from: ").strip()
                                if filename:
                                    imported_tasks, import_message = import_tasks(
                                        filename)
                                    if imported_tasks:
                                        # Handle ID conflicts
                                        existing_ids = {
                                            task.get("id", 0) for task in tasks}
                                        for imported_task in imported_tasks:
                                            if imported_task.get("id", 0) in existing_ids:
                                                imported_task["id"] = next_id
                                                next_id += 1

                                        tasks.extend(imported_tasks)
                                        next_id = recompute_next_id(tasks)
                                        print(
                                            f"✅ Imported {len(imported_tasks)} tasks")
                                    else:
                                        print(f"❌ {import_message}")
                                else:
                                    print("❌ Filename cannot be empty")
                            except (KeyboardInterrupt, EOFError):
                                print("\n👋 Goodbye!")
                                raise SystemExit(0)

                        elif import_export_choice == 3:  # Export completed only
                            completed_tasks = [
                                task for task in tasks if task.get("done", False)]
                            if completed_tasks:
                                export_success, export_message = export_tasks(
                                    tasks, filename="completed_tasks.json",
                                    filter_func=lambda t: t.get("done", False)
                                )
                                if export_success:
                                    print(f"✅ {export_message}")
                                else:
                                    print(f"❌ {export_message}")
                            else:
                                print("📭 No completed tasks to export")

                        elif import_export_choice == 4:  # Export pending only
                            pending_tasks = [
                                task for task in tasks if not task.get("done", False)]
                            if pending_tasks:
                                export_success, export_message = export_tasks(
                                    tasks, filename="pending_tasks.json",
                                    filter_func=lambda t: not t.get(
                                        "done", False)
                                )
                                if export_success:
                                    print(f"✅ {export_message}")
                                else:
                                    print(f"❌ {export_message}")
                            else:
                                print("📭 No pending tasks to export")

                        elif import_export_choice == 5:  # Back
                            continue

                    except Exception as e:
                        print(f"❌ Import/Export operation failed: {e}")
                        log_error("ImportExportError",
                                  f"Import/Export operation failed: {e}")

                elif choice == 8:  # Statistics & Recovery
                    try:
                        print("\n🔧 Statistics & Recovery:")
                        print("1) View session statistics")
                        print("2) List backup files")
                        print("3) Recover from backup")
                        print("4) Clear error log")
                        print("5) Back to main menu")

                        stats_choice = safe_get_menu_choice(1, 5)

                        if stats_choice == 1:  # View statistics
                            display_statistics()

                        elif stats_choice == 2:  # List backups
                            try:
                                tasks_file = CONFIG['tasks_file']
                                dir_path = os.path.dirname(tasks_file) or "."

                                if not os.path.isdir(dir_path):
                                    print("📭 No backup files found")
                                else:
                                    base_name = os.path.basename(tasks_file)
                                    backup_pattern = f"{base_name}.backup."
                                    backup_files = [f for f in os.listdir(
                                        dir_path) if f.startswith(backup_pattern)]

                                    if backup_files:
                                        backup_files.sort(reverse=True)
                                        print(
                                            f"\n💾 Available backups ({len(backup_files)}):")
                                        for i, backup_file in enumerate(backup_files, 1):
                                            print(f"{i:2}. {backup_file}")
                                    else:
                                        print("📭 No backup files found")
                            except Exception as e:
                                print(f"❌ Failed to list backups: {e}")
                                log_error("BackupListError", str(e))

                        elif stats_choice == 3:  # Recover from backup
                            recovered_tasks, recovery_message = try_recover_from_backup(
                                CONFIG["tasks_file"])
                            if recovered_tasks:
                                try:
                                    replace_choice = input(
                                        "Replace current tasks with recovered tasks? (y/N): ").lower().strip()
                                except (KeyboardInterrupt, EOFError):
                                    replace_choice = "n"

                                if replace_choice in ('y', 'yes'):
                                    tasks.clear()
                                    tasks.extend(recovered_tasks)
                                    next_id = recompute_next_id(tasks)
                                    print(
                                        f"✅ Recovered {len(recovered_tasks)} tasks")
                                else:
                                    print("❌ Recovery cancelled")
                            else:
                                print(f"❌ Recovery failed: {recovery_message}")

                        elif stats_choice == 4:  # Clear error log
                            ERROR_LOG.clear()
                            print("✅ Error log cleared")

                        elif stats_choice == 5:  # Back
                            continue

                    except Exception as e:
                        print(f"❌ Statistics operation failed: {e}")
                        log_error("StatsError",
                                  f"Statistics operation failed: {e}")

            except (KeyboardInterrupt, EOFError):
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Unexpected error in main loop: {e}")
                log_error("UnexpectedError", f"Main loop error: {e}")
                continue

    except Exception as e:
        # Ultimate safety net
        print(f"❌ Critical error: {e}")
        log_error("CriticalError", f"Critical application error: {e}")
        print("🔄 Application shutting down safely...")


if __name__ == "__main__":
    run_todo_manager()
