print("*********** Welcome to Smart Converter v1.0 ***********")

conversion_count = 0

while True:
    print("\n" + "="*50)
    choice = int(input("- Menu -\n1 for Length (km ↔ miles)\n2 for Temperature (°C ↔ °F)\n3 for Weight (kg ↔ lb)\n4 for Currency (EUR ↔ USD)\n5 for Data (MB ↔ GB)\n6 to quit\nChoose a conversion option: "))
    if choice == 1:
        length = int(input(
            "\n1 for (km → miles)\n2 for (miles → km)\nChoose a conversion option: "))
        if length == 1:
            km = float(input("Enter distance in km: "))
            result = km * 0.621371
            conversion_count += 1
            print(f"{km} km = {result:.3f} miles")
            print(f"Conversions performed: {conversion_count}")
        elif length == 2:
            miles = float(input("Enter distance in miles: "))
            result = miles / 0.621371
            conversion_count += 1
            print(f"{miles} miles = {result:.3f} km")
            print(f"Conversions performed: {conversion_count}")
        else:
            print("Invalid option")
    elif choice == 2:
        temperature = int(
            input("1 for (°C → °F)\n2 for (°F → °C)\nChoose a conversion option: "))
        if temperature == 1:
            celsius = float(input("Enter temperature in °C: "))
            result = celsius * 9/5 + 32
            conversion_count += 1
            print(f"{celsius} °C = {result:.2f} °F")
            print(f"Conversions performed: {conversion_count}")
        elif temperature == 2:
            fahrenheit = float(input("Enter temperature in °F: "))
            result = (fahrenheit - 32) * 5/9
            conversion_count += 1
            print(f"{fahrenheit} °F = {result:.2f} °C")
            print(f"Conversions performed: {conversion_count}")
        else:
            print("Invalid option")
    elif choice == 3:
        weight = int(
            input("1 for (kg → lb)\n2 for (lb → kg)\nChoose a conversion option: "))
        if weight == 1:
            kg = float(input("Enter weight in kg: "))
            result = kg * 2.20462
            conversion_count += 1
            print(f"{kg} kg = {result:.3f} pounds")
            print(f"Conversions performed: {conversion_count}")
        elif weight == 2:
            pounds = float(input("Enter weight in pounds: "))
            result = pounds / 2.20462
            conversion_count += 1
            print(f"{pounds} pounds = {result:.3f} kg")
            print(f"Conversions performed: {conversion_count}")
        else:
            print("Invalid option")
    elif choice == 4:
        currency = int(
            input("1 for (EUR → USD)\n2 for (USD → EUR)\nChoose conversion option: "))
        if currency == 1:
            eur = float(input("Enter amount in EUR: "))
            result = eur * 1.08
            conversion_count += 1
            print(f"{eur} EUR = {result:.2f} USD")
            print(f"Conversions performed: {conversion_count}")
        elif currency == 2:
            usd = float(input("Enter amount in USD: "))
            result = usd / 1.08
            conversion_count += 1
            print(f"{usd} USD = {result:.2f} EUR")
            print(f"Conversions performed: {conversion_count}")
        else:
            print("Invalid option")
    elif choice == 5:
        data = int(
            input("1 for (MB → GB)\n2 for (GB → MB)\nChoose conversion option: "))
        if data == 1:
            mb = float(input("Enter size in MB: "))
            result = mb / 1024
            conversion_count += 1
            print(f"{mb} MB = {result:.3f} GB")
            print(f"Conversions performed: {conversion_count}")
        elif data == 2:
            gb = float(input("Enter size in GB: "))
            result = gb * 1024
            conversion_count += 1
            print(f"{gb} GB = {result:.3f} MB")
            print(f"Conversions performed: {conversion_count}")
        else:
            print("Invalid option")
    elif choice == 6:
        print(f"Thank you for using Smart Converter!")
        print(f"Total conversions performed: {conversion_count}")
        break
    else:
        print("Invalid option. Please choose 1-6.")
