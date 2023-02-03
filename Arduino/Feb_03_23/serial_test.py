import serial

ser = serial.Serial('/dev/ttyACM0',9600)
user_input = input('send mesage: ')

if user_input=='F':
  ser.write(b'F')
elif user_input == 'B':
  ser.write(b'B')
elif user_input == 'S':
  ser.write(b'S')  
else:
  print ('choose either F, B or S')  
'''
s = [0,1]

while True:
  read_serial=ser.readline()
  s[0] = str(int (ser.readline(),16))
  print (s[0] )
  print (read_serial )
'''