numero=int(input("Digite um número: "))

if (numero%2)==0:
    print("O número",numero,'é par')
    print("O número de pares até",numero,':')
    for i in range(1,numero+1,2):
        print(i)

else:
    print("O número",numero,"é impar")
    print("O número de impares até",numero,':')
    for i in range(1,numero+1,2):
        print(i)

