import RPi.GPIO as GPIO
import time 
# using Board numbers
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# 3 pins: 2 for direction, 1 for speed => pins will decalred as outputs
# 1. Outout, 2 inputs pins
ENA, inp1, inp2 = 7, 11, 13, 15# 25, 24, 23
GPIO.setup(ENA, GPIO.OUT) 
GPIO.setup(inp1, GPIO.OUT)
GPIO.setup(inp2, GPIO.OUT)
pwm = GPIO.PWM(ENA, 100)
pwm.start(0)

i = 0
while True:
  i+=1  
  GPIO.output(inp1, GPIO.LOW)
  GPIO.output(inp2, GPIO.LOW) 
  print (i)
  if i == 1000:
    break    
#p = GPIO.PWM(ENA, 1000)
#p.start(25)

