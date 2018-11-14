class Viajante():

    def __init__(self):
        pass

    def testarNacionalidade(self):
        self.dizerOla()

    def dizerOla(self):
        pass

class Brasileiro(Viajante):
    def __init__(self):
        pass

    def dizerOla(self):
        print("Fala meu parça!")

class Espanhol(Viajante):
    def __init__(self):
        pass

    def dizerOla(self):
        print("Hola amigo!")

class Americano(Viajante):
    def __init__(self):
        pass

    def dizerOla(self):
        print("Hi there!")


a = Brasileiro()
b = Espanhol()
c = Americano()

a.testarNacionalidade()
b.testarNacionalidade()
c.testarNacionalidade()