from herança_ex_01 import Personagem

class Superman1(Personagem):
    def __init__(self, nome, poder, idade, altura, vilao, local, roupa):
        super().__init__(nome, poder, idade, altura, vilao, local)
    
        self.roupa = roupa 

    def Voar(self):
        return print(f"o {self.nome} pode voar")
    

Superman = Superman1("Superman", "multiplos", 25, 1.75, "lex luthor", "metropolis", "Traje especial" ) 

Superman.Voar()

Superman.vilao1()