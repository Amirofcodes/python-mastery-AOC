# Todo Manager - Template for Progressive Learning
#
# Instructions:
# 1. Copy this template to todo_manager_v1.py to start fresh practice
# 2. Complete each section by typing the solution yourself to build muscle memory
# 3. Only use concepts from Primitive Types + Control Flow + Functions + Data Structures (sections 01-04)
# 4. Focus on lists, dictionaries, and data manipulation
# 5. Test each CRUD operation thoroughly before moving to the next
#
# Learning Goals: Master data structures, CRUD operations, and state management
# Real-World Application: Build data management systems with professional patterns
#
# ===== PROJECT OVERVIEW =====
#
# Build a comprehensive task management system:
# - Add tasks with unique IDs and titles
# - List all tasks with status indicators
# - Toggle task completion by ID
# - Delete tasks by ID with confirmation
# - Clear all tasks with confirmation
# - Professional menu system
#
# Data Structure:
# - Task: {"id": int, "title": str, "done": bool}
# - Tasks: List of task dictionaries
# - Auto-incrementing ID system
#
# ===== DATA STRUCTURE DESIGN =====
#
# Task Dictionary Structure:
# {
#     "id": 1,           # Unique identifier (int)
#     "title": "Task",   # Task description (str)  
#     "done": False      # Completion status (bool)
# }
#
# Display Format:
# [1] [ ] Buy groceries     # Pending task
# [2] [x] Finish homework   # Completed task

# ===== CORE CRUD FUNCTIONS =====

def add_task(tasks, next_id):
    """Add a new task to the task list.
    
    Args:
        tasks (list): List of task dictionaries
        next_id (int): Next available ID for new task
        
    Returns:
        int: Updated next_id for future tasks
    """
    # TODO: Implement task addition
    # Core concept: Dictionary creation and list manipulation
    # title = input("Enter your task title: ").strip()
    # if title:
    #     task = {"id": next_id, "title": title, "done": False}
    #     tasks.append(task)
    #     print(f"✅ Added task #{next_id}: {title}")
    #     return next_id + 1
    # else:
    #     print("❌ Task title cannot be empty")
    #     return next_id
    pass


def list_tasks(tasks):
    """Display all tasks with formatting and status indicators.
    
    Args:
        tasks (list): List of task dictionaries
    """
    # TODO: Implement task listing
    # Core concept: List iteration and dictionary access
    # if not tasks:
    #     print("📭 No tasks yet!")
    #     return
    
    # print(f"\n You have {len(tasks)} Total")
    # for task in tasks:
    #     status = "[x]" if task["done"] else "[ ]"
    #     print(f"[{task['id']}] {status} {task['title']}")
    pass


def toggle_by_id(tasks):
    """Toggle completion status of a task by ID.
    
    Args:
        tasks (list): List of task dictionaries
    """
    # TODO: Implement task toggling
    # Core concept: List searching and boolean manipulation
    # task_id = int(input("Choose a task ID: "))
    # for task in tasks:
    #     if task["id"] == task_id:
    #         task["done"] = not task["done"]
    #         status = "completed" if task["done"] else "pending"
    #         print(f"✅ Task #{task_id} marked as {status}")
    #         return
    # print(f"❌ Task with ID {task_id} not found")
    pass


def delete_by_id(tasks):
    """Delete a task by ID with confirmation.
    
    Args:
        tasks (list): List of task dictionaries
    """
    # TODO: Implement task deletion
    # Core concept: List searching and removal
    # task_id = int(input("Choose a task ID: "))
    # for task in tasks:
    #     if task["id"] == task_id:
    #         # Optional: Add confirmation
    #         # confirm = input(f"Delete '{task['title']}'? (y/N): ").lower()
    #         # if confirm in ('y', 'yes'):
    #         tasks.remove(task)
    #         print(f"✅ Deleted task #{task_id}: {task['title']}")
    #         return
    # print(f"❌ Task with ID {task_id} not found")
    pass


def clear_all(tasks):
    """Clear all tasks with confirmation.
    
    Args:
        tasks (list): List of task dictionaries
    """
    # TODO: Implement task clearing
    # Core concept: List clearing with user confirmation
    # if tasks:
    #     count = len(tasks)
    #     # Optional: Add confirmation
    #     # confirm = input(f"Clear all {count} tasks? (y/N): ").lower()
    #     # if confirm in ('y', 'yes'):
    #     tasks.clear()
    #     print(f"✅ Cleared {count} tasks")
    # else:
    #     print("📭 No tasks to clear")
    pass


# ===== USER INTERFACE FUNCTIONS =====

