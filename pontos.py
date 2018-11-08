class Ponto2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str("Valor x: " + str(self.x) + ", Valor y: " + str(self.y))

class Ponto3D(Ponto2D):

    def __init__(self, x, y, z):
        Ponto2D.__init__(self, x, y)
        self.z = z
    
    def __str__(self):
        return str(Ponto2D.__str__(self) + ", Valor z: " + str(self.z))


a = Ponto2D(2, 3)
b = Ponto3D(2, 4, 6)

print(a)
print(b)