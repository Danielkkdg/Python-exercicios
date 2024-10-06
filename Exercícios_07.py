#Faça um código para ler 5 nomes de usuários e
#suas respectivas senhas, e armazenar cada
#lista em um array diferente, após completar a
#digitação, imprimir , nome, senha e posição
#dos dados no array
#Altere o sistema anterior e faça um sistema
#de login, pedindo a senha do usuário e
#mostrando seu nome e a mensagem, login
#efetuado com sucesso.
dados =  []
temp = []
for x in range(0,3):
    temp.append(input("Crie um nome de usuario: "))
    temp.append(input("Crie uma senha: "))
    dados.append(temp[:])
    temp.clear()
print("Cadastros criado com sucesso...\n"
      "estar e a lista dos cadastrados:\n"
      f"{dados}")
temp.append(input("Digite seu nome de usuario: "))
temp.append(input("Digite sua senha: "))
if len (dados):
    if temp in dados:
        print("Login Efetuado com sucesso...")
    else:
        print("Senha ou Usuario, incorreto...")
