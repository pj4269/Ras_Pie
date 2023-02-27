import cv2

from imutils.video import VideoStream
# import BasicMotionDetector
from BasicMotionDetector import BasicMotionDetector
import numpy as np
import datetime
import imutils


frame_size = (224, 224)
'''
cap0 = cv2.VideoCapture(0) #  Cam0 size is controled not Cam1
'''
cap0 = VideoStream(src=0).start()
'''
cap0.set(cv2.CAP_PROP_FRAME_HEIGHT,12) 
cap0.set(cv2.CAP_PROP_FRAME_WIDTH,12) 

cap0.set(3,200) # width
cap0.set(4,200) # height
'''
cap1 = cv2.VideoCapture(2)

'''
w = cap0.get(3)
h = cap0.get(4)
print (w,h)
'''
'''
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT,400) 
cap1.set(cv2.CAP_PROP_FRAME_WIDTH,400) 
'''
cap1.set(3,200)  # width
cap1.set(4,200)  # height
'''cap1.resize()'''
w = cap1.get(3)
h = cap1.get(4)
print (w,h, cv2.__version__)

''' VideoStream uses VideoCapture but runs on a thread so it can run faster!'''
from imutils.video import VideoStream

motion0 = BasicMotionDetector()
total = 0

# webcam1 = VideoStream(src=0).start()
# webcam2 = VideoStream(src=2).start()


while True:
    
    
  ret1, webcam2 = cap1.read()
  '''
  for stream in (webcam1, webcam2):

    cv2.imshow('Cam 0', stream)
  '''
  my_cameras = []
  frames = []

  for cap, Motion in zip(cap0, motion0): 
    ret0, webcam1 = cap.read()

    if (ret0):
      # Display the resulting frame
      # 1st try: Works!
      frame0 = cv2.resize( webcam1, frame_size)
      my_cameras.append(frame0)
      '''1. Turning Gray '''
      gray = cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY)
      '''2. Blurring it '''
      gray = cv2.GaussianBlur(gray, (21, 21), 0)

      '''3. Motion '''
      locs = Motion.update(gray)
    
      ''' 3. B) Accumulating frames '''
      # we should allow the motion detector to "run" for a bit and accumulate a set of frames to form a nice average
      '''
      frame = stream.read()
      frame = imutils.resize(frame, width=400)
      '''
      if total < 32:
        frames.append(frame0)
        continue    

      frame0 = gray
      cv2.imshow('Cam 0', frame0)

  if (ret1):
    # Display the resulting frame
    frame1 = cv2.resize( webcam2, frame_size)
    my_cameras.append(frame1)    
    # cv2.imshow('Cam 1', frame1)
  ''' This is not working - Feb 27, 23
  for frame in my_cameras:
    cv2.imshow('Cam ', frame)
  '''


  if cv2.waitKey(1) & 0xFF == ord('q'):
    break


