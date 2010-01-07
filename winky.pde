#include <SHT1x.h>

// data and clock pins
#define dataPin 10
#define clockPin 11

SHT1x sht1x(dataPin, clockPin);

void setup()
{
   Serial.begin(115200); // Open serial connection to report values to host
}

void loop()
{
  float temp_c;
  float humidity;

  // Read values from the sensor
  temp_c = sht1x.readTemperatureC();
  humidity = sht1x.readHumidity();

  // Print the values to the serial port
  Serial.print(temp_c);
  Serial.print(",");
  Serial.print(humidity);
  Serial.println("");

  delay(10);
}
