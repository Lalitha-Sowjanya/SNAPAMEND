import tkinter as tk  
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askopenfilename
import cv2
import matplotlib.pyplot as plot
win=tk.Tk()  
win.title("snapAmend")
win.geometry("750x1000")
win.configure(bg='#4a7abc')
lbl=ttk.Label(win,text="SNAPAMEND",font=("Times",20),background='#4a7abc',foreground='pink').grid(column=0,row=0)
def Sketch():
    Tk().withdraw() 
    filename=askopenfilename() 
    image=plot.imread(filename,1)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    inverted=cv2.bitwise_not(gray)
    blurred=cv2.GaussianBlur(inverted,(111,111),0)
    invertedBlur=255-blurred
    pencilSketch=cv2.divide(gray,invertedBlur,scale=256.0)
    ps=cv2.cvtColor(pencilSketch,cv2.COLOR_BGR2RGB)
    plot.imshow(ps)
    plot.axis('off')
    plot.show()
button1=Button(win,text="Sketch",font=('Times',12),height=0,width=10,padx=10,pady=10,bg='#4a7abc',fg='yellow',activebackground='green',activeforeground='white',command=Sketch).grid(column=0,row=1)
def BlackandWhite():
    Tk().withdraw() 
    filename = askopenfilename() 
    image=plot.imread(filename,1)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    bw=cv2.cvtColor(gray,cv2.COLOR_BGR2RGB)
    plot.imshow(bw)
    plot.axis('off')
    plot.show()
button2=Button(win,text="Black&White",font=('Times',12),height=0,width=10,padx=10,pady=10,bg='#4a7abc',fg='yellow',activebackground='green',activeforeground='white',command=BlackandWhite).grid(column=0,row=2)
def ImageBlur():
    Tk().withdraw() 
    filename = askopenfilename() 
    image=plot.imread(filename,1)
    Blur=cv2.blur(image,(10,10))
    plot.imshow(Blur)
    plot.axis('off')
    plot.show()
button3=Button(win,text="Blur",font=('Times',12),height=0,width=10,padx=10,pady=10,bg='#4a7abc',fg='yellow',activebackground='green',activeforeground='white',command=ImageBlur).grid(column=0,row=3)
def Border():
    Tk().withdraw() 
    filename = askopenfilename() 
    image=plot.imread(filename,1)
    def black():
        image1=cv2.copyMakeBorder(image,20,20,20,20,cv2.BORDER_CONSTANT,None,value=0)
        plot.imshow(image1)
        plot.axis('off')
        plot.show()
    def yellow():
        image1=cv2.copyMakeBorder(image, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[255, 255, 0])
        plot.imshow(image1)
        plot.axis('off')
        plot.show()
    def pink():
        image1=cv2.copyMakeBorder(image,20,20,20,20,cv2.BORDER_CONSTANT,value=[255,0,255])
        plot.imshow(image1)
        plot.axis('off')
        plot.show()
    def red():
        image1=cv2.copyMakeBorder(image,20,20,20,20,cv2.BORDER_CONSTANT,value=[255,0,0])
        plot.imshow(image1)
        plot.axis('off')
        plot.show()
    def Darkblue():
        image1=cv2.copyMakeBorder(image,20,20,20,20,cv2.BORDER_CONSTANT,value=[0,0,255])
        plot.imshow(image1)
        plot.axis('off')
        plot.show()
    def Lightgreen():
        image1=cv2.copyMakeBorder(image,20,20,20,20,cv2.BORDER_CONSTANT,value=[0,255,0])
        plot.imshow(image1)
        plot.axis('off')
        plot.show()
    lbl1=ttk.Label(win,text="Choose color",font=("Times",18),background='#4a7abc',foreground='pink').grid(column=0,row=5)
    button20=Button(win,text="Black",font=('Times',12),height=0,width=10,padx=10,pady=10,bg='#4a7abc',fg='yellow',activebackground='green',activeforeground='white',command=black).grid(column=0,row=6)
    button21=Button(win,text="Pink",font=('Times',12),height=0,width=10,padx=10,pady=10,bg='#4a7abc',fg='yellow',activebackground='green',activeforeground='white',command=pink).grid(column=1,row=6)
    button22=Button(win,text="DarkBlue",font=('Times',12),height=0,width=10,padx=10,pady=10,bg='#4a7abc',fg='yellow',activebackground='green',activeforeground='white',command=Darkblue).grid(column=0,row=7)
    button23=Button(win,text="Red",font=('Times',12),height=0,width=10,padx=10,pady=10,bg='#4a7abc',fg='yellow',activebackground='green',activeforeground='white',command=red).grid(column=1,row=7)
    button24=Button(win,text="LightGreen",font=('Times',12),height=0,width=10,padx=10,pady=10,bg='#4a7abc',fg='yellow',activebackground='green',activeforeground='white',command=Lightgreen).grid(column=0,row=8)
    button25=Button(win,text="Yellow",font=('Times',12),height=0,width=10,padx=10,pady=10,bg='#4a7abc',fg='yellow',activebackground='green',activeforeground='white',command=yellow).grid(column=1,row=8)
