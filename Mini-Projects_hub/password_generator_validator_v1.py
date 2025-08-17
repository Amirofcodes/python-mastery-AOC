# Password Generator & Validator — v1 (functions)
# Scope: primitives, control flow, strings, functions (+ import random)
# No try/except, no comprehensions, no classes.

import random

# ---- Character pools (simple strings, no advanced data structures) ----
LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?/"

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
# CLI INTERFACE
# -------------------------

def display_menu():
    print("\n" + "=" * 50)
    print("🔐 Password Generator & Validator v1.0")
    print("1) Generate simple password (letters + digits)")
    print("2) Generate secure password (all categories)")
    print("3) Validate existing password")
    print("4) Run self-tests")
    print("5) Quit")
    choice = int(input("Choose option (1-5): "))
    return choice


def get_password_length():
    length = int(input("Enter password length: "))
    return max(1, length)  # Ensure at least 1


def run_password_tool():
    """Main CLI loop for the password tool."""
    while True:
        choice = display_menu()

        if choice < 1 or choice > 5:
            print("Invalid option. Please choose 1-5.")
            continue

        if choice == 5:
            print("Thank you for using Password Tool v1.0!")
            break

        elif choice == 1:
            length = get_password_length()
            password = generate_simple_password(length)
            print(f"Generated simple password: {password}")

        elif choice == 2:
            length = get_password_length()
            password = generate_secure_password(length)
            print(f"Generated secure password: {password}")

        elif choice == 3:
            password = input("Enter password to validate: ")
            is_valid, message = validate_password(password)
            status = "✅ STRONG" if is_valid else "❌ WEAK"
            print(f"{status}: {message}")

        elif choice == 4:
            _run_self_tests()


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
