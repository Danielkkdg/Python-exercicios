#Faça um código para ler 5 nomes de usuários e
#suas respectivas senhas, e armazenar cada
#lista em um array diferente, após completar a
#digitação, imprimir , nome, senha e posição
#dos dados no array
#Altere o sistema anterior e faça um sistema
#de login, pedindo a senha do usuário e
#mostrando seu nome e a mensagem, login
#efetuado com sucesso.
import Biblioteca
import Biblioteca
from Biblioteca import criação_conta,registradas,login

o=0
while o!=2:
    print("Menu inicial...")
    criação_conta()
    r = int(input("Se deseja ver o registro das contas criadas digite 1: \n"
              "se deseja logar digite 2: "))
    if r == 1:
        registradas()
        p=int(input("Se deseja logar digite 1: \n"
                "se deseja encerrar digite 2: "))
        if p==1:
            r=2
        else:
            o=2
    if r==2:
        login()
    o=int(input("Se deseja refazer os cadastro digite 1: \n"
            "se deseja encerrar digite 2: "))
print("Finalizado...")
