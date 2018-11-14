class Empresa():

    Clientela = []

    def __init__(self, *clientes):
        for elem in clientes:
            self.Clientela.append(elem)
    
    def impDadosClientes(self):
        for cliente in self.Clientela:
            cliente.impDadosGeral()
class Pessoa():
    
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def impDadosGeral(self):
        self.impDados()
        print(self.nome)
        print(self.endereco)
        print(self.telefone)
        

class P_Fisica(Pessoa):
    
    def __init__(self, cpf, nome, endereco, telefone):
        self.cpf = cpf
        super().__init__(nome, endereco, telefone)

    def impDados(self):
        print(self.cpf)

class P_Juridica(Pessoa):
    
    def __init__(self, cnpj, nome, endereco, telefone):
        self.cnpj = cnpj
        super().__init__(nome, endereco, telefone)
    
    def impDados(self):
        print(self.cnpj)

joao = P_Fisica(1100, "Joao", "Rua da Margarida, 17", 999876756)
joao_emp = P_Fisica(11001789472, "Tecflex Tecidos", "Rua da Margarida, 1720", 999876756)
emp = Empresa(joao, joao_emp)

emp.impDadosClientes()