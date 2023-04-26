class Forme:
    def aire(self):
        return 0

class Cercle(Forme):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def aire(self):
        air = 3.14159 * self.radius**2
        return f"L'aire du Cercle est de {air}"

f = Forme()
c = Cercle(7)
print(c.aire())