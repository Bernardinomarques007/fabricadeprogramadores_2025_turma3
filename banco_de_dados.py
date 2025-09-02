import sqlite3


try:
    con = sqlite3.connect("meu_banco.db")

    cur = con.cursor()

# criando as tabelas
    cur.execute("CREATE TABLE cliente(id_cliente, cpf_ou_cnpj, endereco, nome, telefone, id_servico)")

    cur.execute("CREATE TABLE servico(id_servico, pagamento, forma_de_pagamento, data_de_inicio, data_de_conclucao, id_funcionario, endereco_servico, id_cliente )")

    cur.execute("CREATE TABLE funcionario(id_funcionario, cpf, nome, data_de_nasc, data_de_pagamento, telefone, endereco, valor_salarial )")


    cur.execute("INSERT INTO cliente VALUES(1, '555.666.777-88', 'rua esmola: numero 100', 'lazaro','4002-8922', 1)")
    
    cur.execute("INSERT INTO servico VALUES(1, 1, 'pix', '10/02/2025', '10/4/2025', 1, 'rua limoeiro: numero 150', 1)")

    cur.execute("INSERT INTO funcionario VALUES(1, '111.222.333-34', 'lazarinho', '10/03/1999', 'todo dia 15', '1534-0977', 'rua das laranjeiras: numero 1500', '1.600' )")

    con.commit()

except ConnectionRefusedError as c:
    print("Erro de conexão com o banco")
