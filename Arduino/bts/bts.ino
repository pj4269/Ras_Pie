
 /* Same sketch as DRV

  IBT-2 (BTS7960) H-Bridge Demo
  ibt2-demo.ino
  Demonstrates operation of IBT-2 (BTS7960) H-Bridge Motor Driver
  
  DroneBot Workshop 2022
  https://dronebotworkshop.com
*/
 
// Motor Connections (Both must use PWM pins)
#define RPWM 5
#define LPWM 6
 
void setup() {
 
  // Set motor connections as outputs
  pinMode(RPWM, OUTPUT);
  pinMode(LPWM, OUTPUT);
 
  // Stop motors
  analogWrite(RPWM, 0);
  analogWrite(LPWM, 0);
}
 
void loop() {
 
  // Accelerate forward
  digitalWrite(RPWM, LOW);
  for (int i = 0; i < 255; i++) {
    analogWrite(LPWM, i);
    delay(20);
  }
  // Jan 31, 23: Stop
  analogWrite(RPWM, 0);
  analogWrite(LPWM, 0);  
 
  delay(100000);
 
  // Decelerate forward
  for (int i = 255; i >= 0; i--) {
    analogWrite(LPWM, i);
    delay(20);
  }
  // Jan 31, 23: Stop
  analogWrite(RPWM, 0);
  analogWrite(LPWM, 0);  
 
  delay(1500);
 
  // Accelerate reverse
  digitalWrite(LPWM, LOW);
  for (int i = 0; i < 255; i++) {
    analogWrite(RPWM, i);
    delay(20);
  }
 
  delay(10000);
 
  // Decelerate reverse
  for (int i = 255; i >= 0; i--) {
    analogWrite(RPWM, i);
    delay(20);
  }
 
  delay(500);
  // Jan 31, 23: Stop
  analogWrite(RPWM, 0);
  analogWrite(LPWM, 0);
  delay(200000);
  
  
}

