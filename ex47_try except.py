while True:
    idade=input("Digite a idade ou sair (encerrar o programa.)")

    if idade.lower()== "sair":
        break

    try:
        idade=int(idade)
        if idade>=18:
            print('Maior de idade')
        else:
            print("Menor de idade")
    except ValueError:
        print("Valor inválido!")