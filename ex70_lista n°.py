n1=[44,23,18,20]
print(f"linha 02:{n1}")

#adicionar no final da lista
n1.append(25)
print(f"linha 06:{n1}")

#adicionar na posição desejada e o valor na lista
n1.insert(2,10) # 2 posição, 10 valor
print(f"linha 10:{n1}")

#remover elementos 
n1.remove(44)
n1.remove(20)
print(f"linha 15:{n1}")

#remover a posição na lista
del n1[0]
print(f"linha 19:{n1}")

#imprimir a info que ta na lista, uma embaixo da outra
for i in n1:
    print(f"linha 23:{i}")

    #qntd de elementos na lista
    comprimento=len(n1)
    print(f"Linha 27: {comprimento}")