"""
Created on Fri Apr 29 08:53:27 2022

@author: ljhs8
"""
from tkinter import *
#from PIL import ImageTk, Image
import random

imagelist ={
    'M_GREY':["assets\MU_GREY.png",None]
    
    }

def get(name):
    if name in imagelist:
        if imagelist[name][1] is None:
            #image = Image.open(imagelist[name][0])
            #image = image.resize((y,x),Image.ANTIALIAS)
            #imagelist[name][1] = ImageTk.PhotoImage(image)
            i = 2
        return imagelist[name][1]
    return None    

Grey_field = ["#777877","#777877","#88898a","#696969"]
Red_field = ["#6e2b30", "#8f1821","#61070e","#c4101e"]

def generated(location, H, W, killstate):
    field = Grey_field
    if killstate == 1:
        field = Red_field
    for h in range(H):
        for w in range(W):
            pixel = Frame(
                master = location,
                bg = random.choice(field),
                ) #frame option
            #pixel = Crame(
             #   master = location,
              #  bg = random.choice(Grey_field),
               # relief = # pick an option thats nice
               # ) #canvas option
            pixel.grid(row=h, column = w)
            pixel.configure(width = 50, height = 50)
            w += 1
        h += 1
    return None

def degenerated(location):
    for thing in location.grid_slaves():
        thing.destroy()
    return
