# Smart Unit Converter - Template for Progressive Learning
#
# Instructions:
# 1. Copy this template to unit_converter_v1.py to start fresh practice
# 2. Complete each section by typing the solution yourself to build muscle memory
# 3. Only use concepts from Primitive Types + Control Flow (sections 01-02)
# 4. Focus on menus, loops, conditionals, and input/output
# 5. Test each conversion category before moving to the next
#
# Learning Goals: Master interactive CLI programs with robust menu systems
# Real-World Application: Build professional command-line tools with user-friendly interfaces
#
# ===== PROJECT OVERVIEW =====
#
# Build a comprehensive unit converter supporting 5 categories:
# - Length (km ↔ miles)
# - Temperature (°C ↔ °F) 
# - Weight (kg ↔ lb)
# - Currency (EUR ↔ USD)
# - Data (MB ↔ GB)
#
# Core Features:
# - Interactive menu system
# - Bidirectional conversions
# - Session counter
# - Input validation
# - Professional formatting
#
# ===== CONVERSION FORMULAS =====
#
# Length:    miles = km * 0.621371  |  km = miles / 0.621371
# Temperature: °F = °C * 9/5 + 32   |  °C = (°F - 32) * 5/9  
# Weight:    pounds = kg * 2.20462  |  kg = pounds / 2.20462
# Currency:  USD = EUR * 1.08       |  EUR = USD / 1.08
# Data:      GB = MB / 1024         |  MB = GB * 1024
#
# ===== STEP-BY-STEP IMPLEMENTATION =====

print("*********** Welcome to Smart Unit Converter v1.0 ***********")

# TODO: Define conversion constants for clean code
# Core concept: Constants for maintainable formulas
# MILES_PER_KM = ?
# POUNDS_PER_KG = ?
# EUR_TO_USD = ?
# MB_PER_GB = ?

# TODO: Initialize session counter
# Core concept: Variable to track user activity
# conversion_count = ?

