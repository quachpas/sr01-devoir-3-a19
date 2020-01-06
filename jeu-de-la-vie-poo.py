import tkinter as tk   ## notice lowercase "t" in tkinter here
import tkinter.messagebox as messagebox
import time as time
import random as random
import math as math
from tkinter import constants

        
class Tableau():
    def __init__(self, n):
        self.tableau = [[bool(0) for j in range(n)] for i in range(n)]
    
    def initialiser_tableau(self, n, pourcentage_vie):
        nombre_de_blocs = n*n
        nombre_de_blocs_vivants = 0
        pourcentage_vie_actuel = 0
        
        # Tableau blanc
        for i in range(0, n):
            for j in range(0, n):
                self.tableau[i][j] = False
        
        while (float(pourcentage_vie_actuel) < pourcentage_vie and pourcentage_vie != float(0)):
            x_random = random.randint(0, n - 1)
            y_random = random.randint(0, n - 1)
            i=0
            while(self.tableau[x_random][y_random] == True):#and i<n*n:
                if (x_random == n-1):
                    x_random=0
                    if (y_random==n-1):
                        y_random=0
                    else:
                        y_random=y_random+1
                else:
                    x_random=x_random+1
                i=i+1
                print("Case ", x_random, " ", y_random, "\n")
                time.sleep(0.5)
                                
            self.tableau[x_random][y_random] = True
            nombre_de_blocs_vivants += 1
            pourcentage_vie_actuel = float(nombre_de_blocs_vivants/nombre_de_blocs)
            print("pourcentage actuel :", pourcentage_vie_actuel, "\n")

    def chercher_case(self, i,j, n):
        return self.tableau[(i+n*10)%n-1][(j+n*10)%n-1]

    def nombre_de_voisins(self, i, j, n):
        nbr_de_voisins = 0
        nbr_de_voisins += 1 if self.chercher_case(i-1, j-1, n) else 0
        nbr_de_voisins += 1 if self.chercher_case(i-1, j, n) else 0
        nbr_de_voisins += 1 if self.chercher_case(i-1, j+1, n) else 0
        nbr_de_voisins += 1 if self.chercher_case(i, j-1, n) else 0
        nbr_de_voisins += 1 if self.chercher_case(i, j+1, n) else 0
        nbr_de_voisins += 1 if self.chercher_case(i+1, j-1, n) else 0
        nbr_de_voisins += 1 if self.chercher_case(i+1, j, n) else 0
        nbr_de_voisins += 1 if self.chercher_case(i+1, j+1, n) else 0
        #print("Le nombre de voisins de (", i, ",", j,") est ", nbr_de_voisins, "\n")
        return nbr_de_voisins

    def mise_a_jour_grille(self, n):
        copie_tableau = Tableau(n)
        for i in range(n):
            for j in range(n):
                copie_tableau.tableau[i][j] = self.tableau[i][j]
                
        # Analyse grille
        for i in range(n):
            for j in range(n):
                if (copie_tableau.nombre_de_voisins(i, j, n) < 2 or copie_tableau.nombre_de_voisins(i, j, n) > 3):
                    self.tableau[i][j] = False
                elif (copie_tableau.nombre_de_voisins(i, j, n) == 3):
                    self.tableau[i][j] = True
    

