import time

escolha_tempo = input('Escolha a duração para o temporizador em segundos: ')
#verificar se o usuario informou números através do isdigit()

if escolha_tempo.isdigit():
    escolha_tempo = int(escolha_tempo)
else:
    print('Inválido.')
    quit()

while escolha_tempo:
    minutos, segundos = divmod(escolha_tempo, 60)
    tempo = '{:02d}:{:02d}'.format(minutos, segundos)
    print(tempo, end="\r") #usar barra invertida +n ou barra invertida + r (testar as duas possibilidades).
    time.sleep(1)
    escolha_tempo = escolha_tempo - 1

print('FIM!!')
