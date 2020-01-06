# Mise à jour du tableau 
    ## On crée un deuxième Tableau qui est une copie du premier
    ## On met à jour le premier Tableau à partir du deuxième
    def mise_a_jour_grille(self, n):
        
        # Copie du tableau
        copie_tableau = Tableau(n)
        for i in range(n):
            for j in range(n):
                copie_tableau.tableau[i][j] = self.tableau[i][j]
                
        # Analyse grille
        for i in range(n):
            for j in range(n):
                if (copie_tableau.nombre_de_voisins(i, j, n) < 2 or copie_tableau.nombre_de_voisins(i, j, n) > 3):
                    self.tableau[i][j] = False
                elif (copie_tableau.nombre_de_voisins(i, j, n) == 3):
                    self.tableau[i][j] = True