class Jeu_de_la_vie():    
    
    def __init__(self, couleur_cellule, couleur_fond, taille_fenetre, taille_grille, statut, pourcentage_vie, vitesse_animation):
        # Parametres
        self.couleur_cellule = couleur_cellule
        self.couleur_fond = couleur_fond
        self.taille_fenetre = taille_fenetre
        self.taille_grille = taille_grille
        self.taille_bloc = self.taille_fenetre/self.taille_grille
        self.pas = int(1000/vitesse_animation)
        self.statut = False
        self.pourcentage_vie = pourcentage_vie
        self.grille = Tableau(self.taille_grille)
        
        # GUI
        self.root = tk.Tk()
        self.root.title("SR01 - Devoir 3 - Jeu de la vie")
        self.root.resizable(False, False)
            
        self.menu_cote = tk.Frame(self.root, width = self.taille_fenetre*0.3, height = self.taille_fenetre, bg = "#f0f0f0", relief = "flat", borderwidth = 2)
        self.menu_cote.pack(expand = False, fill = "both", side = "right", anchor = "nw")
        self.principale = tk.Frame(self.root, width = self.taille_fenetre, height = self.taille_fenetre, bg = "white")
        self.principale.pack(expand = False, fill = "both", side = "left")
        
        self.canevas = tk.Canvas(self.principale, width = taille_fenetre, height = taille_fenetre, bg = "white")    
        self.canevas.pack(fill = 'both', expand = 1)
        
        
        self.bouton_lancer = tk.Button(self.menu_cote, text = "Lancer", relief = "solid", fg = "blue", width = 20, command =self.lancer_jeu)
        self.bouton_lancer.pack(side = "top")
        
        self.bouton_arreter = tk.Button(self.menu_cote, text = "Arreter", relief = "solid", fg = "blue", width = 20, command =self.arreter_jeu)
        self.bouton_arreter.pack(side = "top")
        
        self.bouton_init = tk.Button(self.menu_cote, text = "Initialiser", relief = "solid", fg = "blue", width = 20, command =self.initialiser_jeu)
        self.bouton_init.pack(side = "top")
        
        self.bouton_init = tk.Button(self.menu_cote, text='Quitter', relief='solid', fg='blue', width=20, command=self.root.destroy)
        self.bouton_init.pack(side='bottom')
        
        self.bouton_vitesse = tk.Scale(self.menu_cote, orient = "horizontal", from_ = 1, to = 100, length = 180, variable = vitesse_animation, bg = "#f0f0f0", relief = "flat", highlightthickness = 0, label = "Vitesse", fg = "blue", command = self.slider_vitesse_animation)
        self.bouton_vitesse.pack(side = "bottom")

        self.bouton_pourcentage_vie = tk.Scale(self.menu_cote, orient = "horizontal", from_= 0, to = 1, length = 180,  variable = pourcentage_vie, resolution = 0.001, bg = "#f0f0f0", relief = "flat", highlightthickness = 0, label = "% de Vie", fg = "blue", bd = "0", command = self.slider_pourcentage_vie)
        self.bouton_pourcentage_vie.set(self.pourcentage_vie)
        self.bouton_pourcentage_vie.pack(side = "bottom")
        
        self.bouton_taille_grille = tk.Scale(self.menu_cote, orient = "horizontal", from_= 5, to = 100, length = 180, variable = taille_grille, bg = "#f0f0f0", relief = "flat", highlightthickness = 0, label = "Taille de la grille", fg = "blue", command = self.slider_taille_grille)
        self.bouton_taille_grille.pack(side = "bottom")
        

    def lancer_jeu(self):
        self.statut = True
        self.bouton_taille_grille.config(state = "disabled", label = "Taille de la grille (DESACTIVE)", length = 220)
        self.bouton_pourcentage_vie.config(state = "disabled", label = "% de Vie (DESACTIVE)", length = 220)
        self.bouton_vitesse.config(length = 220)
        
        self.boucle()
        
        
    def boucle(self):
        if (self.statut == True):
            self.grille.mise_a_jour_grille(self.taille_grille)
            self.dessiner_grille()
            self.root.after(self.pas, self.boucle)
        
    def arreter_jeu(self):
        self.statut = False
        self.bouton_taille_grille.config(state = "active", label = "Taille de la grille", length = 180)
        self.bouton_pourcentage_vie.config(state = "active", label = "% de Vie", length = 180)
        self.bouton_vitesse.config(length = 180)
        
    def initialiser_jeu(self):
        self.grille.initialiser_tableau(self.taille_grille, self.pourcentage_vie)
        self.dessiner_grille()
        
    def dessiner_grille(self):
        self.canevas.delete("all")
        position_x = 0
        position_y = 0
        for i in range(self.taille_grille):
            position_x = 0
            for j in range(self.taille_grille):
                if (self.grille.tableau[i][j] == True):
                    self.canevas.create_rectangle(position_x, position_y, position_x + self.taille_bloc, position_y + self.taille_bloc, fill = self.couleur_cellule)
                else:
                    self.canevas.create_rectangle(position_x, position_y, position_x + self.taille_bloc, position_y + self.taille_bloc, fill = self.couleur_fond)
                position_x += self.taille_bloc
            position_y += self.taille_bloc
            
    
    def slider_pourcentage_vie(self, nouvelle_valeur):
        self.pourcentage_vie = float(nouvelle_valeur)
        
    def slider_vitesse_animation(self, nouvelle_valeur):
        self.vitesse_animation = int(nouvelle_valeur)
        self.pas = int(1000/self.vitesse_animation)
    
    def slider_taille_grille(self, nouvelle_valeur):
        self.taille_grille = int(nouvelle_valeur)
        self.taille_bloc = self.taille_fenetre/self.taille_grille
        self.grille.__init__(self.taille_grille)
        


Fenetre = Jeu_de_la_vie("red", "white", 834, 5, False, 0.3, 1)
Fenetre.root.mainloop()