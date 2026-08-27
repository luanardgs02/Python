import tkinter as tk  # Importa a biblioteca tkinter para criar a interface gráfica
from tkinter import font  # Importa o módulo font do tkinter para personalizar fontes

# Função que será chamada quando o botão for pressionado
def mostrar_mensagem():
    # Cria uma nova janela para exibir a mensagem
    mensagem_janela = tk.Toplevel(janela)  # Cria uma janela secundária (Toplevel) associada à janela principal
    mensagem_janela.title("Mensagem")  # Define o título da janela de mensagem
    mensagem_janela.geometry("300x100")  # Define o tamanho da janela de mensagem (300x100 pixels)

    # Define a mensagem com cor roxa
    mensagem_label = tk.Label(mensagem_janela, text="Olá, Mundo", font=fonte_grande, fg="purple")  # Cria um Label com texto "Olá, Mundo", fonte grande e cor roxa
    mensagem_label.pack(pady=20)  # Adiciona o Label à janela de mensagem com um espaçamento vertical de 20 pixels

# Cria a janela principal
janela = tk.Tk()  # Cria a janela principal da aplicação
janela.title("Interface Simples")  # Define o título da janela principal

# Define o tamanho da janela (largura x altura)
janela.geometry("500x400")  # Define o tamanho da janela principal (500x400 pixels)

# Define uma fonte maior para o botão e a mensagem
fonte_grande = font.Font(size=16)  # Cria uma fonte com tamanho 16

# Cria um botão com tamanho maior e fonte maior
botao = tk.Button(janela, text="Clique aqui", command=mostrar_mensagem, font=fonte_grande, height=2, width=20)  # Cria um botão com texto "Clique aqui", fonte grande, altura 2 e largura 20
botao.pack(pady=50)  # Adiciona o botão à janela principal com um espaçamento vertical de 50 pixels

# Inicia o loop principal da interface gráfica
janela.mainloop()  # Inicia o loop principal da interface gráfica, que fica aguardando interações do usuário