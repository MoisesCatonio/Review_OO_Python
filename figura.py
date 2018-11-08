class Figura_Geometrica:

    def __init__(self, x=-1, y=-1):
        if(x>0 and y>0):
            self.x = x
            self.y = y
            return
        elif(x>0 and y<0):
            self.x = x
            self.y = x
            return
        elif(x<0 and y>0):
            self.x = y
            self.y = y
            return

    def calcularArea(self):
        return (self.x*self.y)

class Figura_Complexa(Figura_Geometrica):

    figuras_determinantes = []
    area_total = 0

    def adicionarFigura(self, figura):
        self.figuras_determinantes.append(figura)
    
    def calcularAreaComplexa(self):
        for figura in self.figuras_determinantes:
            self.area_total = self.area_total + figura.calcularArea()
        print("A área resultante é: " + str(self.area_total))

quad1 = Figura_Geometrica(3)
quad2 = Figura_Geometrica(10)

ret1 = Figura_Geometrica(2,7)
ret2 = Figura_Geometrica(5,3)

calculador = Figura_Complexa()

calculador.adicionarFigura(quad1)
calculador.adicionarFigura(quad2)
calculador.adicionarFigura(ret1)
calculador.adicionarFigura(ret2)

calculador.calcularAreaComplexa()