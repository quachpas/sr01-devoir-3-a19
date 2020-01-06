# Boucle interne du jeu
    def boucle(self):
        if (self.statut == True):
            self.grille.mise_a_jour_grille(self.taille_grille)
            self.dessiner_grille()
            self.root.after(self.pas, self.boucle)