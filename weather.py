from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image,ImageTk

root=Tk()
root.title("Weather App")
root.geometry("890x470+300+100")
root.configure(bg="#57adff")
root.resizable(False,False)

##Icon
image_icon=PhotoImage(file="Images/Logo.png")
root.iconphoto(False,image_icon)

Round_box=PhotoImage(file="Images/Rectangular_box_1.png")
Label(root,image=Round_box,bg="#57adff").place(x=30,y=150)

#label

label1=Label(root,text="Temperature",font=('Helvetica',11),fg="white",bg="black")
label1.place(x=50,y=155)

label2=Label(root,text="Humidity",font=('Helvetica',11),fg="white",bg="black")
label2.place(x=50,y=175)

label3=Label(root,text="Pressure",font=('Helvetica',11),fg="white",bg="black")
label3.place(x=50,y=195)

label4=Label(root,text="Wind Speed",font=('Helvetica',11),fg="white",bg="black")
label4.place(x=50,y=215)

label5=Label(root,text="Description",font=('Helvetica',11),fg="white",bg="black")
label5.place(x=50,y=235)





root.mainloop()
