import mysql.connector , att1

from att1 import linha, pesquisar, inserir

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="turmab"
)
while True:
    linha()
    print("Menu: ")
    linha()
    x= int(input("Digite 1 para Pesquisar: \n"
                 "Digite 2 para Inserir: \n"
                 "Digite 3 para Sair: "))

    meucursor = banco.cursor()
    pesquisa = 'select * from alunos;'
    meucursor.execute(pesquisa)
    resultado = meucursor.fetchall()

    linha()
    if x == 1:
        pesquisar(banco)

    elif x ==2:
        inserir(banco,meucursor)

    else:
        meucursor.close()
        banco.close()
        print("Finalizado...")
        break





