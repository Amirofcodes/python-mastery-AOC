# Password Toolkit - Template for Progressive Learning
#
# Instructions:
# 1. Copy this template to password_toolkit_v1.py to start fresh practice
# 2. Complete each section by typing the solution yourself to build muscle memory
# 3. Only use concepts from Primitive Types + Control Flow + Functions (sections 01-03)
# 4. Focus on string manipulation, random generation, and validation logic
# 5. Test each feature thoroughly before moving to the next
#
# Learning Goals: Master string operations, random generation, and validation patterns
# Real-World Application: Build security tools with professional password standards
#
# ===== PROJECT OVERVIEW =====
#
# Build a comprehensive password toolkit with generation and validation:
# - Generate simple passwords (letters + digits)
# - Generate secure passwords (letters + digits + symbols)
# - Validate passwords against strength rules
# - Interactive CLI menu system
# - Self-testing capabilities
#
# Security Principles:
# - Randomness for unpredictability
# - Category requirements for strength
# - Length requirements for security
# - Clear validation feedback
#
# ===== IMPORTS AND CONSTANTS =====

import random

# TODO: Define character pools for password generation
# Core concept: String constants for clean, maintainable code
# LOWER = "abcdefghijklmnopqrstuvwxyz"
# UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# DIGITS = "0123456789"
# SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?/"


# ===== PASSWORD GENERATION FUNCTIONS (Pure Logic) =====

def generate_simple_password(length):
    """Generate password using letters (both cases) and digits only.
    
    Args:
        length (int): Desired password length
        
    Returns:
        str: Generated password
    """
    # TODO: Implement simple password generation
    # Core concept: Random selection from combined character pool
    # pool = LOWER + UPPER + DIGITS
    # pwd = ""
    # for _ in range(length):
    #     pwd += random.choice(pool)
    # return pwd
    pass


def generate_secure_password(length):
    """Generate password ensuring all categories are represented.
    
    Args:
        length (int): Desired password length (minimum 4 for all categories)
        
    Returns:
        str: Generated secure password
    """
    # TODO: Implement secure password generation
    # Core concept: Guarantee category representation
    # if length < 4:
    #     length = 4  # Minimum to include all categories
    
    # # Required one of each category
    # lower_char = random.choice(LOWER)
    # upper_char = random.choice(UPPER)
    # digit_char = random.choice(DIGITS)
    # symbol_char = random.choice(SYMBOLS)
    
    # pwd = lower_char + upper_char + digit_char + symbol_char
    
    # # Fill remaining positions from full pool
    # full_pool = LOWER + UPPER + DIGITS + SYMBOLS
    # for _ in range(length - 4):
    #     pwd += random.choice(full_pool)
    
    # return pwd
    pass


# ===== PASSWORD VALIDATION FUNCTIONS =====

def is_strong(password, min_length=8, require_lower=True, require_upper=True,
              require_digit=True, require_symbol=True):
    """Check if password meets strength requirements (boolean only).
    
    Args:
        password (str): Password to validate
        min_length (int): Minimum required length
        require_lower (bool): Require lowercase letter
        require_upper (bool): Require uppercase letter
        require_digit (bool): Require digit
        require_symbol (bool): Require symbol
        
    Returns:
        bool: True if password meets all requirements
    """
    # TODO: Implement strength checking logic
    # Core concept: Boolean validation with multiple criteria
    
    # Check length requirement
    # if len(password) < min_length:
    #     return False
    
    # Check category requirements using loops (no comprehensions yet)
    # has_lower = False
    # has_upper = False
    # has_digit = False
    # has_symbol = False
    
    # for ch in password:
    #     if ch.islower():
    #         has_lower = True
    #     elif ch.isupper():
    #         has_upper = True
    #     elif ch.isdigit():
    #         has_digit = True
    #     elif ch in SYMBOLS:
    #         has_symbol = True
    
    # # Check all requirements
    # if require_lower and not has_lower:
    #     return False
    # if require_upper and not has_upper:
    #     return False
    # if require_digit and not has_digit:
    #     return False
    # if require_symbol and not has_symbol:
    #     return False
    
    # return True
    pass


def validate_password(password, min_length=8, require_lower=True, require_upper=True,
                      require_digit=True, require_symbol=True):
    """Validate password with detailed feedback.
    
    Args:
        password (str): Password to validate
        min_length (int): Minimum required length
        require_lower (bool): Require lowercase letter
        require_upper (bool): Require uppercase letter  
        require_digit (bool): Require digit
        require_symbol (bool): Require symbol
        
    Returns:
        tuple: (is_valid, message) with detailed feedback
    """
    # TODO: Implement detailed validation with user-friendly messages
    # Core concept: Tuple return for status + detailed feedback
    
    # Check length first
    # if len(password) < min_length:
    #     return False, f"Too short: need at least {min_length} characters."
    
    # Check each category with specific error messages
    # has_lower = any(c.islower() for c in password)
    # has_upper = any(c.isupper() for c in password)
    # has_digit = any(c.isdigit() for c in password)
    # has_symbol = any(c in SYMBOLS for c in password)
    
    # if require_lower and not has_lower:
    #     return False, "Missing a lowercase letter."
    # if require_upper and not has_upper:
    #     return False, "Missing an uppercase letter."
    # if require_digit and not has_digit:
    #     return False, "Missing a digit."
    # if require_symbol and not has_symbol:
    #     return False, "Missing a symbol."
    
    # return True, "Password is strong."
    pass


# ===== I/O HELPER FUNCTIONS =====

