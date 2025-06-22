import pandas as pd
import random

# List of 50 garden-suitable crops/plants/flowers
crops_data = {
    "Rose": {"temp": (18, 24), "humidity": (70, 80), "soil_moisture": (21, 40), "ph": (6, 6.9), "light_intensity": (25000, 40000)},
    "Daisy": {"temp": (15, 24), "humidity": (40, 60), "soil_moisture": (40, 60), "ph": (6, 8), "light_intensity": (15000, 25000)},
    "Jasmine": {"temp": (10, 35), "humidity": (40, 80), "soil_moisture": (72, 75), "ph": (5.5, 7), "light_intensity": (25000, 33000)},
    "Sunflower": {"temp": (21, 26), "humidity": (40, 60), "soil_moisture": (60, 80), "ph": (6, 7.5), "light_intensity": (30000, 50000)},
    "Tomato": {"temp": (21, 27), "humidity": (50, 70), "soil_moisture": (60, 80), "ph": (6.2, 6.8), "light_intensity": (20000, 30000)},
    "Lemon": {"temp": (21, 38), "humidity": (40, 60), "soil_moisture": (40, 60), "ph": (5.5, 6.5), "light_intensity": (20000, 30000)},
    "Lavender": {"temp": (16, 29), "humidity": (20, 35) , "soil_moisture": (30, 50), "ph": (6.5, 7.5), "light_intensity": (25000, 35000)},
    "Basil": {"temp": (26, 32), "humidity": (40, 70), "soil_moisture": (40, 60), "ph": (6, 7.5), "light_intensity": (20000, 30000)},
    "Mint": {"temp": (18, 25), "humidity": (40, 50), "soil_moisture": (60, 80), "ph": (6.5, 7), "light_intensity": (10000, 20000)},
    "Coriander": {"temp": (17, 27), "humidity": (50, 70), "soil_moisture": (40, 60), "ph": (4.5, 7.8), "light_intensity": (15000, 25000)},
    "Thyme": {"temp": (15, 24), "humidity": (40, 50), "soil_moisture": (30, 50), "ph": (6,8 ), "light_intensity": (20000, 30000)},
    "Orchid": {"temp": (20, 32), "humidity": (40, 70), "soil_moisture": (40, 60), "ph": (5.5, 6.5), "light_intensity": (15000, 25000)},
    "Petunia": {"temp": (18, 24), "humidity": (40, 60), "soil_moisture": (40, 60), "ph": (5.5, 7), "light_intensity": (20000, 30000)},
    "Chrysanthemum": {"temp": (20, 28), "humidity": (70, 90), "soil_moisture": (40, 60), "ph": (6.5, 6.9), "light_intensity": (20000, 30000)},
    "Tulip": {"temp": (4, 16), "humidity": (40, 60), "soil_moisture": (30, 50), "ph": (6, 7), "light_intensity": (15000, 25000)},
    "Zinnia": {"temp": (23, 28), "humidity": (40, 60), "soil_moisture": (40, 60), "ph": (5.5, 7.5), "light_intensity": (20000, 30000)},
    "Marigold": {"temp": (18, 30), "humidity": (60, 70), "soil_moisture": (40, 60), "ph": (5.8, 6.2), "light_intensity": (20000, 30000)},
    "Aloe Vera": {"temp": (13, 27), "humidity": (30, 50), "soil_moisture": (30, 50), "ph": (6, 7.5), "light_intensity": (20000, 30000)},
    "Fern": {"temp": (15, 24), "humidity": (40, 70), "soil_moisture": (60, 80), "ph": (5.5, 7), "light_intensity": (5000, 15000)},
    "Peony": {"temp": (15, 21), "humidity": (40, 60), "soil_moisture": (30, 50), "ph": (6.5, 7), "light_intensity": (15000, 25000)},
    "Hibiscus": {"temp": (15, 35), "humidity": (40,60), "soil_moisture": (35, 60), "ph": (6, 7), "light_intensity": (25000, 35000)},
    "Begonia": {"temp": (18, 24), "humidity": (50, 90), "soil_moisture": (42, 60), "ph": (5.5, 6.5), "light_intensity": (10000, 20000)},
    "Dahlia": {"temp": (20, 22), "humidity": (40, 70), "soil_moisture": (36, 60), "ph": (6.5, 7), "light_intensity": (20000, 30000)},
    "Geranium": {"temp": (18, 24), "humidity": (40, 70), "soil_moisture": (30, 50), "ph": (6, 6.8), "light_intensity": (20000, 30000)},
    "Carnation": {"temp": (13.2, 14.3), "humidity": (40, 70), "soil_moisture": (40, 60), "ph": (6, 7.5), "light_intensity": (25000, 35000)},
}

# Generate random data with units for 50 crops
def generate_data_with_units(crop, count):
    temp_range = crops_data[crop]["temp"]
    humidity_range = crops_data[crop]["humidity"]
    soil_moisture_range = crops_data[crop]["soil_moisture"]
    ph_range = crops_data[crop]["ph"]
    light_intensity_range = crops_data[crop]["light_intensity"]

    data = []
    for _ in range(count):
        row = {
            "Temperature (°C)": round(random.uniform(*temp_range), 2),
            "Humidity (%)": round(random.uniform(*humidity_range), 2),
            "Soil Moisture (%)": round(random.uniform(*soil_moisture_range), 2),
            "pH": round(random.uniform(*ph_range), 2),
            "Light Intensity (Lux)": round(random.uniform(*light_intensity_range), 2),
            "Crop Name": crop
        }
        data.append(row)
    return data

# Generate 200 readings for each of 50 crops/plants/flowers
data = []
readings_per_crop = 2500
for crop in list(crops_data.keys())[:50]:
    data.extend(generate_data_with_units(crop, readings_per_crop))

# Create a DataFrame and save it to an Excel file
df = pd.DataFrame(data)
file_path = "garden_crops_environment_with_units.xlsx"
df.to_excel(file_path, index=False)

print(f"Data saved to {file_path}")
