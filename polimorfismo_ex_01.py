# Para funcionar precisa do arquivo herança_ex_02, e o arquivo herança_ex_01 na mesma pasta

from herança_ex_01 import Personagem
from herança_ex_02 import Superman1

superman = Superman1("Superman", "multiplos", 25, 1.75, "lex luthor", "metropolis", "Traje especial" )
batman = Personagem("batman", "ser rico", 25, 1.75, "coringa", "gotham city")


def teste(teste2):
    print(f" tentando comunicação com {teste2.nome}")
    teste2.vilao1()


print("-"*50)
teste(superman)

print("-"*50)
teste(batman)

__package__ = None  