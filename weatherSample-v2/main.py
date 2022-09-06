from flask import Flask, render_template
import requests, json

app = Flask(__name__)

@app.route(f"/")
def home():
    # New York
    api_url="http://api.weatherapi.com/v1/current.json?key=25aea85b29904b80bb244012220507&q=New%20York&aqi=no"
    response = requests.get(api_url)
    response.raise_for_status()
    if response.status_code != 204:
        res = json.loads(response.content.decode('utf-8'))
        temp = res['current']['temp_c']
        wind_speed = res['current']['condition']['text']
        weather_code = res['current']['cloud']

        if weather_code < 10 and weather_code > 0:
            weather="Mainly Clear"
        elif weather_code > 40 and weather_code < 50:
            weather = "Fog"
        elif weather_code > 50 and weather_code < 56:
            weather = "Drizzle"
        elif weather_code > 60 and weather_code < 70:
            weather = "Light Rain"
        else:
            weather = "Rain"

        return render_template("index.html",temp=temp,wind_speed=wind_speed,weather=weather, location='New York')

    else:

        print("Error: "+response.status_code)
        
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')