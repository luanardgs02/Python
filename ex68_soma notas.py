quantidade=0
soma=0

for i in range(1,6):
    nota=float(input(f'Digite a {i} °nota: '))

    while nota<0 or nota>10:
       nota=float(input(f'Nota incorreta!\n Digite a {i} °nota: '))

if nota>6.9:
        soma+=nota
else:
    quantidade=quantidade+1

print(f"A soma das notas acima de 6.9 é: {soma}")
print(f"A quantidade das notas abaixo de 6.9 é: {quantidade}")