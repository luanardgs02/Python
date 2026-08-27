def numeros_pares(limite):
    pares=[]
    for numero in range(0,limite+1,2):
        pares.append(numero)
    return pares

def numeros_impares(limite):
    impares=[]
    for numero in range(1,limite+1,2):
        impares.append(numero)
    return impares
while True:
    try:
        numero=int(input('Digite um número inteiro positivo: '))
        if numero<0:
            print("Digite novamente.")
            continue
        break
    except ValueError:
        print("Entrada inválida! Tente novamente.")

if numero%2==0:
    resultado=numeros_pares(numero)
    print(f'Números pares até {numero}: {resultado}')
else:
    resultado=numeros_impares(numero)
    print(f'Números impares até {numero}: {resultado}')