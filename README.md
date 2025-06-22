# Crop Prediction Model using Sensor Data and Random Forest

This repository contains a machine learning-based application designed to predict the most suitable crop based on real-time environmental conditions. The model gathers sensor data—including **soil moisture**, **temperature**, **humidity**, and **light intensity**—via an **Arduino-based sensor setup**, and uses a **Random Forest algorithm** to accurately recommend the best crop for cultivation.

---

## 🚀 Features

- **Real-Time Sensor Integration**: Collects live data from sensors using Arduino (DHT11, Soil Moisture Sensor, LDR, etc.).
- **Crop Prediction**: Predicts optimal crops using a trained Random Forest classifier.
- **User-Friendly Interface**: Optional integration with a web dashboard (e.g., Streamlit or Flask).
- **Scalable Dataset**: Supports CSV datasets of different agro-climatic zones.
- **Offline Compatibility**: The model runs locally without requiring internet access.

---

## 🧪 Sensors Used

- **DHT11** - for Temperature and Humidity
- **Soil Moisture Sensor**
- **LDR (Light Dependent Resistor)** - for Light Intensity
- **Arduino Uno / Nano**
- **ESP8266 (optional)** - for sending sensor data over Wi-Fi

---

## 📦 Installation

### 🔧 Prerequisites

- Python 3.8 or higher
- Arduino IDE (to upload code to Arduino)
- Required Python Libraries:
  - pandas
  - scikit-learn
  - joblib
  - serial (pyserial)
  - streamlit *(optional, if UI used)*

---

### 💻 Steps

1. **Clone the repository:**

```bash
git clone https://github.com/parvejsir/crop_prediction_model.git
cd crop_prediction_model
```
2. **create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3.**Install dependencies:**
```bash
pip install -r requirements.txt
```
4.**Connect and upload Arduino code:**
Use the Arduino IDE to upload the sensor_reading.ino file to your board.
5.**Run the model :**
```bash
python integrate.py
```
---

## Dataset
The model was trained on a CSV dataset with the following features:
Soil Moisture
Temperature (°C)
pH Level
Humidity (%)
Light Intensity (lux)
Target Crop (label)
You can expand or fine-tune the dataset for your specific region.

---

## File Structure
```
crop_prediction_model/
├── app.py               # Streamlit Web UI (optional)
├── predict.py           # Command-line prediction logic
├── model/
│   └── crop_rf_model.pkl  # Trained Random Forest model
├── arduino/
│   └── sensor_reading.ino # Arduino code for sensor data
├── dataset/
│   └── crop_data.csv     # Training dataset
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation


```

---

## Requirements
Here are the major dependencies for the app:
- **Pandas**:  For data manipulation and preprocessing
- **Scikit-Learn**: For building and using machine learning models
- **MatPlotlib**: For data visualization and plotting
- **Joblib**: For saving and loading trained models

Install all dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

## Troubleshooting
### Common Issues:
1. **Serial Port Not Found:**:
   - Ensure the correct COM port is selected for your Arduino.

2. **Model Not Predicting Correctly:**:
   - Verify sensor calibration and units.

3. **Permission Error in Serial Read:**:
   - Try running as administrator or use sudo on Unix systems.

---

## Future Enhancements
- Add support for more sensors (e.g.,rainfall sensor).
- Deploy as a mobile app using Flutter + Flask API.
- Add GPS support for location-specific crop suggestions.
- Store data logs in the cloud for analytics and crop tracking.

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push the branch:
   ```bash
   git push origin feature-name
   ```
4. Submit a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
- Thanks to the open-source sensor community.
- Arduino + Python integration resources.
- Scikit-learn for the ML backend.

