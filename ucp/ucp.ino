#include <SPI.h>      
#include <SD.h>
#include <ArduinoJson.h>   
File myFile;
int randNumber1;
int randNumber2;
int randNumber5;
int temp=0;
int noise=0;
int randNumber3;
StaticJsonDocument<256> doc;
void setup() {
  Serial.begin(9600);
  while (!Serial)continue;
  Serial.print("Initializing SD card...");
  if (!SD.begin()) {
    Serial.println("initialization failed!");
    while (1);
  }
  Serial.println("initialization done.");
  randomSeed(analogRead(0));
}
void loop() {
  randNumber1 = random(-5,5);
  randNumber2 = random(-10,10);
  randNumber5 = random(80,90);
  randNumber3 = random(-2,2);
  myFile = SD.open("data~1.jso");
  if (myFile) {
    deserializeJson(doc, myFile);
    myFile.println();
    myFile.close();
    doc["label_2"]=int(doc["label_2"])-randNumber1;
    doc["label_14"]=int(doc["label_14"])+randNumber2;
    doc["label_17"]=int(doc["label_17"])+randNumber1;
    doc["label_18"]=int(doc["label_2"])-randNumber2;
    doc["label_6"]=int(doc["label_6"])-randNumber1;
    doc["label_20"]=int(doc["label_20"])-randNumber3;
    doc["label_10"]=int(doc["label_10"])+randNumber3;
    doc["label_29"]=randNumber5;
    SD.remove("data~1.jso");
    myFile = SD.open("data~1.jso", FILE_WRITE);
    serializeJson(doc, Serial);
    serializeJson(doc, myFile);
    myFile.close();
  } else {
    Serial.println("error opening data~1.jso");
  }
  Serial.println("Completed");
  delay(1000);
}
