import random
print('===JOGO DE ADIVINHAÇÃO===')
escolha_numero = input('Escolha o número teto do desafio: ')

if escolha_numero.isdigit(): #função que verifica se todos os textos da string são caracteres númericos.
   escolha_numero = int(escolha_numero)
else:
    print('Erro, informe um número!')
    quit()#encerra a função do script

random_number = random.randint(0, escolha_numero)

while True:
    resposta_usuario = input('Adivinhe o número: ')
    
    if resposta_usuario.isdigit():
        resposta_usuario  = int(resposta_usuario)
    else:
        print('Erro. Informe um número')
        continue #enquanto o usuário não digitar um número o codigo continuará rodando.
        
    if resposta_usuario == random_number:
        print('PARABÉNS, VOCÊ ACERTOU!!')
        break
    elif resposta_usuario > random_number:
        print('O número digitado é maior do que o número sorteado.')
    else:
        print('O número digitado é menor do que o número sorteado.')
        
