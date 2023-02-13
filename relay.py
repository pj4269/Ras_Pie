import RPi.GPIO as GPIO
import time 
#GPIO.setmode(GPIO.BCM) # L298
GPIO.setwarnings(False)
pin_num = 21  #40#21
# Setting GPIO numbering mode
GPIO.setmode(GPIO.BCM)#BOARD)#BCM  
GPIO.setup(pin_num , GPIO.OUT, initial = GPIO.LOW) 

L = GPIO.LOW
H = GPIO.HIGH

print ('From the relay')
i = 0
while True:
  
  GPIO.output(pin_num, True)
  print (1)
  time.sleep(1)
  GPIO.output(pin_num, False)
  time.sleep(1)
  print (2)
  
  i+=1
  print (i)
  
  GPIO.output(pin_num, H)
  time.sleep(1)
  
  GPIO.output(pin_num, L)
  
  time.sleep(1)
  
  
  if i == 2:
      GPIO.cleanup()
      break