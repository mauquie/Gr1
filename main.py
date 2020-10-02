import random
from random import randint


class Carte():
    def __init__(self):
        self.RANGS =["2","3","4","5","6","7","8","9","X","V","D","R","A"]
        self.COULEURS = ["P","C","K","T"]

        
class Croupier(Carte):
    """
        La classe croupier prend comme parametre:
            paquet -> paquet de 52 carte
    """
    def __init__(self):
        Carte.__init__(self)
        self.paquet = []
    def rassembler(self): #Méthode qui crée 52 cartes non mélangé
        for i in range(0, len(self.COULEURS)):
            for j in range(0, len(self.RANGS)):
                self.paquet.append(self.COULEURS[i] + self.RANGS[j])

    def melanger(self): #Méthode qui va mélanger les 52 cartes
        random.shuffle(self.paquet)

    def couper(self): #Méthode qui va couper le paquet
        rand = randint(1, 50)
        t_paquet = []
        for i in range (0, rand):
            _paquett.append(self.paquet[0])
            self.paquet.pop(0)
        for i in range (0, len(t_paquet)):
            self.paquet.append(t_paquet[0])
            t_paquet.pop(0)

    def nouvelle_donne(self):
        self.rassembler()
        self.melanger()
        self.couper()



class Joueur(Croupier):

    def __init__(self , nom = "Joueur", main = None, tapis=500):
        Croupier.__init__(self)
        self.nom=nom
        self.main=main#les cartes en main sont une liste
        self.tapis=tapis#tapis étant le nombre de jetons

    def vider_main(self):#on supprime la main actuelle
        for i in range(0,5):#le mode de jeu est de 5 carte privatives...
            self.main.pop()#on les supprimes

    def recevoir(self):
        if len(self.main + 1)!= 0:
            vider_main()
        for i in range(5):
            self.main.append(self.paquet[-1])
            self.paquet.pop()#besoin de 5 nouvelles cartes, en fonction de croupier.. en attente de plus d'info sur la classe
            