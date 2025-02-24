#include <SPI.h>
#include <MFRC522.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <SoftwareSerial.h>
#include <RTClib.h>
// Define pins for MFRC522
#define SS_PIN 10
#define RST_PIN 9
// Define pins for LCD display
#define LCD_ADDRESS 0x27
#define LCD_ROWS 2
#define LCD_COLS 16
// Define pins for buzzer

#define BUZZER_PIN 8
// Define pins for GSM module
#define GSM_TX_PIN 7
#define GSM_RX_PIN 6
// Define variables for storing member names and RFID tags
String memberNames[4] = {"Nishanth R S", "Rahul S R", "Darshan G B", "Hemanth V S"};
String memberTags[4] = {"13302911", "13325610", "93AF10F8", "C3AD95F7"};
String memberids[4] = {"21BS0470","21BS0474","21BS0456","21BS0460"};
// Create instances for necessary libraries
MFRC522 mfrc522(SS_PIN, RST_PIN);
LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_ROWS, LCD_COLS);
SoftwareSerial gsm(GSM_TX_PIN, GSM_RX_PIN);
RTC_DS1307 rtc;
// Define variables for storing current date and time
DateTime now;
int currentDay, currentMonth, currentYear, currentHour, currentMinute,
currentSecond;
void setup() {
// Initialize serial communication
Serial.begin(9600);
// Initialize LCD display
lcd.init();
lcd.backlight();
lcd.clear();
lcd.setCursor(1, 0);
lcd.print(" WELCOME");
lcd.setCursor(0, 1);
lcd.print("Scan ID card ");
Serial.println("Ready to read RFID cards");
// Initialize MFRC522
SPI.begin();
mfrc522.PCD_Init();
// Initialize GSM module
gsm.begin(9600);
// Initialize RTC
rtc.begin();
// Set current date and time
rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
// Set buzzer pin as output
pinMode(BUZZER_PIN, OUTPUT);
}
void loop() {
// Check for new RFID tag
if (mfrc522.PICC_IsNewCardPresent()) {
if (mfrc522.PICC_ReadCardSerial()) {
// Get RFID tag number
String content = "";
byte letter;
for (byte i = 0; i < mfrc522.uid.size; i++) {
Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
Serial.print(mfrc522.uid.uidByte[i], HEX);
content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? "0" : ""));
content.concat(String(mfrc522.uid.uidByte[i], HEX));
}
Serial.println();
Serial.print("UID Number: ");
content.toUpperCase();
Serial.println(content);
// Check if tag matches any of the member tags
for (int i = 0; i < 4; i++) {
if (content == memberTags[i]) {
// Get current date and time
now = rtc.now();
currentDay = now.day();
currentMonth = now.month();
currentYear = now.year();
currentHour = now.hour();
currentMinute = now.minute();
currentSecond = now.second();
// Sound buzzer for 1 second
digitalWrite(BUZZER_PIN, HIGH);
delay(1000);
digitalWrite(BUZZER_PIN, LOW);
// Display member name and current date and time on LCD
lcd.clear();
lcd.setCursor(0, 0);
lcd.print(memberNames[i]);
lcd.setCursor(0, 1);
lcd.print("Reg no:");
lcd.print( memberids[i]);
delay(3000);
lcd.clear();
lcd.setCursor(0, 0);
lcd.print("Present at Clg:");
lcd.setCursor(00, 01);
lcd.print(String(currentDay) + "/" + String(currentMonth) + "/" + String(currentYear) + "" + String(currentHour) + ":" + String(currentMinute) + ":" + String(currentSecond));
delay(5000);
lcd.clear();
delay(2000);
lcd.setCursor(1, 0);
lcd.print(" WELCOME");
lcd.setCursor(0, 1);
lcd.print("Scan ID card ");
Serial.println("Ready to read RFID cards");
// Send SMS to designated number
String smsMessage = "Dear Student, " + memberNames[i] + " Regno:"+ memberids[i] + " You are Present on " + String(currentDay) + "-" + String(currentMonth) + "-" + String(currentYear) + " at time " + String(currentHour) + ":" + String(currentMinute) + ":" + String(currentSecond) + " in Electronics Lab at Governmenet Science college, Hassan 573217" + " -Thank You";
Serial.println("Dear Student, " + memberNames[i] + " Regno:"+ memberids[i] + " You are Present on " + String(currentDay) + "-" + String(currentMonth) + "-" + String(currentYear) + " at time " + String(currentHour) + ":" + String(currentMinute) + ":" + String(currentSecond) + " in Electronics Lab at Governmenet Science college, Hassan 573217" + " -Thank You");
}
}
}
}
}