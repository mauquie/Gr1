class Carte():
    def __init__(self,couleur,rang):
        RANGS =["2","3","4","5","6","7","8","9","X","V","D","R","A"]
        COULEURS = ["P","C","K","T"]
        self.nbcouleur=couleur
        self.couleur=COULEURS[self.nbcouleur]
        self.nbrang=rang
        self.rang=RANGS[self.nbrang]
