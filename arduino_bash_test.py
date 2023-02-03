import os

print ('Testing Bash command... ')
#ls -l /dev/ttyACM*
# sudo chmod a+rw /dev/ttyACM0

os.system('echo hi')
os.system('ls -l /dev/ttyACM*')
os.system('sudo chmod a+rw /dev/ttyACM0')
