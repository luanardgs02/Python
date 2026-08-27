temp=float(input("Digite o valor da temperatura em graus °C: "))

if temp<0:
    print("Atenção: Gelo!",temp,"graus °C.")
elif temp>30:
    print("Atenção: Quente!",temp,"graus °C.")
else:
    print("Temperatura:",temp,"°C")