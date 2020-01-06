# Méthode d'initialisation du tableau. 
## Remise à zéro du tableau
## Cases en vie aléatoirement avec un certain pourcentage
def initialiser_tableau(self, n, pourcentage_vie):
        nombre_de_blocs = n*n
        nombre_de_blocs_vivants = 0
        pourcentage_vie_actuel = 0 # Variable pour comparer 
        
        # On met le tableau à zéro. 
        for i in range(0, n):
            for j in range(0, n):
                self.tableau[i][j] = False
        
        # Boucle pour les cellules en vie
        while (float(pourcentage_vie_actuel) < pourcentage_vie and pourcentage_vie != float(0)):
            
            # Coordonnées aléatoires
            x_random = random.randint(0, n - 1)
            y_random = random.randint(0, n - 1)
            
            # Vérification que la case n'est pas déjà en vie
            ## Si c'est le cas, on choisit une autre case en parcourant le tableau
            while(self.tableau[x_random][y_random] == True):
                if (x_random == n-1):
                    x_random=0
                    if (y_random==n-1):
                        y_random=0
                    else:
                        y_random=y_random+1
                else:
                    x_random=x_random+1
        
            self.tableau[x_random][y_random] = True # Cellule en vie
            
            # Calcul du pourcentage
            nombre_de_blocs_vivants += 1
            pourcentage_vie_actuel = float(nombre_de_blocs_vivants/nombre_de_blocs)