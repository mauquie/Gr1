class Coup(Croupier, Joueur): #faire un coup
    def __Init__(Croupier, Joueur):# faire une nouvelle donne(Joueurs et Croupier)
        Croupier.__init__(self)
        Joueur.__init__(self)
        #RANGS[12]>RANGS[11]>RANGS[10]>RANGS[9]>RANGS[8]>RANGS[7]>RANGS[6]>RANGS[5]>RANGS[4]>RANGS[3]>RANGS[2]>RANGS[1]>RANGS[0]
        
        
         
        Hauteur=0
        Paire=200 #2 carte de meme valeures mais de couleur différentes
        DeuxPaires=300# 2*2 carte de meme valeures mais de couleur différentes (ex: 2C 2P RK RC 7T)
        Brelan=400# 3 cartes de meme valeures != couleurs
        Suite=500#5 cartes ayant des valeures successive != couleurs diff
        Couleur=600# 5 carrte meme couleurs
        Full=700# 3 carte meme val id !=couleurs + 2 carte id != couleurs
        Carre=800# 4 carte meme val != couleurs
        QuinteFlush=900# 5 carte qui se suive + meme couleurs
        QuinteFlushRoyale=1000# 5 carte qui se suivent  + meme couleurs avec " A R D V 10"

    def avoir_couleur ():
        couleur = True # On part du principe que le joueur a une couleur
        for i in range(0, 4): 
            if self.main[0][0] != self.main[i][0]: # On teste si la carte selectionné a la meme couleur que la première carte
                couleur == False

    def avoir_carre():
        carre = True  # On part du principe que le joueur a un carre : False est retournée en cas contraire 
        compteur = 0
        a=4
        for i in range(0, 5):
            for j in range(0,a):
                if self.main[i][0] == self.main[-a][0]:# On teste si la carte selectionné a la meme valeur que la première carte
                    compteur+= 1
            a = a - 1
        if  compteur_carre < 1 :
            carre = False
                

    def analyse_main():
        pass
                
    def gagnant():
        pass
        #i in range(len(self.listeJoueur)
        
        
    def ListeDeJoueurs(Joueur,self): #liste de joueurs participant au coup Croupier
        joueur.append(self)
        
    def Distribuer(Croupier): # demander au Croupier de distribuer N cartes à la liste des joueurs
        pass
