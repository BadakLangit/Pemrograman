import requests

# Function to fetch exchange rates
def fetch_exchange_rate(base_currency, target_currency):
    api_url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        rates = response.json()["rates"]
        if target_currency in rates:
            return rates[target_currency]
        else:
            raise ValueError(f"Currency {target_currency} not supported.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None

# Main conversion function
def convert_currency(amount, base_currency, target_currency):
    rate = fetch_exchange_rate(base_currency, target_currency)
    if rate:
        converted_amount = amount * rate
        return converted_amount
    else:
        return None

# User Input
def main():
    print("Currency Converter")
    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    target_currency = input("Enter the target currency (e.g., EUR): ").upper()
    try:
        amount = float(input("Enter the amount to convert: "))
        converted_amount = convert_currency(amount, base_currency, target_currency)
        if converted_amount is not None:
            print(f"{amount:.2f} {base_currency} = {converted_amount:.2f} {target_currency}")
        else:
            print("Conversion failed.")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

if __name__ == "__main__":
    main()
