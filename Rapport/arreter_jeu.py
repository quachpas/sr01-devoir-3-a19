# Méthode du bouton <Arrêter>
    def arreter_jeu(self):
        # Changement du statut de l'application
        ## Le changement de statut est suffisant pour arrêter la boucle du jeu
        self.statut = False
        
        # Modification des boutons pour les réactiver
        self.bouton_taille_grille.config(state = "active", label = "Taille de la grille", length = 180)
        self.bouton_pourcentage_vie.config(state = "active", label = "% de Vie", length = 180)
        self.bouton_vitesse.config(length = 180)