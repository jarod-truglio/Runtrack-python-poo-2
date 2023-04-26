class Personne:
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge(self):
        print(f"L'âge de la personne est {self.age}")

    def Bonjour(self):
        print("Bonjour")

    def ModifierAge(self):
        self.age += 1
    
class Eleve(Personne):
    def AllerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

class Professeur:
    def __init__(self, matiereEnseignee, age=40):
        self.__matiereEnseignee = matiereEnseignee
        self.age = age

    def enseigner(self):
        print("Bonjour")
        print(f"Le cours {self.__matiereEnseignee} va commencer")

p = Personne()
e = Eleve()
Prof = Professeur("d'Histoire")

e.Bonjour()
e.ModifierAge()
e.AllerEnCours()
e.afficherAge()
Prof.enseigner()