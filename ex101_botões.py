import tkinter as tk
from tkinter import messagebox

# Funções para exibir as mensagens de saudação
def bom_dia():
    messagebox.showinfo("Saudação", "Bom dia!")  # Exibe a mensagem "Bom dia!"

def boa_tarde():
    messagebox.showinfo("Saudação", "Boa Tarde!")  # Exibe a mensagem "Boa Tarde!"

def boa_noite():
    messagebox.showinfo("Saudação", "Boa noite!")  # Exibe a mensagem "Boa noite!"

# Cria a janela principal
janela = tk.Tk()
janela.title("Saudações")  # Define o título da janela

# Define o tamanho da janela (largura x altura)
janela.geometry("400x150")

# Adiciona a mensagem 1 acima dos botões
mensagem = tk.Label(janela, text="Clique em um dos botões para receber uma saudação.", font=("Arial", 12))
mensagem.pack(pady=10)  # Adiciona a mensagem à janela com espaçamento vertical

# Cria um frame para organizar os botões lado a lado
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)  # Adiciona o frame à janela com espaçamento vertical

# Botão "Bom dia!"
botao_bom_dia = tk.Button(frame_botoes, text="Bom dia", command=bom_dia)
botao_bom_dia.pack(side="left", padx=20)  # Adiciona o botão ao frame, alinhado à esquerda

# Botão "Boa Tarde!"
botao_boa_tarde = tk.Button(frame_botoes, text="Boa Tarde", command=boa_tarde)
botao_boa_tarde.pack(side="left", padx=20)  # Adiciona o botão ao frame, alinhado à esquerda

# Botão "Boa noite!"
botao_boa_noite = tk.Button(frame_botoes, text="Boa noite", command=boa_noite)
botao_boa_noite.pack(side="left", padx=20)  # Adiciona o botão ao frame, alinhado à esquerda

# Inicia o loop principal da interface gráfica
janela.mainloop()