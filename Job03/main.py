class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def Perimetre(self):
        perimetre = self.__longueur + self.__largeur * 2
        print(f"Le Perimetre du Rectangle est de : {perimetre}")

    def Surface(self):
        surface = self.__longueur * self.__largeur
        print(f"Le Surface du Rectangle est de : {surface}")

    def get_Longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

class Parrallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def Volume(self):
        volume = self.get_Longueur() * self.get_largeur() * self.hauteur
        print(f"Le Volume du Parrallelepipede est de : {volume}")

r = Rectangle(10,10)
p = Parrallelepipede(10,10,10)

r.Perimetre()
r.Surface()
p.Volume()