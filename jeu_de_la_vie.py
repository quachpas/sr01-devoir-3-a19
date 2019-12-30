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



# ----------- INITIALISATION -------------
#grille = # On définit la variable grille
#sauvegarde_grille =  # On définit de même sa sauvegarde

root = Tk() # Fenêtre principale Tkinter
root.title("SR01 - Devoir 3 - Jeu de la vie")
root.resizable(False, False)
# Barre menu
menu_cote = Frame(root, width=hauteur_fenetre*0.3, height=hauteur_fenetre, bg='#CCC', relief='sunken', borderwidth=2)
menu_cote.pack(expand=False, fill='both', side='right', anchor='nw')
# Fenêtre grille    
canevas = Frame(root, width=largeur_fenetre, height=hauteur_fenetre, bg='white')
canevas.pack(expand=False, fill='both', side='left')



# -----------  MENU TKINTER WIDGETS --------------

## -- Boutons --
## Lancer 
bouton_lancer = Button(menu_cote, text='Lancer', fg='blue', width=20)
bouton_lancer.pack(side='top')
## Arreter
bouton_arreter = Button(menu_cote, text='Arreter', fg='blue', width=20)
bouton_arreter.pack(side='top')
## Initialiser
bouton_init = Button(menu_cote, text='Initialiser', fg='blue', width=20)
bouton_init.pack(side='top')

## -- Paramètres real time -- 
## Pourcentage de vie
bouton_taille_grille = Scale(menu_cote, orient='horizontal', from_=0, to=100, length=120, label='% de Vie', fg='blue')
bouton_taille_grille.pack(side='bottom')

## -- Paramètres init --
## Vitesse
bouton_taille_grille = Scale(menu_cote, orient='horizontal', from_=1, to=100, length=120, label='Vitesse', fg='blue')
bouton_taille_grille.pack(side='bottom')
## Taille de la grille
bouton_taille_grille = Scale(menu_cote, orient='horizontal', from_=1, to=100, length=120, label='Taille de la grille', fg='blue')
bouton_taille_grille.pack(side='bottom')


root.mainloop() # Appel boucle


