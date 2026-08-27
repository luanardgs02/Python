# ler o arquivo inteiro de uma vez
with open('base_dados.csv','r') as arquivo:
    conteudo=arquivo.read()
    print(conteudo)

# ler arquivo linha por linha
with open('base_dados.csv','r') as arquivo:
   for conteudo in arquivo:
    print(conteudo)
