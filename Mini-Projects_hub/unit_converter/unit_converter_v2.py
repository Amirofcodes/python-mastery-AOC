# Scope: primitives, control flow, strings, functions (+ import random)
# No try/except, no comprehensions, no classes.

print("*********** Welcome to Smart Converter v2.0 ***********")

# Constants (immutable config at module scope; not modified)
MILES_PER_KM = 0.621371
POUNDS_PER_KG = 2.20462
EUR_TO_USD = 1.08
MB_PER_GB = 1024


# ---------- Pure conversion functions (math only) ----------
def km_to_miles(km):
    return km * MILES_PER_KM


def miles_to_km(miles):
    return miles / MILES_PER_KM


def c_to_f(c):
    return c * 9 / 5 + 32


def f_to_c(f):
    return (f - 32) * 5 / 9


def kg_to_lb(kg):
    return kg * POUNDS_PER_KG


def lb_to_kg(lb):
    return lb / POUNDS_PER_KG


def eur_to_usd(eur):
    return eur * EUR_TO_USD


def usd_to_eur(usd):
    return usd / EUR_TO_USD


def mb_to_gb(mb):
    return mb / MB_PER_GB


def gb_to_mb(gb):
    return gb * MB_PER_GB


# ---------- I/O helpers (no business logic) ----------
def display_menu():
    print("\n" + "=" * 50)
    print("🧮 Smart Converter v2.0")
    choice = int(
        input(
            "- Menu -\n"
            "1) Length (km ↔ miles)\n"
            "2) Temperature (°C ↔ °F)\n"
            "3) Weight (kg ↔ lb)\n"
            "4) Currency (EUR ↔ USD)\n"
            "5) Data (MB ↔ GB)\n"
            "6) Quit\n"
            "Choose a conversion option (1-6): "
        )
    )
    return choice


def choose_direction(opt1_label, opt2_label):
    direction = int(input("\n1) " + opt1_label + "\n2) " +
                    opt2_label + "\nChoose: "))
    if direction != 1 and direction != 2:
        print("Invalid option")
        return 0
    return direction


def read_float(prompt):
    return float(input(prompt))


def format_result(value_in, value_out, in_label, out_label, decimals=3):
    # keep formatting simple; temp uses 2 decimals via caller
    return f"{value_in} {in_label} = {value_out:.{decimals}f} {out_label}"


# ---------- Orchestrator ----------
def run_converter():
    conversion_count = 0

    while True:
        choice = display_menu()

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
            direction = choose_direction("km → miles", "miles → km")
            if direction == 1:
                km = read_float("Enter distance in km: ")
                miles = km_to_miles(km)
                result_msg = format_result(km, miles, "km", "miles")
                converted = True
            elif direction == 2:
                miles = read_float("Enter distance in miles: ")
                km = miles_to_km(miles)
                result_msg = format_result(miles, km, "miles", "km")
                converted = True

        elif choice == 2:
            direction = choose_direction("°C → °F", "°F → °C")
            if direction == 1:
                c = read_float("Enter temperature in °C: ")
                f = c_to_f(c)
                result_msg = format_result(c, f, "°C", "°F", decimals=2)
                converted = True
            elif direction == 2:
                f = read_float("Enter temperature in °F: ")
                c = f_to_c(f)
                result_msg = format_result(f, c, "°F", "°C", decimals=2)
                converted = True

        elif choice == 3:
            direction = choose_direction("kg → lb", "lb → kg")
            if direction == 1:
                kg = read_float("Enter weight in kg: ")
                lb = kg_to_lb(kg)
                result_msg = format_result(kg, lb, "kg", "lb")
                converted = True
            elif direction == 2:
                lb = read_float("Enter weight in lb: ")
                kg = lb_to_kg(lb)
                result_msg = format_result(lb, kg, "lb", "kg")
                converted = True

        elif choice == 4:
            direction = choose_direction("EUR → USD", "USD → EUR")
            if direction == 1:
                eur = read_float("Enter amount in EUR: ")
                usd = eur_to_usd(eur)
                result_msg = format_result(eur, usd, "EUR", "USD", decimals=2)
                converted = True
            elif direction == 2:
                usd = read_float("Enter amount in USD: ")
                eur = usd_to_eur(usd)
                result_msg = format_result(usd, eur, "USD", "EUR", decimals=2)
                converted = True

        elif choice == 5:
            direction = choose_direction("MB → GB", "GB → MB")
            if direction == 1:
                mb = read_float("Enter size in MB: ")
                gb = mb_to_gb(mb)
                result_msg = format_result(mb, gb, "MB", "GB")
                converted = True
            elif direction == 2:
                gb = read_float("Enter size in GB: ")
                mb = gb_to_mb(gb)
                result_msg = format_result(gb, mb, "GB", "MB")
                converted = True

        # single print+counter place
        if converted:
            conversion_count += 1
            print(result_msg)
            print(f"Conversions performed: {conversion_count}")


if __name__ == "__main__":
    run_converter()
