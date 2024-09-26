import requests

class Currency_convertor:
    rates = {}

    def __init__(self, url):
        # Fetch the data from the API
        data = requests.get(url).json()

        # Check if the API call was successful
        if data.get("success") == True:
            # Extract the rates from the response
            self.rates = data["rates"]
        else:
            # If the API call was unsuccessful, print the error and stop execution
            print("Error fetching data from API:", data.get("error", "Unknown error"))
            raise Exception("Failed to retrieve currency data.")

    def convert(self, from_currency, to_currency, amount):
        # Save the initial amount for display purposes
        initial_amount = amount

        # Check if from_currency is different from EUR (the base currency for the free plan)
        if from_currency != 'EUR':
            # Convert the amount to EUR first
            amount = amount / self.rates[from_currency]

        # Convert from EUR to the target currency
        amount = round(amount * self.rates[to_currency], 2)

        # Display the result
        print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))


# Driver code
if __name__ == "__main__":
    YOUR_ACCESS_KEY = '32ff292d98cd6e95a55e981447402f1b'  # Replace with your actual API key
    url = f'http://data.fixer.io/api/latest?access_key={YOUR_ACCESS_KEY}'

    try:
        c = Currency_convertor(url)
        from_country = input("From Country (e.g., USD, INR): ").upper()
        to_country = input("To Country (e.g., EUR, GBP): ").upper()
        amount = float(input("Amount: "))
        c.convert(from_country, to_country, amount)

    except Exception as e:
        print("An error occurred:", str(e))


