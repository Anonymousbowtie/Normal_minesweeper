"""
Created on Wed Apr 27 22:26:28 2022

@author: ljhs8
"""
from tkinter import Button
from tkinter import Label
import settings
import random

class Cell:
    all = []
    cell_count_obj = None
    death_count_obj = None
    cell_count = settings.CELL_COUNT - settings.MINESCOUNT
    killcount = 0
    killstate = 0
    def __init__(self,x,y,is_mine=False):
        self.is_mine = is_mine
        self.cell_bt_obj = None
        self.x=x
        self.y=y
        self.clicked = False
        self.counted = False
        self.sus = False
        #initializess object
        Cell.all.append(self)
        #add object to overall list
        
        
        
    @ staticmethod
    def reset(minesnum):
        Cell.all = []
        Cell.cell_count = settings.CELL_COUNT - minesnum
        Cell.Exploded = False
        Cell.cell_count_obj.configure(
            text = f'Cells left: {Cell.cell_count}'
            )
    @ staticmethod 
    def get_killstate():
        return Cell.killstate
        
    def create_bt_obj(self,location):
        btn = Button(
            location,
            text = "",
            width = 4,
            height = 2
        )
        btn.bind('<Button-1>',self.left_click)
        btn.bind('<Button-3>',self.right_click)
        btn.configure(width = 2, height = 1)
        
        self.cell_bt_obj = btn
    
    
    @ staticmethod
    def create_cellcount_label(location):
        lbl = Label(
            location,
            text = f"Cells left: {Cell.cell_count}",
            width = 12,
            height = 4,
            bg = 'grey',
            fg = 'white',
            font = ("Arial",20)
        )
        Cell.cell_count_obj = lbl
        
    @ staticmethod
    def create_deathcount_label(location):
        lbl = Label(
            location,
            text = f"kills: {Cell.killcount}",
            width = 12,
            height = 4,
            bg = 'black',
            fg = 'red',
            font = ("Arial",10)
        )
        Cell.death_count_obj = lbl
    
        
        
    def left_click(self,event):
        self.clicked = True
        if self.sus == True:
            return
        if self.is_mine ==True:
            self.show_mine()
        else:
            if self.surrounding_mines_len ==0:
                for cell_obj in self.surrounding_cells:
                    if cell_obj.clicked ==False:
                        cell_obj.left_click(True)
                    cell_obj.show_cell()
            self.show_cell()
        
    def right_click(self,event):
        print("who knows amirite")
        if not self.sus:
            self.cell_bt_obj.configure(
                bg = 'orange'
                )
            self.sus = True
        else:
            self.cell_bt_obj.configure(
                bg = 'SystemButtonFAce'
                )
            self.sus = False
            
        
        
    def show_mine(self):
        self.cell_bt_obj.configure(bg = "red")
        Cell.killcount += 1
        print ("you just killed a man you dingus! \n")
        if Cell.death_count_obj:
            Cell.death_count_obj.configure(
                text =  f"kills: {Cell.killcount}"
                )
        if Cell.killcount % 10 == 0:
            Cell.killstate = 1
        else:
            Cell.killstate = 0
        if Cell.killcount > 15:
            Cell.killstate = random.randint(0,1)
        
        
    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    @ property
    def surrounding_mines_len(self):
        #print(self.surrounding_cells)
        counter = 0
        for cell in self.surrounding_cells:
            if cell.is_mine == True:
                counter += 1
        return counter
        
     
    @ property
    def surrounding_cells(self):
        surroundings = [
            self.get_cell_by_axis(self.x-1, self.y-1),
            self.get_cell_by_axis(self.x-1, self.y),
            self.get_cell_by_axis(self.x-1, self.y+1),
            self.get_cell_by_axis(self.x, self.y-1),
            self.get_cell_by_axis(self.x, self.y+1),
            self.get_cell_by_axis(self.x+1, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y),
            self.get_cell_by_axis(self.x+1, self.y+1)
            ]
        surroundings = [cell for cell in surroundings if cell is not None]
        return surroundings
    
    
    def show_cell(self):
        if self.counted == False:
            Cell.cell_count -= 1
            self.counted = True
        if self.surrounding_mines_len != 0:
            self.cell_bt_obj.configure(
                text = self.surrounding_mines_len
            )
        else:
            self.cell_bt_obj.configure(
                bg = 'green'
                )
        if self.sus:
            self.cell_bt_obj.configure(
                bg = 'SystemButtonFace'
                )
        if Cell.cell_count_obj:
            Cell.cell_count_obj.configure(
                text = f'Cells left: {Cell.cell_count}'
                )

        self.cell_bt_obj.unbind('<Button-1>')
        self.cell_bt_obj.unbind('<Button-3>')
    
    @ staticmethod
    def randomize_mines(minenum):
        for cell in Cell.all:
            cell.is_mine = False
        picked_cells = random.sample(
            Cell.all, minenum
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
            
    
    def __repr__(self):
        return f"Cell({self.x},{self.y})"
    