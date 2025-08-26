class pessoa():
    def __init__(self, idade, raca, cabelo, altura, sexo, casado, endereco, telefone, CPF, empregado ):
        self.__telefone = telefone
        self.__cpf = CPF
        self.idade = idade
        self.raca = raca
        self.cabelo = cabelo 
        self.altura = altura
        self.sexo = sexo
        self._casado = casado
        self.__endereco = endereco
        self.empregado = empregado

        @property

        