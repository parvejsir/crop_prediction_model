#include <DHT.h>
#include <Wire.h>
#include <BH1750.h>

// Pin configurations
#define DHTPIN A1               // Pin connected to DHT sensor
#define SOIL_MOISTURE_PIN A0    // Pin for soil moisture sensor
#define DHTTYPE DHT11           // DHT11 sensor type

// Soil moisture calibration values (adjust based on your sensor's behavior)
#define MIN_SOIL_MOISTURE 1023  // Value when soil is completely dry
#define MAX_SOIL_MOISTURE 0     // Value when soil is completely wet

// Initialize sensors
DHT dht(DHTPIN, DHTTYPE);
BH1750 lightMeter;

void setup() {
  Wire.begin();
  Serial.begin(9600);           // Start serial communication at 9600 baud rate
  dht.begin();                  // Initialize DHT sensor
  lightMeter.begin();           // Initialize BH1750 light sensor
  pinMode(SOIL_MOISTURE_PIN, INPUT);  // Set soil moisture sensor pin as input
}

void loop() {
  // Read temperature and humidity from DHT sensor
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  
  // Read soil moisture value (analog)
  int soilMoistureRaw = analogRead(SOIL_MOISTURE_PIN);
  
  // Convert soil moisture to percentage
  int soilMoisturePercent = map(soilMoistureRaw, MIN_SOIL_MOISTURE, MAX_SOIL_MOISTURE, 0, 100);
  soilMoisturePercent = constrain(soilMoisturePercent, 0, 100); // Ensure percentage stays between 0 and 100

  // Read light intensity from BH1750 sensor
  float lux = lightMeter.readLightLevel();

  // Check if DHT readings are valid
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Print sensor data as comma-separated values
  Serial.print(temperature);
  Serial.print(",");
  Serial.print(humidity);
  Serial.print(",");
  Serial.print(soilMoisturePercent); // Output soil moisture as percentage
  Serial.print(",");
  Serial.print(lux);
  Serial.println("\n");

  delay(2000);  // Wait for 2 seconds before the next reading
}
