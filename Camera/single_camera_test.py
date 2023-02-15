
import cv2
import numpy

cam = cv2.VideoCapture(0)
'''
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,120) 
cam.set(cv2.CAP_PROP_FRAME_WIDTH,120)
'''
cam.set(3,400)
cam.set(4,400)

while True:
  ret, image = cam.read()
  cv2.imshow('Imagetest',image)
  k = cv2.waitKey(1)
  if k != -1:
    break
cv2.imwrite('Camera/test_image_2.jpg', image)
cam.release()
cv2.destroyAllWindows()


'''New: Feb 13, 23 '''
'''
cam2 = cv2.VideoCapture(1)

while True:
  ret, image2 = cam2.read()
  cv2.imshow('Imagetest2',image2)
  k = cv2.waitKey(1)
  if k != -1:
    break
cv2.imwrite('Camera/test_image_2.jpg', image2)
cam2.release()
cv2.destroyAllWindows()
'''


'''
# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)

# allow the camera to warmup
time.sleep(0.1)

# grab an image from the camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array

# display the image on screen and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)
'''