# Real-Time-Weather-Monitoring-System-and-Future-Prediction-using-IOT-and-Machine-Learning


This project presents an **IoT-based real-time weather monitoring system** that collects **temperature and humidity** data through sensors and predicts future weather conditions using **Machine Learning (Linear Regression)**. The system aims to improve forecasting accuracy for applications such as **smart cities, agriculture, and disaster management**.

## 🌍 Overview
- **Real-time data collection** using IoT sensors (ESP32 + DHT22).
- **Machine Learning-based prediction** of temperature and humidity 24 hours ahead.
- **Cloud storage & API** integration for seamless data access.
- **User-friendly web dashboard** for real-time monitoring & visualization.

## 📌 Features
✔ **IoT Sensor-Based Monitoring:** Uses ESP32 microcontroller & DHT22 sensor.  
✔ **Machine Learning Prediction:** Linear Regression model predicts future temperature/humidity.  
✔ **Cloud-Based Data Storage:** Stores real-time sensor data on a cloud platform.  
✔ **Web-Based Visualization:** Users can access live weather data & predictions via a dashboard.  
✔ **Scalable & Customizable:** Can be extended to include more weather parameters (wind, pressure, etc.).  

## 🏗 System Architecture
1️⃣ **ESP32 + DHT22 Sensor** → Captures real-time temperature & humidity data.  
2️⃣ **Wi-Fi Connectivity** → Transmits sensor data to the cloud.  
3️⃣ **Cloud Storage (ThingSpeak / Firebase / AWS IoT Core)** → Stores & processes data.  
4️⃣ **Machine Learning Model** → Uses historical data for 24-hour future predictions.  
5️⃣ **API & Web Dashboard** → Displays real-time data & forecasts in a user-friendly interface.  

## 🧠 Machine Learning Model
The system uses **Linear Regression** to predict future temperature and humidity.  
**Input Features:**
- **tempC**: Current temperature (°C)
- **humidity**: Current humidity (%)
- **hour**: Time of day (0-23)

**Target Variables:**
- **future_tempC** (Temperature 24 hours ahead)
- **future_humidity** (Humidity 24 hours ahead)

## 📂 Dataset
The dataset should contain:
- `date_time` (timestamp)
- `tempC` (temperature in °C)
- `humidity` (humidity %)
- Data collected from IoT sensors or CSV files.

## 🛠 Installation & Usage
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/real-time-weather-monitoring.git
cd real-time-weather-monitoring
