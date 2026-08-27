def maior_valor(a,b):
    if a>b:
        return a
    elif a==b:
        return "igual"
    else:
        return b
    
n1=float(input('Digite o 1° valor: '))
n2=float(input('Digite o 2° valor: '))

resultado=maior_valor(n1,n2)

print(f'O maior número entre {n1} e {n2} é {resultado}')