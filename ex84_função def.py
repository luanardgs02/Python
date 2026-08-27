#função simples que imprime saudação
def saudacao():
    print('Hello World!')
#chamando a função
saudacao()

#############

#função com parametro
def saudacao_personalizada(nome):
    print(f'Olá,{nome}')

saudacao_personalizada('Alice')
saudacao_personalizada('José')

#################################
#função que retorna um valor
def soma(a,b):
    resultado=a+b
    return resultado

resultado_soma=soma(3,5)
print(f'A soma é {resultado_soma}')

#########################################

#função com argumentos padrão
def saudacao_completa(nome,sobrenome='Silva'):
    print(f'Olá,{nome} {sobrenome}!')

saudacao_completa('João')
saudacao_completa('Maria',"Eduarda")