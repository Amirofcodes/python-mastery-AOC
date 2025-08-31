# Password Toolkit — v2.0 (exceptions + file I/O)
# Scope: primitives, control flow, strings, functions + robust exception handling + file operations
# Features: Bulletproof file I/O, configuration loading, batch operations, comprehensive error handling

import random
import os
import json
from datetime import datetime

# ---- Character pools (simple strings, no advanced data structures) ----
LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?/"

# ---- Global state and configuration ----
ERROR_LOG = []  # Track session errors
PASSWORD_HISTORY = []  # Track generated passwords
CONFIG = {
    "min_length": 8,
    "require_lower": True,
    "require_upper": True,
    "require_digit": True,
    "require_symbol": True,
    "history_file": "password_history.json",
    "config_file": "password_config.json",
    "max_history": 100
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


def safe_get_menu_choice(min_choice=1, max_choice=8):
    """Get menu choice with comprehensive validation."""
    while True:
        try:
            choice = int(input(f"Choose option ({min_choice}-{max_choice}): "))
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


def safe_get_string(prompt, min_length=1, max_length=None):
    """Get a string with validation."""
    while True:
        try:
            value = input(prompt).strip()

            if len(value) < min_length:
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
# GENERATORS (pure functions)
# -------------------------


def generate_simple_password(length):
    """
    Generate a password of `length` using letters (both cases) + digits.
    Must respect requested length.
    """
    pool = LOWER + UPPER + DIGITS
    pwd = ""
    for _ in range(length):
        pwd += random.choice(pool)
    return pwd


def generate_secure_password(length):
    """
    Generate a password that includes at least:
      - 1 lowercase, 1 uppercase, 1 digit, 1 symbol
    and fills the remaining (if any) from ALL categories.
    NOTE: To avoid lists/shuffle, we’ll place the 4 required chars first,
    then append the rest randomly from the full pool.
    """
    if length < 4:
        # Minimal length to satisfy category presence
        length = 4  # keep it simple for v1

    # Required one of each:
    lower_char = random.choice(LOWER)
    upper_char = random.choice(UPPER)
    digit_char = random.choice(DIGITS)
    symbol_char = random.choice(SYMBOLS)

    pwd = lower_char + upper_char + digit_char + symbol_char

    # Full pool for remaining characters
    full_pool = LOWER + UPPER + DIGITS + SYMBOLS

    for _ in range(length - 4):
        pwd += random.choice(full_pool)

    # We are NOT shuffling (to avoid lists). That’s fine for v1.
    return pwd


# -------------------------
# VALIDATION (pure functions)
# -------------------------

def is_strong(password, min_length=8, require_lower=True, require_upper=True,
              require_digit=True, require_symbol=True):
    """
    Check password against rules; return True/False ONLY.
    (Detailed messages live in validate_password)
    """
    # Length check
    if len(password) < min_length:
        return False

    # Category checks via simple loops (no comprehensions yet)
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False

    for ch in password:
        if ch.islower():
            has_lower = True
        elif ch.isupper():
            has_upper = True
        elif ch.isdigit():
            has_digit = True
        elif ch in SYMBOLS:
            has_symbol = True

    if require_lower and not has_lower:
        return False
    if require_upper and not has_upper:
        return False
    if require_digit and not has_digit:
        return False
    if require_symbol and not has_symbol:
        return False

    return True


def validate_password(password, min_length=8, require_lower=True, require_upper=True,
                      require_digit=True, require_symbol=True):
    """
    Return a tuple: (is_valid, message)
      - is_valid: True/False
      - message: clear, user-friendly reason
    """
    # Length first
    if len(password) < min_length:
        return False, f"Too short: need at least {min_length} characters."

    # Category presence checks (recompute flags)
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False

    for ch in password:
        if ch.islower():
            has_lower = True
        elif ch.isupper():
            has_upper = True
        elif ch.isdigit():
            has_digit = True
        elif ch in SYMBOLS:
            has_symbol = True

    if require_lower and not has_lower:
        return False, "Missing a lowercase letter."
    if require_upper and not has_upper:
        return False, "Missing an uppercase letter."
    if require_digit and not has_digit:
        return False, "Missing a digit."
    if require_symbol and not has_symbol:
        return False, "Missing a symbol."

    return True, "Password is strong."


# -------------------------
# FILE I/O OPERATIONS WITH BULLETPROOF ERROR HANDLING
# -------------------------

def load_config(filename=None):
    """Load configuration from file with comprehensive error handling."""
    if filename is None:
        filename = CONFIG["config_file"]

    default_config = CONFIG.copy()

    try:
        with open(filename, "r", encoding="utf-8") as f:
            loaded_config = json.load(f)

        # Validate config file format
        if not isinstance(loaded_config, dict):
            print("❌ Invalid config format (must be a JSON object); using defaults")
            log_error("ConfigError", "Config root must be object")
            return False, "Invalid config format; using defaults"

        # Validate and merge configuration
        for key, value in loaded_config.items():
            if key in default_config:
                # Type validation
                if isinstance(default_config[key], bool) and isinstance(value, bool):
                    CONFIG[key] = value
                elif isinstance(default_config[key], int) and isinstance(value, int):
                    if key == "min_length" and value >= 1:
                        CONFIG[key] = value
                    elif key == "max_history" and value >= 0:
                        CONFIG[key] = value
                elif isinstance(default_config[key], str) and isinstance(value, str):
                    CONFIG[key] = value
                else:
                    log_error("ConfigError",
                              f"Invalid type for {key}: {type(value)}")
            else:
                log_error("ConfigError", f"Unknown config key: {key}")

        print(f"✅ Configuration loaded from {filename}")
        return True, f"Configuration loaded successfully"

    except FileNotFoundError:
        print(f"⚠️ Config file {filename} not found, using defaults")
        log_error("FileNotFoundError", f"Config file not found: {filename}")
        return False, "Config file not found, using defaults"
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in config file: {e}")
        log_error("JSONDecodeError", f"Invalid JSON in config: {e}")
        return False, f"Invalid JSON in config file: {e}"
    except PermissionError:
        print(f"❌ Permission denied reading {filename}")
        log_error("PermissionError", f"Cannot read config file: {filename}")
        return False, f"Permission denied reading {filename}"
    except Exception as e:
        print(f"❌ Unexpected error loading config: {e}")
        log_error("ConfigError", f"Unexpected config load error: {e}")
        return False, f"Unexpected error: {e}"


def save_config(filename=None):
    """Save current configuration to file."""
    if filename is None:
        filename = CONFIG["config_file"]

    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(filename) if os.path.dirname(
            filename) else ".", exist_ok=True)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(CONFIG, f, indent=2)
        print(f"✅ Configuration saved to {filename}")
        return True, f"Configuration saved successfully"
    except PermissionError:
        print(f"❌ Permission denied writing {filename}")
        log_error("PermissionError", f"Cannot write config file: {filename}")
        return False, f"Permission denied writing {filename}"
    except Exception as e:
        print(f"❌ Unexpected error saving config: {e}")
        log_error("ConfigError", f"Unexpected config save error: {e}")
        return False, f"Unexpected error: {e}"


