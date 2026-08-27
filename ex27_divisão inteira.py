n1=int(input('Digite o 1° valor inteiro e positivo: '))
n2=int(input('Digite o 2° valor inteiro e positivo: '))

#verificação
if n1<=0 or n2<=0:
    print('Por favor, digite apenas números positivos')
else:
    resultado=n1//n2
    print('O resultado da divisão inteira de',n1,'por',n2,'é:',resultado)