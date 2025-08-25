import requests

API_KEY = "404c93ef558024e5dec9943d45383046"  # Get from openweathermap.org
CITY = "Varanasi,IN"

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url).json()
print("API Response:", response)

temperature = response["main"]["temp"]
humidity = response["main"]["humidity"]
rainfall = response.get("rain", {}).get("1h", 0)  # Rainfall in last 1 hour
print(f"Temp: {temperature}°C, Humidity: {humidity}%, Rainfall: {rainfall}mm")
