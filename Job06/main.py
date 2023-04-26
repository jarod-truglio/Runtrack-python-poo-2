class Véhicule:
    def __init__(self, marque, annee, prix, modele):
        self.marque = marque
        self.annee = annee
        self.prix = prix
        self.modele = modele

    def InformationsVehicules(self):
        print(self.marque, self.annee, self.prix, self.modele)

    def Demarrer(self):
        print("Attention je roule")

class Voiture(Véhicule):
    def __init__(self, marque, annee, prix, modele,portes=4):
        super().__init__(marque, annee, prix, modele)
        self.portes = portes

    def InformationsVehicules(self):
        print("-----------------")
        print("La marque est :",self.marque)
        print("Le modèle est :",self.modele)
        print("L'année est :", self.annee)
        print("La Voiture possède :",self.portes, "portes")
        print("Le prix est de :",self.prix)
        print("-----------------")

    def Demarrer(self):
        print("Tut ! Tut ! Oh Chauffare je roule !")

class Moto(Véhicule):
    def __init__(self, marque, annee, prix, modele, roue=2):
        super().__init__(marque, annee, prix, modele)
        self.roue = roue

    def InformationsVehicules(self):
        print("-----------------")
        print("La marque est :",self.marque)
        print("Le modèle est :",self.modele)
        print("L'année est :", self.annee)
        print("La Moto possède :",self.roue, "roues")
        print("Le prix est de :",self.prix)
        print("-----------------")

    def Demarrer(self):
        print("Chauf marcel je roule !")

v = Voiture("Mercedes","2020","18500 $","Classe A")
m = Moto("Yamaha","1987","4500 $","1200 Vmax")
v.InformationsVehicules()
v.Demarrer()
m.InformationsVehicules()
m.Demarrer()