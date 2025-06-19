#Weather app using request and API
import requests


API_KEY = '025b79582054465c255a2f38a85de835'
BASIC_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
         'APPID': API_KEY,
         'q': city,
         'units': 'metric',
         'lang': 'en'
     }
    try:
        response = requests.get(BASIC_URL, params)
        data = response.json()

        if response.status_code == 200:
            weather = data['weather'][0]['description'].capitalize()
            temperature = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            print(f"\n🌤️ Weather in {city.title()}:")
            print(f"📝 {weather}")
            print(f"🌡️ Temp: {temperature}°C (Feels like {feels_like}°C)")
            print(f"💧 Humidity: {humidity}%\n")
        else:
            print("Weather not found.")
    except Exception as e:
        print("Faild to get weather.")

def main():
    print(" Welcome to Weather App")
    while True:
        print("Welcome to the weather app. Enter the city you wish to get weather for or 'quit to exit the app.")
        city = input("\nEnter the city you want to get weather for: ")
        if city.lower() == "q" or city.lower() == "quit":
            print("\nThank you for using Weather App")
            break
        get_weather(city)

if __name__ == "__main__":
    main()

