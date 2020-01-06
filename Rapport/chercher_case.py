# Retourne le booléen d'une case (i,j)
    def chercher_case(self, i,j, n):
        
        # Mode d'adressage prenant en comptant les bords
        ## Le coefficient est présent pour ajuster en cas de débordement trop conséquent
        return self.tableau[(i+n*10)%n-1][(j+n*10)%n-1]