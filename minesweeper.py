"""
Created on Wed Apr 27 13:16:30 2022

@author: ljhs8
"""

from tkinter import *
from cell import Cell
import settings
import utils
import ass
#from PIL import ImageTk, Image

page = Tk()
#window settings
page.configure(bg="black")
page.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
page.title("Normal Minesweeper")
page.resizable(False,False)

icon = PhotoImage(file = 'assets/mine.png')
page.iconphoto(False, icon)


mines = settings.MINESCOUNT
gx = settings.GRID_WIDTH
gy = settings.GRID_HEIGHT

#frame settings
top_fr = Frame(
    page,
    bg = 'black',
    width = settings.WIDTH,
    height = utils.height_pct(25)
)
top_fr.place(x=0, y = 0)
left_fr = Frame(
    page,
    bg = 'black',
    width=utils.width_pct(25),
    height=utils.height_pct(75)
)
left_fr.place(x = 0, y=utils.height_pct(25))
cen_fr = Frame(
    page,
    bg = 'black',
    width= utils.width_pct(75),
    height= utils.height_pct(75)
)
cen_fr.place(x=utils.width_pct(25),y=utils.height_pct(25))
cen_fr.configure( bg = 'grey')
#buttons in grid
def populate(w,h):
    for x in range(w):
        for y in range(h):
            c = Cell(x,y)
            c.create_bt_obj(cen_fr)
            c.cell_bt_obj.grid(
                row = x, column=y
                )
    return


def  depopulate():
    for thing in cen_fr.grid_slaves():
        thing.destroy()
    return


populate(settings.GRID_HEIGHT, settings.GRID_WIDTH)



NewGame = Frame(
    left_fr,
    bg = 'black',
    height = utils.height_pct(75),
    width = utils.width_pct(25)
    )
NewGame.place(x=0, y=utils.height_pct(25))
N_Label = Label(
    master = NewGame,
    text = "New game settings",
    bg = 'black',
    fg = 'white'
    )
N_Label.place(x = utils.width_pct(5),
              y=utils.height_pct(0))


def new_game():
    mines = NM.get()
    gx = NX.get()
    gy = NY.get()
    depopulate()
    Cell.reset(mines,gx,gy)
    NM.configure(
        to = gy*gx
        )
    populate(gy, gx)
    Cell.randomize_mines(mines)
    ass.degenerated(top_fr)
    ks = Cell.get_killstate()
    ass.generated(top_fr,3,15,ks)
    return


n_g_b = Button(
    master = NewGame,
    text = "Start new gamer moment",
    command = new_game
    )

n_g_b.place(x =utils.width_pct(3),
            y=utils.height_pct(6))

NM = Scale(
    master = NewGame,
    activebackground = "orange",
    from_ = 1, to = gx*gy,
    orient = HORIZONTAL,
    bg = 'black',
    fg = 'white',
    label = "Mines"
    )

NM.place(x=utils.width_pct(5),
         y=utils.height_pct(12))
NM.set(settings.MINESCOUNT)

NX = Scale(
    master = NewGame,
    activebackground = "orange",
    from_ = 9, to = settings.GRID_WIDTH,
    orient = HORIZONTAL,
    bg = 'black',
    fg = 'white',
    label = "Witdh"
    )
NY = Scale(
    master = NewGame,
    activebackground = "orange",
    from_ = 9, to = settings.GRID_HEIGHT,
    orient = HORIZONTAL,
    bg = 'black',
    fg = 'white',
    label = "Heigth"
    )
NX.place(x=utils.width_pct(5),
         y=utils.height_pct(22))
NX.set(settings.GRID_WIDTH)
NY.place(x=utils.width_pct(5),
          y=utils.height_pct(32))
NY.set(settings.GRID_HEIGHT)
ks = 0

ass.generated(top_fr,3,15, ks)

#canvas.create_image(0,0,image=ass.get(
  #  'M_GREY',
 #   ))

#calling static methods from cell class file
Cell.randomize_mines(mines)
Cell.create_cellcount_label(left_fr)
Cell.cell_count_obj.place(x=utils.width_pct(3),y=0)
Cell.create_deathcount_label(left_fr)
Cell.death_count_obj.place(x =utils.width_pct(5),
                           y = utils.height_pct(9))
#page.wm_attributes('-transparentcolor','brown')

#run window
page.mainloop()
