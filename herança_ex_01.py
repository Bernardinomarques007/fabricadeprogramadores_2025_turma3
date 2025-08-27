class Personagem:
    def __init__(self, nome, poder, idade, altura, vilao, local):
        self.nome = nome
        self.poder = poder
        self.idade = idade
        self.altura = altura
        self.vilao = vilao
        self.local = local

    def veiculo(self):
       return print (f" o {self.nome} tem um veiculo")
        
    def poder1(self):
        return print(f"o poder do {self.nome} é {self.poder}")

    def vilao1(self):
        return print(f"o {self.vilao} é o vilão do {self.nome}")

    def local1(self):
        return print(f"o {self.nome} atua principalmente em {self.local}")


batman = Personagem("batman", "ser rico", 25, 1.75, "coringa", "gotham city") 

batman.vilao1()