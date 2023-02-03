import RPi.GPIO as GPIO
import time
# using Board numbers
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output for servo
GPIO.setup(11, GPIO.OUT)

servo1 = GPIO.PWM(11, 50)# 50 Hz pulse

servo1.start(0)# start running with value of 0

print ('Waiting for 2 secs')
time.sleep(2)

duty = 2 # define variable duty

while duty <=12: # loop from 2 to 12 (0 to 180 degrees)
    servo1.ChangeDutyCycle(duty)
    time.sleep(1)
    duty = duty + 1
    
time.sleep(2)
servo1.ChangeDutyCycle(7)# Turn back to 90 deg
time.sleep(2)
servo1.ChangeDutyCycle(2)# Turn back to 0 deg
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

servo1.stop()
GPIO.cleanup()
print ('GoodBye')



