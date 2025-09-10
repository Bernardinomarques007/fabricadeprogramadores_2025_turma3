import sqlite3

try:

    con = sqlite3.connect("banco_de_dados.db")

    cur = con.cursor()  


    print("| BANCO_DE_DADOS.db ")
    print("| SEJA BEM VINDO ")
    print("| escolha em qual tabela você quer inserir, por favor, escolha o numero da tabela")
    print("| 1 - FUNCIONÁRIOS")
    print("| 2 - SALA ou ESCRITORIO")


    funcao = int(input("- "))

    if funcao == 1:

        try:

            con = sqlite3.connect("banco_de_dados.db")

            cur = con.cursor() 

            funcionario = input("Insira o nome do funcionario: ")

            setor = input("Insira o setor desse funcionário: ")

            cur.execute("INSERT INTO func (nome, setor) VALUES(?,?)", (funcionario, setor) )

            con.commit()

            print("FUNCIONARIO REGISTRADO COM SUCESSO")

        except:
            print("ERRO AO TENTAR INSERIR O FUNCIONARIO")

    elif funcao == 2:
        
        try:
            con = sqlite3.connect("banco_de_dados.db")

            cur = con.cursor() 

            local = input("Insira o nome do escritorio ou sala: ")

            id_funcionario = input("Insira o id registrado do funcionário responsável pela chave do local: ")
    
            cur.execute("INSERT INTO sala (local, id_funcionario) VALUES(?,?)", (local, id_funcionario))

            con.commit()

            print("SALA/ESCRITORIO INSERIDO COM SUCESSO")

        except:

            print("ERRO AO INSERIR A SALA")



except ConnectionRefusedError as c:
    print("erro")