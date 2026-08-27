lista=[]

for i in range(1,3):
    numero=int(input(f'Digite o {i}° número: '))
    lista.append(numero)

print(lista)
valor_maximo=max(lista)
valor_minimo=min(lista)
print(f"O valor máximo é: {valor_maximo}")
print(f"O valor minimo é {valor_minimo}")