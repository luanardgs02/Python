soma=0.0
quantidade=0
for i in range(1,6):
    peso=float(input(f'Digite o {i} ° peso: '))
    if peso>=55.2:
        soma=soma+peso
        quantidade=quantidade+1
print("A soma de {quantidade} de pesos acima ou igual a 55,2kg é: {soma} kg")