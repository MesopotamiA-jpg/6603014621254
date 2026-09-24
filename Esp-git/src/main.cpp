#include <Arduino.h>

// บอร์ด ESP32 (DevKit) ส่วนใหญ่จะมีหลอดไฟ LED สีฟ้าในตัวเชื่อมอยู่กับขา 2
#define LED_PIN 2

void setup() {
  // เริ่มต้นการสื่อสารผ่าน Serial ด้วยความเร็ว 115200
  Serial.begin(115200);
  
  // ตั้งค่าขา 2 ให้เป็น Output เพื่อส่งไฟออกไปควบคุม LED
  pinMode(LED_PIN, OUTPUT);
  
  Serial.println("ESP32 System Ready!");
  Serial.println("Project by Narongwit Started.");
}

void loop() {
  digitalWrite(LED_PIN, HIGH);   // สั่งจ่ายไฟ (เปิด LED)
  Serial.println("LED Status: ON");
  delay(1000);                   // หน่วงเวลาไว้ 1 วินาที (1000 มิลลิวินาที)
  
  digitalWrite(LED_PIN, LOW);    // สั่งตัดไฟ (ปิด LED)
  Serial.println("LED Status: OFF");
  delay(1000);                   // หน่วงเวลาไว้ 1 วินาที
}