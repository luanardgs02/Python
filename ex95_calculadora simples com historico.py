def calcular(num1,num2,operador):
    if operador=='+':
        return num1+num2
    elif operador=='-':
        return num1-num2
    elif operador=='*':
        return num1*num2
    elif operador=='/':
        return num1/num2
    else:
        return "Operador inválido"

num1=float(input("Digite o 1° valor: "))
num2=float(input("Digite o 2° valor: "))
operador=input('Digite o operador (+,-,*,/): ')
resultado=calcular(num1,num2,operador)
with open('historico_calculo.txt','a') as arquivo:
    arquivo.write(f'{num1} {operador} {num2} = {resultado}\n')
print('Resultado:',resultado)