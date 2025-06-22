import serial
import time

# Establish serial connection to COM8 (adjust if needed)
ser = serial.Serial('COM8', 9600, timeout=1)
time.sleep(2)  # Wait for the connection to initialize

def read_sensor_data():
    try:
        # Read data from Arduino
        data = ser.readline().decode('utf-8').strip()  # Read one line
        return data
    except Exception as e:
        print(f"Error reading data: {e}")
        return None

# Loop to read and print sensor data continuously
while True:
    sensor_data = read_sensor_data()
    if sensor_data:
        print(f"Raw data received: {sensor_data}")  # Print raw data
        try:
            # Try to split and parse data
            temp, hum, soil, light= sensor_data.split(",")
            print(f"Temperature: {temp} °C, Humidity: {hum} %, Soil Moisture: {soil}, Light Intensity(lux): {light} ")
        except ValueError:
            # Handle cases where data isn't as expected
            print("Invalid data received. Check format.")
    else:
        print("No data received.")
    
    time.sleep(2)  # Wait 2 seconds before next reading