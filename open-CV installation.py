ref: https://raspberrypi-guide.github.io/electronics/using-usb-webcams

4. Test code:
    
    import cv2

cam = cv2.VideoCapture(0)

while True:
  ret, image = cam.read()
  cv2.imshow('Imagetest',image)
  k = cv2.waitKey(1)
  if k != -1:
    break
cv2.imwrite('Camera/test_image_2.jpg', image)
cam.release()
cv2.destroyAllWindows()


3.  a) sudo apt install fswebcam

    b) check connected cameras:   lsusb

    b) capture image: (worked)
        
       fswebcam -r 1280*720 --no-banner Camera/test1.jpg
 
    

2. enable Camera Module on Ras Pie
   
sudo raspi-config


Ref:  https://pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/


1. Install
pip3 install opencv-python 
sudo apt-get install libcblas-dev
sudo apt-get install libhdf5-dev
sudo apt-get install libhdf5-serial-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev 
sudo apt-get install libqtgui4 
sudo apt-get install libqt4-test