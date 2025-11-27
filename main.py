from flask import Flask, request, render_template
import requests
import pickle
import numpy as np

app = Flask(__name__)

API_KEY = "b42af580054e40ba272b70e3e856952d"

# Crop labels (adjust this list to match your model's training data)
CROP_LABELS = [
    'rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
    'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
    'banana', 'mango', 'grapes', 'watermelon', 'muskmelon',
    'apple', 'orange', 'papaya', 'coconut', 'cotton',
    'jute', 'coffee'
]

# Load your crop recommendation model
try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    print("Error: model.pkl not found. Please ensure the model file exists.")
    model = None


def get_weather_data(city):
    """Fetch weather data from OpenWeatherMap API"""
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get("cod") != 200:
            return None

        weather_data = {
            "temperature": round(data["main"]["temp"], 1),
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].title(),
            "rain": "rain" in data["weather"][0]["main"].lower()
        }
        return weather_data
    
    except Exception as e:
        print(f"Weather API Error: {e}")
        return None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form data
        N = float(request.form.get("nitrogen", 0))
        P = float(request.form.get("phosphorous", 0))
        K = float(request.form.get("potassium", 0))
        temperature = float(request.form.get("temperature", 0))
        humidity = float(request.form.get("humidity", 0))
        ph = float(request.form.get("ph", 0))
        rainfall = float(request.form.get("rainfall", 0))
        city = request.form.get("city", "").strip()

        if model is None:
            return render_template("error.html", error="Model not loaded.")

        # Prepare input data
        input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        
        # Check if prediction is probabilities or class index
        if isinstance(prediction, np.ndarray) and len(prediction) > 1:
            # Model returned probabilities, get the class with highest probability
            crop_index = np.argmax(prediction)
            crop_result = CROP_LABELS[crop_index]
        elif isinstance(prediction, (int, np.integer)):
            # Model returned class index
            crop_result = CROP_LABELS[prediction]
        else:
            # Model returned string (unlikely but handle it)
            crop_result = str(prediction)

        # Get weather data
        weather = None
        if city:
            weather = get_weather_data(city)
            if not weather:
                weather = {"error": "Unable to fetch weather data."}

        return render_template(
            "result.html",
            crop=crop_result,
            weather=weather,
            city=city
        )
    
    except Exception as e:
        print(f"Prediction error: {e}")
        return render_template("error.html", error=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)