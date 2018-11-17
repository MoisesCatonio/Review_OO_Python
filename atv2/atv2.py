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
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone

    @property
    def nome(self):
        return self._nome

    @property
    def endereco(self):
        return self._endereco

    @property
    def telefone(self):
        return self._telefone

    @endereco.setter
    def endereco(self, valor):
        self._endereco = valor
    
    @telefone.setter
    def telefone(self, valor):
        self._telefone = valor

    def impDadosGeral(self):
        self.impDados()
        print(self.nome)
        print(self.endereco)
        print(self.telefone)
        

class P_Fisica(Pessoa):
    
    def __init__(self, cpf, nome, endereco, telefone):
        self._cpf = cpf
        super().__init__(nome, endereco, telefone)

    def impDados(self):
        print(self.cpf)

    @property
    def cpf(self):
        return self._cpf

class P_Juridica(Pessoa):
    
    def __init__(self, cnpj, nome_f, nome, endereco, telefone):
        self._cnpj = cnpj
        self._nome_f = nome
        super().__init__(nome, endereco, telefone)
    
    def impDados(self):
        print(self.cnpj)
    
    @property
    def cnpj(self):
        return self._cnpj

    @property
    def nome_f(self):
        return self._nome_f

    @nome_f.setter
    def nome_f(self, valor):
        self._nome_f = valor


joao = P_Fisica(1100, "Joao", "Rua da Margarida, 17", 999876756)
joao_emp = P_Fisica(11001789472, "Tecflex Tecidos", "Rua da Margarida, 1720", 999876756)
emp = Empresa(joao, joao_emp)

emp.impDadosClientes()