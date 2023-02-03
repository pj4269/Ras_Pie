import serial

ser = serial.Serial('/dev/ttyACM0',9600)
user_input = input('send mesage: ')

if user_input=='on':
  ser.write(b'H')
elif user_input == 'off':
  ser.write(b'L')
else:
  print ('choose either on or off')  
'''
s = [0,1]

while True:
  read_serial=ser.readline()
  s[0] = str(int (ser.readline(),16))
  print (s[0] )
  print (read_serial )
'''