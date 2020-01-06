# Calcul du nombre de voisins d'une case
    def nombre_de_voisins(self, i, j, n):
        nbr_de_voisins = 0
        nbr_de_voisins += 1 if self.chercher_case(i-1, j-1, n) else 0
        nbr_de_voisins += 1 if self.chercher_case(i-1, j, n) else 0
        nbr_de_voisins += 1 if self.chercher_case(i-1, j+1, n) else 0
        nbr_de_voisins += 1 if self.chercher_case(i, j-1, n) else 0
        nbr_de_voisins += 1 if self.chercher_case(i, j+1, n) else 0
        nbr_de_voisins += 1 if self.chercher_case(i+1, j-1, n) else 0
        nbr_de_voisins += 1 if self.chercher_case(i+1, j, n) else 0
        nbr_de_voisins += 1 if self.chercher_case(i+1, j+1, n) else 0
        return nbr_de_voisins