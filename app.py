from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "92e92fd164f2a8e5f1f8b9a5083c108e"

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None

    if request.method == "POST":
        city = request.form["city"]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()
        print(data)
        print(response.status_code)
        print(data)

        if data.get("cod") == 200:
            weather = {
                "city": city,
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"]
            }

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)