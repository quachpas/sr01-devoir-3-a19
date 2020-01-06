# Méthode du slider <pourcentage de vie>
    def slider_pourcentage_vie(self, nouvelle_valeur):
        # On met à jour la valeur
        self.pourcentage_vie = float(nouvelle_valeur)
        
    # Méthode du slider <vitesse d'animation>
    def slider_vitesse_animation(self, nouvelle_valeur):
        # On met à jour la valeur
        self.vitesse_animation = int(nouvelle_valeur)
        # On recalcule le pas utilisé pour animer le jeu dans la boucle pour
        self.pas = int(1000/self.vitesse_animation)
    
    # Méthode du slider <Taille de la grille>
    def slider_taille_grille(self, nouvelle_valeur):
        # On met à jour la valeur
        self.taille_grille = int(nouvelle_valeur)
        # On recalcule la taille d'un bloc pour les afficher
        self.taille_bloc = self.taille_fenetre/self.taille_grille
        # On réinitialise les variables tableaux à la bonne taille
        self.grille.__init__(self.taille_grille)