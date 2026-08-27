def inverter_string(texto):
    return texto[::-1]

nome=input('Digite um nome: ')

inverso=inverter_string(nome)

print(f'A palavra {nome} é: {inverso}')
