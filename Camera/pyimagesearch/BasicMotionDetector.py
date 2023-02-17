import imutils
import cv2


# ref:  https://pyimagesearch.com/2016/01/18/multiple-cameras-with-the-raspberry-pi-and-opencv/

class BasicMotionDetector:
  def __init__(self, accumWeight=0.5, deltaThresh=5, minArea=5000):
    self.isv2 = imutils.is_cv2()
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