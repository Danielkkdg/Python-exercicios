usuario=[""]*5
senha=[""]*len(usuario)
tam=len(usuario)
def criação_conta():
    for z in range(tam):
        usuario [z]= input("Crie seu nome para usuario: ")
        senha [z]= input("Crie sua senha: ")
    print("Contas criadas com sucesso...")


def registradas():
    print("contas registradas...")
    for x in range(tam):
        print(f"Login da {x} conta \n"
              f"usuario:{usuario[x]} \n"
              f"senha: {senha[x]}")


def login():
    print("Login: ")
    log = input("Digite seu nome de usuario: ")
    sen = input("Digite sua senha: ")
    for c in range(tam):
        if log == usuario[c] and sen == senha[c]:
            print("Login Sucess...")
















