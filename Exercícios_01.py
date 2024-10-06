#Faca um programa para receber dois times, e mostre o resultado do jogo.
time1 = input("Digite o primeiro time: ")
time2 = input("Digite o segundo time: ")
gol1 = int(input(f"Digite a quantidade de gols do {time1} : "))
gol2 = int(input(f"Digite a quantidade de gols do {time2}: "))
if gol1 > gol2:
    print(f"{time1} vencedor")
elif gol2 > gol1:
    print(f"{time2} vencedor")
elif gol1==gol2:
    print("Terminou empatado. ")