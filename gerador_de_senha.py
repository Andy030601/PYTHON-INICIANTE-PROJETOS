import random
import string

def senhas_aleatoria(len_pass = 8):
    letra = string.ascii_letters
    numeros = string.digits
    pontuacao = string.punctuation
    
    opcao = letra + numeros + pontuacao
    
    senha = ""
    
    for i in range(0, len_pass):
        digitos = random.choice(opcao)
        senha = senha + digitos
        
    return senha

escolha_senha = input('Quantos digitos você quer na sua senha? ')

if escolha_senha.isdigit():
    escolha_senha = int(escolha_senha)
else:
    print('Entrada Inválida.')
    quit()
    
geracao_senha = senhas_aleatoria(len_pass = escolha_senha)
print(f'Senha Gerada automaticamente:\n{geracao_senha}')
