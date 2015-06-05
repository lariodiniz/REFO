# coding: utf-8

from Tkinter import *
import shutil
import tkFileDialog, refocore, tkMessageBox, os

class MontyPython :
    def __init__(self, janela):
        #==========================Configurações============================#
        
        self.janela=janela        
        self.janela.title("REFO- Renomeador de Fotos")

        #========================Botões Suspensos===========================#

        principal=Menu(self.janela)
        principal.add_command(label='Ajuda',command=self.ajuda)
        principal.add_command(label='Quem Somos',command=self.quem)  
        janela.configure(menu=principal)

        #=================Frames da Interface Principal=====================#
        
        caixa=Frame(self.janela,borderwidth=3, relief=GROOVE)
        caixa.pack(fill=X, pady= 5 , padx= 5, side=LEFT)
        baner=Frame(caixa,borderwidth=3, relief=RAISED)
        baner.pack(fill=X, pady= 5 , padx= 5)
        inter=Frame(caixa,borderwidth=3, relief=RAISED)
        inter.pack(fill=X, pady= 5 , padx= 5)
        caixaex=Frame(inter)
        caixaex.grid(row=3, column=2)

        #=================Widgets da Interface Principal===================#
        
        """ logo=PhotoImage(file='img/logo.gif')
        self.logo=Label(baner, image = logo)
        self.logo.image=logo
        self.logo.pack()
        """
        logo=Label(baner, text='Renomeador de Fotos em Massa', font=('Verdana','14','bold')).pack()
        pasta=Label(inter, text='Pasta de Fotos:').grid(row=1, column=1)
        self.pasta=Entry(inter, width=25, state='readonly', readonlybackground ="white")
        self.pasta.grid(row=1, column=2)        
        button_pasta=Button(inter, text="Procurar", command=self.abrir_pasta).grid(row=1, column=3, sticky=W, pady=3, padx=3)
        nome=Label(inter, text='Nome para as Fotos:').grid(row=2, column=1)
        self.nome=Entry(inter, width=25)
        self.nome.insert(0, "Foto")
        self.nome.grid(row=2, column=2)
        extencao=Label(inter, text='Extensão das fotos:').grid(row=3, column=1)        
        self.extencao = StringVar(caixaex)
        self.extencao.set(0)
        for txt, val in (('jpg','0'),('png','1'),('gif','2'),('RAW','3')):
            a=Radiobutton(caixaex,text=txt, value=val,variable=self.extencao).pack(side=LEFT)

        self.varm= IntVar()
        m = Checkbutton(inter, text="Mover fotos repetidas", variable=self.varm).grid(row=4, column=1)

        self.varc= IntVar()
        c = Checkbutton(inter, text="Apagar fotos repetidas", variable=self.varc).grid(row=5, column=1)
        button_renomear=Button(inter, text="Renomear", command=self.renomear).grid(row=6, column=1, sticky=W, pady=3, padx=3)
        button_sair=Button(inter, text="Sair", command=self.sair).grid(row=6, column=3, sticky=E, pady=3, padx=3)

        
        
 #========================Funçoes dos Botões===========================#
        
    def abrir_pasta(self):
        jan=Tk()
        jan.withdraw()
        filename = tkFileDialog.askdirectory(initialdir='.' ,title='Selecione o diretório com Fotos')
        self.pasta["state"]="normal"
        self.pasta.delete(0, END)
        self.pasta.insert(0, filename)
        self.pasta["state"]='readonly'
        
    def renomear(self):             
        
        self.caminho = self.pasta.get()
        extencao=self.extencao.get()
        nome=self.nome.get()
        
        if extencao == "0":
            extencao='jpg'
        elif extencao == "1":
            extencao='png'
        elif extencao == "2":
            extencao='gif'
        elif extencao == "3":
            extencao='RAW'
            
        if self.caminho == '':
            tkMessageBox.showerror("Selecione a Pasta com as fotos", "Selecione a Pasta com as fotos que serão renomeadas")        
        else:
            if self.varm.get() == 1:
                self.moverfotos(refocore.Analise(self.caminho, extencao))
            else:                
                if self.varc.get() == 1:
                    self.result = tkMessageBox.askquestion("Apagar Fotos Repitidas", "As fotos repetidas serão apagadas, Você tem certeza?", icon='question')
                    if self.result == 'yes':
                        self.apagarfotos(refocore.Analise(self.caminho, extencao))

            a=refocore.Renomear(self.caminho, extencao, nome)
            if a == 1:
                tkMessageBox.showinfo("Fotos renomeados", 'Suas Fotos foram renomeadas')
            elif a == 0:
                tkMessageBox.showerror("Fotos não renomeados", 'Suas Fotos não foram renomeadas.\nTente mudar o campo "Nome para as Fotos".')

    def apagarfotos(self, a):
        dic=a        
        for x in dic:
            for y in dic[x]:
                os.remove(self.caminho+'/'+y)
    def moverfotos(self, a):
        dic = a
        if dic != {}:
            os.mkdir(self.caminho+"/"+"Fotos Repitidas")       
        for x in dic:
            for y in dic[x]:
                shutil.move(self.caminho+'/'+y, self.caminho+"/"+"Fotos Repitidas")


        
    
    def sair(self):
        self.janela.destroy()

    def ajuda(self):
        tkMessageBox.showinfo("Ajuda",
                              """1 ° -  Aperte no botão Procurar e selecione a pasta (diretório) onde as fotos estão contidas.

2 ° - De um nome base para as fotos, Ex:
        Se você escolher o nome “FOTO”,
        suas fotos serão renomeadas como; “FOTO1”, FOTO2, “FOTO3”...
      
3° - Escolha a extensão das fotos.

4° - Caso Você queira Mover as Fotos Repitidas marque "Mover fotos repetidas" um diretório será criado dentro do diretorio das fotos.

4° - Caso Você queira apagar as Fotos Repitidas marque "Apagar fotos repetidas"

4° - aperte em Renomear.
""")

    def quem(self):
        tkMessageBox.showinfo("Quem Somos", "REFO foi criado por Lário Diniz e distribuído gratuitamente, seu código é todo em Python e pode ser baixado no https://github.com/lariodiniz/REFO.\n\n Para criticas, sugestões ou reportar erros, enviar email para lariodiniz@gmail.com.")




swallow=Tk()
MontyPython(swallow)
sys.exit(swallow.mainloop())
