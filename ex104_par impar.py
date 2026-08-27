import tkinter as tk

# Função para verificar se o número é par ou ímpar
def verificar_par_impar():
    try:
        # Obtém o valor do campo de entrada
        numero = int(entrada_numero.get())  # Converte o valor para inteiro
        
        # Verifica se o número é par ou ímpar
        if numero % 2 == 0:  # Se o resto da divisão por 2 for 0, é par
            resultado_label.config(text=f"O número {numero} é PAR.", fg="blue")  # Exibe em azul
        else:  # Caso contrário, é ímpar
            resultado_label.config(text=f"O número {numero} é ÍMPAR.", fg="red")  # Exibe em vermelho
    except ValueError:
        # Exibe uma mensagem de erro se o valor não for numérico
        resultado_label.config(text="Por favor, insira um número válido.", fg="black")

# Cria a janela principal
janela = tk.Tk()
janela.title("Verificador de Par ou Ímpar")  # Define o título da janela

# Define o tamanho da janela (largura x altura)
janela.geometry("300x150")

# Rótulo e campo de entrada para o número
rotulo_numero = tk.Label(janela, text="Digite um número inteiro:")  # Rótulo para o campo de entrada
rotulo_numero.pack(pady=5)  # Adiciona o rótulo à janela com espaçamento vertical

entrada_numero = tk.Entry(janela)  # Campo de entrada para o número
entrada_numero.pack(pady=5)  # Adiciona o campo de entrada à janela com espaçamento vertical

# Botão para verificar se o número é par ou ímpar
botao_verificar = tk.Button(janela, text="Verificar", command=verificar_par_impar)
botao_verificar.pack(pady=10)  # Adiciona o botão à janela com espaçamento vertical

# Rótulo para exibir o resultado
resultado_label = tk.Label(janela, text="", font=("Arial", 12))
resultado_label.pack(pady=10)  # Adiciona o rótulo de resultado à janela com espaçamento vertical

# Inicia o loop principal da interface gráfica
janela.mainloop()