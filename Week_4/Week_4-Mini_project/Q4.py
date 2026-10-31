# 4. Weather App Using OpenWeather API

import requests


# Enter your OpenWeather API key
API_KEY = "YOUR_API_KEY"

# OpenWeather API URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# Function to get weather information
def get_weather(city):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        # Send request to OpenWeather API
        response = requests.get(BASE_URL, params=params, timeout=10)

        # Check for errors
        response.raise_for_status()

        # Convert JSON response into Python dictionary
        data = response.json()

        # Extract weather information
        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        weather = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        # Display weather information
        print("\n===== WEATHER REPORT =====")

        print("City:", city_name)
        print("Country:", country)
        print("Temperature:", temperature, "°C")
        print("Feels Like:", feels_like, "°C")
        print("Weather:", weather)
        print("Humidity:", humidity, "%")
        print("Pressure:", pressure, "hPa")
        print("Wind Speed:", wind_speed, "m/s")

    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            print("City not found!")
        elif response.status_code == 401:
            print("Invalid API key!")
        else:
            print("HTTP Error:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Network Error:", e)

    except (KeyError, ValueError):
        print("Unable to process weather information.")


# Main program
print("===== WEATHER APPLICATION =====")

city = input("Enter city name: ")

if API_KEY == "YOUR_API_KEY":
    print("Please enter your OpenWeather API key first.")
elif city.strip():
    get_weather(city)
else:
    print("City name cannot be empty.")

