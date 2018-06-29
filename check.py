import math
import tkinter as tk

#defining introductory window using tk
root = tk.Tk()

w = tk.Label(root, text="Hello World!\n"+"This code tells you if an image is color or grayscale")
x = tk.Label(root, text="To get started, paste your image files on the desktop!")
w.pack()
x.pack()
root.mainloop()

from tkinter import *

#function for classification of images
def show_entry_fields():
    name=e1.get()
    import numpy as np
    import cv2
    strings='Desktop/'+name+'.jpg'
    image = cv2.imread(strings,1)
    if image is None:
        print ("Image not found!")
        return 0
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('gray_image.jpg',gray_image)
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    img1=np.sum(image)
    img2=np.sum(cv2.imread('gray_image.jpg',1))
    val=(int(img1)-int(img2))
    if (((math.fabs(val)/img2)*1000)<1.0):
        print ("Grayscale image")
    else:
        print ("color image")
    
#window for input fields
master = Tk()
Label(master, text="Enter file Name").grid(row=0)

e1 = Entry(master)
e1.grid(row=0, column=1)
Button(master, text='OK', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text=' Quit ', command=master.quit).grid(row=4, column=1, sticky=W, pady=4)

master.mainloop()
