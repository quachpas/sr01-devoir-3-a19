import random
import os
import time
import sys
from Tkinter import *
import Tkinter


N = 20
M = 20

damier = [[0] * N  for x in range(0,M)]
passage = [[0] * N  for x in range(0,M)]
random.seed()

def initDamier():
  for i in range(0,N):
    for j in range(0,M):
      damier[i][j] = random.randint(0,1)

def afficherDamier():
  for i in range(0,2*(N+1)):
    sys.stdout.write("-")
  for i in range(0,N):
    sys.stdout.write("\n-")
    for j in range(0,M):
      if damier[i][j]:
        sys.stdout.write("o ")
      else:
        sys.stdout.write("  ")
    sys.stdout.write("-")
  sys.stdout.write("\n")
  for i in range(0,2*(N+1)):
    sys.stdout.write("-")
  sys.stdout.write("\n")

def getDamier(i, j):
  return damier[(i+N*10)%N][(j+M*10)%M]

def nbVoisins(i, j):
  res = getDamier(i,j+1)
  res += getDamier(i,j-1)
  res += getDamier(i+1,j)
  res += getDamier(i-1,j)
  res += getDamier(i+1,j+1)
  res += getDamier(i-1,j+1)
  res += getDamier(i+1,j-1)
  res += getDamier(i-1,j-1)
  return res

def genererPassage():
  for i in range(0,N):
    for j in range(0,M):
      n = nbVoisins(i,j)
      if (damier[i][j]):
        if ((n >= 4) or (n<=1)):
          passage[i][j] = -1
        else:
          passage[i][j] = 0
      else:
        passage[i][j] = 1 if (n == 3) else 0

def passer():
  for i in range(0,N):
    for j in range(0,M):
      damier[i][j] += passage[i][j]


initDamier()



# Create the window, a canvas and the mouse click event binding
root = Tkinter.Tk()
c = Tkinter.Canvas(root, width=500, height=500, borderwidth=5, background='white')
c.pack()

# Get rectangle diameters
col_width = 25
row_height = 25
# If the tile is not filled, create a rectangle
def update_view():
  for i in range(0,N):
    for j in range(0,M):
      if damier[i][j]:
        c.create_rectangle(j*col_width, i*row_height, (j+1)*col_width, (i+1)*row_height, fill="black")
      else:
        c.create_rectangle(j*col_width, i*row_height, (j+1)*col_width, (i+1)*row_height, fill="white")



while (1):
  afficherDamier()
  update_view()
  root.update()
  genererPassage()
  passer()
  os.system("clear")
root.mainloop()