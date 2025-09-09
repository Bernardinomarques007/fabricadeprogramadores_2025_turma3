import sqlite3

try:

    con = sqlite3.connect("banco_de_dados.db")

    cur = con.cursor()    
    
    cur.execute("CREATE TABLE func("+
                "id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "nome TEXT NOT NULL,"+
                "setor TEXT NOT NULL)")
    
    cur.execute("CREATE TABLE sala("+
                "chave INTEGER PRIMARY KEY AUTOINCREMENT,"+
                "local TEXT NOT NULL,"+
                "id_funcionario INTEGER,"+
                "FOREIGN KEY(id_funcionario) REFERENCES func(id_funcionario) )")
    
    cur.execute("INSERT INTO func (nome, setor) VALUES('Ana Lucia','recepção')")
    cur.execute("INSERT INTO func (nome, setor) VALUES('Bruno Ferreira','financeiro')")
    cur.execute("INSERT INTO func (nome, setor) VALUES('Carla Soarez','depósito')")

    cur.execute("INSERT INTO sala (local, id_funcionario) VALUES('Recepção','1')")
    cur.execute("INSERT INTO sala (local, id_funcionario) VALUES('Escritório Financeiro','2')")
    cur.execute("INSERT INTO sala (local, id_funcionario) VALUES('Depósito','3')")

    con.commit()

except ConnectionRefusedError as c:
    print("ERRO")