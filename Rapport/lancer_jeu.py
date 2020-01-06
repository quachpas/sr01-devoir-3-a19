# Méthode du bouton <Lancer>
    def lancer_jeu(self):
        # Changement du statut de l'application
        self.statut = True
        
        # Modification des boutons pour les désactiver
        self.bouton_taille_grille.config(state = "disabled", label = "Taille de la grille (DESACTIVE)", length = 220)
        self.bouton_pourcentage_vie.config(state = "disabled", label = "% de Vie (DESACTIVE)", length = 220)
        self.bouton_vitesse.config(length = 220)
        
        # Lancement de la boucle du jeu
        self.boucle()