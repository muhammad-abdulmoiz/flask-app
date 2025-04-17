from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_KEY = '3ac9190d2137d4d9534aaf185cc21e4d'

@app.route('/')
def home():
    return "Welcome to Flask Weather App!"

@app.route('/weather')
def get_weather():
    lat = request.args.get('lat', default=44.34)
    lon = request.args.get('lon', default=-10.99)
    
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}"
    
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
