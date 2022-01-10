import tkinter as tk  
from tkinter import ttk
from tkinter import *
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt  
win=tk.Tk()  
win.title("SNAPBOT")
win.geometry("1000x1000")
win.configure(bg='lightblue')
lbl=ttk.Label(win,text="Enter Picture Name").grid(column=0,row=0)
Fixed_path="C:/Users/sasid/Downloads/"
def Sketch():
    image=cv2.imread(Fixed_path+Variable_path.get())
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    inverted=255-gray
    blurred=cv2.GaussianBlur(inverted,(21,21),0)
    invertedBlur=255-blurred
    pencilSketch=cv2.divide(gray,invertedBlur,scale=256.0)
    cv2.imshow("Sketch",pencilSketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    def save():
        directory = r'C:/Users/sasid/Downloads'
        os.chdir(directory)
        cv2.imwrite("NewImage.png",pencilSketch)
        lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=26)
    button=ttk.Button(win,text="Save",command=save).grid(column=1,row=25)  
button1=ttk.Button(win,text="Sketch", command=Sketch).grid(column=1,row=1)
def BlackandWhite():
    image = cv2.imread(Fixed_path+Variable_path.get())
    B,G,R=cv2.split(image)
    cv2.imshow("Black and White",B)
    cv2.waitKey(0)
    def save():
        directory = r'C:/Users/sasid/Downloads'
        os.chdir(directory)
        cv2.imwrite("NewImage.png",B)
        lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=26)
    button=ttk.Button(win,text="Save",command=save).grid(column=1,row=25)  
button2=ttk.Button(win,text="Black and White",command=BlackandWhite).grid(column=1,row=2)
def ImageBlur():
    image = cv2.imread(Fixed_path+Variable_path.get())
    Blur=cv2.blur(image,(10,10))
    cv2.imshow('Blurring',Blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    def save():
        directory = r'C:/Users/sasid/Downloads'
        os.chdir(directory)
        cv2.imwrite("NewImage.png",Blur)
        lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=26)
    button=ttk.Button(win,text="Save",command=save).grid(column=1,row=25)
button3=ttk.Button(win,text="Blur",command=ImageBlur).grid(column=1,row=3)
def ImageSizer():
    image = cv2.imread(Fixed_path+Variable_path.get(),1)
    half = cv2.resize(image, (0, 0), fx =0.3, fy =0.3)
    bigger = cv2.resize(image, (1050, 1610))
    stretch_near = cv2.resize(image, (780, 540),interpolation = cv2.INTER_NEAREST)
    Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
    images =[image, half, bigger, stretch_near]
    count = 4
    for i in range(count):
        plt.subplot(2, 2, i + 1)
        plt.title(Titles[i])
        plt.imshow(images[i])
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
button4=ttk.Button(win,text="Resize",command=ImageSizer).grid(column=1,row=4)
def Border():
    image=cv2.imread(Fixed_path+Variable_path.get())
    window_name = 'Image'
    lbl3=ttk.Label(win,text="Choose colour").grid(column=0,row=13)
    def black():
        image1=cv2.copyMakeBorder(image,25,25,25,25,cv2.BORDER_CONSTANT,None,value=0)
        cv2.imshow(window_name,image1)
        def save():
            directory = r'C:/Users/sasid/Downloads'
            os.chdir(directory)
            cv2.imwrite("NewImage.png",image1)
            lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=26)
        button=ttk.Button(win,text="Save",command=save).grid(column=2,row=17)
    def blue():
        image1=cv2.copyMakeBorder(image, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[255, 255, 0])
        cv2.imshow(window_name,image1)
        def save():
            directory = r'C:/Users/sasid/Downloads'
            os.chdir(directory)
            cv2.imwrite("NewImage.png",image1)
            lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=26)
        button=ttk.Button(win,text="Save",command=save).grid(column=2,row=17)
    def pink():
        image1=cv2.copyMakeBorder(image, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[255, 0, 255])
        cv2.imshow(window_name,image1)
        def save():
            directory = r'C:/Users/sasid/Downloads'
            os.chdir(directory)
            cv2.imwrite("NewImage.png",image1)
            lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=26)
        button=ttk.Button(win,text="Save",command=save).grid(column=2,row=17)
    def Darkblue():
        image1=cv2.copyMakeBorder(image, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[255, 0, 0])
        cv2.imshow(window_name,image1)
        def save():
            directory = r'C:/Users/sasid/Downloads'
            os.chdir(directory)
            cv2.imwrite("NewImage.png",image1)
            lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=26)
        button=ttk.Button(win,text="Save",command=save).grid(column=2,row=17)
    def red():
        image1=cv2.copyMakeBorder(image, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[0, 0, 255])
        cv2.imshow(window_name,image1)
        def save():
            directory = r'C:/Users/sasid/Downloads'
            os.chdir(directory)
            cv2.imwrite("NewImage.png",image1)
            lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=26)
        button=ttk.Button(win,text="Save",command=save).grid(column=2,row=17)
    def Lightgreen():
        image1=cv2.copyMakeBorder(image, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[0, 255, 0])
        cv2.imshow(window_name,image1)
        def save():
            directory = r'C:/Users/sasid/Downloads'
            os.chdir(directory)
            cv2.imwrite("NewImage.png",image1)
            lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=26)
        button=ttk.Button(win,text="Save",command=save).grid(column=2,row=17)
    def yellow():
        image1=cv2.copyMakeBorder(image, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[0, 255, 255])
        cv2.imshow(window_name,image1)
        def save():
            directory = r'C:/Users/sasid/Downloads'
            os.chdir(directory)
            cv2.imwrite("NewImage.png",image1)
            lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=26)
        button=ttk.Button(win,text="Save",command=save).grid(column=2,row=17)
    button20=ttk.Button(win,text="Black",command=black).grid(column=1,row=14)
    button21=ttk.Button(win,text="Blue",command=blue).grid(column=2,row=14)
    button22=ttk.Button(win,text="Pink",command=pink).grid(column=1,row=15)
    button23=ttk.Button(win,text="Dark Blue",command=Darkblue).grid(column=2,row=15)
    button24=ttk.Button(win,text="Red",command=red).grid(column=1,row=16)
    button25=ttk.Button(win,text="Light Green",command=Lightgreen).grid(column=2,row=16)
    button26=ttk.Button(win,text="Yellow",command=yellow).grid(column=1,row=17)
