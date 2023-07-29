#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

// BME280 setup
Adafruit_BME280 bme;

// variables to store information which sensors are present
bool bme_present = false;

void setup() {
  Serial.begin(115200);
  Wire.begin();

  bme_present = bme.begin(0x76, &Wire);

  // configure for weather monitoring
  if (bme_present)
  {
    bme.setSampling(Adafruit_BME280::MODE_FORCED,
                    Adafruit_BME280::SAMPLING_X1, // temperature
                    Adafruit_BME280::SAMPLING_X1, // pressure
                    Adafruit_BME280::SAMPLING_X1, // humidity
                    Adafruit_BME280::FILTER_OFF);
  }
}

void returnEnviro() {
  // create buffer for data
  String buf;
  
  bme.takeForcedMeasurement();
  delay(25);
  float val = bme.readTemperature();
  buf += String(val, 2);
  buf += F(",");
  val = bme.readHumidity();
  buf += String(val, 2);
  buf += F(",");
  val = bme.readPressure() / 100.0F;
  buf += String(val, 2);

  Serial.println(buf);
}

void loop() {
  while (Serial.available() > 0) {
    char incChar = Serial.read();

    switch (incChar) {
      case 'e':
        if (bme_present) {
          returnEnviro();
          break;
        }
        else {
          Serial.println("No environmental sensor");
        }
    }
  }
}
