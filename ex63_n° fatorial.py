numero=int(input("Digite um número inteiro não negativo: "))
if numero<0:
    print("Erro! O fatorial não é definido para números negativos")
else:
    fatorial=1
    for i in range (1,numero+1):
        fatorial=fatorial*i
    print("O fatorial de",numero,'é',fatorial)