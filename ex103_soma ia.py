import tkinter as tk
from tkinter import messagebox

# Função para calcular a soma
def calcular_soma():
    try:
        # Obtém os valores dos campos de entrada
        numero1 = float(entrada_numero1.get())  # Converte o primeiro número para float
        numero2 = float(entrada_numero2.get())  # Converte o segundo número para float
        
        # Calcula a soma
        soma = numero1 + numero2
        
        # Exibe o resultado embaixo dos botões
        resultado_label.config(text=f"Resultado: {soma}", fg="black")  # Atualiza o texto do rótulo de resultado
    except ValueError:
        # Exibe uma mensagem de erro se os valores não forem numéricos
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Função para sair do programa
def sair():
    janela.quit()  # Fecha a janela e encerra o programa

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora de Soma")  # Define o título da janela

# Define o tamanho da janela (largura x altura)
janela.geometry("300x250")

# Rótulo e campo de entrada para o primeiro número
rotulo_numero1 = tk.Label(janela, text="Digite o primeiro número:")  # Rótulo para o primeiro número
rotulo_numero1.pack(pady=5)  # Adiciona o rótulo à janela com espaçamento vertical

entrada_numero1 = tk.Entry(janela)  # Campo de entrada para o primeiro número
entrada_numero1.pack(pady=5)  # Adiciona o campo de entrada à janela com espaçamento vertical

# Rótulo e campo de entrada para o segundo número
rotulo_numero2 = tk.Label(janela, text="Digite o segundo número:")  # Rótulo para o segundo número
rotulo_numero2.pack(pady=5)  # Adiciona o rótulo à janela com espaçamento vertical

entrada_numero2 = tk.Entry(janela)  # Campo de entrada para o segundo número
entrada_numero2.pack(pady=5)  # Adiciona o campo de entrada à janela com espaçamento vertical

# Botão para calcular a soma
botao_calcular = tk.Button(janela, text="Calcular Soma", command=calcular_soma)
botao_calcular.pack(pady=10)  # Adiciona o botão à janela com espaçamento vertical

# Rótulo para exibir o resultado
resultado_label = tk.Label(janela, text="Resultado: ", font=("Arial", 12))
resultado_label.pack(pady=10)  # Adiciona o rótulo de resultado à janela com espaçamento vertical

# Botão para sair
botao_sair = tk.Button(janela, text="Sair", command=sair, bg="red", fg="white")
botao_sair.pack(pady=10)  # Adiciona o botão de sair à janela com espaçamento vertical

# Inicia o loop principal da interface gráfica
janela.mainloop()