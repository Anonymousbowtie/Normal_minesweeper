"""
Created on Sat Apr 30 08:42:00 2022

@author: ljhs8
"""
from tkinter import *
import ass

window = Tk()
window.title('image')
canvas = Canvas(window, width=800, height=800)
canvas.pack()
canvas.create_image(0, 0, anchor='nw', image=ass.get('M_GREY',200,300))

window.mainloop()