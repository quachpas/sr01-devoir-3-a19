# Méthode de dessin de l'application
    def dessiner_grille(self):
        # On supprime l'ancien tableau
        self.canevas.delete("all")
        
        # Initialisation de la position du pointeur
        position_x = 0
        position_y = 0
        # On parcourt le canvas ligne par ligne et on dessine rectangle par rectangle
        for i in range(self.taille_grille):
            position_x = 0
            for j in range(self.taille_grille):
                ### Si la case associée dans le tableau est vivante, on la remplit en rouge
                if (self.grille.tableau[i][j] == True):
                    self.canevas.create_rectangle(position_x, position_y, position_x + self.taille_bloc, position_y + self.taille_bloc, fill = self.couleur_cellule)
                ### Sinon, on ne la remplit pas
                else:
                    self.canevas.create_rectangle(position_x, position_y, position_x + self.taille_bloc, position_y + self.taille_bloc, fill = self.couleur_fond)
                position_x += self.taille_bloc
            ## On passe à la ligne suivante
            position_y += self.taille_bloc