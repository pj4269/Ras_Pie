import cv2

frame_size = (224, 224)

cap0 = cv2.VideoCapture(0) #  Cam0 size is controled not Cam1
'''
cap0.set(cv2.CAP_PROP_FRAME_HEIGHT,12) 
cap0.set(cv2.CAP_PROP_FRAME_WIDTH,12) 
'''
cap0.set(3,200) # width
cap0.set(4,200) # height
cap1 = cv2.VideoCapture(2)

w = cap0.get(3)
h = cap0.get(4)
print (w,h)
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

'''
webcam1 = VideoStream(src=0).start()
webcam2 = VideoStream(src=2).start()
'''

while True:
  ret0, frame0 = cap0.read()
  ret1, frame1 = cap1.read()

  if (ret0):
    # Display the resulting frame
    # 1st try: Works!
    frame0 = cv2.resize( frame0, frame_size)
    cv2.imshow('Cam 0', frame0)

  if (ret1):
    # Display the resulting frame
    frame1 = cv2.resize( frame1, frame_size)    
    cv2.imshow('Cam 1', frame1)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
