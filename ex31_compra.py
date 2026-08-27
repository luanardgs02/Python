# compras com ou sem 10% de desconto
valor_compra=float(input("Digite o valor total da compra: "))
num_itens=int(input("Digite o número de itens: "))

if num_itens>5:
    desconto=valor_compra*0.1
    valor_final=valor_compra-desconto
    print('O valor do desconto é:',desconto)
    print("O valor final da sua compra com desconto é",valor_final)
else:
    valor_final=valor_compra
    print('O valor total da sua compra é',valor_compra)
    # valor_arredonda = round(valor_final,2)
    #print("O valor da compra será de:", valor_arredonda)