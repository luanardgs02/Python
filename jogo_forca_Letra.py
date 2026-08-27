import random
import tkinter as tk
from tkinter import messagebox
 
class HangmanApp:
    def __init__(self, master):
        self.master = master
        master.title("Jogo da Forca")

        self.word_list = ["python", "javascript", "programacao", "computador", "teclado", "mouse"]
        self.word = ""
        self.hidden_word = []
        self.guesses_left = 6
        self.guessed_letters = []

        self.word_label = tk.Label(master, text="Palavra:")
        self.word_label.grid(row=0, column=0)

        self.word_entry = tk.Entry(master)
        self.word_entry.grid(row=0, column=1)

        self.hide_button = tk.Button(master, text="Ocultar", command=self.hide_word)
        self.hide_button.grid(row=0, column=2)

        self.hidden_word_label = tk.Label(master, text="", font=("Arial", 24))
        self.hidden_word_label.grid(row=1, column=0, columnspan=3)

        self.guess_label = tk.Label(master, text="Adivinhar letra:")
        self.guess_label.grid(row=2, column=0)

        self.guess_entry = tk.Entry(master)
        self.guess_entry.grid(row=2, column=1)

        self.guess_button = tk.Button(master, text="Adivinhar", command=self.guess_letter)
        self.guess_button.grid(row=2, column=2)

        self.guesses_left_label = tk.Label(master, text=f"Tentativas restantes: {self.guesses_left}")
        self.guesses_left_label.grid(row=3, column=0, columnspan=3)

        self.guessed_letters_label = tk.Label(master, text="Letras adivinhadas:")
        self.guessed_letters_label.grid(row=4, column=0, columnspan=3)

        self.hangman_canvas = tk.Canvas(master, width=200, height=200)
        self.hangman_canvas.grid(row=5, column=0, columnspan=3)

        self.body_parts = []

    def hide_word(self):
        self.word = self.word_entry.get().lower()
        self.word_entry.delete(0, tk.END)

        if not self.word:
            self.word = random.choice(self.word_list)

        self.hidden_word = ["_"] * len(self.word)
        self.update_hidden_word_label()
        self.guesses_left = 6
        self.guessed_letters = []
        self.update_guesses_left_label()
        self.update_guessed_letters_label()
        self.clear_hangman()
        self.guess_button.config(state="normal")

    def guess_letter(self):
        letter = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if len(letter) != 1 or not letter.isalpha():
            return

        if letter in self.guessed_letters:
            return

        self.guessed_letters.append(letter)
        self.update_guessed_letters_label()

        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.hidden_word[i] = letter
            self.update_hidden_word_label()
        else:
            self.guesses_left -= 1
            self.update_guesses_left_label()
            self.draw_hangman()

        if self.guesses_left == 0:
            self.game_over("Você perdeu!")
        elif "_" not in self.hidden_word:
            self.game_over("Você venceu!")

    def update_hidden_word_label(self):
        self.hidden_word_label.config(text=" ".join(self.hidden_word))

    def update_guesses_left_label(self):
        self.guesses_left_label.config(text=f"Tentativas restantes: {self.guesses_left}")

    def update_guessed_letters_label(self):
        self.guessed_letters_label.config(text=f"Letras adivinhadas: {', '.join(self.guessed_letters)}")

    def draw_hangman(self):
        if self.guesses_left < 6:
            head = self.hangman_canvas.create_oval(80, 20, 120, 60)
            self.body_parts.append(head)
        if self.guesses_left < 5:
            body = self.hangman_canvas.create_line(100, 60, 100, 120)
            self.body_parts.append(body)
        if self.guesses_left < 4:
            left_arm = self.hangman_canvas.create_line(100, 70, 60, 100)
            self.body_parts.append(left_arm)
        if self.guesses_left < 3:
            right_arm = self.hangman_canvas.create_line(100, 70, 140, 100)
            self.body_parts.append(right_arm)
        if self.guesses_left < 2:
            left_leg = self.hangman_canvas.create_line(100, 120, 60, 160)
            self.body_parts.append(left_leg)
        if self.guesses_left < 1:
            right_leg = self.hangman_canvas.create_line(100, 120, 140, 160)
            self.body_parts.append(right_leg)

    def clear_hangman(self):
        for part in self.body_parts:
            self.hangman_canvas.delete(part)
        self.body_parts = []

    def game_over(self, message):
        self.guess_button.config(state="disabled")
        messagebox.showinfo("Game Over", f"{message}\nA palavra era: {self.word}")

root = tk.Tk()
app = HangmanApp(root)
root.mainloop()