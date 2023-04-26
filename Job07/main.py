import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    
    def __str__(self):
        return f"{self.valeur} de {self.couleur}"
    
    def get_valeur(self):
        if self.valeur in ['J', 'Q', 'K']:
            return 10
        elif self.valeur == 'A':
            return 11
        else:
            return int(self.valeur)

class Jeu:
    def __init__(self):
        valeurs = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
        couleurs = ['Coeur', 'Pique', 'Carreau', 'Trèfle']
        self.paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(self.paquet)
    
    def donner_carte(self):
        return self.paquet.pop()
    
    def valeur_main(self, main):
        valeur = 0
        as_count = 0
        for carte in main:
            valeur += carte.get_valeur()
            if carte.valeur == 'A':
                as_count += 1
        while valeur > 21 and as_count > 0:
            valeur -= 10
            as_count -= 1
        return valeur

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []
    
    def recevoir_carte(self, carte):
        self.main.append(carte)
    
    def afficher_main(self, cachee=False):
        print(f"Main de {self.nom}:")
        if cachee:
            print("Carte cachée")
            for carte in self.main[1:]:
                print(carte)
        else:
            for carte in self.main:
                print(carte)
        print(f"Total : {self.calculer_total()}")
    
    def calculer_total(self):
        return Jeu().valeur_main(self.main)

class Partie:
    def __init__(self):
        self.jeu = Jeu()
        self.croupier = Joueur('Croupier')
        self.joueur = Joueur(input("Entrez votre nom : "))
        self.joueur.recevoir_carte(self.jeu.donner_carte())
        self.croupier.recevoir_carte(self.jeu.donner_carte())
        self.joueur.recevoir_carte(self.jeu.donner_carte())
        self.croupier.recevoir_carte(self.jeu.donner_carte())
        self.joueur.afficher_main()
        self.croupier.afficher_main(True)
    
    def tour_joueur(self):
        while True:
            choix = input("Voulez-vous prendre une carte (P) ou passer (S) ? ").lower()
            if choix == 'p':
                self.joueur.recevoir_carte(self.jeu.donner_carte())
                self.joueur.afficher_main()
                if self.joueur.calculer_total() > 21:
                    print(f"{self.joueur.nom} a dépassé 21, il perd.")
                    return False
            elif choix == 's':
                return True
    
    def tour_croupier(self):
        self.croupier.afficher_main(False)
        while self.croupier.calculer_total() < 17:
            self.croupier.recevoir_carte(self.jeu.donner_carte())