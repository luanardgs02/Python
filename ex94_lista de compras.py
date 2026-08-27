compras=[]
while True:
    item=input("Digite um item para adicionar à lista (ou fim para sair): ")
    if item.lower() == 'fim':
        break
    compras.append(item)
with open('lista_compras.txt','w',encoding='utf8') as arquivo:
    for item in compras:
        arquivo.write(f' - {item}\n')
print("Lista de compras salva com sucesso!")