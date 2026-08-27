def media(lista):
    return sum(lista)/len(lista)

numeros=[]
for i in range(6):
    numero=float(input(f'Digite o {i+1}° número: '))
    numeros.append(numero)

resultado=media(numeros)

print(f'A média dos números {numeros} é: {resultado}')
