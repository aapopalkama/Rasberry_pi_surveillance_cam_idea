import numpy as np
import cv2
import time
import os




#   This code opens the camera and examines if there is a person in the picture.
#   If the program detects a human, the program will capture the image.
#   Suitable for raspberry pi surveillance camera project, for example

#   Next, the program that examines if there is an identifiable person in the image, if so, the program will delete the image.


#   Path to the folder where you want to save the images.

path = "path to folder"
# initialize the HOG descriptor/person detector

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cv2.startWindowThread()

# open webcam video stream
video = cv2.VideoCapture(0)

# the output will be written to output.avi
out = cv2.VideoWriter(
    'output.avi',
    cv2.VideoWriter_fourcc(*'MJPG'),
    15.,
    (640,480))

# 15 fps
count=0
while(True):
    # Capture frame-by-frame
    ret, frame = video.read()

    timestamp = time.strftime("%a %H:%M:%S")

    # resizing for faster detection
    frame = cv2.resize(frame, (640, 480))
    # using a greyscale picture, also for faster detection
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # detect people in the image
    # returns the bounding boxes for the detected objects
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )

    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    box = []
    picture_time = 0
    for (xA, yA, xB, yB) in boxes:
        # display the detected boxes in the colour picture
        box.append(xA)
        cv2.rectangle(frame, (xA, yA), (xB, yB),
                          (0, 255, 0), 2)

        # If human is detected take "screenshot" and save image
        now = time.time()
        if (now - picture_time) > 1000:
            print(count)
            picture_taking_ok = True
            cv2.imwrite(os.path.join(path,"img"+str(count)+".jpg"),frame)
            count+=1
            picture_time = now


    # Write the output video 
    out.write(frame.astype('uint8'))
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# When everything done, release the capture
video.release()
# and release the output
out.release()
# finally, close the window
cv2.destroyAllWindows()
cv2.waitKey(1)