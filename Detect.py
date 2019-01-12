import cv2,os
from Sqlpy import *
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
def mark():
    def predict(path,date):
        
        if(isavail(date) != True ):
            newDate(date)
        im =cv2.imread(path)
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)
        flag = False
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
            if(conf <70):
                updateAttedance(Id,date,'Present')
                data = getData(Id)
                if(data != None):
                    cv2.putText(im,str(data[0]),(x,y+h+30),font,1,(255,0,0))
                    cv2.putText(im,str(data[1]),(x,y+h+60),font,1,(255,0,0))
                    cv2.putText(im,str(data[-1]),(x,y+h+90),font,1,(255,0,0))
                else:
                    cv2.putText(im,str(Id),(x,y+h+120),font,1,(255,0,0))
    #    if(conf<65):
    #             if(Id==1):
    #                 Id="Anirban"
    #             elif(Id==2):
    #             Id="Sam"
    #         else:
    #         Id="Unknown"   
            print(Id)
                #cv2.putText(im,str(data[4]),(x,y+h+120),font,1,(255,0,0))
            plt.imshow(im,cmap = 'gray' , interpolation = 'bicubic')
            cv2.imshow('im',im)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def ina(result):
        def printtext(enm):
        #global e
            date = enm.get()
            if (date.count('/') == 2):
                date_split = date.split('/')
                day = date_split[0]
                month = date_split[1]
                year = date_split[2]
                if((len(day)==2) and (len(month) == 2) and (len(year) == 4)):
                    toor.destroy()
                    for path in Studentpaths:
                        predict(path,date)
                else:
                    toor.destroy()
                    ina('Write the data in specified order dd//mm//yyyy')
            else:
                toor.destroy()
                ina('Write correct date')
        toor = Tk()

        toor.title('Date')
    #    print('123')
        labelText=StringVar()
        labelText.set("Enter the date in dd//mm/yyyy format")
    #    print(labelText)
        labelDir=Label(toor, textvariable=labelText, height=4)
        labelDir.pack(side="top")
        toor.update()
      #  print('321')
        directory=StringVar(None)
        e=Entry(toor,textvariable=directory,width=50)
        e.pack(side="left")
        #e = Entry(root)
        #e.pack()
        e.focus_set()

        b = Button(toor,text='okay',command=(lambda en=e:printtext(en)))
        b.pack(side='bottom')
        toor.mainloop()
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(r'trainner.yml')
    cascadePath = r"C:/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    font = cv2.FONT_HERSHEY_SIMPLEX
    #font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
    path = r'test-data'
    Studentpaths=[os.path.join(path,f) for f in os.listdir(path)]
    result = 'Enter the date in dd/mm/yy format'
    ina(result)
