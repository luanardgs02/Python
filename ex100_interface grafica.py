import tkinter as tk
from tkinter import messagebox

# Função que será chamada quando o botão for pressionado
def mostrar_mensagem():
    # Obtém o nome, a idade e o gênero dos campos de entrada
    nome = campo_nome.get()  # Pega o texto digitado no campo do nome
    idade = campo_idade.get()  # Pega o texto digitado no campo da idade
    genero = genero_selecionado.get()  # Obtém o gênero selecionado

    # Verifica se os campos foram preenchidos
    if nome and idade and genero:  # Se todos os campos não estiverem vazios
        mensagem = f"Olá, {nome}, você tem {idade} anos de idade."
        
        # Cria uma nova janela para exibir a mensagem
        mensagem_janela = tk.Toplevel(janela)
        mensagem_janela.title("Mensagem")
        mensagem_janela.geometry("300x100")

        # Define a cor do texto com base no gênero selecionado
        if genero == "Feminino":
            cor = "pink"  # Cor rosa para feminino
        else:
            cor = "blue"  # Cor azul para masculino

        # Exibe a mensagem na nova janela com a cor correspondente
        mensagem_label = tk.Label(mensagem_janela, text=mensagem, font=("Arial", 12), fg=cor)
        mensagem_label.pack(pady=20)
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")  # Exibe um aviso se algum campo estiver vazio

# Cria a janela principal
janela = tk.Tk()
janela.title("Formulário com Gênero")  # Define o título da janela

# Define o tamanho da janela (largura x altura)
janela.geometry("400x250")

# Usa o gerenciador de layout grid para posicionar os elementos
rotulo_nome = tk.Label(janela, text="Nome:")  # Rótulo para o campo do nome
rotulo_nome.grid(row=0, column=0, padx=10, pady=5, sticky="w")  # Posiciona o rótulo na linha 0, coluna 0, alinhado à esquerda

campo_nome = tk.Entry(janela)  # Campo de entrada para o nome
campo_nome.grid(row=0, column=1, padx=10, pady=5, sticky="ew")  # Posiciona o campo na linha 0, coluna 1

rotulo_idade = tk.Label(janela, text="Idade:")  # Rótulo para o campo da idade
rotulo_idade.grid(row=1, column=0, padx=10, pady=5, sticky="w")  # Posiciona o rótulo na linha 1, coluna 0, alinhado à esquerda

campo_idade = tk.Entry(janela)  # Campo de entrada para a idade
campo_idade.grid(row=1, column=1, padx=10, pady=5, sticky="ew")  # Posiciona o campo na linha 1, coluna 1

rotulo_genero = tk.Label(janela, text="Gênero:")  # Rótulo para o campo do gênero
rotulo_genero.grid(row=2, column=0, padx=10, pady=5, sticky="w")  # Posiciona o rótulo na linha 2, coluna 0, alinhado à esquerda

# Cria uma variável para armazenar o gênero selecionado
genero_selecionado = tk.StringVar(janela)

# Cria RadioButtons para selecionar o gênero
radio_feminino = tk.Radiobutton(janela, text="Feminino", variable=genero_selecionado, value="Feminino")
radio_feminino.grid(row=2, column=1, padx=10, pady=5, sticky="w")  # Posiciona o RadioButton para feminino na linha 2, coluna 1

radio_masculino = tk.Radiobutton(janela, text="Masculino", variable=genero_selecionado, value="Masculino")
radio_masculino.grid(row=3, column=1, padx=10, pady=5, sticky="w")  # Posiciona o RadioButton para masculino na linha 3, coluna 1

# Cria um botão para exibir a mensagem e o posiciona à direita
botao = tk.Button(janela, text="Enviar", command=mostrar_mensagem)
botao.grid(row=4, column=1, padx=10, pady=20, sticky="e")  # Posiciona o botão na linha 4, coluna 1, alinhado à direita

# Configura a coluna 1 para expandir e ocupar o espaço disponível
janela.columnconfigure(1, weight=1)

# Inicia o loop principal da interface gráfica
janela.mainloop()