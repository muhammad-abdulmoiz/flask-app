from flask import Flask, jsonify, request
import requests, json

app = Flask(__name__)

API_KEY = ''

weather_history = []
MAX_HISTORY = 5

@app.route('/')
def home():
    return "Welcome to Flask Weather App!"

@app.route('/weather')
def get_weather():
    lat = request.args.get('lat', default=44.34)

    lon = request.args.get('lon', default=-10.99)
    
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}"
    
    response = requests.get(url)
    data = json.loads(response.text)
    
    # Structured result using the JSON Response
    # (This structure is based on the API Response in documentation, and needs to be updated)
    result = {
        "location": data.get("name"),
        "temperature": {
            "current": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "min": data["main"]["temp_min"],
            "max": data["main"]["temp_max"]
        },
        "pressure": data["main"]["pressure"],
        "humidity": data["main"]["humidity"],
        "weather": {
            "main": data["weather"][0]["main"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"]
        },
        "wind": data.get("wind"),
        "clouds": data.get("clouds"),
        "rain": data.get("rain", {}),
        "time": data.get("dt")
    }
    
    weather_history.append(result)
    if len(weather_history) > MAX_HISTORY:
        weather_history.pop(0)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
