import requests
import json
baseUrl = "http://api.weatherapi.com/v1"

city = input("Enter city/region: ")

response = requests.get(baseUrl+f'/current.json?key=7739e42c316d4967aaa53455242003&q={city}&aqi=yes')
data = json.loads(response.text)
print(f"""
Date: {data['current']['last_updated']}
Location: {data['location']['name']},{data['location']['region']},{data['location']['country']}
Weather:
\tTemperature = {data['current']['temp_c']}*C  or {data['current']['temp_f']}*F
\tCondition = {data['current']['condition']['text']}
\tHumidity = {data['current']['humidity']}
\tAQI = {data['current']['air_quality']['o3']}
""")