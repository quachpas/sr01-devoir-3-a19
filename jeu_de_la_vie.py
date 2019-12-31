from tkinter import *   ## notice lowercase 't' in tkinter here
from tkinter.messagebox import *
from time import *
from random import *
from math import *
# ------------- PARAMETRES ---------------

## -- Fenêtre principale -- 
couleur_cellule = 'red'
couleur_fond = 'white'
hauteur_fenetre = 834
largeur_fenetre = 834
statut = False # Lancer le jeu ou le mettre en pause

## -- Initialisation --
## Taille de la grille
taille_grille = 5
taille_bloc = hauteur_fenetre/taille_grille
pourcentage_vie_actuel = 0

## Tableau
tableau = [[bool(0) for j in range(taille_grille)] for i in range(taille_grille)]
copie_tableau = [[bool(0) for j in range(taille_grille)] for i in range(taille_grille)]

## Pourcentage de vie
pourcentage_vie = 0

## Vitesse 
vitesse_animation = 1
pas = int(1000/vitesse_animation)

# -------------  FONCTIONS ---------------

## -- Initialiser la grille --
## -- Lancer le jeu --
def lancer_jeu():
    global statut
    global bouton_taille_grille
    global bouton_pourcentage_vie
    global bouton_vitesse
    global tableau
    global copie_tableau
    
    statut = True
    bouton_taille_grille.config(state=DISABLED, label="Taille de la grille (DESACTIVE)", length=220)
    bouton_pourcentage_vie.config(state=DISABLED, label="% de Vie (DESACTIVE)", length=220)
    bouton_vitesse.config(length=220)
    mise_a_jour_grille(tableau, copie_tableau)
    #print("Le jeu s'est lancé; statut = %d" % statut)
## -- Arrêter le jeu --
def arreter_jeu():
    global statut
    global bouton_taille_grille
    global bouton_pourcentage_vie
    global bouton_vitesse
    
    statut = False
    bouton_taille_grille.config(state=ACTIVE, label="Taille de la grille", length=180)
    bouton_pourcentage_vie.config(state=ACTIVE, label="% de Vie", length=180)
    bouton_vitesse.config(length=180)
    #print("Le jeu s'est arrêté; statut = %d" % statut)

## -- Initialiser le tableau grille[][] avec des valeurs random --     
def initialiser_tableau(tableau):    
    global pourcentage_vie
    global pourcentage_vie_actuel
    global taille_grille
    nombre_de_blocs = taille_grille*taille_grille
    nombre_de_blocs_vivants = 0
    
    pourcentage_vie_actuel = 0
    for i in range(0,taille_grille):
        for j in range(0,taille_grille):
            tableau[i][j] = False
    
    while (pourcentage_vie_actuel <= pourcentage_vie and pourcentage_vie != float(0)):
        x_random = randint(0, taille_grille-1)
        #print("<---- x rand : %d --->" % x_random)
        y_random = randint(0, taille_grille-1)
        #print("<---- y rand : %d --->" % y_random)
        tableau[x_random][y_random] = True
        nombre_de_blocs_vivants += 1
        pourcentage_vie_actuel = float(nombre_de_blocs_vivants/nombre_de_blocs)
        #print("<---- pourcentage actuel : %f --->" % pourcentage_vie_actuel)
        
    
    #print("La grille est initialisée.\n")


## -- Dessiner la grille vide --
def dessiner_grille(tableau):
    global taille_grille
    global taille_bloc
    global couleur_cellule
    global couleur_fond
    
    # Effacer la grille précédente
    canevas.delete("all")
        
    # Dessiner la nouvelle grille
    position_x = 0
    position_y = 0
    for i in range(taille_grille):
        position_x = 0
        for j in range(taille_grille):
            tag = str(position_x) + "-" + str(position_y)
            if (tableau[i][j] == True):
                canevas.create_rectangle(position_x, position_y, position_x + taille_bloc, position_y + taille_bloc, fill=couleur_cellule, tags=("Cellule vivante", tag))
            else:
                canevas.create_rectangle(position_x, position_y, position_x + taille_bloc, position_y + taille_bloc, fill=couleur_fond, tags=("Cellule morte", tag))
            position_x += taille_bloc
        position_y += taille_bloc    
    
    # Debugging
    #print(canevas.find_all())
    
## -- Initialiser le jeu --         
def initialiser_jeu():
    # Appeler initialiser_grille(grille, pourcentage_vie)
    # Appeler dessiner_grille(canevas)
    initialiser_tableau(tableau)
    dessiner_grille(tableau)
    #print("Le jeu est initialisé.\n")
    nombre_de_voisins(5,5,tableau)
    
    
## -- Chercher case -- 
def chercher_case(i, j, tableau):   
    #print((i+taille_grille)%taille_grille, " ", (j+taille_grille)%taille_grille, " ", tableau[(i+taille_grille)%taille_grille][(j+taille_grille)%taille_grille], "\n")
    return tableau[(i+taille_grille*10)%taille_grille-1][(j+taille_grille*10)%taille_grille-1]

