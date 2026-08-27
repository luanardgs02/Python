import tkinter as tk
from tkinter import messagebox

# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit():
    try:
        celsius = float(entrada_temperatura.get())  # Obtém a temperatura digitada
        fahrenheit = (celsius * 9/5) + 32  # Fórmula de conversão
        messagebox.showinfo("Resultado", f"{celsius}°C é igual a {fahrenheit:.2f}°F")  # Exibe o resultado
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")  # Exibe erro se o valor não for numérico

# Função para converter Fahrenheit para Celsius
def fahrenheit_para_celsius():
    try:
        fahrenheit = float(entrada_temperatura.get())  # Obtém a temperatura digitada
        celsius = (fahrenheit - 32) * 5/9  # Fórmula de conversão
        messagebox.showinfo("Resultado", f"{fahrenheit}°F é igual a {celsius:.2f}°C")  # Exibe o resultado
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")  # Exibe erro se o valor não for numérico

# Cria a janela principal
janela = tk.Tk()
janela.title("Conversor de Temperatura")  # Define o título da janela

# Define o tamanho da janela (largura x altura)
janela.geometry("300x150")

# Rótulo e campo de entrada para a temperatura
rotulo_temperatura = tk.Label(janela, text="Digite a temperatura:")  # Rótulo para o campo de entrada
rotulo_temperatura.pack(pady=10)  # Adiciona o rótulo à janela com espaçamento vertical

entrada_temperatura = tk.Entry(janela)  # Campo de entrada para a temperatura
entrada_temperatura.pack(pady=5)  # Adiciona o campo de entrada à janela com espaçamento vertical

# Botões para escolher a conversão
botao_celsius_fahrenheit = tk.Button(janela, text="Celsius para Fahrenheit", command=celsius_para_fahrenheit)
botao_celsius_fahrenheit.pack(pady=5)  # Adiciona o botão à janela com espaçamento vertical

botao_fahrenheit_celsius = tk.Button(janela, text="Fahrenheit para Celsius", command=fahrenheit_para_celsius)
botao_fahrenheit_celsius.pack(pady=5)  # Adiciona o botão à janela com espaçamento vertical

# Inicia o loop principal da interface gráfica
janela.mainloop()