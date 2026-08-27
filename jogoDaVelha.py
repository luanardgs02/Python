import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Velha")
        self.jogada = True  # True para 'X', False para 'O'
        self.tabuleiro = [" " for _ in range(9)]  # Cria uma lista para o tabuleiro
        self.botoes = []

        # Criação dos botões
        for i in range(9):
            botao = tk.Button(master, text=" ", font=("Arial", 24), width=5, height=2,
                              command=lambda i=i: self.fazer_jogada(i))
            botao.grid(row=i // 3, column=i % 3)
            self.botoes.append(botao)

    def fazer_jogada(self, i):
        if self.tabuleiro[i] == " ":
            self.tabuleiro[i] = 'O' if self.jogada else 'X'
            self.botoes[i].config(text=self.tabuleiro[i])
            if self.verificar_vitoria():
                messagebox.showinfo("Fim de Jogo", f"{'X' if not self.jogada else 'O'} ganhou!")
                self.reiniciar_jogo()
            elif " " not in self.tabuleiro:
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.reiniciar_jogo()
            else:
                self.jogada = not self.jogada

    def verificar_vitoria(self):
        combinacoes_vencedoras = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Linhas
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Colunas
            (0, 4, 8), (2, 4, 6)              # Diagonais
        ]
        for a, b, c in combinacoes_vencedoras:
            if self.tabuleiro[a] == self.tabuleiro[b] == self.tabuleiro[c] != " ":
                return True
        return False

    def reiniciar_jogo(self):
        for i in range(9):
            self.tabuleiro[i] = " "
            self.botoes[i].config(text=" ")
        self.jogada = True

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaVelha(root)
    root.mainloop()