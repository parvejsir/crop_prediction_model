import serial
import time
import joblib
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load the trained model and scaler
model = joblib.load('C:/Users/Asus/Desktop/IOT Project Asli wala/IOT Project/Model.pkl')

scaler = joblib.load('C:/Users/Asus/Desktop/IOT Project Asli wala/IOT Project/model.pkl/scalar.pkl')

# Establish serial connection
ser = serial.Serial('COM8', 9600, timeout=1)  # Adjust the COM port accordingly
time.sleep(2)  # Give some time for the serial connection to initialize

def read_sensor_data():
    ser.write(b'1')  # Send a command to the Arduino to start sending data
    data = ser.readline().decode('utf-8').strip()
    return data

def process_sensor_data():
    while True:
        sensor_data = read_sensor_data()
        print(f"Raw sensor data received: {sensor_data}")  # Debug: Print raw sensor data
        
        if sensor_data:
            try:
                # Check if the data has exactly 4 values
                data_parts = sensor_data.split(',')
                if len(data_parts) != 4:
                    raise ValueError("Incomplete or invalid sensor data format.")
                
                # Convert the sensor data into floats
                temp, hum, soil, light = map(float, data_parts)
                pH = 5.5 # Replace this with actual pH sensor data if available

                print(f"Temperature: {temp} °C, Humidity: {hum} %, Soil Moisture: {soil}, pH: {pH}, Light Intensity: {light}")
                
                # Prepare the input data
                input_data = [[temp, hum, soil, pH, light]]
                
                # Scale the input data using the loaded scaler
                input_data_scaled = scaler.transform(input_data)
                print(f"Input data after scaling: {input_data_scaled}")
                
                # Get the probability distribution for all crop classes
                crop_probabilities = model.predict_proba(input_data_scaled)[0]  # [0] to extract probabilities for this instance

                # Get the indices of the top 3 probabilities
                top_3_indices = np.argsort(crop_probabilities)[-3:][::-1]
                
                # Get the crop names from the label encoder
                crop_classes = model.classes_  # These are the names of the crops

                # Print the top 3 crops
                print("Top 3 predicted crops:")
                for i in top_3_indices:
                    print(f"{crop_classes[i]}: {crop_probabilities[i]*100:.2f}%")
            
            except ValueError as ve:
                print(f"Invalid sensor data received: {ve}")
                
        time.sleep(2)  # Add a delay to match the Arduino's data rate

# Call the function to process sensor data
process_sensor_data()
