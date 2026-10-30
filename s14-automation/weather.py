import httpx

URL = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 37.5665,
    "longitude": 126.978,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    "timezone": "Asia/Seoul",
}

response = httpx.get(URL, params=params, timeout=10)
print(response.status_code)
data = response.json()
now = data["current"]
print(f"서울 {now['time']}")
print(f"기온 {now['temperature_2m']}°C · 습도 {now['relative_humidity_2m']}%")
