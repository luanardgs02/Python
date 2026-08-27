agenda={}

while True:
    nome=input("Digite o nome do contato (ou 'fim' para sair): ")
    if nome.lower == "fim":
        break

    telefone=input('Digite o telefone de contato: ')

    agenda[nome]=telefone
    print(agenda)

    with open('agenda.txt','w',encoding="utf8") as arquivo:
        for nome,telefone in agenda.items():
            arquivo.write(f'{nome}: {telefone}\n')
    print('Agenda salva com sucesso!')