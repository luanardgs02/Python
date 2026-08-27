palavra=str(input("Digite uma palavra: "))
palavra=palavra.replace(' ','').lower()
palavra=palavra.replace('-','').lower()
palavra=palavra.replace(',','').lower()
conta_inv=''
for letra in palavra:
    #conta=letra
    conta_inv=letra+conta_inv
if conta_inv.lower()==palavra.lower():
        print('A palavra',palavra, 'é um palidromo!')
else:
        print('A palavra',palavra,'não é um palidromo!')