# TODO: Create main program loop
# Core concept: while True loop with menu system
# while True:

    # TODO: Display main menu
    # Core concept: Professional menu presentation
    # print("\n" + "=" * 50)
    # print("🧮 Smart Converter v1.0")
    # choice = int(input(
    #     "- Menu -\n"
    #     "1) Length (km ↔ miles)\n"
    #     "2) Temperature (°C ↔ °F)\n"
    #     "3) Weight (kg ↔ lb)\n"
    #     "4) Currency (EUR ↔ USD)\n"
    #     "5) Data (MB ↔ GB)\n"
    #     "6) Quit\n"
    #     "Choose a conversion option (1-6): "
    # ))

    # TODO: Validate menu choice
    # Core concept: Input validation with clear error messages
    # if choice < 1 or choice > 6:
    #     print("Invalid option. Please choose 1-6.")
    #     continue

    # TODO: Handle quit option
    # Core concept: Clean program exit with summary
    # if choice == 6:
    #     print("Thank you for using Smart Converter!")
    #     print(f"Total conversions performed: {conversion_count}")
    #     break

    # TODO: Track successful conversions
    # Core concept: Boolean flag to control counter increment
    # converted = False
    # result_msg = ""

    # ===== LENGTH CONVERSION (Choice 1) =====
    # TODO: Implement length conversion
    # Core concept: Nested menu for direction selection
    # if choice == 1:
    #     direction = int(input("\n1) km → miles\n2) miles → km\nChoose: "))
    #     if direction == 1:
    #         # TODO: km to miles conversion
    #         # km = float(input("Enter distance in km: "))
    #         # result = km * MILES_PER_KM
    #         # result_msg = f"{km} km = {result:.3f} miles"
    #         # converted = True
    #     elif direction == 2:
    #         # TODO: miles to km conversion
    #         # miles = float(input("Enter distance in miles: "))
    #         # result = miles / MILES_PER_KM
    #         # result_msg = f"{miles} miles = {result:.3f} km"
    #         # converted = True
    #     else:
    #         print("Invalid option")

    # ===== TEMPERATURE CONVERSION (Choice 2) =====
    # TODO: Implement temperature conversion
    # Core concept: Temperature formulas with proper precision
    # elif choice == 2:
    #     direction = int(input("\n1) °C → °F\n2) °F → °C\nChoose: "))
    #     if direction == 1:
    #         # TODO: Celsius to Fahrenheit conversion
    #         # c = float(input("Enter temperature in °C: "))
    #         # result = c * 9/5 + 32
    #         # result_msg = f"{c} °C = {result:.2f} °F"
    #         # converted = True
    #     elif direction == 2:
    #         # TODO: Fahrenheit to Celsius conversion
    #         # f = float(input("Enter temperature in °F: "))
    #         # result = (f - 32) * 5/9
    #         # result_msg = f"{f} °F = {result:.2f} °C"
    #         # converted = True
    #     else:
    #         print("Invalid option")

    # ===== WEIGHT CONVERSION (Choice 3) =====
    # TODO: Implement weight conversion
    # Core concept: Mass unit conversions with standard precision
    # elif choice == 3:
    #     direction = int(input("\n1) kg → lb\n2) lb → kg\nChoose: "))
    #     if direction == 1:
    #         # TODO: Kilograms to pounds conversion
    #         # kg = float(input("Enter weight in kg: "))
    #         # result = kg * POUNDS_PER_KG
    #         # result_msg = f"{kg} kg = {result:.3f} lb"
    #         # converted = True
    #     elif direction == 2:
    #         # TODO: Pounds to kilograms conversion
    #         # lb = float(input("Enter weight in lb: "))
    #         # result = lb / POUNDS_PER_KG
    #         # result_msg = f"{lb} lb = {result:.3f} kg"
    #         # converted = True
    #     else:
    #         print("Invalid option")

    # ===== CURRENCY CONVERSION (Choice 4) =====
    # TODO: Implement currency conversion
    # Core concept: Financial calculations with appropriate precision
    # elif choice == 4:
    #     direction = int(input("\n1) EUR → USD\n2) USD → EUR\nChoose: "))
    #     if direction == 1:
    #         # TODO: Euro to US Dollar conversion
    #         # eur = float(input("Enter amount in EUR: "))
    #         # result = eur * EUR_TO_USD
    #         # result_msg = f"{eur} EUR = {result:.2f} USD"
    #         # converted = True
    #     elif direction == 2:
    #         # TODO: US Dollar to Euro conversion
    #         # usd = float(input("Enter amount in USD: "))
    #         # result = usd / EUR_TO_USD
    #         # result_msg = f"{usd} USD = {result:.2f} EUR"
    #         # converted = True
    #     else:
    #         print("Invalid option")

    # ===== DATA CONVERSION (Choice 5) =====
    # TODO: Implement data conversion
    # Core concept: Digital storage unit conversions
    # elif choice == 5:
    #     direction = int(input("\n1) MB → GB\n2) GB → MB\nChoose: "))
    #     if direction == 1:
    #         # TODO: Megabytes to Gigabytes conversion
    #         # mb = float(input("Enter size in MB: "))
    #         # result = mb / MB_PER_GB
    #         # result_msg = f"{mb} MB = {result:.3f} GB"
    #         # converted = True
    #     elif direction == 2:
    #         # TODO: Gigabytes to Megabytes conversion
    #         # gb = float(input("Enter size in GB: "))
    #         # result = gb * MB_PER_GB
    #         # result_msg = f"{gb} GB = {result:.3f} MB"
    #         # converted = True
    #     else:
    #         print("Invalid option")

    # TODO: Display result and update counter
    # Core concept: Centralized result handling and progress tracking
    # if converted:
    #     conversion_count += 1
    #     print(result_msg)
    #     print(f"Conversions performed: {conversion_count}")

# ===== TESTING CHECKLIST =====
#
# □ All 5 conversion categories work correctly
# □ Bidirectional conversions produce accurate results
# □ Menu validation handles invalid choices gracefully
# □ Session counter tracks conversions properly
# □ Output formatting uses appropriate decimal precision
# □ Program exits cleanly with summary
#
# ===== ENHANCEMENT IDEAS (For Later Versions) =====
#
# v2 (Functions): Extract conversion logic into pure functions
# v2.1 (Exceptions): Add bulletproof error handling and input validation
# v3 (Classes): Create Converter classes with inheritance
# v4 (Modules): Organize into importable modules
# v5 (GUI): Add graphical user interface
#
# ===== DEBUGGING TIPS =====
#
# 1. Test each conversion category individually
# 2. Verify formulas with known values (e.g., 0°C = 32°F)
# 3. Check decimal precision matches requirements
# 4. Ensure counter only increments on successful conversions
# 5. Test edge cases like zero values and large numbers
