import json
import random

f = open("words.json", encoding="utf8")

words = json.load(f)
print(list(words.keys()))
choice_c = random.choice(list(words.keys()))

print("Olá, seja bem-vindo!")
print("###########################")

tentativas = 5
ganhou = False


while tentativas > 0 and ganhou is not True:
    print("Dica: " + words[choice_c])
    escolha_user = input("Data: DDMMAAAA\n")
    print('##########################\n')
    
    if len(escolha_user) != 8:
        print('Erro na entrada, a resposta deve conter 8 digitos.')
        continue
    
    if escolha_user.isdigit():
        checagem = []
        pontuacao = 0
        for i in range(8):
            if escolha_user[i] == choice_c[i]:
                checagem.append("V")
                pontuacao = pontuacao + 1
            else:
                checagem.append("X")
        print('Resposta: \n')
        print('|'.join(checagem))
        print('|'.join(escolha_user))
        print('############################\n')        
        
        if pontuacao == 8:
            ganhou= True
    else:
        print("Erro na entrada, a resposta deve ser uma data.")
        continue
    
    tentativas = tentativas-1

if ganhou == True:
    print('VITÓRIAAA!!!')
else:
    print('Derrota :(')
    print('Resposta era: ' + choice_c)