## -- Compter le nombre de voisins d'une case grille[i][j] --         
def nombre_de_voisins(i, j, tableau):
    nbr_de_voisins = 0
    nbr_de_voisins += 1 if chercher_case(i-1, j-1, tableau) else 0
    nbr_de_voisins += 1 if chercher_case(i-1, j, tableau) else 0
    nbr_de_voisins += 1 if chercher_case(i-1, j+1, tableau) else 0
    nbr_de_voisins += 1 if chercher_case(i, j-1, tableau) else 0
    nbr_de_voisins += 1 if chercher_case(i, j+1, tableau) else 0
    nbr_de_voisins += 1 if chercher_case(i+1, j-1, tableau) else 0
    nbr_de_voisins += 1 if chercher_case(i+1, j, tableau) else 0
    nbr_de_voisins += 1 if chercher_case(i+1, j+1, tableau) else 0
    #print("Le nombre de voisins de (", i, ",", j,") est ", nbr_de_voisins, "\n")
    return nbr_de_voisins

## -- Mise à jour grille --             
def mise_a_jour_grille(tableau, copie_tableau):
    global taille_grille
    global statut
    global pas
    
    if (statut == True):
        # copie du tableau précédent
        for i in range(taille_grille):
            for j in range(taille_grille):
                copie_tableau[i][j] = tableau[i][j]
                
        # Analyse grille
        for i in range(taille_grille):
            for j in range(taille_grille):
                if (nombre_de_voisins(i, j, copie_tableau) < 2 or nombre_de_voisins(i, j, copie_tableau) > 3):
                    tableau[i][j] = False
                elif (nombre_de_voisins(i, j, copie_tableau) == 3):
                    tableau[i][j] = True
        
        dessiner_grille(tableau)
        root.after(pas, mise_a_jour_grille, tableau, copie_tableau)

## -- Mise à jour des Sliders -- 
def slider_taille_grille(val):
    global taille_grille
    global taille_bloc
    global pourcentage_vie
    global vitesse_animation
    global tableau
    global copie_tableau
    
    taille_grille = int(val)
    taille_bloc = hauteur_fenetre/taille_grille
    #print("Slider_val =",val,"\nTaille grille = ", taille_grille, "\nPourcentage_vie =", pourcentage_vie, "\nVitesse = ", vitesse_animation,"\n")
    tableau = [[0 for j in range(taille_grille)] for i in range(taille_grille)]
    copie_tableau = [[0 for j in range(taille_grille)] for i in range(taille_grille)]

    
def slider_pourcentage_vie(val):
    global taille_grille
    global pourcentage_vie
    global vitesse_animation
    pourcentage_vie = float(val)
    #print("Slider_val =",val,"\nTaille grille = ", taille_grille, "\nPourcentage_vie =", pourcentage_vie, "\nVitesse = ", vitesse_animation,"\n")
    
def slider_vitesse_animation(val):
    global taille_grille
    global pourcentage_vie
    global vitesse_animation 
    global pas
    
    vitesse_animation = int(val)
    pas = int(1000/vitesse_animation)
    #print("Slider_val =",val,"\nTaille grille = ", taille_grille, "\nPourcentage_vie =", pourcentage_vie, "\nVitesse = ", vitesse_animation,"\n")
    

# ----------- INITIALISATION -------------
#grille = # On définit la variable grille
#sauvegarde_grille =  # On définit de même sa sauvegarde

# Configuration
root = Tk() # Fenêtre principale Tkinter
root.title("SR01 - Devoir 3 - Jeu de la vie")
root.resizable(False, False)

# Barre menu
menu_cote = Frame(root, width=hauteur_fenetre*0.3, height=hauteur_fenetre, bg='#f0f0f0', relief='flat', borderwidth=2)
menu_cote.pack(expand=False, fill='both', side='right', anchor='nw')
# Fenêtre grille    
grille = Frame(root, width=largeur_fenetre, height=hauteur_fenetre, bg='white')
grille.pack(expand=False, fill='both', side='left')
# Canevas
canevas = Canvas(grille, width=largeur_fenetre, height=hauteur_fenetre, bg='white')
canevas.pack(fill=BOTH, expand=1)
    
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
bouton_vitesse = Scale(menu_cote, orient='horizontal', from_=1, to=100, length=180, variable=vitesse_animation, bg='#f0f0f0', relief='flat', highlightthickness=0, label='Vitesse', fg='blue', command=slider_vitesse_animation)
bouton_vitesse.pack(side='bottom')

## Pourcentage de vie ## -- Paramètres real time -- 
bouton_pourcentage_vie = Scale(menu_cote, orient='horizontal', from_=0, to=1, length=180,  variable=pourcentage_vie, resolution=0.001, bg='#f0f0f0', relief='flat', highlightthickness=0, label='% de Vie', fg='blue', bd='0', command=slider_pourcentage_vie)
bouton_pourcentage_vie.pack(side='bottom')

## Taille de la grille ## -- Paramètres init --
bouton_taille_grille = Scale(menu_cote, orient='horizontal', from_=5, to=500, length=180, variable=taille_grille, bg='#f0f0f0', relief='flat', highlightthickness=0, label='Taille de la grille', fg='blue', command=slider_taille_grille)
bouton_taille_grille.pack(side='bottom')

root.mainloop() # Appel boucle