def save_password_history(filename=None):
    """Save password history to file with comprehensive error handling."""
    if filename is None:
        filename = CONFIG["history_file"]

    if not PASSWORD_HISTORY:
        return True, "No passwords to save"

    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(filename) if os.path.dirname(
            filename) else ".", exist_ok=True)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(PASSWORD_HISTORY, f, indent=2)

        print(f"✅ Saved {len(PASSWORD_HISTORY)} passwords to {filename}")
        return True, f"Saved {len(PASSWORD_HISTORY)} passwords successfully"

    except PermissionError:
        print(f"❌ Permission denied writing {filename}")
        log_error("PermissionError", f"Cannot write history file: {filename}")
        return False, f"Permission denied writing {filename}"
    except OSError as e:
        print(f"❌ File system error: {e}")
        log_error("OSError", f"File system error saving history: {e}")
        return False, f"File system error: {e}"
    except Exception as e:
        print(f"❌ Unexpected error saving history: {e}")
        log_error("HistoryError", f"Unexpected history save error: {e}")
        return False, f"Unexpected error: {e}"


def load_password_history(filename=None):
    """Load password history from file with error recovery."""
    global PASSWORD_HISTORY
    if filename is None:
        filename = CONFIG["history_file"]

    try:
        with open(filename, "r", encoding="utf-8") as f:
            loaded_history = json.load(f)

        # Validate and normalize loaded data
        if isinstance(loaded_history, list):
            # Normalize: accept either list[dict] or list[str] for backward compatibility
            normalized = []
            for item in loaded_history:
                if isinstance(item, dict):
                    normalized.append(item)
                elif isinstance(item, str):
                    # Convert legacy string entries to new format
                    normalized.append({
                        "password": item,
                        "type": "imported",
                        "timestamp": datetime.now().isoformat(),
                        "strength": "strong" if is_strong(item) else "weak"
                    })
                else:
                    log_error("HistoryError",
                              f"Unsupported entry type: {type(item)}")

            PASSWORD_HISTORY = normalized
            print(
                f"✅ Loaded {len(PASSWORD_HISTORY)} passwords from {filename}")
            return True, f"Loaded {len(PASSWORD_HISTORY)} passwords successfully"
        else:
            log_error("HistoryError", "Invalid history file format")
            return False, "Invalid history file format"

    except FileNotFoundError:
        print(f"⚠️ History file {filename} not found, starting fresh")
        log_error("FileNotFoundError", f"History file not found: {filename}")
        PASSWORD_HISTORY = []
        return False, "History file not found, starting fresh"
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in history file: {e}")
        log_error("JSONDecodeError", f"Invalid JSON in history: {e}")
        PASSWORD_HISTORY = []
        return False, f"Invalid JSON in history file: {e}"
    except PermissionError:
        print(f"❌ Permission denied reading {filename}")
        log_error("PermissionError", f"Cannot read history file: {filename}")
        return False, f"Permission denied reading {filename}"
    except Exception as e:
        print(f"❌ Unexpected error loading history: {e}")
        log_error("HistoryError", f"Unexpected history load error: {e}")
        PASSWORD_HISTORY = []
        return False, f"Unexpected error: {e}"


