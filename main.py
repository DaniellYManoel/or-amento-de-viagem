# fazer o gráfico 
from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox

from PIL import Image, ImageTk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


co0 = "#0d141c" #"#232b2b" preta
co1 = "#d1d6d5" # siza
co2 = "#4fa882" # verde
co3 = "#38576b" # valor
co4 = "#403d3d" #letra
co5 = "#e06636" # - profit
co6 = "#038cfc" # azul
co7 = "#3fbfb9" # verde
co8 = "#263238" # + verde
co9 = "#b9bdc6"     #"#e9edf5"  + verde
co10 = "#6e8faf" #
co11 = "#f2f4f2" # siza escuro
co12 = "#feffff" #branco


colors = ['#5588bb', '#66bbbb', '#99bb55', '#ee9944', '#444466', '#bb5555']

# criando janela -----------------------------------------------------------

janela = Tk ()
janela.title ("")
janela.geometry('820x610')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)# false pq nã opodemos alterar o tamanho da janela
style = ttk.Style(janela)

# Frames -----------------------------------------------------------
frameCima = Frame(janela, width=1043, height=50, bg=co1)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=290, bg=co1, padx=10)
frameMeio.grid(row=1, column=0)

frame_esquerda = Frame(frameMeio, width=250, height=290,bg=co9, pady=0,relief="raised") #janela do meio no canto esquedo
frame_esquerda.place(x=0, y=5)

frame_direita = Frame(frameMeio, width=630, height=290,bg=co1, pady=0, relief="raised")
frame_direita.place(x=250, y=5)

frameBaixo = Frame(janela,width=820, height=300, bg=co1)
frameBaixo.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)


# Logo -------------------------------------------------------------------------------------------------

app_ = Label(frameCima, text=" Orçamento de viagem", compound=LEFT, padx=5, anchor=NW, font=('Verdana 20'), bg=co1,fg=co4)
app_.place(x=0, y=0)

#abrindo imagem 
app_img =Image.open('avioes.png')
app_img = app_img.resize((45, 45))# tamanho da imagem
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=900, compound=LEFT, padx=5, anchor=NW, bg= co1, fg=co4)
app_logo.place(x=320, y=0)

# frame esquedo
def Totais():
    l_nome = Label(frame_esquerda, text="Meu orçamento e despesas", width=31, anchor=NW, font=('Verdana 11 '), bg=co3, fg=co12)
    l_nome.place(x=0, y=0)

 # orçamento total-------------------------
    l_total_orcamento = Label(frame_esquerda, text='Orçamento total', anchor=E, font=(' Verdana 10'), bg=co9, fg=co0)
    l_total_orcamento.place(x=10, y=50)

    valor_total = 10000
    l_orcamento = Label(frame_esquerda, text='R${:,.2f}'.format(valor_total), width=20, anchor=NW, font=(' Verdana 12'), bg=co1, fg=co4)
    l_orcamento.place(x=10, y=80)

     # despesas total-------------------------
    l_total_despesas = Label(frame_esquerda, text='Despesas totais', anchor=E, font=(' Verdana 10'), bg=co9, fg=co0)
    l_total_despesas.place(x=10, y=120)

    valor_despesas = 10000

    l_despesas = Label(frame_esquerda, text='R${:,.2f}'.format(valor_despesas), width=20, anchor=NW, font=(' Verdana 12'), bg=co1, fg=co4)
    l_despesas.place(x=10, y=150)

     # Restante total-------------------------
    l_total_restante = Label(frame_esquerda, text='Total Restante', anchor=E, font=(' Verdana 10'), bg=co9, fg=co0)
    l_total_restante.place(x=10, y=190)

    valor_retante = 10000

    l_restante = Label(frame_esquerda, text='R${:,.2f}'.format(valor_retante), width=20, anchor=NW, font=(' Verdana 12'), bg=co1, fg=co4)
    l_restante.place(x=10, y=220)

#Grafico -----------------------------------------
def grafico():

    # Faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(7, 4), dpi=87)
    ax = figura.add_subplot(111)

    lista_valores = [56,78,45,92]
    lista_categorias = ['Alimentação', 'Transporte','Acomodação','Entreterimento']

    # Only "explode" the 2nd slice (i.e 'Hogs')
    explode = []
    for i in lista_categorias:
        explode.append(0.05)
    
    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2),autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)
    ax.legend(lista_categorias, loc="upper right", bbox_to_anchor=(1.55,0.50)) # o loc="center rightt" está dando erro 'loc' são pré-definidos e não incluem 'center rightt'.

    # Frame para pie
    frame_meio_pie = Frame(frame_direita, width=600,height=290,bg=co11, pady=0, relief="raised")
    frame_meio_pie.place(x=-140, y=-25)
    l_nome = Label(frame_direita, text="Para onde estão indo minhas despesas totais?", width=60, height=1, anchor=CENTER,pady=2,font=('Verdana 11'), bg=co10, fg=co12)
    l_nome.place(x=0,y=0)

    canva_categoria =FigureCanvasTkAgg(figura, frame_meio_pie)
    canva_categoria.get_tk_widget().grid(row=0,column=0,padx=0)