def display_menu():
    """Display main menu with professional formatting."""
    # TODO: Implement menu display
    # Core concept: Professional CLI interface design
    # print("\n" + "=" * 40)
    # print("📝 To-Do List Manager v1.0")
    # print("=" * 40)
    # print("1) Add task")
    # print("2) List tasks")
    # print("3) Toggle done by ID")
    # print("4) Delete by ID")
    # print("5) Clear all")
    # print("6) Quit")
    # print("=" * 40)
    pass


# ===== MAIN ORCHESTRATOR FUNCTION =====

def run_todo_manager():
    """Main program loop coordinating all functionality."""
    # TODO: Implement main program logic
    # Core concept: State management with data structures
    
    # Initialize application state
    # tasks = []
    # next_id = 1
    
    # while True:
    #     display_menu()
    #     choice = int(input("Choose an option: "))
    
    #     # Validate menu choice
    #     if choice < 1 or choice > 6:
    #         print("❌ Invalid choice. Please choose 1-6.")
    #         continue
    
    #     if choice == 6:  # Quit
    #         print("Thank you for using To-Do List Manager v1.0!")
    #         break
    
    #     elif choice == 1:  # Add task
    #         next_id = add_task(tasks, next_id)
    
    #     elif choice == 2:  # List tasks
    #         list_tasks(tasks)
    
    #     elif choice == 3:  # Toggle task
    #         if tasks:
    #             toggle_by_id(tasks)
    #         else:
    #             print("📭 No tasks to toggle!")
    
    #     elif choice == 4:  # Delete task
    #         if tasks:
    #             delete_by_id(tasks)
    #         else:
    #             print("📭 No tasks to delete!")
    
    #     elif choice == 5:  # Clear all
    #         clear_all(tasks)
    
    pass


# ===== PROGRAM ENTRY POINT =====

if __name__ == "__main__":
    # TODO: Call main function
    # run_todo_manager()
    pass

# ===== TESTING CHECKLIST =====
#
# □ Add task creates proper dictionary structure
# □ List tasks displays correct format and status
# □ Toggle changes done status correctly
# □ Delete removes correct task by ID
# □ Clear all removes all tasks
# □ Menu handles invalid choices gracefully
# □ ID system increments properly
# □ Empty list scenarios handled gracefully
#
# ===== DATA STRUCTURE PATTERNS =====
#
# 1. Dictionary Design:
#    - Consistent key names ("id", "title", "done")
#    - Appropriate data types (int, str, bool)
#    - Required vs optional fields
#
# 2. List Operations:
#    - Append for adding new items
#    - Iteration for searching/displaying
#    - Remove for deletion
#    - Clear for bulk operations
#
# 3. ID Management:
#    - Auto-incrementing counter
#    - Unique identification system
#    - Persistent across operations
#
# ===== SEARCH PATTERNS =====
#
# 1. Linear Search by ID:
#    for task in tasks:
#        if task["id"] == target_id:
#            # Found the task
#            break
#
# 2. Existence Checking:
#    found = False
#    for task in tasks:
#        if task["id"] == target_id:
#            found = True
#            break
#
# 3. List Comprehensions (Advanced):
#    # Future enhancement for filtering
#    completed = [task for task in tasks if task["done"]]
#
# ===== USER EXPERIENCE PATTERNS =====
#
# 1. Status Indicators:
#    - ✅ for success messages
#    - ❌ for error messages  
#    - 📭 for empty states
#    - [x] for completed tasks
#    - [ ] for pending tasks
#
# 2. Confirmation Prompts:
#    - Destructive operations (delete, clear)
#    - Clear user intent required
#    - Default to safe option (N)
#
# 3. Error Handling:
#    - Graceful handling of invalid IDs
#    - Empty list state management
#    - Input validation
#
# ===== ENHANCEMENT IDEAS (For Later Versions) =====
#
# v2 (Exceptions + Persistence): Add JSON file storage and bulletproof error handling
# v2.1 (Advanced Features): Add due dates, priorities, categories
# v2.2 (Search/Filter): Add task search and filtering capabilities
# v3 (Classes): Create Task and TodoManager classes
# v4 (Database): Add SQLite database storage
# v5 (Web): Add web interface with REST API
#
# ===== DEBUGGING TIPS =====
#
# 1. Print task list structure to verify dictionary format
# 2. Test with empty task list scenarios
# 3. Verify ID uniqueness and increment logic
# 4. Test edge cases like invalid IDs
# 5. Check boolean toggle logic works correctly
# 6. Verify list operations don't cause index errors
#
# ===== REAL-WORLD APPLICATIONS =====
#
# This pattern applies to:
# - Customer management systems
# - Inventory tracking
# - User account management  
# - Content management systems
# - Any CRUD application with persistent data