def add_to_history(password, password_type="generated"):
    """Add password to history with metadata."""
    global PASSWORD_HISTORY

    entry = {
        "password": password,
        "type": password_type,
        "timestamp": datetime.now().isoformat(),
        "strength": "strong" if is_strong(password) else "weak"
    }

    PASSWORD_HISTORY.append(entry)

    # Maintain history size limit
    max_history = CONFIG.get("max_history", 100)
    if len(PASSWORD_HISTORY) > max_history:
        PASSWORD_HISTORY = PASSWORD_HISTORY[-max_history:]


def batch_generate_passwords(count, password_type="secure", length=12):
    """Generate multiple passwords with partial failure recovery."""
    generated = []
    errors = []

    for i in range(count):
        try:
            if password_type == "simple":
                password = generate_simple_password(length)
            else:
                password = generate_secure_password(length)

            add_to_history(password, f"batch_{password_type}")
            generated.append(password)

        except Exception as e:
            error_msg = f"Failed to generate password {i+1}: {e}"
            errors.append(error_msg)
            log_error("GenerationError", error_msg)

    return generated, errors


# -------------------------
# CLI INTERFACE
# -------------------------

def display_menu():
    """Display enhanced menu with file operations."""
    print("\n" + "=" * 65)
    print("🔐 Password Toolkit v2.0 - Bulletproof Edition 🛡️")
    print("- Main Menu -")
    print("1) Generate simple password (letters + digits)")
    print("2) Generate secure password (all categories)")
    print("3) Batch generate passwords")
    print("4) Validate existing password")
    print("5) View password history")
    print("6) Save/Load operations")
    print("7) Configuration & Statistics")
    print("8) Run self-tests")
    print("9) Quit")
    print("=" * 65)

    return safe_get_menu_choice(1, 9)


def display_save_load_menu():
    """Display save/load operations menu."""
    print("\n💾 Save/Load Operations:")
    print("1) Save password history")
    print("2) Load password history")
    print("3) Save configuration")
    print("4) Load configuration")
    print("5) Back to main menu")

    return safe_get_menu_choice(1, 5)


def display_config_menu():
    """Display configuration and statistics menu."""
    print("\n⚙️ Configuration & Statistics:")
    print("1) View current configuration")
    print("2) Modify password requirements")
    print("3) View session statistics")
    print("4) Clear error log")
    print("5) Back to main menu")

    return safe_get_menu_choice(1, 5)


def get_password_length():
    """Get password length with enhanced validation."""
    return safe_get_int("Enter password length: ", min_val=1, max_val=128)


def display_statistics():
    """Display comprehensive session statistics."""
    print("\n📊 Session Statistics:")
    print(f"Passwords generated: {len(PASSWORD_HISTORY)}")
    print(f"Total errors logged: {len(ERROR_LOG)}")

    if PASSWORD_HISTORY:
        strong_count = sum(
            1 for entry in PASSWORD_HISTORY if entry.get("strength") == "strong")
        print(f"Strong passwords: {strong_count}/{len(PASSWORD_HISTORY)}")

        # Show recent passwords (without revealing actual passwords)
        print("\n🔍 Recent Password History (last 5):")
        for entry in PASSWORD_HISTORY[-5:]:
            timestamp = entry.get("timestamp", "unknown")[
                :19]  # Remove microseconds
            password_type = entry.get("type", "unknown")
            strength = entry.get("strength", "unknown")
            print(f"  {timestamp} | {password_type} | {strength}")

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


