nome=input('Digite seu nome: ')
with open('presença.txt','a') as arquivo:
    arquivo.write(f'{nome} - Presente \n')
print("Presença registrada com sucesso!")