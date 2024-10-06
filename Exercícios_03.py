#Faça um programa que receba dois horarios de entrada e mostre o horario de saida:

h1 = int(input("Digite o primeiro horario : "))
m1 = int(input("Digite os minutos do primeiro horario : "))
h2 = int(input("Digite o segundo horario  : "))
m2 = int(input("Digite os minutos do segundo horario : "))
if h1 > 12:
    h1=h1-12
if h2 > 12:
    h2 = h2 - 12
hr = h1+h2
mi = m1+m2
if hr>12:
    hr=hr-12
if mi>=60:
    mi=mi-60
    hr=hr+1
    print(f"{hr}:{mi}")
elif mi <60:
    print(f"{hr}:{mi}")