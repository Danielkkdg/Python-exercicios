#Faça um programa para receber dois tipos de combustiveis, "G"  para Gasolinar
#"E" para Etanol, e informe quantos custou os litros desejados pelo usario.


comb = input("Digite o tipo de combustivel: ")
litros = float(input("Digite quantos  litros deseja: "))
if comb == "Gasolina" or comb == "g" or comb == "G":
   r = litros *5.70
   print(f"vc abasteceu {litros} L de Gasolina e custou R$ {r}" )
elif comb == "Etanol" or comb == "e" or comb == "E":
   r1= litros * 4.80
   print(f"vc abasteceu {litros} L de Etanol e custou R$ {r1}" )
else:
   print("invalido")