nameEntered=ttk.Entry(win,width=12,textvariable=Variable_path).grid(column=1,row=0)
button5=ttk.Button(win,text="Add Border",command=Border).grid(column=1,row=5)
def AddText():
    image=cv2.imread(Fixed_path+Variable_path.get())
    window_name='Texted Image'
    def simple():
        font=cv2.FONT_HERSHEY_SIMPLEX
        def black():
            color=(0,0,0)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def lightblue():
            color=(255,255,0)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def pink():
            color=(255,0,255)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def darkblue():
            color=(255,0,0)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def Red():
            color=(0,0,255)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def lightgreen():
            color=(0,255,0)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def yellow():
            color=(0,255,255)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        lbl3=ttk.Label(win,text="Enter the text here").grid(column=0,row=39)
        text=tk.StringVar()
        txt=ttk.Entry(win,width=50,textvariable=text).grid(column=1,row=39)
        button15=ttk.Button(win,text="Black",command=black).grid(column=1,row=35)
        button16=ttk.Button(win,text="Light Blue",command=lightblue).grid(column=2,row=35)
        button17=ttk.Button(win,text="Pink",command=pink).grid(column=1,row=36)
        button18=ttk.Button(win,text="Dark Blue",command=darkblue).grid(column=2,row=36)
        button19=ttk.Button(win,text="Red",command=Red).grid(column=1,row=37)
        button20=ttk.Button(win,text="Light Green",command=lightgreen).grid(column=2,row=37)
        button21=ttk.Button(win,text="Yellow",command=yellow).grid(column=1,row=38)
    def plain():
        font=cv2.FONT_HERSHEY_PLAIN
        def black():
            color=(0,0,0)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def lightblue():
            color=(255,255,0)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def pink():
            color=(255,0,255)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def darkblue():
            color=(255,0,0)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def Red():
            color=(0,0,255)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def lightgreen():
            color=(0,255,0)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def yellow():
            color=(0,255,255)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        lbl3=ttk.Label(win,text="Enter the text here").grid(column=0,row=39)
        text=tk.StringVar()
        txt=ttk.Entry(win,width=50,textvariable=text).grid(column=1,row=39)
        button15=ttk.Button(win,text="Black",command=black).grid(column=1,row=35)
        button16=ttk.Button(win,text="Light Blue",command=lightblue).grid(column=2,row=35)
        button17=ttk.Button(win,text="Pink",command=pink).grid(column=1,row=36)
        button18=ttk.Button(win,text="Dark Blue",command=darkblue).grid(column=2,row=36)
        button19=ttk.Button(win,text="Red",command=Red).grid(column=1,row=37)
        button20=ttk.Button(win,text="Light Green",command=lightgreen).grid(column=2,row=37)
        button21=ttk.Button(win,text="Yellow",command=yellow).grid(column=1,row=38)
    def duplex():
        font=cv2.FONT_HERSHEY_DUPLEX
        def black():
            color=(0,0,0)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def lightblue():
            color=(255,255,0)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def pink():
            color=(255,0,255)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def darkblue():
            color=(255,0,0)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def Red():
            color=(0,0,255)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def lightgreen():
            color=(0,255,0)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def yellow():
            color=(0,255,255)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        lbl3=ttk.Label(win,text="Enter the text here").grid(column=0,row=39)
        text=tk.StringVar()
        txt=ttk.Entry(win,width=50,textvariable=text).grid(column=1,row=39)
        button15=ttk.Button(win,text="Black",command=black).grid(column=1,row=35)
        button16=ttk.Button(win,text="Light Blue",command=lightblue).grid(column=2,row=35)
        button17=ttk.Button(win,text="Pink",command=pink).grid(column=1,row=36)
        button18=ttk.Button(win,text="Dark Blue",command=darkblue).grid(column=2,row=36)
        button19=ttk.Button(win,text="Red",command=Red).grid(column=1,row=37)
        button20=ttk.Button(win,text="Light Green",command=lightgreen).grid(column=2,row=37)
        button21=ttk.Button(win,text="Yellow",command=yellow).grid(column=1,row=38)
    def Complex():
        font=cv2.FONT_HERSHEY_COMPLEX
        def black():
            color=(0,0,0)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def lightblue():
            color=(255,255,0)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def pink():
            color=(255,0,255)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def darkblue():
            color=(255,0,0)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def Red():
            color=(0,0,255)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def lightgreen():
            color=(0,255,0)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def yellow():
            color=(0,255,255)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        lbl3=ttk.Label(win,text="Enter the text here").grid(column=0,row=39)
        text=tk.StringVar()
        txt=ttk.Entry(win,width=50,textvariable=text).grid(column=1,row=39)
        button15=ttk.Button(win,text="Black",command=black).grid(column=1,row=35)
        button16=ttk.Button(win,text="Light Blue",command=lightblue).grid(column=2,row=35)
        button17=ttk.Button(win,text="Pink",command=pink).grid(column=1,row=36)
        button18=ttk.Button(win,text="Dark Blue",command=darkblue).grid(column=2,row=36)
        button19=ttk.Button(win,text="Red",command=Red).grid(column=1,row=37)
        button20=ttk.Button(win,text="Light Green",command=lightgreen).grid(column=2,row=37)
        button21=ttk.Button(win,text="Yellow",command=yellow).grid(column=1,row=38)
    def triplex():
        font=cv2.FONT_HERSHEY_TRIPLEX
        def black():
            color=(0,0,0)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def lightblue():
            color=(255,255,0)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def pink():
            color=(255,0,255)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def darkblue():
            color=(255,0,0)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def Red():
            color=(0,0,255)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def lightgreen():
            color=(0,255,0)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def yellow():
            color=(0,255,255)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        lbl3=ttk.Label(win,text="Enter the text here").grid(column=0,row=39)
        text=tk.StringVar()
        txt=ttk.Entry(win,width=50,textvariable=text).grid(column=1,row=39)
        button15=ttk.Button(win,text="Black",command=black).grid(column=1,row=35)
        button16=ttk.Button(win,text="Light Blue",command=lightblue).grid(column=2,row=35)
        button17=ttk.Button(win,text="Pink",command=pink).grid(column=1,row=36)
        button18=ttk.Button(win,text="Dark Blue",command=darkblue).grid(column=2,row=36)
        button19=ttk.Button(win,text="Red",command=Red).grid(column=1,row=37)
        button20=ttk.Button(win,text="Light Green",command=lightgreen).grid(column=2,row=37)
        button21=ttk.Button(win,text="Yellow",command=yellow).grid(column=1,row=38)
    def compsmall():
        font=cv2.FONT_HERSHEY_COMPLEX_SMALL
        def black():
            color=(0,0,0)
            org=(30,30)
            fontScale=1
            thickness=2
            lbl3=ttk.Label(win,text="Enter the text here").grid(column=0,row=39)
            text=tk.StringVar()
            txt=ttk.Entry(win,width=100,textvariable=text).grid(column=1,row=39)
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def lightblue():
            color=(255,255,0)
            org=(30,30)
            fontScale=1
            thickness=2
            lbl3=ttk.Label(win,text="Enter the text here").grid(column=0,row=39)
            text=tk.StringVar()
            txt=ttk.Entry(win,width=100,textvariable=text).grid(column=1,row=39)
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def pink():
            color=(255,0,255)
            org=(30,30)
            fontScale=1
            thickness=2
            lbl3=ttk.Label(win,text="Enter the text here").grid(column=0,row=39)
            text=tk.StringVar()
            txt=ttk.Entry(win,width=100,textvariable=text).grid(column=1,row=39)
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def darkblue():
            color=(255,0,0)
            org=(30,30)
            fontScale=1
            thickness=2
            lbl3=ttk.Label(win,text="Enter the text here").grid(column=0,row=39)
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def Red():
            color=(0,0,255)
            org=(30,30)
            fontScale=1
            thickness=2
            lbl3=ttk.Label(win,text="Enter the text here").grid(column=0,row=39)
            text=tk.StringVar()
            txt=ttk.Entry(win,width=100,textvariable=text).grid(column=1,row=39)
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def lightgreen():
            color=(0,255,0)
            org=(30,30)
            fontScale=1
            thickness=2
            lbl3=ttk.Label(win,text="Enter the text here").grid(column=0,row=39)
            text=tk.StringVar()
            txt=ttk.Entry(win,width=100,textvariable=text).grid(column=1,row=39)
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        def yellow():
            color=(0,255,255)
            org=(30,30)
            fontScale=1
            thickness=2
            image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
            cv2.imshow(window_name,image1)
            def save():
                directory = r'C:/Users/sasid/Downloads'
                os.chdir(directory)
                cv2.imwrite("NewImage.png",image1)
                lbl2=ttk.Label(win,text="Successfully saved").grid(column=1,row=41)
            button=ttk.Button(win,text="Save",command=save).grid(column=1,row=40)
        lbl3=ttk.Label(win,text="Enter the text here").grid(column=0,row=39)
        text=tk.StringVar()
        txt=ttk.Entry(win,width=50,textvariable=text).grid(column=1,row=39)
        button15=ttk.Button(win,text="Black",command=black).grid(column=1,row=35)
        button16=ttk.Button(win,text="Light Blue",command=lightblue).grid(column=2,row=35)
        button17=ttk.Button(win,text="Pink",command=pink).grid(column=1,row=36)
        button18=ttk.Button(win,text="Dark Blue",command=darkblue).grid(column=2,row=36)
        button19=ttk.Button(win,text="Red",command=Red).grid(column=1,row=37)
        button20=ttk.Button(win,text="Light Green",command=lightgreen).grid(column=2,row=37)
        button21=ttk.Button(win,text="Yellow",command=yellow).grid(column=1,row=38)
    button9=ttk.Button(win,text="SIMPLEX",command=simple).grid(column=1,row=27)
    button10=ttk.Button(win,text="PLAIN",command=plain).grid(column=1,row=28)
    button11=ttk.Button(win,text="DUPLEX",command=duplex).grid(column=1,row=29)
    button12=ttk.Button(win,text="COMPLEX",command=Complex).grid(column=1,row=30)
    button13=ttk.Button(win,text="TRIPLEX",command=triplex).grid(column=1,row=31)
    button14=ttk.Button(win,text="COMPLEX SMALL",command=compsmall).grid(column=1,row=32)
Variable_path=tk.StringVar()  
nameEntered=ttk.Entry(win,width=12,textvariable=Variable_path).grid(column=1,row=0)
button6=ttk.Button(win,text="Add Text",command=AddText).grid(column=1,row=6)
win.mainloop()  
