n1=float(input("Digite o valor da 1° nota: "))
n2=float(input("Digite o valor da 2° nota: "))
n3=float(input("Digite o valor da 3° nota: "))

media=(n1+n2+n3)/3

media_arredonda= round(media,2)
print("A média final das notas foi de",media_arredonda)

if media>=7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")