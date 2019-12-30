from tkinter import *   ## notice lowercase 't' in tkinter here

from random import randint


# --------GAME OF LIFE--------


# ----Parameters

taille_grille = 80   # number of blocks on the grid
taille_bloc = 10  # size of a block (pixels)

dt = 50          # pause duration
step = 10        # pause duration increase / decrease step size

cell_color = 'red'
background_color = 'white'



# ----Functions

def init_grille(grid):
    "Intializes the grid with random values."
    for i in range(taille_grille):
        for j in range(taille_grille):
            grid[i][j] = randint(0,1)


def nombre_de_voisins(i, j, grid):
    """Returns the number of alive niehgbours of the cell (i,j)."""
    res = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            if grid[(i+k)%taille_grille][(j+l)%taille_grille]: res+=1
    if grid[i][j]: res-=1  # in case the center is counted

    return res


def update(grid, grid_cpy):
    """Updates the grid, applying death and birth condition."""
    for i in range(taille_grille):  # copies the grid
        for j in range(taille_grille):
            grid_cpy[i][j] = grid[i][j]

    for i in range(taille_grille):
        for j in range(taille_grille):
            nb_neighb = nombre_de_voisins(i, j, grid_cpy)  # use the grid copy !

            if (not grid_cpy[i][j]) and nb_neighb == 3:  # birth rule
                grid[i][j] = 1
            elif grid_cpy[i][j] and (nb_neighb < 2 or 3 < nb_neighb):  # death rules
                grid[i][j] = 0



def animationLoop(grid, grid_cpy):
    """Renders the blocks."""
    global dt

    update(grid, grid_cpy)
    can.delete(ALL)
    posx = 0  # x coordinate of the drawing cursor
    posy = 0  # y coordinate of the drawing cursor
    for i in range(taille_grille):
        posx = 0
        for j in range(taille_grille):
            if grid[i][j]:
                # draw a rectangle with upper left corner at (posx, posy)
                can.create_rectangle(posx, posy, posx + taille_bloc, posy + taille_bloc, fill = cell_color)
            posx += taille_bloc   # moves the cursor for the next block
        posy += taille_bloc       # new line

    root.after(dt, animationLoop, grid, grid_cpy)

# ----Keyboard events

def reset(event):
    """Resets the grid."""
    global grid
    init_grille(grid)

def faster(event):
    """Accelerates the animation."""
    global dt
    if dt-step > 1: dt -= step
    else: dt = 1

def slower(event):
    """Slows the animation."""
    global dt
    dt += step



# ----Initialization

grid = [[0 for j in range(taille_grille)] for i in range(taille_grille)]
grid_cpy = [[0 for j in range(taille_grille)] for i in range(taille_grille)]

init_grille(grid)

root = Tk()
root.title("Game of life")

can = Canvas(root, height=taille_grille * taille_bloc, width=taille_grille * taille_bloc, bg=background_color)

can.bind("<r>", reset)
can.bind("<f>", faster)
can.bind("<s>", slower)

can.focus_set()
can.pack()

animationLoop(grid, grid_cpy)

print("             ----Game Of Life----")
print(" Press R to reset.")
print(" Press F to increase the animation speed.")
print(" press S to decrease the animation speed.")

root.mainloop()
