numero=int(input('Digite um número inteiro positivo: '))
if numero>1:
    primo_eh= True # true pode ser substituido por 1 nesse exercicio
for i in range(2,numero):
    if (numero%i==0):
        primo_eh= False
    break
if (primo_eh== True):
    print('O número',numero,'é primo')
else:
    print("O número",numero,"não é primo")