def display_password_history():
    """Display password history with security considerations."""
    if not PASSWORD_HISTORY:
        print("📝 No passwords in history")
        return

    print(f"\n📝 Password History ({len(PASSWORD_HISTORY)} entries):")

    try:
        show_passwords = input(
            "🔍 Show actual passwords? (y/N): ").lower().strip()
    except (KeyboardInterrupt, EOFError):
        print("\n👋 Goodbye!")
        raise SystemExit(0)

    reveal_passwords = show_passwords in ('y', 'yes')

    for i, entry in enumerate(PASSWORD_HISTORY, 1):
        timestamp = entry.get("timestamp", "unknown")[:19]
        password_type = entry.get("type", "unknown")
        strength = entry.get("strength", "unknown")

        if reveal_passwords:
            password = entry.get("password", "***")
            print(
                f"{i:3}. {timestamp} | {password_type:15} | {strength:6} | {password}")
        else:
            length = len(entry.get("password", ""))
            print(
                f"{i:3}. {timestamp} | {password_type:15} | {strength:6} | [hidden, {length} chars]")


def run_password_tool():
    """Main CLI loop with bulletproof exception handling."""
    # Welcome banner and initialization
    print("🎉 Welcome to Password Toolkit v2.0!")
    print("🛡️ Now with bulletproof file I/O and comprehensive error handling!")
    print("🔐 All your passwords are tracked and can be saved securely!")

    # Load configuration and history on startup
    load_config()
    load_password_history()

    try:
        while True:
            try:
                choice = display_menu()

                if choice == 9:  # Quit
                    print("\n👋 Thank you for using Password Toolkit v2.0!")
                    print(
                        f"📊 Session summary: {len(PASSWORD_HISTORY)} passwords generated, {len(ERROR_LOG)} errors handled")

                    # Offer to save before quitting
                    if PASSWORD_HISTORY:
                        try:
                            save_choice = input(
                                "💾 Save password history before quitting? (Y/n): ").lower().strip()
                        except (KeyboardInterrupt, EOFError):
                            save_choice = "n"  # treat interrupt as "do not save"

                        if save_choice not in ('n', 'no'):
                            save_password_history()

                    print("🎯 No crashes occurred - bulletproof success! 🛡️")
                    break

                elif choice == 1:  # Generate simple password
                    try:
                        length = get_password_length()
                        password = generate_simple_password(length)
                        add_to_history(password, "simple")
                        print(f"✅ Generated simple password: {password}")

                        # Show strength
                        is_valid, message = validate_password(password)
                        strength_status = "🟢 STRONG" if is_valid else "🟡 WEAK"
                        print(f"   Strength: {strength_status} - {message}")

                    except Exception as e:
                        print(f"❌ Password generation failed: {e}")
                        log_error("GenerationError",
                                  f"Simple password generation failed: {e}")

                elif choice == 2:  # Generate secure password
                    try:
                        length = get_password_length()
                        password = generate_secure_password(length)
                        add_to_history(password, "secure")
                        print(f"✅ Generated secure password: {password}")

                        # Secure passwords should always be strong, but let's verify
                        is_valid, message = validate_password(password)
                        strength_status = "🟢 STRONG" if is_valid else "🟡 WEAK"
                        print(f"   Strength: {strength_status} - {message}")

                    except Exception as e:
                        print(f"❌ Password generation failed: {e}")
                        log_error("GenerationError",
                                  f"Secure password generation failed: {e}")

                elif choice == 3:  # Batch generate passwords
                    try:
                        count = safe_get_int(
                            "How many passwords to generate? ", min_val=1, max_val=50)

                        print("Password type:")
                        print("1) Simple (letters + digits)")
                        print("2) Secure (all categories)")
                        type_choice = safe_get_menu_choice(1, 2)

                        length = get_password_length()

                        password_type = "simple" if type_choice == 1 else "secure"
                        generated, errors = batch_generate_passwords(
                            count, password_type, length)

                        print(
                            f"\n✅ Successfully generated {len(generated)} passwords")
                        if errors:
                            print(f"❌ {len(errors)} errors occurred:")
                            for error in errors[:3]:  # Show first 3 errors
                                print(f"   {error}")

                        # Show generated passwords
                        if generated:
                            try:
                                show_batch = input(
                                    "🔍 Display generated passwords? (y/N): ").lower().strip()
                            except (KeyboardInterrupt, EOFError):
                                print("\n👋 Goodbye!")
                                raise SystemExit(0)

                            if show_batch in ('y', 'yes'):
                                for i, pwd in enumerate(generated, 1):
                                    print(f"{i:2}. {pwd}")

                    except Exception as e:
                        print(f"❌ Batch generation failed: {e}")
                        log_error("BatchError",
                                  f"Batch generation failed: {e}")

                elif choice == 4:  # Validate existing password
                    try:
                        password = safe_get_string(
                            "Enter password to validate: ", min_length=1)
                        is_valid, message = validate_password(password,
                                                              min_length=CONFIG["min_length"],
                                                              require_lower=CONFIG["require_lower"],
                                                              require_upper=CONFIG["require_upper"],
                                                              require_digit=CONFIG["require_digit"],
                                                              require_symbol=CONFIG["require_symbol"])

                        status = "🟢 STRONG" if is_valid else "🔴 WEAK"
                        print(f"{status}: {message}")

                        # Add to history for tracking
                        add_to_history(password, "validated")

                    except Exception as e:
                        print(f"❌ Password validation failed: {e}")
                        log_error("ValidationError",
                                  f"Password validation failed: {e}")

                elif choice == 5:  # View password history
                    try:
                        display_password_history()
                    except Exception as e:
                        print(f"❌ Failed to display history: {e}")
                        log_error("HistoryError",
                                  f"Failed to display history: {e}")

                elif choice == 6:  # Save/Load operations
                    try:
                        save_load_choice = display_save_load_menu()

                        if save_load_choice == 1:  # Save history
                            save_password_history()
                        elif save_load_choice == 2:  # Load history
                            load_password_history()
                        elif save_load_choice == 3:  # Save config
                            save_config()
                        elif save_load_choice == 4:  # Load config
                            load_config()
                        elif save_load_choice == 5:  # Back
                            continue

                    except Exception as e:
                        print(f"❌ Save/Load operation failed: {e}")
                        log_error("FileIOError",
                                  f"Save/Load operation failed: {e}")

                elif choice == 7:  # Configuration & Statistics
                    try:
                        config_choice = display_config_menu()

                        if config_choice == 1:  # View config
                            print("\n⚙️ Current Configuration:")
                            for key, value in CONFIG.items():
                                print(f"  {key}: {value}")
                        elif config_choice == 2:  # Modify requirements
                            print(
                                "⚠️ Configuration modification not implemented in v2.0")
                            print(
                                "   Edit password_config.json manually or use defaults")
                        elif config_choice == 3:  # View statistics
                            display_statistics()
                        elif config_choice == 4:  # Clear error log
                            ERROR_LOG.clear()
                            print("✅ Error log cleared")
                        elif config_choice == 5:  # Back
                            continue

                    except Exception as e:
                        print(f"❌ Configuration operation failed: {e}")
                        log_error("ConfigError",
                                  f"Configuration operation failed: {e}")

                elif choice == 8:  # Run self-tests
                    try:
                        _run_self_tests()
                    except Exception as e:
                        print(f"❌ Self-tests failed: {e}")
                        log_error("TestError", f"Self-tests failed: {e}")

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


