from tkinter import *   ## notice lowercase 't' in tkinter here
from tkinter.messagebox import *
from time import *
from random import randint

# ------------- PARAMETRES ---------------

## -- Fenêtre principale -- 
couleur_cellule = 'red'
couleur_fond = 'white'
hauteur_fenetre = 600
largeur_fenetre = 600
statut = False # Lancer le jeu ou le mettre en pause

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
## -- Lancer le jeu --
def lancer_jeu():
    statut = True
    print("Le jeu s'est lancé\n")
## -- Arrêter le jeu --
def arreter_jeu():
    statut = False
    print("Le jeu s'est arrêté\n")
    
def initialiser_jeu():
    
    
    
    
    print("Le jeu est initialisé\n")

def slider_taille_grille(val):
    taille_grille = val
    #print("Slider_val =",val,"\nTaille grille = ", taille_grille, "\nPourcentage_vie =", pourcentage_vie, "\nVitesse = ", vitesse_animation,"\n")
    
def slider_pourcentage_vie(val):
    pourcentage_vie = val
    #print("Slider_val =",val,"\nTaille grille = ", taille_grille, "\nPourcentage_vie =", pourcentage_vie, "\nVitesse = ", vitesse_animation,"\n")
    
def slider_vitesse_animation(val):
    vitesse_animation = val
    #print("Slider_val =",val,"\nTaille grille = ", taille_grille, "\nPourcentage_vie =", pourcentage_vie, "\nVitesse = ", vitesse_animation,"\n")
    

# ----------- INITIALISATION -------------
#grille = # On définit la variable grille
#sauvegarde_grille =  # On définit de même sa sauvegarde

root = Tk() # Fenêtre principale Tkinter
root.title("SR01 - Devoir 3 - Jeu de la vie")
root.resizable(False, False)
# Barre menu
menu_cote = Frame(root, width=hauteur_fenetre*0.3, height=hauteur_fenetre, bg='#f0f0f0', relief='flat', borderwidth=2)
menu_cote.pack(expand=False, fill='both', side='right', anchor='nw')
# Fenêtre grille    
canevas = Frame(root, width=largeur_fenetre, height=hauteur_fenetre, bg='white')
canevas.pack(expand=False, fill='both', side='left')
    
# -----------  MENU TKINTER WIDGETS --------------

## -- Boutons --
## Lancer 
bouton_lancer = Button(menu_cote, text='Lancer', relief='solid', fg='blue', width=20, command=lancer_jeu)
bouton_lancer.pack(side='top')
## Arreter
bouton_arreter = Button(menu_cote, text='Arreter', relief='solid', fg='blue', width=20, command=arreter_jeu)
bouton_arreter.pack(side='top')
## Initialiser
bouton_init = Button(menu_cote, text='Initialiser', relief='solid', fg='blue', width=20, command=initialiser_jeu)
bouton_init.pack(side='top')


## Quitter ## Bouton
bouton_init = Button(menu_cote, text='Quitter', relief='solid', fg='blue', width=20, command=root.destroy)
bouton_init.pack(side='bottom')

## Vitesse ## -- Paramètres init --
bouton_vitesse = Scale(menu_cote, orient='horizontal', from_=1, to=100, length=120, variable=vitesse_animation, bg='#f0f0f0', relief='flat', highlightthickness=0, label='Vitesse', fg='blue', command=slider_vitesse_animation)
bouton_vitesse.pack(side='bottom')

## Pourcentage de vie ## -- Paramètres real time -- 
bouton_pourcentage_vie = Scale(menu_cote, orient='horizontal', from_=0, to=100, length=120, variable=pourcentage_vie, bg='#f0f0f0', relief='flat', highlightthickness=0, label='% de Vie', fg='blue', bd='0', command=slider_pourcentage_vie)
bouton_pourcentage_vie.pack(side='bottom')

## Taille de la grille ## -- Paramètres init --
bouton_taille_grille = Scale(menu_cote, orient='horizontal', from_=1, to=100, length=120, variable=taille_grille, bg='#f0f0f0', relief='flat', highlightthickness=0, label='Taille de la grille', fg='blue', command=slider_taille_grille)
bouton_taille_grille.pack(side='bottom')


root.mainloop() # Appel boucle


