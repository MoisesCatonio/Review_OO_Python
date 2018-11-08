class Veiculo:
    
    def __init__(self, ligado=False):
        self._ligado = ligado

    def isLigado(self):
        print("Verificando valor por método!")
        return self._ligado
    
    def ligar(self):
        self._ligado = True

    def desligar(self):
        self._ligado = False

    ligado = property(isLigado, ligar, desligar)

class Automovel(Veiculo):
    def __init__(self):
        pass

    def ligar(self):
        super().ligar()
        print("Automóvel Ligado!")

    def desligar(self):
        super().desligar()
        print("Automóvel Desligado!")

class Motocicleta(Veiculo):
    def __init__(self):
        pass

    def ligar(self):
        super().ligar()
        print("Motocicleta Ligada!")
    
    def desligar(self):
        super().desligar()
        print("Motocicleta Desligada!")

class Onibus(Veiculo):
    def __init__(self):
        pass
    
    def ligar(self):
        super().ligar()
        print("Ônibus Ligado!")
    
    def desligar(self):
        super().desligar()
        print("Ônibus Desligado!")

a = Automovel()

b = Motocicleta()

c = Onibus()

a.ligar()
b.ligar()
c.ligar()

print(a.ligado)
print(b.ligado)
print(c.ligado)

a.desligar()
b.desligar()
c.desligar()

print(a.ligado)
print(b.ligado)
print(c.ligado)