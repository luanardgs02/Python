nome=input('Digite o seu nome: ')
print(nome)

with open('base_dados.csv','a') as arquivo:
    arquivo.write(f'Seja bem-vindo(a){nome}.\n')