button4=Button(win,text="Add Border",font=('Times',12),height=0,width=10,padx=10,pady=10,bg='#4a7abc',fg='yellow',activebackground='green',activeforeground='white',command=Border).grid(column=0,row=4)
def AddText():
    Tk().withdraw() 
    filename = askopenfilename() 
    image=plot.imread(filename,1)
    font=cv2.FONT_HERSHEY_SIMPLEX
    def black():
        color=(0,0,0)
        org=(10,20)
        fontScale=1
        thickness=4
        image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
        plot.imshow(image1)
        plot.axis('off')
        plot.show()
    def yellow():
        color=(255,255,0)
        org=(10,20)
        fontScale=1
        thickness=2
        image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
        plot.imshow(image1)
        plot.axis('off')
        plot.show()
    def pink():
        color=(255,0,255)
        org=(10,20)
        fontScale=1
        thickness=2
        image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
        plot.imshow(image1)
        plot.axis('off')
        plot.show()
    def Red():
        color=(255,0,0)
        org=(10,20)
        fontScale=1
        thickness=2
        image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
        plot.imshow(image1)
        plot.axis('off')
        plot.show()
    def Darkblue():
        color=(0,0,255)
        org=(10,20)
        fontScale=1
        thickness=2
        image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
        plot.imshow(image1)
        plot.axis('off')
        plot.show()
    def lightgreen():
        color=(0,255,0)
        org=(10,20)
        fontScale=1
        thickness=2
        image1=cv2.putText(image,text.get(),org,font,fontScale,color,thickness,cv2.LINE_AA)
        plot.imshow(image1)
        plot.axis('off')
        plot.show()
    button7=Button(win,text="Black",font=('Times',12),height=0,width=10,padx=10,pady=10,bg='#4a7abc',fg='yellow',activebackground='green',activeforeground='white',command=black).grid(column=0,row=11)
    button8=Button(win,text="Yellow",font=('Times',12),height=0,width=10,padx=10,pady=10,bg='#4a7abc',fg='yellow',activebackground='green',activeforeground='white',command=yellow).grid(column=1,row=11)
    button9=Button(win,text="Pink",font=('Times',12),height=0,width=10,padx=10,pady=10,bg='#4a7abc',fg='yellow',activebackground='green',activeforeground='white',command=pink).grid(column=0,row=12)
    button10=Button(win,text="Red",font=('Times',12),height=0,width=10,padx=10,pady=10,bg='#4a7abc',fg='yellow',activebackground='green',activeforeground='white',command=Red).grid(column=1,row=12)
    button11=Button(win,text="DarkBlue",font=('Times',12),height=0,width=10,padx=10,pady=10,bg='#4a7abc',fg='yellow',activebackground='green',activeforeground='white',command=Darkblue).grid(column=0,row=13)
    button12=Button(win,text="LightGreen",font=('Times',12),height=0,width=10,padx=10,pady=10,bg='#4a7abc',fg='yellow',activebackground='green',activeforeground='white',command=lightgreen).grid(column=1,row=13)
    lbl2=ttk.Label(win,text="Enter title",font=("Times",20),background='#4a7abc',foreground='pink').grid(column=0,row=10)
    text=StringVar()
    txt=ttk.Entry(win,width=15,textvariable=text).grid(column=1,row=10)
button5=Button(win,text="Add Text",font=('Times',12),height=0,width=10,padx=10,pady=10,bg='#4a7abc',fg='yellow',activebackground='green',activeforeground='white',command=AddText).grid(column=0,row=9)
def close():
    win.destroy()
    win.quit()
button6=Button(win,text="Exit",font=('Times',12),height=0,width=10,padx=10,pady=10,bg='#4a7abc',fg='yellow',activebackground='green',activeforeground='white',command=close).grid(column=0,row=14)
win.mainloop()   
