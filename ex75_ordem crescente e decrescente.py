paises=['Brasil','México','Dinamarca','França','Nova Zelandia']
print(paises)
print('------Ordem Alfábetica------')
paises.sort()
print(paises)

for i in paises:
    print(i)
###########        ##########         ###########
print('------Ordem Decrescente------')
paises.sort(reverse=True)
print(paises)

for i in paises:
    print(i)