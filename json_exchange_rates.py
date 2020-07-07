import json


# create a class Exchange Rates

class ExchangeRates:
    # with required attributes
    def __init__(self):
        pass

        # method to return the exchange rates

    def fetch_ExchangeRates(self):
        with open("exchange_rates.json", "r") as jsonfile:
            dataset = json.load(jsonfile)
            # For loop to get all exchange rates
            for e in dataset:
                if e == "rates":
                    print(dataset(["rates"]))
            currency = input("What currency would you like the exchange rate of, please see list.\n")
            # display exchange rates with specific currencies
            print(dataset["rates"][currency])

e = ExchangeRates
e.__init__(ExchangeRates)

# fetch the data from exchange_rates.json
# method to return the exchange rates


# creating an object of class
# rate_display = ExchangeRates ("exchange_rates.json")

# print(rate_display.rates)

# display the data

# display the type of data


# method to return the exchange rates
# display exchange rates with specific currencies
