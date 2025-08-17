# Scope: primitives, control flow, strings, functions (+ import random)
# No try/except, no comprehensions, no classes.
print("*********** Welcome to Smart Converter v1.2 ***********")

# Constants (just variables)
MILES_PER_KM = 0.621371
POUNDS_PER_KG = 2.20462
EUR_TO_USD = 1.08
MB_PER_GB = 1024

conversion_count = 0

while True:
    print("\n" + "=" * 50)
    print("🧮 Smart Converter v1.0")
    choice = int(input(
        "- Menu -\n"
        "1) Length (km ↔ miles)\n"
        "2) Temperature (°C ↔ °F)\n"
        "3) Weight (kg ↔ lb)\n"
        "4) Currency (EUR ↔ USD)\n"
        "5) Data (MB ↔ GB)\n"
        "6) Quit\n"
        "Choose a conversion option (1-6): "
    ))

    # quick guard (still no try/except)
    if choice < 1 or choice > 6:
        print("Invalid option. Please choose 1-6.")
        continue

    if choice == 6:
        print("Thank you for using Smart Converter!")
        print(f"Total conversions performed: {conversion_count}")
        break

    converted = False  # track if a valid conversion happened
    result_msg = ""    # store the final message to print once

    if choice == 1:
        direction = int(input("\n1) km → miles\n2) miles → km\nChoose: "))
        if direction == 1:
            km = float(input("Enter distance in km: "))
            result = km * MILES_PER_KM
            result_msg = f"{km} km = {result:.3f} miles"
            converted = True
        elif direction == 2:
            miles = float(input("Enter distance in miles: "))
            result = miles / MILES_PER_KM
            result_msg = f"{miles} miles = {result:.3f} km"
            converted = True
        else:
            print("Invalid option")

    elif choice == 2:
        direction = int(input("\n1) °C → °F\n2) °F → °C\nChoose: "))
        if direction == 1:
            c = float(input("Enter temperature in °C: "))
            result = c * 9/5 + 32
            result_msg = f"{c} °C = {result:.2f} °F"
            converted = True
        elif direction == 2:
            f = float(input("Enter temperature in °F: "))
            result = (f - 32) * 5/9
            result_msg = f"{f} °F = {result:.2f} °C"
            converted = True
        else:
            print("Invalid option")

    elif choice == 3:
        direction = int(input("\n1) kg → lb\n2) lb → kg\nChoose: "))
        if direction == 1:
            kg = float(input("Enter weight in kg: "))
            result = kg * POUNDS_PER_KG
            result_msg = f"{kg} kg = {result:.3f} lb"
            converted = True
        elif direction == 2:
            lb = float(input("Enter weight in lb: "))
            result = lb / POUNDS_PER_KG
            result_msg = f"{lb} lb = {result:.3f} kg"
            converted = True
        else:
            print("Invalid option")

    elif choice == 4:
        direction = int(input("\n1) EUR → USD\n2) USD → EUR\nChoose: "))
        if direction == 1:
            eur = float(input("Enter amount in EUR: "))
            result = eur * EUR_TO_USD
            result_msg = f"{eur} EUR = {result:.2f} USD"
            converted = True
        elif direction == 2:
            usd = float(input("Enter amount in USD: "))
            result = usd / EUR_TO_USD
            result_msg = f"{usd} USD = {result:.2f} EUR"
            converted = True
        else:
            print("Invalid option")

    elif choice == 5:
        direction = int(input("\n1) MB → GB\n2) GB → MB\nChoose: "))
        if direction == 1:
            mb = float(input("Enter size in MB: "))
            result = mb / MB_PER_GB
            result_msg = f"{mb} MB = {result:.3f} GB"
            converted = True
        elif direction == 2:
            gb = float(input("Enter size in GB: "))
            result = gb * MB_PER_GB
            result_msg = f"{gb} GB = {result:.3f} MB"
            converted = True
        else:
            print("Invalid option")

    # single print+counter place
    if converted:
        conversion_count += 1
        print(result_msg)
        print(f"Conversions performed: {conversion_count}")
