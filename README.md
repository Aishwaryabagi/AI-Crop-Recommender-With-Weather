🌾 AgriAI – Intelligent Precision Farming System

AI-powered crop recommendation, real-time weather insights, and an interactive farming chatbot — now live on Vercel.

🔗 🌐 Live Demo (Hosted on Vercel)

👉 https://your-vercel-url.vercel.app/

((https://ai-argi.vercel.app/))

🚀 Overview

AgriAI is a modern precision agriculture platform that uses machine learning and real-time weather data to help farmers make smart, data-driven crop decisions.
It also includes a built-in AgriAI Chatbot that assists users with soil, weather, and farming questions.

This platform is fully deployed on Vercel, making it fast, secure, and globally accessible.

🌟 Key Features
✅ Machine Learning Crop Recommendation

Predicts the best crop based on:

Nitrogen (N)

Phosphorus (P)

Potassium (K)

pH level

Humidity

Temperature

Rainfall

✅ Weather API Integration

Live weather data fetched via OpenWeather API:

Temperature

Humidity

Weather condition

Irrigation suggestions

✅ Agriculture Chatbot

Smart rule-based chatbot for:

Soil nutrient explanations

Crop suitability

pH / humidity / rainfall queries

System guidance

✅ Beautiful Modern UI

Gradient backgrounds

Glassmorphism cards

Smooth animations

Fully responsive

Professional design

✅ Fully Deployed on Vercel

Zero-config deployment

Automatic HTTPS

Global CDN

Fast API responses

🧠 Tech Stack
Frontend

HTML5, CSS3

JavaScript

Responsive UI

Backend

Python

Flask

Jinja2 Templates

Machine Learning

Scikit-Learn

Pickle Model (crop_model.pkl)

External API

OpenWeather API (live weather)

Deployment

Vercel

📂 Project Structure
AgriAI/
│── main.py
│── crop_model.pkl
│── requirements.txt
│── vercel.json
│── templates/
│     ├── index.html
│     └── result.html
│── static/
└── README.md

🛠️ Installation (Local Setup)
1️⃣ Clone the repository
git clone https://github.com/yourusername/AgriAI.git
cd AgriAI

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Add Weather API Key

Inside main.py:

API_KEY = "YOUR_OPENWEATHER_API_KEY"

4️⃣ Run the app
python main.py

5️⃣ Visit in browser
http://127.0.0.1:5000/
