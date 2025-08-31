# Smart Unit Converter v2.1 — Robust Exception Handling
# Scope: primitives, control flow, strings, functions + exceptions
# Features: Comprehensive error handling, input validation, retry loops

# Constants (immutable config at module scope; not modified)
MILES_PER_KM = 0.621371
POUNDS_PER_KG = 2.20462
EUR_TO_USD = 1.08
MB_PER_GB = 1024

# Physical constraints
ABSOLUTE_ZERO_C = -273.15
ABSOLUTE_ZERO_F = -459.67


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


# ---------- Safe Input Functions (with exception handling) ----------
def safe_get_number(prompt, min_val=None, max_val=None, unit=""):
    """Get a number with validation and retry loop."""
    while True:
        try:
            raw = input(prompt)
            value = float(raw)
        except ValueError:
            print("❌ Please enter a valid number")
            continue
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Goodbye!")
            raise SystemExit(0)
        else:
            # Block non-finite numbers (NaN, inf, -inf)
            if value != value or value in (float("inf"), float("-inf")):
                print("❌ Please enter a finite number")
                continue

            # Range validation
            if min_val is not None and value < min_val:
                print(f"❌ Value must be >= {min_val}{unit}")
                continue
            if max_val is not None and value > max_val:
                print(f"❌ Value must be <= {max_val}{unit}")
                continue

            return value


def safe_get_menu_choice():
    """Get menu choice with validation and retry loop."""
    while True:
        try:
            choice = int(input("Choose a conversion option (1-6): "))
            if 1 <= choice <= 6:
                return choice
            print("❌ Please choose a number between 1-6")
        except ValueError:
            print("❌ Please enter a valid number")
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Goodbye!")
            raise SystemExit(0)


def safe_get_direction(opt1_label, opt2_label):
    """Get direction choice with validation and retry loop."""
    while True:
        try:
            print(f"\n1) {opt1_label}")
            print(f"2) {opt2_label}")
            direction = int(input("Choose direction (1 or 2): "))
            if direction in (1, 2):
                return direction
            print("❌ Please choose 1 or 2")
        except ValueError:
            print("❌ Please enter 1 or 2")
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Goodbye!")
            raise SystemExit(0)


# ---------- I/O helpers (no business logic) ----------
def display_menu():
    """Display menu and get user choice safely."""
    print("\n" + "=" * 50)
    print("🧮 Smart Converter v2.1 - Bulletproof Edition")
    print("- Menu -")
    print("1) Length (km ↔ miles)")
    print("2) Temperature (°C ↔ °F)")
    print("3) Weight (kg ↔ lb)")
    print("4) Currency (EUR ↔ USD)")
    print("5) Data (MB ↔ GB)")
    print("6) Quit")

    return safe_get_menu_choice()


def format_result(value_in, value_out, in_label, out_label, decimals=3):
    """Format conversion result with consistent decimal places for both input and output."""
    return f"{value_in:.{decimals}f} {in_label} = {value_out:.{decimals}f} {out_label}"


# ---------- Orchestrator with Robust Error Handling ----------
def run_converter():
    """Main converter loop with comprehensive exception handling."""
    # Welcome banner (moved here for import safety)
    print("*********** Welcome to Smart Converter v2.1 ***********")
    print("🛡️ All inputs are now protected with error handling!")
    print("Try entering invalid values - the program won't crash! 🚀")

    conversion_count = 0

    while True:
        try:
            choice = display_menu()

            if choice == 6:
                print("Thank you for using Smart Converter v2.1!")
                print(f"Total conversions performed: {conversion_count}")
                break

            converted = False  # track if a valid conversion happened
            result_msg = ""    # store the final message to print once

            if choice == 1:  # Length conversion
                direction = safe_get_direction("km → miles", "miles → km")
                if direction == 1:
                    km = safe_get_number(
                        "Enter distance in km: ", min_val=0, unit=" km")
                    miles = km_to_miles(km)
                    result_msg = format_result(km, miles, "km", "miles")
                    converted = True
                elif direction == 2:
                    miles = safe_get_number(
                        "Enter distance in miles: ", min_val=0, unit=" miles")
                    km = miles_to_km(miles)
                    result_msg = format_result(miles, km, "miles", "km")
                    converted = True

            elif choice == 2:  # Temperature conversion
                direction = safe_get_direction("°C → °F", "°F → °C")
                if direction == 1:
                    c = safe_get_number(
                        "Enter temperature in °C: ", min_val=ABSOLUTE_ZERO_C, unit="°C")
                    f = c_to_f(c)
                    result_msg = format_result(c, f, "°C", "°F", decimals=2)
                    converted = True
                elif direction == 2:
                    f = safe_get_number(
                        "Enter temperature in °F: ", min_val=ABSOLUTE_ZERO_F, unit="°F")
                    c = f_to_c(f)
                    result_msg = format_result(f, c, "°F", "°C", decimals=2)
                    converted = True

            elif choice == 3:  # Weight conversion
                direction = safe_get_direction("kg → lb", "lb → kg")
                if direction == 1:
                    kg = safe_get_number(
                        "Enter weight in kg: ", min_val=0, unit=" kg")
                    lb = kg_to_lb(kg)
                    result_msg = format_result(kg, lb, "kg", "lb")
                    converted = True
                elif direction == 2:
                    lb = safe_get_number(
                        "Enter weight in lb: ", min_val=0, unit=" lb")
                    kg = lb_to_kg(lb)
                    result_msg = format_result(lb, kg, "lb", "kg")
                    converted = True

            elif choice == 4:  # Currency conversion
                direction = safe_get_direction("EUR → USD", "USD → EUR")
                if direction == 1:
                    eur = safe_get_number(
                        "Enter amount in EUR: ", min_val=0, unit=" EUR")
                    usd = eur_to_usd(eur)
                    result_msg = format_result(
                        eur, usd, "EUR", "USD", decimals=2)
                    converted = True
                elif direction == 2:
                    usd = safe_get_number(
                        "Enter amount in USD: ", min_val=0, unit=" USD")
                    eur = usd_to_eur(usd)
                    result_msg = format_result(
                        usd, eur, "USD", "EUR", decimals=2)
                    converted = True

            elif choice == 5:  # Data conversion
                direction = safe_get_direction("MB → GB", "GB → MB")
                if direction == 1:
                    mb = safe_get_number(
                        "Enter size in MB: ", min_val=0, unit=" MB")
                    gb = mb_to_gb(mb)
                    result_msg = format_result(mb, gb, "MB", "GB")
                    converted = True
                elif direction == 2:
                    gb = safe_get_number(
                        "Enter size in GB: ", min_val=0, unit=" GB")
                    mb = gb_to_mb(gb)
                    result_msg = format_result(gb, mb, "GB", "MB")
                    converted = True

            # Display result and update counter
            if converted:
                conversion_count += 1
                print(f"✅ {result_msg}")
                print(f"📊 Conversions performed: {conversion_count}")

        except Exception as e:
            # Catch any unexpected errors (shouldn't happen with proper input validation)
            print("❌ Unexpected error. Returning to main menu...")
            print("🔄 Please try again or contact support if this persists.")
            # For debugging: print(f"(debug) {e!r}")
            continue


if __name__ == "__main__":
    run_converter()
