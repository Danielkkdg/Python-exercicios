def pesquisar(banco):
    meucursor = banco.cursor()
    pesquisa = 'select * from alunos;'
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()
    for x in resultado:
        print(x)




def inserir(banco,meucursor):
    nome1 = input("Digite seu nome: ")
    telefone1 = int(input("Digite seu numero: "))

    sql = "insert into alunos (nome, telefone) VALUES (%s,%s)"
    data = (nome1, telefone1)
    meucursor.execute(sql, data)
    banco.commit()



def linha():
    print("-"*30)