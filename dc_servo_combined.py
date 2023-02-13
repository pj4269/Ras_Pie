import RPi.GPIO as GPIO
import time 
#GPIO.setmode(GPIO.BCM) # L298
GPIO.setwarnings(False)

# Setting GPIO numbering mode
GPIO.setmode(GPIO.BOARD) # Rasberry Pie

# 3 pins: 2 for direction, 1 for speed => pins will decalred as outputs
# 1. Output, 2 inputs pins
# 1st dc motor
ENA, ENA2,  inp1, inp2 = 7, 11, 13, 15
# Aug 9th: 2nd dc motor
ENA3, ENA4, inp3, inp4      = 22, 24, 16, 18

GPIO.setup(ENA , GPIO.OUT) 
GPIO.setup(ENA2, GPIO.OUT)
GPIO.setup(inp1, GPIO.OUT)
GPIO.setup(inp2, GPIO.OUT)

GPIO.output(7, True)
GPIO.output(11, True) 
# Aug 9th
GPIO.setup(ENA3, GPIO.OUT) 
GPIO.setup(ENA4, GPIO.OUT)
GPIO.setup(inp3, GPIO.OUT)
GPIO.setup(inp4, GPIO.OUT)

GPIO.output(ENA3, True)
GPIO.output(ENA4, True)

# Aug 11th: Servo motor = Set pin 37 as an output for servo
GPIO.setup(37, GPIO.OUT)
servo1 = GPIO.PWM(37, 50)# 50 Hz pulse



L = GPIO.LOW
H = GPIO.HIGH

p = GPIO.PWM(ENA, 1000)
p.start(100)
# start slow
p.ChangeDutyCycle(10) 

i = 0
while True:
   
  y = input() 
    
  i+=1
  
  if y == 'f':
    print ('Forward')
    GPIO.output(inp1, H)
    GPIO.output(inp2, L)
    # Aug 9th: 
    GPIO.output(inp3, H)
    GPIO.output(inp4, L)
    y = 'z'
  elif y == 'b':
    print ('Backward')
    GPIO.output(inp1, L)
    GPIO.output(inp2, H)     
    y = 'z'
  elif y == 's':
    print ('Stop')
    GPIO.output(inp1, L)
    GPIO.output(inp2, L)
    
    GPIO.output(inp3, L)
    GPIO.output(inp4, L)     
    
    y = 'z'


  if y == 'l':
    print ('Low speed')
    p.ChangeDutyCycle(5)     
    y = 'z'
  elif y == 'm':
    print ('Medium speed')
    p.ChangeDutyCycle(20)     
    y = 'z'    
  elif y == 'h':
    print ('High speed')
    p.ChangeDutyCycle(30)     
    y = 'z'
  elif y == 'se':# servo
    # Val = 0 = Pulse Off  
    servo1.start(0)
    duty = 2 # define variable duty
    # 2  = 0   degrees
    # 7  = 90  degrees
    # 12 = 180 degrees
    
    while duty <=12: # loop from 2 to 12 (0 to 180 degrees) for 10 steps
      servo1.ChangeDutyCycle(duty)
      time.sleep(1)
      duty = duty + 1
    time.sleep(1)
    servo1.ChangeDutyCycle(7)# Turn back to 90 deg with no steps in between
    time.sleep(1)
    servo1.ChangeDutyCycle(2)# Turn back to 0 deg with no steps in between
    time.sleep(1)
    servo1.ChangeDutyCycle(0)

    servo1.stop()
    GPIO.cleanup()
    print ('GoodBye')






        
  print (i)
  if i == 4:
    GPIO.output(inp1, L)
    GPIO.output(inp2, L)
    break
  time.sleep(5)
