palavra=str(input("Digite uma palavra: "))
contador_vogais=0
for letra in palavra:
    if letra.lower() in 'aeiouáéíóúãõàèìòùâêôûî':
        contador_vogais=contador_vogais+1

print('O número de vogais na palavra',palavra,'é:',contador_vogais)