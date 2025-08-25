class AnimaisMárinhos():
    def __init__(self, espécie, cor, tamanho, sexo, anfibio ):
        self.espécie = espécie
        self.cor = cor
        self.tamanho = tamanho
        self.sexo = sexo
        self.anfibio = anfibio


    def anfibio1(self):
        return print(f"esse animal marinho é um {self.espécie}, e ele {self.anfibio} um anfibio")
    
    def alimenticio(self):
        return print(f"esse animal marinho é um {self.espécie}, ele é popular no ramo alimenticio")
    
    def brasileiro(self):
        return print(f"Esse é um {self.espécie} cor de {self.cor}, ele é nativo da fauna brasileira")
    
    def extincao(self):
        return print(f"esse é o {self.espécie}, ele é um animal marinho que mede {self.tamanho}m, está em risco de extinção")

animal1 = AnimaisMárinhos('golfinho', 'cinza', 2.00, 'macho', 'não é')
animal2 = AnimaisMárinhos('Salmão', 'salmão', 0.50, 'macho', 'não é')
animal3 = AnimaisMárinhos('Boto', 'rosa', 1.70, 'macho', 'não é')
animal4 = AnimaisMárinhos('vaquita-marinha', 'cinza', 1.50, 'macho', 'não é')

animal1.anfibio1()
animal2.alimenticio()
animal3.brasileiro()
animal4.extincao()
