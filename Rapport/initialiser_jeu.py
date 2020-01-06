# Méthode du bouton <initialisation>
    def initialiser_jeu(self):
        # On appelle la méthode de l'objet grille 
        self.grille.initialiser_tableau(self.taille_grille, self.pourcentage_vie)
        
        # On appelle la méthode de dessin
        self.dessiner_grille()
