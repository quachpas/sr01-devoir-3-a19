from tkinter import *   ## notice lowercase 't' in tkinter here

from random import randint

# ------------- PARAMETRES ---------------

## -- Canevas -- 
couleur_cellule = 'red'
couleur_fond = 'white'
hauteur_fenetre = 5000
largeur_fenetre = 5000

## -- Initialisation --
## Taille de la grille
global taille_grille = 30
taille_bloc = taille_grille/6
## Pourcentage de vie
global pourcentage_vie = 20

## -- Temps réel -- 
## Vitesse 
global vitesse_animation = 5

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
grille = # On définit la variable grille
sauvegarde_grille =  # On définit de même sa sauvegarde

root = Tk() # Fenêtre principale Tkinter
root.title("SR01 - Devoir 3 - Jeu de la vie")

canevas = Canvas(root, height=hauteur_fenetre, width=largeur_fenetre, bg=couleur_fond)

canevas.focus_set() # Fenetre en premier plan
canevas.pack # Réorganisation widgets 

root.mainloop() # Appel boucle