import cv2,os
import numpy as np
from PIL import Image

def training():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector= cv2.CascadeClassifier(r"C:\Python\Python37-32\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml");
    def getImagesAndLabels(path):
        #get the path of all the files in the folderd
        Studentpaths=[os.path.join(path,f) for f in os.listdir(path)] 
        #create empth face list
        faceSamples=[]
        #create empty ID list
        Ids=[]
        #now looping through all the image paths and loading the Ids and the images
        for student in Studentpaths:
            print(student)
            imagePaths=[os.path.join(student,f) for f in os.listdir(student)] 
            for imagePath in imagePaths:
                print(imagePath)
            #loading the image and converting it to gray scale
                pilImage=Image.open(imagePath).convert('L')
            #Now we are converting the PIL image into numpy array
                imageNp=np.array(pilImage,'uint8')
            #getting the Id from the image
                Id=int(os.path.split(student)[-1].replace('s',''))
                print (Id)
            # extract the face from the training image sample
                faces=detector.detectMultiScale(imageNp)
            #If a face is there then append that in the list as well as Id of it
                for (x,y,w,h) in faces:
                    faceSamples.append(imageNp[y:y+h,x:x+w])
                    Ids.append(Id)
        print(Ids)
        return faceSamples,Ids


    faces,Ids = getImagesAndLabels(r'C:\Users\User\Desktop\face-recognition-attendance-system-master\training-data')
    recognizer.train(faces, np.array(Ids))
    recognizer.save(r'trainner.yml')

