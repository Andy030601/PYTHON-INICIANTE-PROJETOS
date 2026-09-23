import random

pontos_usuario = 0
pontos_computador = 0

options = ['r', 'p', 't']
#toda lista começa com número 0 (regra do apartamento) //  All list go with number zero

while True:
    escolha_usuario = input('Escolha R(ROCHA), P(PAPEL), T(TESOURA) ou S para Sair:  ').lower()
    #lower() é uma funçaõ que transformar os caracteres em minúsculo //it is a function that converts characters to lowercase
    if escolha_usuario == 's':
        break
    
    if escolha_usuario not in options:
        continue    
    
    computador = random.randint(0, 2)
    # aqui, o computador fará a sua escolha // here, the computer do the your choice.
    escolha_computador = options[computador] 
    
    print('O computador escolheu' + escolha_computador)
    
    if escolha_usuario == escolha_computador:
        print('EMPATE')
    elif escolha_usuario == 'r' and escolha_computador == 't':
        print('Você ganho a rodada!')
        pontos_usuario = pontos_usuario + 1
    elif escolha_usuario == 'p' and escolha_computador == 'r':
        print('Você ganhou a rodada!') 
        pontos_usuario = pontos_usuario + 1
    elif escolha_usuario == 't' and escolha_computador == 'p':
        print('Você ganhou a rodada!')
        pontos_usuario = pontos_usuario + 1
    else:
        print('O computador ganhou a rodada!')
        pontos_computador = pontos_computador + 1
        
print('Sua pontuação: ' + str(pontos_usuario))
print('Pontuação do computador: ' + str(pontos_computador))

if pontos_computador > pontos_usuario:
    print('DERROTA:(')
elif pontos_computador == pontos_usuario:
    print('Empate.')
else:
    print('VITÓRIAAA!!')