def display_menu():
    """Display main menu and get user choice."""
    # TODO: Implement menu display
    # Core concept: Professional menu presentation
    # print("\n" + "=" * 50)
    # print("🔐 Password Generator & Validator v1.0")
    # print("1) Generate simple password (letters + digits)")
    # print("2) Generate secure password (all categories)")
    # print("3) Validate existing password")
    # print("4) Run self-tests")
    # print("5) Quit")
    # choice = int(input("Choose option (1-5): "))
    # return choice
    pass


def get_password_length():
    """Get desired password length from user."""
    # TODO: Implement length input with validation
    # Core concept: Input validation and sensible defaults
    # length = int(input("Enter password length: "))
    # return max(1, length)  # Ensure at least 1
    pass


# ===== MAIN ORCHESTRATOR FUNCTION =====

def run_password_tool():
    """Main program loop coordinating all functionality."""
    # TODO: Implement main program logic
    # Core concept: Central coordinator using helper functions
    
    # while True:
    #     choice = display_menu()
    
    #     # Validate menu choice
    #     if choice < 1 or choice > 5:
    #         print("Invalid option. Please choose 1-5.")
    #         continue
    
    #     if choice == 5:  # Quit
    #         print("Thank you for using Password Tool v1.0!")
    #         break
    
    #     elif choice == 1:  # Generate simple password
    #         length = get_password_length()
    #         password = generate_simple_password(length)
    #         print(f"Generated simple password: {password}")
    
    #     elif choice == 2:  # Generate secure password
    #         length = get_password_length()
    #         password = generate_secure_password(length)
    #         print(f"Generated secure password: {password}")
    
    #     elif choice == 3:  # Validate password
    #         password = input("Enter password to validate: ")
    #         is_valid, message = validate_password(password)
    #         status = "✅ STRONG" if is_valid else "❌ WEAK"
    #         print(f"{status}: {message}")
    
    #     elif choice == 4:  # Run self-tests
    #         _run_self_tests()
    
    pass


# ===== SELF-TESTING FUNCTIONS =====

def _run_self_tests():
    """Run comprehensive self-tests to verify functionality."""
    # TODO: Implement self-testing logic
    # Core concept: Automated testing for reliability
    
    # Test generation length consistency
    # p1 = generate_simple_password(12)
    # assert isinstance(p1, str) and len(p1) == 12
    
    # p2 = generate_secure_password(4)
    # assert isinstance(p2, str) and len(p2) == 4
    
    # # Test secure password category requirements
    # assert any(c.islower() for c in p2)
    # assert any(c.isupper() for c in p2)
    # assert any(c.isdigit() for c in p2)
    # assert any(c in SYMBOLS for c in p2)
    
    # # Test validation logic
    # assert is_strong("Aa1!aaaa") is True
    # assert is_strong("aaaaaaa") is False  # Missing upper, digit, symbol
    # assert is_strong("AAAAAAA1") is False  # Missing lower, symbol
    
    # # Test detailed validation messages
    # ok, msg = validate_password("Aa1!aaaa")
    # assert ok and "strong" in msg.lower()
    
    # ok, msg = validate_password("Aaaaaaaa")  # Missing digit + symbol
    # assert ok is False and ("digit" in msg.lower() or "symbol" in msg.lower())
    
    # # Test length requirements
    # ok, msg = validate_password("Aa1!", min_length=8)
    # assert not ok and "short" in msg.lower()
    
    # print("All self-tests passed ✅")
    pass


# ===== PROGRAM ENTRY POINT =====

if __name__ == "__main__":
    # TODO: Call main function
    # run_password_tool()
    pass

# ===== TESTING CHECKLIST =====
#
# □ Simple password generation respects length
# □ Secure password includes all required categories
# □ Password validation correctly identifies weak passwords
# □ Detailed validation provides helpful error messages
# □ Menu system handles invalid choices gracefully
# □ Self-tests verify all functionality
# □ Generated passwords are random and unpredictable
#
# ===== SECURITY PRINCIPLES =====
#
# 1. Randomness:
#    - Use random.choice() for unpredictable selection
#    - Each character independently selected
#    - No predictable patterns
#
# 2. Category Requirements:
#    - Lowercase letters (a-z)
#    - Uppercase letters (A-Z)  
#    - Digits (0-9)
#    - Symbols (!@#$%^&*...)
#
# 3. Length Requirements:
#    - Minimum 8 characters for basic security
#    - Longer passwords exponentially more secure
#    - Balance usability vs security
#
# ===== STRING MANIPULATION TECHNIQUES =====
#
# 1. Character Pool Creation:
#    - Combine strings with + operator
#    - Define constants for reusability
#    - Include all necessary character types
#
# 2. Random Selection:
#    - random.choice() for single character
#    - Loop for multiple characters
#    - Build string incrementally
#
# 3. Validation Patterns:
#    - Character testing with .islower(), .isupper(), .isdigit()
#    - Membership testing with 'in' operator
#    - Boolean flags for requirement tracking
#
# ===== ENHANCEMENT IDEAS (For Later Versions) =====
#
# v2 (Exceptions): Add bulletproof error handling and file I/O
# v2.1 (Configuration): Add customizable password rules
# v2.2 (History): Track generated passwords with strength analysis
# v3 (Classes): Create PasswordGenerator and PasswordValidator classes
# v4 (Entropy): Add password strength scoring and entropy calculation
# v5 (GUI): Add graphical interface with visual strength indicators
#
# ===== DEBUGGING TIPS =====
#
# 1. Test with known password examples
# 2. Verify category requirements with simple passwords
# 3. Check edge cases like minimum length passwords
# 4. Test random generation produces different results
# 5. Validate error messages are user-friendly
# 6. Ensure self-tests cover all functionality
