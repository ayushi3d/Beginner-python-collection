
import requests

while True:
    city = input("Enter city name (or type 'q' to quit): ")

    if city.lower() == 'q':
        print("Goodbye! 🌦")
        break

    url = f"https://wttr.in/{city}?format=3"  # Short format: city, temp, condition
    response = requests.get(url)

    if response.status_code == 200:
        print("📡 Weather:", response.text)
    else:
        print("❌ Couldn't fetch weather. Try another city.\n")