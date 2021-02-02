#include <SPI.h>
#include <MFRC522.h>

#include <WiFi.h>
#include <HTTPClient.h>

const char *ssid = "Iphone";
const char *password = "cyrildelak";

#define RST_PIN 22
#define SS_PIN 21
#define GREEN_PIN 2
#define RED_PIN 4

MFRC522 mfrc522(SS_PIN, RST_PIN); // Create MFRC522 instance

void setup()
{
  Serial.begin(115200);
  while (!Serial)
    ;
  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(RED_PIN, OUTPUT);
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
  SPI.begin();
  mfrc522.PCD_Init();
  delay(4);
  mfrc522.PCD_DumpVersionToSerial();
  Serial.println(F("Scan PICC to see UID, SAK, type, and data blocks..."));
}

void loop()
{
  if (WiFi.status() == WL_CONNECTED && mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial())
  {
    HTTPClient http;
    http.begin("http://172.20.10.3:3000/open");
    for (int a = 0; mfrc522.uid.uidByte[a]; a += 1)
      Serial.print(mfrc522.uid.uidByte[a], HEX);

    int httpResponseCode = http.POST((char *)mfrc522.uid.uidByte);

    if (httpResponseCode == 200)
    {
      digitalWrite(GREEN_PIN, HIGH);
      delay(500);
      digitalWrite(GREEN_PIN, LOW);
    }
    else
    {
      digitalWrite(RED_PIN, HIGH);
      delay(500);
      digitalWrite(RED_PIN, LOW);
    }
    // Free resources
    http.end();
    delay(500);
  }
}