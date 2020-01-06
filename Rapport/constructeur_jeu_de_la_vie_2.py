        ## Frame Fenetre principale
        ### Frame
        self.principale = tk.Frame(self.root, width = self.taille_fenetre, height = self.taille_fenetre, bg = "white")
        self.principale.pack(expand = False, fill = "both", side = "left")
        ### Canevas de dessin
        self.canevas = tk.Canvas(self.principale, width = taille_fenetre, height = taille_fenetre, bg = "white")    
        self.canevas.pack(fill = 'both', expand = 1)
        
        ## Boutons de l'application
        self.bouton_lancer = tk.Button(self.menu_cote, text = "Lancer", relief = "solid", fg = "blue", width = 20, command =self.lancer_jeu)
        self.bouton_lancer.pack(side = "top")
        
        self.bouton_arreter = tk.Button(self.menu_cote, text = "Arreter", relief = "solid", fg = "blue", width = 20, command =self.arreter_jeu)
        self.bouton_arreter.pack(side = "top")
        
        self.bouton_init = tk.Button(self.menu_cote, text = "Initialiser", relief = "solid", fg = "blue", width = 20, command =self.initialiser_jeu)
        self.bouton_init.pack(side = "top")
        
        self.bouton_quitter = tk.Button(self.menu_cote, text = "Quitter", relief = "solid", fg= "blue", width = 20, command = self.root.destroy)
        self.bouton_quitter.pack(side = "bottom")
        