# -------------------------
# SELF-TESTS
# -------------------------

def _run_self_tests():
    # Generation length checks
    p1 = generate_simple_password(12)
    assert isinstance(p1, str) and len(p1) == 12

    p2 = generate_secure_password(4)
    assert isinstance(p2, str) and len(p2) == 4

    # Secure must contain all categories (positions 0..3 guarantee this)
    assert any(c.islower() for c in p2)
    assert any(c.isupper() for c in p2)
    assert any(c.isdigit() for c in p2)
    assert any(c in SYMBOLS for c in p2)

    # is_strong basic checks
    assert is_strong("Aa1!aaaa") is True
    assert is_strong("aaaaaaa") is False          # no upper, digit, symbol
    assert is_strong("AAAAAAA1") is False         # no lower, no symbol
    assert is_strong("Aa1aaaaa", require_symbol=False) is True

    # validate_password messages
    ok, msg = validate_password("Aa1!aaaa")
    assert ok and "strong" in msg.lower()

    ok, msg = validate_password("Aaaaaaaa")  # missing digit + symbol
    assert ok is False and ("digit" in msg.lower() or "symbol" in msg.lower())

    # Length rule
    ok, msg = validate_password("Aa1!", min_length=8)
    assert not ok and "short" in msg.lower()

    print("All self-tests passed ✅")


if __name__ == "__main__":
    run_password_tool()