# ------------------ criando frames para tabelas -----------------------
l_nome = Label(frameBaixo, text="Quais são as suas depesas", width=87, anchor=NW, padx=6, font=('Verdana 11'), bg=co10, fg=co12)#fg e a cor da letra
l_nome.grid(row=0,column=0, columnspan=6, pady=0)

frame_tabela = Frame(frameBaixo, width=300, height=250, bg=co1)
frame_tabela.grid(row=1,column=0,pady=0)

frame_operacoes = Frame(frameBaixo, width=220, height=250, bg=co1)
frame_operacoes.grid(row=1, column=1, padx=5)

frame_configuracao = Frame(frameBaixo, width=220, height=250, bg= co1)
frame_configuracao.grid(row=1, column=2, padx=5)


#Função para mostra_renda
def mostra_renda():

    # creating a treeview with dual scrollbars
    tabela_head = ['id','Tipo', 'Descrição','Total']

    lista_itens = [['1','ddd','dddddd','122'],['2','ddd','dddddd','122']]

    global tree

    tree = ttk.Treeview(frame_tabela, selectmode="extended",columns=tabela_head,show="headings")
    # Vertical scrollbar
    vsb =ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1,row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd=["nw","nw","center","e","e"]
    h=[20,90,120,80,70]
    n=0

    for col in tabela_head:
        tree.heading(col,text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])

        n+=1

    for item in lista_itens:
        tree.insert('','end', values=item)


mostra_renda()

# Configuracoes Despesas
l_info = Label(frame_operacoes, text="Insira novas despesas", anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
l_info.place(x=10, y=10)

l_categoria = Label(frame_operacoes, text="Categoria", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_categoria.place(x=10, y=40)

#Definindo categorias
categorias =['Transporte','Arrendamento','Alimentacao','Enterterimento','Outros']
combo_categoria_despesas = ttk.Combobox(frame_operacoes, width=12,font=('Ivy 10'))
combo_categoria_despesas['values'] = (categorias)
combo_categoria_despesas.place(x=80, y=41)

l_descricao = Label(frame_operacoes, text="Descrição", anchor=NW,font=('Ivy 10 '), bg=co1,fg=co4)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frame_operacoes, width=16,justify='left', relief="solid")
e_descricao.place(x=80,y=71)

l_valor_quantia= Label(frame_operacoes, text="Quantia",anchor=NW, font=('IVy 10 '), bg=co1, fg=co4)
l_valor_quantia.place(x=10, y=120)
e_valor_despesa = Entry(frame_operacoes, width=16, justify='left',relief="solid")
e_valor_despesa.place(x=80, y=121)


# Botão Inserir
img_add_despesas = Image.open('mais.png')
img_add_despesas = img_add_despesas.resize((17,17))
img_add_despesas = ImageTk.PhotoImage(img_add_despesas)
botao_inserir_despesas = Button(frame_operacoes, image= img_add_despesas, compound=LEFT, anchor=NW, text=" Adicionar".upper(), width=94, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1,fg=co0)
botao_inserir_despesas.place(x=80,y=151)


# Configurações Quantia Total --------------------------------
l_descricao = Label(frame_configuracao, text="Atualizar Quantia Total", anchor=NW, font=('Verdana 10 bold'), bg=co1,fg=co4)
l_descricao.place(x=10,y=10)

l_valor_quantia = Label(frame_configuracao, text="Quantia Total",anchor=NW, font=('Ivy 10 '),bg=co1, fg=co4)
l_valor_quantia.place(x=10,y=40)
e_valor_quantia = Entry(frame_configuracao, width=14, justify='left',relief="solid")
e_valor_quantia.place(x=110,y=41)

# Botao Atualizar
img_atualizar_quantia = Image.open('atualizar.png')
img_atualizar_quantia = img_atualizar_quantia.resize((17,17))
img_atualizar_quantia = ImageTk.PhotoImage(img_atualizar_quantia)
botao_inserir_quantia = Button(frame_configuracao, image=img_atualizar_quantia, compound=LEFT, anchor=NW, text=" Atualizar".upper(), width=80, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
botao_inserir_quantia.place(x=110, y=70)

#Operacao Excluir
l_exucluir = Label(frame_configuracao, text="Excluir ação", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_descricao.place(x=10, y=120)

# Botao Deletar
img_delete=Image.open('excluir.png')
img_delete = img_delete.resize((20,20))
img_delete = ImageTk.PhotoImage(img_delete)
botao_deletar = Button(frame_configuracao, image=img_delete, compound=LEFT,anchor=NW, text="  Deletar".upper(), width=80, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1,fg=co0)
botao_deletar.place(x=110, y=120)



grafico()
Totais()


style.theme_use("clam")
style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 9)) 




janela.mainloop()