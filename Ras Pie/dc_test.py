import RPi.GPIO as GPIO
import time
# using Board numbers
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# 3 pins: 2 for direction, 1 for speed => pins will decalred as outputs
# 1. Outout, 2 inputs pins
ENA, inp1, inp2 = 25, 23, 24 # In the intermediary motor`
GPIO.setup(ENA, GPIO.OUT) # ena will be defined
GPIO.setup(inp1, GPIO.OUT) # ena will be defined
GPIO.setup(inp2, GPIO.OUT) # ena will be defined

pwm = GPIO.PWM(ENA, 100)# 100 Hz pulse or freq
pwm.start(0) # start pwm with duty cycle = 0

# Now: send the duty cycle number
dir = 1
while dir:
    print ('Loop running')
    GPIO.output(inp1, GPIO.LOW)
    GPIO.output(inp2, GPIO.HIGH)
    #pwm.ChangeDutyCycle(100) # DC motor running at 50% capacity
    if dir ==10000:
        break
    dir+=1
'''
# Set pin 11 as an output for servo
GPIO.setup(18, GPIO.OUT)

servo1 = GPIO.PWM(18, 207)# 207 Hz pulse

servo1.start(0)# start running with value of 0

print ('Waiting for 2 secs')
time.sleep(2)


try: 
    while True: # loop from 2 to 12 (0 to 180 degrees)
      for i in range(100):   
        servo1.ChangeDutyCycle(i)
        time.sleep(0.02)
      for i in range(100):   
        servo1.ChangeDutyCycle(100-i)
        time.sleep(0.02)  
except KeyboardInterrupt:
    pass

servo1.stop()
GPIO.cleanup()
print ('GoodBye')
'''

print ('hi')


