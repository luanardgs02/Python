lista=[]
while True:
    print("\nMenu de lista:")
    print('Opção 1: Adicionar')
    print('Opção 2: Remover')
    print('Opção 3: Tamanho')
    print('Opção 4: Inserir na posição')
    print('Opção 5: Remover a posição')
    print('Opção 6: Mostrar o maior valor')
    print('Opção 7: Mostrar o menor valor')
    print('Opção 8: Colocar em ordem Crescente')
    print('Opção 9: Colocar em ordem Decrescente')
    print('Opção 10: Mostrar a lista na Horizontal')
    print('Opção 11: Mostrar a lista na Vertical')
    print('Opção 12: Sair')

opcao=int(input('Escolha uma opção: '))


    #adicionar
if opcao==1:
    item=input('Digite o valor a ser adicionado: ')
    lista.append(item)
    print(f'Item {item} adicionado com sucesso!')

    #remover
elif opcao==2:
    item=input('Digite o item a ser removido: ')
    if item in lista:
        lista.remove(item)
        print(f'Item {item} removido com sucesso!')
    else:
        print(f'Item {item} não encontrado!')

    #tamanho
elif opcao==3:
    print('O tamanho da lista é:',len(lista))

    #inserir na posição
elif opcao==4:
    posicao=int(input('Digite a posição para inserir: '))
    item=input('Digite o item a ser adicionado: ')
    if posicao>=0 and posicao<=len(lista): #0 <= posicao <= len(lista):
        lista.insert(posicao,item)
    else:
        print('Posição inválida!')

    #remover na posição
elif opcao==5:
    posicao=int(input('Digite a posição para remover: '))
    if posicao>=0 and posicao<=len(lista): #0 <= posicao <= len(lista):
        lista.pop(posicao)
    else:
        print('Posição inválida!')

    #valor máximo
elif opcao==6:
    if lista:
        print('O maior valor da lista é:',max(lista))
    else:
        print('A lista está vazia!')

    #valor minimo
elif opcao==7:
    if lista:
        print('O menor valor da lista é:',min(lista))
    else:
        print('A lista está vazia!')

    #ordem crescente
elif opcao==8:
    lista_copia=lista.copy()
    lista_copia.sort()
    print('Lista ordenada em ordem crescente:',lista_copia)

    #ordem decrescente
elif opcao==9:
    lista_copia=lista.copy()
    lista_copia.sort(reverse=True)
    print('Lista ordenada em ordem decrescente:',lista_copia)

    #lista na horizontal
elif opcao==10:
    print('A lista atual é:',lista)

    #lista na vertical
elif opcao==11:
    for i in lista:
        print(i)

#sair
elif opcao==12:
    print('Saindo...')
    #break

else:
    print('Opção inválida! Tente novamente.')
