import sqlite3


try:
    con = sqlite3.connect("meu_banco.db")

    cur = con.cursor()

    res = cur.execute("SELECT * FROM cliente")
    cliente = res.fetchone()

    print(cliente)

    cur.close

except ConnectionRefusedError as c:
    print("ERRO")
