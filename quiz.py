print("===BEM-VINDO AO QUIZ DO ANDY===")
answer_user= input("QUER COMEÇAR S/N: ")
print(answer_user)

if answer_user != 'S':
    quit()
    
score = 0

print('COMEÇANDO...')
print('Quem inventou a lâmpada?\n (A) Thomas Edison\n (B) Marie Curie\n (C) Edson Arantes\n (D) Albert Einstein\n')
answer_1 = input('Resposta: ')

if answer_1 == 'A':
    print('Parbéns, você acertou!')
    score = score + 1
else:
    print('Uhm, essa não é a resposta correta! O invertor da lâmpada foi Thomas Edison.')

print('Em que ano ocorreu o ataque às Torres Gêmeas?\n (A) 1991\n (B) 2001\n (C) 2011\n (D) 2021\n')
answer_2 = input('Resposta: ')

if answer_2 == 'B':
    print('Parabéns, você acertou!')
    score = score + 1
else: 
    print('Uhm, essa não é a resposta correta! O ataque às Torres Gêmeas occoreu no dia 11 de Setembro de 2001.')
    
print('Qual o menor Estado do Brasil?\n (A) Acre\n (B) Santa Catarina\n (C) Alagoas\n (D) Sergipe\n')
answer_3 = input('Resposta: ')

if answer_3 == 'D':
    print('Parabéns, você acertou!')
    score = score + 1
else:
    print('Uhm, essa não é a resposta correta! O menor Estado do Brasil é o Estado de Sergipe, que fica localizado na região Nordeste.')
    
print(f'O quiz acabou, sua pontuação foi: {score} XP')
