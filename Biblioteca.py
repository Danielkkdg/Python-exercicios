usuario=[""]*5
senha=[""]*len(usuario)
tam=len(usuario)


def linha():
    print("-"*30)


def criação_conta():
    for z in range(tam):
        usuario [z]= input("Crie seu nome para usuario: ")
        senha [z]= input("Crie sua senha: ")
        linha()
    print("Contas criadas com sucesso...")


def registradas():
    print("contas registradas...")
    linha()
    for x in range(tam):
        print(f"Conta {x+1}:  \n"
              f"usuario:{usuario[x]} \n"
              f"senha: {senha[x]}")
        linha()


def login():
    print("Login: ")
    linha()
    b=0
    log = input("Digite seu nome de usuario: ")
    sen = input("Digite sua senha: ")
    linha()
    if log in usuario and sen in senha:
        print("Login Sucess...")
        linha()
    else:
        while True:
            print("Usuario ou Senha, Invalido...")
            linha()
            log = input("Digite seu nome de usuario: ")
            sen = input("Digite sua senha: ")
            linha()
            if  log in usuario and sen in senha:
                print("Login Sucess...")
                linha()
                break
            b+=1
            if b==3:
                print("Usuario Bloqueado...")
                linha()
                break