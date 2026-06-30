# 🌦️  Weather App

A simple Weather App built using **Python**, **Flask**, and the **OpenWeather API**. Users can enter a city name to view the current weather information, including temperature, humidity, and weather conditions.

---

## 📌 Features

- 🌍 Search weather by city name
- 🌡️ Display current temperature (°C)
- 💧 Display humidity
- ☁️ Display weather description
- 🎨 Simple and responsive user interface

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Requests Library
- OpenWeather API

---

## 📁 Project Structure

```
Weather-App/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Flask-Weather-App.git
```

### 2. Go to the project folder

```bash
cd Flask-Weather-App
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Add your OpenWeather API Key

Open `app.py` and replace:

```python
API_KEY = "YOUR_API_KEY"
```

with your own API key.

### 5. Run the application

```bash
python app.py
```

### 6. Open in your browser

```
http://127.0.0.1:5000
```

---

## 📸 Output

- Enter a city name.
- Click **Search**.
- View the current temperature, humidity, and weather description.

---

## 📖 How It Works

1. User enters a city name.
2. Flask receives the request.
3. The application sends a request to the OpenWeather API.
4. The API returns weather data in JSON format.
5. Flask extracts the required information.
6. The weather details are displayed on the webpage.



## 📄 License

This project is created for learning and internship purposes.
