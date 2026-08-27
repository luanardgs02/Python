import tkinter as tk

# Função para calcular a média e exibir o resultado
def calcular_media():
    try:
        # Obtém as notas dos campos de entrada
        nota1 = float(entrada_nota1.get())  # Converte a primeira nota para float
        nota2 = float(entrada_nota2.get())  # Converte a segunda nota para float
        nota3 = float(entrada_nota3.get())  # Converte a terceira nota para float

        # Verifica se as notas estão no intervalo de 0 a 10
        if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10:
            # Calcula a média
            media = (nota1 + nota2 + nota3) / 3

            # Verifica se o aluno foi aprovado ou reprovado
            if media >= 6:
                resultado_label.config(text=f"Média: {media:.2f}\nAluno APROVADO", fg="green")  # Exibe em verde
            else:
                resultado_label.config(text=f"Média: {media:.2f}\nAluno REPROVADO", fg="red")  # Exibe em vermelho
        else:
            # Exibe uma mensagem de erro se as notas estiverem fora do intervalo
            resultado_label.config(text="Por favor, insira notas entre 0 e 10.", fg="black")
    except ValueError:
        # Exibe uma mensagem de erro se os valores não forem numéricos
        resultado_label.config(text="Por favor, insira valores numéricos válidos.", fg="black")

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora de Média")  # Define o título da janela

# Define o tamanho da janela (largura x altura)
janela.geometry("400x280")

# Rótulo e campo de entrada para a primeira nota
rotulo_nota1 = tk.Label(janela, text="Digite a primeira nota (0 a 10):")  # Rótulo para a primeira nota
rotulo_nota1.pack(pady=5)  # Adiciona o rótulo à janela com espaçamento vertical

entrada_nota1 = tk.Entry(janela)  # Campo de entrada para a primeira nota
entrada_nota1.pack(pady=5)  # Adiciona o campo de entrada à janela com espaçamento vertical

# Rótulo e campo de entrada para a segunda nota
rotulo_nota2 = tk.Label(janela, text="Digite a segunda nota (0 a 10):")  # Rótulo para a segunda nota
rotulo_nota2.pack(pady=5)  # Adiciona o rótulo à janela com espaçamento vertical

entrada_nota2 = tk.Entry(janela)  # Campo de entrada para a segunda nota
entrada_nota2.pack(pady=5)  # Adiciona o campo de entrada à janela com espaçamento vertical

# Rótulo e campo de entrada para a terceira nota
rotulo_nota3 = tk.Label(janela, text="Digite a terceira nota (0 a 10):")  # Rótulo para a terceira nota
rotulo_nota3.pack(pady=5)  # Adiciona o rótulo à janela com espaçamento vertical

entrada_nota3 = tk.Entry(janela)  # Campo de entrada para a terceira nota
entrada_nota3.pack(pady=5)  # Adiciona o campo de entrada à janela com espaçamento vertical

# Botão para calcular a média
botao_calcular = tk.Button(janela, text="Calcular Média", command=calcular_media)
botao_calcular.pack(pady=10)  # Adiciona o botão à janela com espaçamento vertical

# Rótulo para exibir o resultado
resultado_label = tk.Label(janela, text="", font=("Arial", 12))
resultado_label.pack(pady=10)  # Adiciona o rótulo de resultado à janela com espaçamento vertical

# Inicia o loop principal da interface gráfica
janela.mainloop()