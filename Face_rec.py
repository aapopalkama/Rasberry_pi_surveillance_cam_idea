#   Libaries
import face_recognition
import os
import cv2

#   This is well suited for a rasberry pi surveillance camera project, for example.
#   Examine saved images and detects familiar faces and keep images of strangers.

#   Path to the folder where the images are located for identification
path_unknown = "path to folder"

#   Path to the folder where identified faces are
path_known = "path to folder"

#   Using cv2.imread() method
identified_1 = cv2.imread(path_known+"Joe Biden.jpg")
identified_2 = cv2.imread(path_known+"Elon Musk.jpg")
identified_3 = cv2.imread(path_known+"Kamala harris.jpg")

#   convert the input frame from BGR to RGB
#   face 1
identified_1 = cv2.cvtColor(identified_1,cv2.COLOR_BGR2RGB)
img_encoding_1 = face_recognition.face_encodings(identified_1)[0]
#   face2
identified_2 = cv2.cvtColor(identified_2,cv2.COLOR_BGR2RGB)
img_encoding_2 = face_recognition.face_encodings(identified_2)[0]
#   face 3
identified_3 = cv2.cvtColor(identified_3,cv2.COLOR_BGR2RGB)
img_encoding_3 = face_recognition.face_encodings(identified_3)[0]
#       ... And so on..

#   Create arrays of known face encodings.
img_encoding = [img_encoding_1, img_encoding_2, img_encoding_3]

#   Retrieves all images from the folder
for image in os.listdir(path_unknown):
#   Must use "try" if faces cannot be identified from the image
    try:
#       Using cv2.imread() method
        img2 = cv2.imread(path_unknown+image)
#       convert the input frame from BGR to RGB
#       If the face is recognized then delete the image from the file
        img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

        img_encoding2 = face_recognition.face_encodings(img2)[0]
        #   Compare faces
        result = face_recognition.compare_faces(img_encoding, img_encoding2)
        print("Result: ", result,"-",image)
        
        if result[0] == True:
#       if result[0] == False:
#       Delete the image if the faces are idenetified.   
            print("Joe Biden identified")
            os.remove(path_unknown+image)
        elif result[1] == True:
            print("Elon Musk identified")
#       elif result[1] == False:
            os.remove(path_unknown+image)    
        elif result[2] == True:
            print("Kamala Harris identified")
#       elif result[2] == False: 
            os.remove(path_unknown+image)    
#       ... And so on..
   
    except IndexError as e:
#       If the face cannot be detected then delete the image from the file.
        print("Could not recognize any faces in image")

#       Delete the image if the face cannot be detected.
#       If you want keep image just remove (os.remove(path_unknown+image)) but keep except IndexError 
        os.remove(path_unknown+image)
