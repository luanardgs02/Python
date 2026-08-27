#lista vazia
minha_lista=[]
print(f'linha 03: {minha_lista}')

# lista com valores iniciais
frutas=['maçã','banana','laranja']
print(f'linha 07: {frutas}')

#elementos da lista por indice(posição)
print(f'linha 10: {frutas[0]}')
print(f'linha 11: {frutas[1]}')

# adicionar elementos a lista
frutas.append('uva')
print(f'linha 15: {frutas}')

#remover itens da lista
frutas.remove('banana')
print(f'linha 19: {frutas}')

# qntd de itens da lista
tamanho=len(frutas)
print(f'linha 23: {tamanho}')

# iterando sobre os elementos da lista com loop for
for fruta in frutas:
    print(f'linha 27: {fruta}')

    # verificação de um item da lista
if "maçã" in frutas:
    print(f'linha 31: A maçã está na lista')
else:
    print(f'linha 33: A maçã não está na lista')

    #copiando uma lista
    copia_frutas=frutas.copy()
    print(f'linha 37: {copia_frutas}')
    print(f'linha 38: {frutas}')

    #concatenando as listas (unir)
    outras_frutas=['pêssego','morango']
    todas_as_frutas=frutas+outras_frutas
    print(f'linha 43: {todas_as_frutas}')
