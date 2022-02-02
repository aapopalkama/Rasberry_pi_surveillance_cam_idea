
# Rasberry_pi_surveillance_cam_idea
 The program recognizes the human who appears in the camera from the video and takes a "screenshot" and saves it.  Another program examines the recorded images and compares the faces from those images to the pre recognized faces. If the program recognizes the face then it will delete the image.

# Requirements
* I strongly recommend using anaconda to installing packages.
* conda install -c conda-forge opencv
* conda install -c anaconda cmake
* conda install -c conda-forge dlib
* conda install -c conda-forge face_recognition

# person_detection.py
This code opens the camera and examines if there are people visible in the image. If the program detects a human, the program will capture an image and save it. 

# Face_rec.py
* You need to save the images of faces you want to compare with the images saved in the code above. 

* This code examines images stored by person_detection.py. The program opens a folder containing unknown images and compares them to the known faces you have saved. If the program recognizes there is a picture of the same person by person_detection.py and in the known faces you have saved, it will delete the photo from person_detection.py. If there is no match in your known saved faces for the image, it will not delete it but it will leave it in the folder. 

