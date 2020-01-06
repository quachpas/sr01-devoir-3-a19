# Constructeur de l'application 
    def __init__(self, couleur_cellule, couleur_fond, taille_fenetre, taille_grille, statut, pourcentage_vie, vitesse_animation):
        
        # Parametres
        self.couleur_cellule = couleur_cellule # Couleur d'une cellule en vie
        self.couleur_fond = couleur_fond # Couleur d'une cellule morte
        self.taille_fenetre = taille_fenetre # Taille de la fenetre qui contiendra le jeu de la vie en pixels
        self.taille_grille = taille_grille # Taille de la GRILLE du jeu de la vie en nombre de blocs
        self.taille_bloc = self.taille_fenetre/self.taille_grille # Calcul de la taille d'un bloc
        self.vitesse_animation = vitesse_animation # Vitesse de l'animation
        self.pas = int(1000/vitesse_animation) # Le pas est par défaut à 1s, vitesse de 1 à 100. Vitesse de 0.1 s à 1.0s
        self.statut = False # Le booléen du jeu. Marche ou Arrêt
        self.pourcentage_vie = pourcentage_vie # Le pourcentage de vie demandé pour l'initialisation du jeu
        self.grille = Tableau(self.taille_grille) # Initialisation d'un objet grille
        
        # Interface Graphique Utilisateur
        ## Configuration Tkinter
        self.root = tk.Tk() 
        self.root.title("SR01 - Devoir 3 - Jeu de la vie")
        self.root.resizable(False, False) # Non extensible
        
        ## Frame Menu des boutons sur le côté
        self.menu_cote = tk.Frame(self.root, width = self.taille_fenetre*0.3, height = self.taille_fenetre, bg = "#f0f0f0", relief = "flat", borderwidth = 2)
        self.menu_cote.pack(expand = False, fill = "both", side = "right", anchor = "nw")
 