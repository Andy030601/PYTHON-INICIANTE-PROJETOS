import customtkinter as ctk 
#______________INICIO DA FUNÇÃO_______________________
def media_notas():
    n1 = float(nota1.get())
    n2 = float(nota2.get())
    n3 = float(nota3.get())

    media = (n1 + n2 + n3)/3
    executar.configure(text = f'A média das notas é de  {media:.1f} pontos.')
    
#________________STATUS________________________________   
#    if media >= 7:
#        status = 'Aprovado'
#    elif media >= 5:
#        status ='Recuperação'
#    else:
#        status = 'Reprovado'

#     return media, status

ctk.set_appearance_mode('dark')

#______________INICIO DA JANELA_______________________

janela = ctk.CTk()
janela.geometry("600x450")
janela.title('Sitema Escolar')
janela.iconbitmap('escola.ico')
janela.resizable(False, False)

#______________COMPONENTES DA JANELA_______________________
#TITULO - SUBTITULO - 3 ENTRY P/ NOTAS - 1 BOTÃO

titulo = ctk.CTkLabel(janela,
                      text= 'Sistema Escolar de Notas',
                      text_color='yellow',
                      font= ('Arial', 20),
                      )
subtitulo = ctk.CTkLabel(janela,
                         text= 'Bem-vindo(a) ao sistema de notas escolar!',
                         text_color= 'orange',
                         font= ('Arial', 15)
                         )
executar = ctk.CTkLabel(janela,
                        text = ''
                        )


titulo.pack(pady=20)
subtitulo.pack()

nota1 = ctk.CTkEntry(janela,
                     width= 200,
                     height= 50,
                     border_color= 'grey',
                     placeholder_text= 'Nota da 1° Unidade:'
                     )
nota2 = ctk.CTkEntry(janela,
                     width= 200,
                     height= 50,
                     border_color= 'grey',
                     placeholder_text= 'Nota da 2° Unidade:'
                     )
nota3 = ctk.CTkEntry(janela,
                     width= 200,
                     height= 50,
                     border_color= 'grey',
                     placeholder_text= 'Nota da 3° Unidade:'
                     )


nota1.pack(pady=20)
nota2.pack()
nota3.pack(pady=20)

botao = ctk.CTkButton(janela,
                      width= 200,
                      height= 35,
                      text= 'Calcular Média',
                      font= ('Arial', 20),
                      text_color= 'black',
                      hover_color= 'orange',
                      cursor = 'hand2',
                      fg_color='yellow',
                      command= media_notas
                      )


botao.pack(pady=10)
executar.pack()
janela.mainloop()
