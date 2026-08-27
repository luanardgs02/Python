
n1=int(input("Digite nota 1: "))
while n1<0 or n1>10:
    n1=int(input("Digite nota 1: "))
n2=int(input("Digite nota 2: "))
while n2<0 or n2>10:
    n2=int(input("Digite nota 2: "))
n3=int(input("Digite nota 3: "))
while n3<0 or n3>10:
    n3=int(input("Digite nota 3: "))

media=(n1+n2+n3)/3

op=int(input("Informe a opção desejada: \n1. Verificar a média \n2. Verificar situação \n"))
while op!=1 and op!=2:
    print("Opção inválida. Tente novamente!")
    op=int(input("Informe a opção desejada: \n1. Verificar a média \n2. Verificar situação \n"))

    if op==1:
        print("Média é: ",media)
    else:
        if media>=7:
             print("Aluno aprovado. Média: ",media)
        elif media<3:
            print("Aluno reprovado. Média: ",media)
        else:
            op2=int(input("Você está de recuperação: Deseja inserir a nota? \n1)SIM \n2)NÃO \n"))
        while op2!=1 and op2!=2:
            print("Opção inválida. Tente novamente!")
            op2=int(input("Você está de recuperação: Deseja inserir a nota? \n1)SIM \n2)NÃO \n"))

        if op2==1:
            nota=int(input("Digite a nota de recuperação: "))
            if nota>=5:
             print("Aluno aprovado.")
            else:
             print("Aluno reprovado.")
        else:
             print ("Fim do programa.")