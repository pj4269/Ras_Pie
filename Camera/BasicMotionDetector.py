import imutils
import cv2


# ref:  https://pyimagesearch.com/2016/01/18/multiple-cameras-with-the-raspberry-pi-and-opencv/
#  source code:  https://github.com/PyImageSearch/imutils/blob/master/imutils/video/videostream.py

class BasicMotionDetector:
  def __init__(self, accumWeight=0.5, deltaThresh=5, minArea=5000):
    self.isv2 = imutils.is_cv2()  #  comment it out : Dec 23, 23
    self.accumWeight = accumWeight
    self.deltaThresh = deltaThresh
    self.minArea = minArea
    self.avg = None
  def update(self, image):
    # initialize the list of locations containing motion
    locs = []
    # if the average image is None, initialize it
    if self.avg is None:
      self.avg = image.astype("float")
      return locs
    cv2.accumulateWeighted(image, self.avg, self.accumWeight)
    frameDelta = cv2.absdiff(image, cv2.convertScaleAbs(self.avg) )
    # threshold the delta image and apply a series of dilations  to help fill in holes
    thresh = cv2.threshold(frameDelta, self.deltaThresh, 255,cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    # find contours in the thresholded image, taking care to  use the appropriate version of OpenCV
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # loop over the contours
    for c in cnts:# only add the contour to the locations list if it exceeds the minimum area
      if cv2.contourArea(c) > self.minArea:
        locs.append(c)
        # return the set of locations
    return locs    