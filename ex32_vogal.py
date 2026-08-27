#letra=input tbm funciona
letter=str(input("Digite uma letra: "))
#if letter=="a" or letter=="e"...: opção mais longa
# lower- minuscula; upper- maiuscula;
if letter.lower() in 'aeiouáéíóúãõàèìòùâêôû':
    print('A letra',letter, 'é uma vogal.')
else:
     print("A letra digitada",letter, "não é uma vogal.")