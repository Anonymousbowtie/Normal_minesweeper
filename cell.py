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
        self.LPress = False
        self.RPress = False
        #initializess object
        Cell.all.append(self)
        #add object to overall list



    @ staticmethod
    def reset(minesnum,x,y):
        Cell.all = []
        Cell.cell_count = x*y - minesnum
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
            height = 2,
            bg = settings.WHITE
        )
        btn.bind('<Button-1>',self.left_click)
        btn.bind('<Button-3>',self.right_click)
        btn.configure(width = 2, height = 1)
        btn.bind("<ButtonRelease-1>", self.resetPressedState)
        btn.bind("<ButtonRelease-3>", self.resetPressedState)
        btn.bind("<Double-Button-1>", self.chording)

        self.cell_bt_obj = btn


    @ staticmethod
    def create_cellcount_label(location):
        lbl = Label(
            location,
            text = f"Cells left: {Cell.cell_count}",
            width = 12,
            height = 2,
            bg = 'grey',
            fg = 'white',
            font = ("Arial",15)
        )
        Cell.cell_count_obj = lbl

    @ staticmethod
    def create_deathcount_label(location):
        lbl = Label(
            location,
            #text = f"kills: {Cell.killcount}",
            text  = "",
            width = 12,
            height = 1,
            bg = 'black',
            fg = 'red',
            font = ("Arial",10)
        )
        Cell.death_count_obj = lbl



    def left_click(self,event):
        if self.sus == True:
            return
        self.LPress = True

        if self.is_mine ==True:
            self.show_mine()
            return

        else:
            self.clicked = True
            if self.surrounding_mines_len ==0:
                self.cell_bt_obj['state'] = 'disabled'
                for cell_obj in self.surrounding_cells:
                    if cell_obj.clicked ==False:
                        cell_obj.left_click(True)

                    cell_obj.show_cell()
            self.show_cell()
        self.cell_bt_obj['state'] = 'disabled'
        self.cell_bt_obj.configure(
        relief = 'sunken'
        )



    def right_click(self,event):
        self.RPress = True
        print("who knows amirite")
        if not self.sus:
            self.cell_bt_obj.configure(
                bg = 'orange'
                )
            self.sus = True
        else:
            self.cell_bt_obj.configure(
                bg = settings.WHITE
                )
            self.sus = False

    def resetPressedState(self, event):

        self.cell_bt_obj.configure(
            relief = 'sunken'
            )
        if self.sus == False and self.RPress:
            self.cell_bt_obj.configure(
                relief = 'raised'
                )
            if self.is_mine and self.clicked:
                self.show_mine()
                print("the dead really do stay where you bury them")
        self.RPress = False
        self.LPress = False

    def show_mine(self):

        self.cell_bt_obj.configure(
            bg = "red"
            )
        if self.clicked == True:
            return
        self.cell_bt_obj['state'] = 'disabled'
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
        self.clicked = True


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
        if self.sus:
            return
        if self.counted == False:
            Cell.cell_count -= 1
            self.counted = True
        if self.surrounding_mines_len != 0:
            self.cell_bt_obj.configure(
                text = self.surrounding_mines_len,
                relief = 'sunken',
                bg = settings.GREY
            )
        else:
            self.cell_bt_obj.configure(
                bg = settings.GREY,
                relief = 'sunken',
                borderwidth = .75
                )

        if Cell.cell_count_obj:
            Cell.cell_count_obj.configure(
                text = f'Cells left: {Cell.cell_count}'
                )

        self.cell_bt_obj.unbind('<Button-1>')
        self.cell_bt_obj.unbind('<Button-3>')

    def chording(self,event):
        if self.clicked ==False:
            return
        suscount = 0
        susneed = self.surrounding_mines_len
        for cell in self.surrounding_cells:
            if cell.sus ==True:
                suscount += 1
        if suscount == susneed:
            for cell in self.surrounding_cells:
                if cell.sus == False:
                    cell.left_click(True)



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
