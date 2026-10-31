# 5. Live Cryptocurrency Price Fetcher

import requests


# CoinGecko API URL
API_URL = "https://api.coingecko.com/api/v3/simple/price"


# Function to fetch cryptocurrency prices
def get_crypto_prices():

    # Cryptocurrency IDs
    crypto_ids = "bitcoin,ethereum,dogecoin,solana,ripple"

    # Currencies in which prices will be displayed
    currencies = "usd,inr"

    params = {
        "ids": crypto_ids,
        "vs_currencies": currencies
    }

    try:
        # Send request to CoinGecko API
        response = requests.get(API_URL, params=params, timeout=15)

        # Check response status
        response.raise_for_status()

        # Convert JSON response into dictionary
        data = response.json()

        # Display cryptocurrency prices
        print("\n===== LIVE CRYPTOCURRENCY PRICES =====")

        for coin, price in data.items():

            print("\nCryptocurrency:", coin.capitalize())

            print("Price in USD: $", price["usd"])

            print("Price in INR: ₹", price["inr"])

            print("--------------------------------")

    except requests.exceptions.RequestException as e:
        print("Unable to fetch cryptocurrency prices.")
        print("Error:", e)

    except (KeyError, ValueError):
        print("Error processing cryptocurrency data.")


# Main program
print("===== CRYPTOCURRENCY PRICE FETCHER =====")

get_crypto_prices()


