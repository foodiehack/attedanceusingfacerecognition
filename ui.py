from tkinter import *
from trainer import *
from Detect import *
import os
def function1():
    print("You Clicked")
def rename():
    choice = input("Enter 1 for changing name for trianing data and 2 for test data")
    if(choice == str(1)):
        f = input("Enter the id with s")
        pa = r'training-data'
        pa = os.path.join(pa,f)
        image_list = os.listdir(pa)
        for i,  image in enumerate(image_list):
            ext = os.path.splitext(image)[1]
            if ext == '.jpeg' or ext == '.jpg' or ext == ".png":
                src = pa + "\\" + image
                dst = pa + '\\' + str(i) + '.jpg'
                os.rename(src, dst)
    elif(choice == str(2)):
        pa = r'test-data'
        #pa = os.path.join(pa,f)
        image_list = os.listdir(pa)
        for i,  image in enumerate(image_list):
            j =i+1
            src = pa + '\\' + image
            dst = pa + '\\' + 'test' +str(j) +'.jpg'
            os.rename(src, dst)
    else:
        ina('ENter the correct choice')


root = Tk()
root.title("Biometrics")

'''fname = Canvas(bg="black", height=500, width=500)
fname.pack(side=TOP)

image1 = PhotoImage(file='C:\\Users\\Lenovo\\Downloads\\tk.jpg')
image = fname.create_image(900, 50, anchor = NE, image=image1)
fname.pack()'''
root.geometry("1000x500")
frame = Frame(root)
frame.pack(fill=X)
label = Label(frame, text="Facial Attendance System", bd=5, bg='Pink', font='Times 32', relief='solid')
label.pack(fill=X)

otherframe = Frame(root, height=2, bd=2)
otherframe.pack()

button1 = Button(otherframe, bd=10, height=5, width=80, text="Training", command=lambda: training())
button1.pack()
button2 = Button(otherframe, bd=10, height=5, width=80, text="Mark Attendance", command= mark)
button2.pack()
button3 = Button(otherframe, bd=10, height=5, width=80, text="Convert images to jpg ", command=lambda: rename())
button3.pack()
button4 = Button(otherframe, bd=10, height=5, width=80, text="Enter Details Manually", command=lambda: InsertorUpdate())
button4.pack()

root.mainloop()
