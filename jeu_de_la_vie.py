from tkinter import *   ## notice lowercase 't' in tkinter here

from random import randint

# ------------- PARAMETRES ---------------

## -- Canevas -- 
couleur_cellule = 'red'
couleur_fond = 'white'
hauteur_fenetre = 600
largeur_fenetre = 600

## -- Initialisation --
## Taille de la grille
taille_grille = 30
taille_bloc = taille_grille/6
## Pourcentage de vie
pourcentage_vie = 20

## -- Temps réel -- 
## Vitesse 
vitesse_animation = 5

# -------------  FONCTIONS ---------------

## -- Initialiser la grille --




# -----------  MENU TKINTER WIDGETS --------------

## -- Boutons --
## Lancer
## Arreter
## Initialiser

## -- Paramètres init --
## Taille de la grille
## Pourcentage de vie

## -- Paramètres real time -- 
## Vitesse

# ----------- INITIALISATION -------------
#grille = # On définit la variable grille
#sauvegarde_grille =  # On définit de même sa sauvegarde

root = Tk() # Fenêtre principale Tkinter
root.title("SR01 - Devoir 3 - Jeu de la vie")
root.resizable(False, False)
# Barre menu
sidebar = Frame(root, width=hauteur_fenetre*0.3, height=hauteur_fenetre, bg='black', relief='sunken', borderwidth=2)
sidebar.pack(expand=False, fill='both', side='right', anchor='nw')

# Fenêtre grille    
canevas = Frame(root, width=largeur_fenetre, height=hauteur_fenetre, bg='white')
canevas.pack(expand=False, fill='both', side='left')



root.mainloop() # Appel boucle