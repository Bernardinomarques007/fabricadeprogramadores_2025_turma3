import sqlite3

try:

    con = sqlite3.connect("banco_de_dados.db")

    cur = con.cursor()

    pesquisa = cur.execute("SELECT * FROM func, sala WHERE sala.id_funcionario = 3 AND func.id_funcionario = 3 ")
    chaves = pesquisa.fetchone()
    print(chaves)

except ConnectionRefusedError as c:
    print("ERRO")