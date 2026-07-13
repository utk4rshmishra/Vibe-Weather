# Vibe-Weather
# 🌤️ Vibe-Check Weather Dashboard

> **Ditch the boring weather icons. Get the actual vibe.**

The **Vibe-Check Weather Dashboard** is not your standard weather app. While other apps just show you temperature and humidity, this app uses real-time atmospheric data and Generative AI (Groq/Llama-3.1) to tell you how the weather will actually impact your day—including outfit advice and a "Touch Grass" index.

## ✨ Features

* **Sassy AI Forecasts:** Tired of "Partly Cloudy"? Our AI generates a personalized, opinionated take on the weather.
* **Touch Grass Index:** A custom 1-100 score on how necessary (or dangerous) it is to head outside today.
* **Dynamic Outfit Recommendations:** Get advice on what to wear based on the real-time weather and humidity data.
* **Live Atmospheric Metrics:** Clean, dashboard-style display of temperature, condition, and humidity.
* **Pro Aesthetic:** Built with a modern, dark-mode gradient UI and custom typography.

## 🛠️ Tech Stack

* **Frontend:** Python, Streamlit, Custom CSS
* **Weather Data:** OpenWeatherMap API
* **AI Brain:** Groq API (`llama-3.1-8b-instant` model)
* **Deployment:** Streamlit Community Cloud

## 💻 Local Installation & Setup

Want to run this app on your own machine? 

**1. Download the files**
Download `app.py` and `requirements.txt` to a new folder on your computer.

**2. Install dependencies**
Open your terminal in that folder and run:
```bash
pip install -r requirements.txt
