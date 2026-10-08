import customtkinter as ctk 





ctk.set_appearance_mode('white')

#_____________INICIO DA JANELA__________

janela = ctk.CTk()
janela.geometry('600x400')
janela.title('Divisão amigável')
#janela.iconbitmap('') encontrar imagem para calculadora de descontos e gorjetas
janela.resizable(False, False)

#___________COMPONENETES DA JANELA______

titulo = ctk.CTkLabel(janela,
                      text='Calculadora de Gorjetas e Divisão de Contas',
                      text_color= 'black',
                      font= ('Arial', 20)
                      )
subtitulo = ctk.CTkLabel(janela,
                         text='Informe o valor total do gasto e a quantidade de participantes para dividir a conta:',
                         text_color="#554803",
                         font=('Arial', 15)
                         )
#______________ENTRADAS___________

gasto_total = ctk.CTkEntry(janela,
                           width=250,
                           height=40,
                           border_color='black',
                           placeholder_text='Gasto Total',
                           )
participantes = ctk.CTkEntry(janela,
                             width=250,
                             height=40,
                             border_color='black',
                             placeholder_text='Total de participantes')



titulo.pack(pady=10)
subtitulo.pack(pady = 5)
gasto_total.pack(pady= 10)
participantes.pack()

botao_calculo = ctk.CTkButton(janela,
                              width= 200,
                              height= 35,
                              text= 'Calcular',
                              font= ('Arial', 20),
                              text_color= 'black',
                              hover_color= 'orange',
                              cursor = 'hand2',
                              fg_color='yellow',
                              #command=
                              )


botao_calculo.pack(pady= 10)




janela.mainloop()
