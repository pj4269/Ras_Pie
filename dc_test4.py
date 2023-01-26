import RPi.GPIO as GPIO
import time 
#GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

print ('This one worked')
# 3 pins: 2 for direction, 1 for speed => pins will decalred as outputs
# 1. Outout, 2 inputs pins
ENA, inp1, inp2 = 7, 13, 15# 25, 24, 23
x = 11
GPIO.setup(ENA, GPIO.OUT) 
GPIO.setup(inp1, GPIO.OUT)
GPIO.setup(inp2, GPIO.OUT)
GPIO.setup( x, GPIO.OUT)

GPIO.output(7, True)
GPIO.output(11, True) 


i = 0
while True:
  i+=1  
  GPIO.output(inp1, True)
  GPIO.output(inp2, False) 
  print (i)
  if i == 2:
    break
  time.sleep(5)