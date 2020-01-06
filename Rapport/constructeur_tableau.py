# On construit un simple tableau de taille n x n
def __init__(self, n):
        self.tableau = [[bool(0) for j in range(n)] for i in range(n)]