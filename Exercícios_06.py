#Faça um programa que o usario crie uma senha e tente logar
#O usario tem 3 tentativas para acerta a senha
#Caso erre tem que mostrar o "Usuario bloqueado"
x = 1
codigo = int(input("Crie sua senha: "))
while x < 4:
    senha = int(input("Digite sua senha: "))
    if codigo == senha:
        print("Correto")
        x = x+4
    else:
        print("Incorreto ")
        x = x+1
if senha == codigo:
    print("Login Successful")
elif senha != codigo:
    print("Usuario bloqueado")