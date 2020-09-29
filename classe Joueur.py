class Joueur(Croupier):
    def __init__(self,nom,main,tapis=500,combinaison):
        Croupier.__init__(self)
        self.nom=nom
        self.main=main#les cartes en main sont une liste
        self.tapis=tapis#tapis étant le nombre de jetons

        def main(self):#affiche la main , à enlevée quand ce sera pris en charge par le programme principal
            return (self.main)

        def nouvelle_donne(self):#on supprime la main actuelle
            for i in range(0,5):#le mode de jeu est de 5 carte privatives...
                self.main.pop()#on les supprimes
            
        def recevoir(self,paquet):
            for i in range(5):
                self.main.append(self.paquet[-1])
                self.paquet.pop()#besoin de 5 nouvelles cartes, en fonction de croupier.. en attente de plus d'info sur la classe
