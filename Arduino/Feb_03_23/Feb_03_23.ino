 /* Same sketch as DRV

  Ref: pythonforundergradengineers.com/python-arduino-LED.html
       https://dronebotworkshop.com
*/
 
// Motor Connections (Both must use PWM pins)
#define RPWM 5
#define LPWM 6

const int ledPin = 13; // the pin that the LED is attached to
int incomingByte;      // a variable to read incoming serial data into

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // Set motor connections as outputs
  pinMode(RPWM, OUTPUT);
  pinMode(LPWM, OUTPUT);
 
  // Stop motors => not sure if this is necessary
  analogWrite(RPWM, 0);
  analogWrite(LPWM, 0);  
}

void loop() 
{
  // see if there's incoming serial data:
  if (Serial.available() > 0) 
  {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a capital H (ASCII 72), turn on the LED:
    // Forward - Accelerate
    if (incomingByte == 'F') 
      {
      //digitalWrite(ledPin, HIGH);
      // Accelerate forward
      //digitalWrite(RPWM, LOW);
      for (int i = 0; i < 255; i++) 
          { analogWrite(LPWM, i);
             //delay(20);
          }
      } 
    // if it's an L (ASCII 76) turn off the LED:
    // Reverse - Accelerate
    if (incomingByte == 'B') {
       //digitalWrite(ledPin, LOW);
       // Accelerate reverse
       digitalWrite(LPWM, LOW);
       for (int i = 0; i < 255; i++) {
         analogWrite(RPWM, i);
         //delay(20);
                                     }
                              }
                              
    // Stop                          
    if (incomingByte == 'S') {
      // Jan 31, 23: Stop
      analogWrite(RPWM, 0);
      analogWrite(LPWM, 0);
      //delay(100000);
                             }
  
   }
}   



 

 

