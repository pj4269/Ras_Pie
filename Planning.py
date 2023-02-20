


Feb 20, 22:  Imutils is actually using cv2.VideoCapture() + threading => so let' skip Imutils altogether and directly uise threading
              
            This decision involves: a) creating threading (for speed) myself

                                     b) do all the Image manipulation myself as well.
                                     
            Decide:  Object detector (using sliding windows + neural net)
                    => build sushi-detector => find images from internet                         
                                     
                                     
Feb 15, 23:
    
    a)    
    Width, height has default max and min
    
    #cap1.set(3,1)  # width
    #cap1.set(4,1)  # height
 
    b) VideoCapture(N) between 0-N:  depening on how many cameras are inserted

    c) With some cheap cameras, you can't control the size of an image 

Feb 10, 23: 


4. Test Code: 

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
                                     