from tkinter import *


class Frame_Configuration:

    def __init__(self):
        pass

    def init_components(self):
        #construção do frame principal
        root = Tk()
        frame = Frame(root)
        frame.pack()
        #implementação dos botões
        btCancelar = Button(frame)
        btConfirmar = Button(frame)
        btDefault = Button(frame)
        btRestore = Button(frame)
        btSelecionarIcone = Button(frame)
        btSelecionarPasta = Button(frame)
        #implementação dos combobox
        ckLoopArquivo = Listbox(frame)
        #MenuItem itemFechar
        #implementação dos Labels
        jLabel1 = Label(frame)
        jLabel2 = Label(frame)
        jLabel3 = Label(frame)
        tempo_pagina = Label(frame)
        jLabel5 = Label(frame)
        jLabel6 = Label(frame)
        #Menu menuArquivo
        #MenuBar menuBar
        #Panel painelArquivos
        #Panel painelExibicao
        #Panel painelMain
        #Panel painelTempo
        #Separator separador1
        #Separator separador2
        txtAltura = Text(frame)
        txtComprimento = Text(frame)
        txtIconeSistema = Text(frame)
        txtPastaArquivo = Text(frame)
        txtTempoArquivo = Text(frame)
        txtTempoPagina = Text(frame)
        root.mainloop()


class Frame_Slides:

    def __init__(self):
        pass


Frame_Configuration().init_components()