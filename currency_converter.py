# ---------------------------
#   Currency Converter
# ---------------------------

# Supported currencies with full name and symbol
supported_currencies = {
    "USD": {"name": "US Dollar", "symbol": "$"},
    "EUR": {"name": "Euro", "symbol": "€"},
    "GBP": {"name": "British Pound", "symbol": "£"},
    "PKR": {"name": "Pakistani Rupee", "symbol": "₨"},
    "INR": {"name": "Indian Rupee", "symbol": "₹"},
    "JPY": {"name": "Japanese Yen", "symbol": "¥"},
    "SAR": {"name": "Saudi Riyal", "symbol": "﷼"}
}

# Exchange rates relative to USD (1 USD = ? target currency)
usd_rates = {
    "USD": 1.0,      # Base
    "EUR": 0.91,
    "GBP": 0.79,
    "PKR": 277.5,
    "INR": 83.1,
    "JPY": 147.2,
    "SAR": 3.75
}

# Mapping symbols to codes for easier input
currency_symbols = {info["symbol"]: code for code, info in supported_currencies.items()}


def show_message():
    """Welcome message and display available currencies with full names and symbols."""
    print("\n🌍 Welcome to the   Currency Converter 🌍")
    print("You can convert between the following currencies (or type 'exit' anytime):\n")
    for code, info in supported_currencies.items():
        print(f" {code} - {info['name']} ({info['symbol']})")


def get_currency_input(prompt_text):
    """Get a valid currency code or symbol from the user."""
    while True:
        code = input(prompt_text).upper().strip()

        # Allow exit
        if code.lower() == "exit":
            print("\n👋 Exiting Currency Converter. Goodbye!\n")
            exit()

        # Support symbol input (₹, $, etc.)
        if code in supported_currencies:
            return code
        elif code in currency_symbols:
            return currency_symbols[code]
        else:
            print("❌ Unsupported currency. Please choose from the list shown.")


def get_amount_input(currency_code):
    """Safely get the amount input from the user (numeric and positive only)."""
    while True:
        user_input = input(
            f"Enter the amount in {currency_code} "
            f"({supported_currencies[currency_code]['name']}): "
        )
        try:
            amount = float(user_input)
            if amount < 0:
                print("❌ Please enter a positive amount.")
            else:
                return amount
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")


def convert_currency(from_currency, to_currency, amount):
    """Convert currency using USD as the base reference."""
    if from_currency == to_currency:
        return amount, 1.0  # Same currency

    # Step 1: Convert from source → USD
    amount_in_usd = amount / usd_rates[from_currency]

    # Step 2: Convert USD → target
    result = amount_in_usd * usd_rates[to_currency]

    # Exchange rate: how much 1 unit of source = target
    rate = usd_rates[to_currency] / usd_rates[from_currency]

    return result, rate


def main():
    """Main program logic with loop option and history feature."""
    history = []  # store last 5 conversions

    while True:
        show_message()

        # Get source and target currencies
        from_currency = get_currency_input("\nEnter the currency you want to convert FROM: ")
        to_currency = get_currency_input("Enter the currency you want to convert TO: ")

        # Get amount safely
        amount = get_amount_input(from_currency)

        try:
            # Perform conversion
            result, rate = convert_currency(from_currency, to_currency, amount)

            # Save to history
            history.append(f"{amount:,.2f} {from_currency} → {result:,.2f} {to_currency}")
            if len(history) > 5:
                history.pop(0)

            # Display result
            print("\n📊 Conversion Result:")
            print(f" {amount:,.2f} {from_currency} ({supported_currencies[from_currency]['name']}, {supported_currencies[from_currency]['symbol']})")
            print(f"   = {result:,.2f} {to_currency} ({supported_currencies[to_currency]['name']}, {supported_currencies[to_currency]['symbol']}) ✅")
            print(f" 💱 Exchange Rate: 1 {from_currency} = {rate:.4f} {to_currency}\n")

            # Show recent history
            if history:
                print("📝 Recent Conversions:")
                for h in history:
                    print(" -", h)
                print()

        except Exception as e:
            print(f"\n❌ Error: {e}")

        # Loop control
        again = input("➡️ Convert again? (y/n): ").strip().lower()
        if again.startswith("y"):
            continue
        elif again.startswith("n"):
            print("\n👋 Thank you for using the  Currency Converter. Goodbye!\n")
            break
        else:
            print("❌ Invalid choice. Exiting program.\n")
            break


# Run program
if __name__ == "__main__":
    main()
