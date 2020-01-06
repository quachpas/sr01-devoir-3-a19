        ## Sliders de l'application
        self.bouton_vitesse = tk.Scale(self.menu_cote, orient = "horizontal", from_ = 1, to = 100, length = 180, variable = vitesse_animation, bg = "#f0f0f0", relief = "flat", highlightthickness = 0, label = "Vitesse", fg = "blue", command = self.slider_vitesse_animation)
        self.bouton_vitesse.set(self.vitesse_animation) # Mise du slider sur la valeur passé en paramètre
        self.bouton_vitesse.pack(side = "bottom")

        self.bouton_pourcentage_vie = tk.Scale(self.menu_cote, orient = "horizontal", from_= 0, to = 1, length = 180,  variable = pourcentage_vie, resolution = 0.001, bg = "#f0f0f0", relief = "flat", highlightthickness = 0, label = "% de Vie", fg = "blue", bd = "0", command = self.slider_pourcentage_vie)
        self.bouton_pourcentage_vie.set(self.pourcentage_vie) # Mise du slider sur la valeur passé en paramètre
        self.bouton_pourcentage_vie.pack(side = "bottom")
        
        self.bouton_taille_grille = tk.Scale(self.menu_cote, orient = "horizontal", from_= 5, to = 100, length = 180, variable = taille_grille, bg = "#f0f0f0", relief = "flat", highlightthickness = 0, label = "Taille de la grille", fg = "blue", command = self.slider_taille_grille)
        self.bouton_taille_grille.set(self.taille_grille) # Mise du slider sur la valeur passé en paramètre
        self.bouton_taille_grille.pack(side = "bottom")