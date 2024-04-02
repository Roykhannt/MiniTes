import requests
from datetime import datetime

api_key = "0bd18c77aafa5fef4edf29a23bac011f"
city = "Jakarta"
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
print("Weather forecast:")

if response.status_code == 200:
    data = response.json()
    daily_data = {}
    for forecast in data["list"]:
        date = forecast["dt_txt"].split()[0]
        if date not in daily_data:
            daily_data[date] = forecast["main"]["temp"]
    for date, temp in daily_data.items():
        formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime("%a, %d %B %Y")
        print(f"{formatted_date}: {temp}°C")
else:
    print("Error:", response.status_code)

