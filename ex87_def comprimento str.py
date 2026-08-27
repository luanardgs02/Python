def comprimento_string(texto):
    return len (texto)

nome=input('Digite um nome: ')

tamanho=comprimento_string(nome)

print(f'O comprimento de {nome} é: {tamanho}')