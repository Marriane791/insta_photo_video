from cProfile import label
from cgitb import text
from logging import root
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
from tkinter import messagebox
from instaloader import Instaloade


root = Tk()
root.title("Instagram image and video downloader")
root.minsize(600,500)
root.maxsize(600,500)
HEIGHT = 500
WIDTH = 600
FONT = font.Font(family="Times New Roman", size="18" , weight="bold")

canvas = Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

frame = Frame(root, bg="black")
frame.place(relwidth=1, relheight=1)

background_image = ImageTk.PhotoImage(Image.open(r"/home/marriane/Desktop/CODING/python/instapy/images/insta-dark.jpg"))
background_label = Label(frame, image = background_image)
background_label.place(relx= -0.25,relwidth= 0.7, relheight= 1)


label1 = Label(frame,text = "Download your image or video", font=FONT, bd=5, fg="#0d1137", bg="black")
label1.place(relx=0.48, rely=0.1, relheight=0.1)

FONT = font.Font(family="Times New Roman", size="12" , weight="bold")
label2 = Label(frame, text = "Enter the link adress:", font=FONT, bd=5, fg="#e52165", bg="black")
label2.place(relx=0.48, rely=0.25, relheight=0.1)

entry = Entry(frame, font = FONT, fg="#fbad50")
entry.place(relx=0.48, rely=0.35,relwidth=0.4, relheight=0.05)

button1 = Button(root, text="Download", font=FONT, bg="pink", fg="white", activeforeground="pink",activebackground="black" ,command="" )
button1.place(relx=0.48, rely=0.45, relwidth= 0.2, relheight=0.06)

root.mainloop()
