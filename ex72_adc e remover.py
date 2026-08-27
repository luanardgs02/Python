numeros=[]

for i in range(1,4):
    n1=int(input(f"Digite o {1}° número: "))
    numeros.append(n1)
    
print(numeros)
del numeros[1]
print(numeros)