import os
import _thread
from util import Utilidades
from tkinter import messagebox


class ServiceSlider:

    def __init__(self):
        # varíavel que controla o loop de arquivo
        self.stop = False
        self.pause = False
        self.paginas = []
        self.sistemas = {}

    def get_files(self):
        """
        -> Pega lista de arquivo dentro da pasta indicada no arquivo de configuração
        return: List com path dos arquivos
        """
        lista = []
        try:
            path = Utilidades().getConfiguration().get("arquivos")
            if(os.path.isdir(path)):
                for f in os.listdir(path):
                    lista.append(f)
            else:
                lista.append(path)
        except:
            print(Exception().with_traceback())
        return lista


class ServiceConfiguration:

    def __init__(self):
        pass

    def get_default_screen_size(self, form):
        '''
        ->Pega o tamanho da tela do usuário e seta nos campos do formulário de configuração
        param: form Form_Configuration
        '''
        # Dimension d = Toolkit.getDefaultToolkit().getScreenSize()
        # form.getTxtAltura().setText(String.valueOf(d.height))
        # form.getTxtComprimento().setText(String.valueOf(d.width))
        pass

    def set_dados(self, form):
        '''
        ->Pega os dados de configuração do arquivo e mostrar nos campos do formulário.
        param: form Form_Configuration
        '''
        dados = Utilidades().get_configuration()
        # form.getTxtAltura().setText(dados.get("altura"))
        # form.getTxtComprimento().setText(dados.get("comprimento"))
        # form.getTxtIconeSistema().setText(dados.get("icone"))
        # form.getTxtPastaArquivo().setText(dados.get("arquivos"))
        # form.getTxtTempoArquivo().setText(dados.get("tempoArquivo"))
        # form.getTxtTempoPagina().setText(dados.get("tempoPagina"))
        # form.getCkLoopArquivo().setSelected('true' == dados.get("loopArquivo"))

    def gravar_dados(self, form):
        '''
        Grava os dados do formulário no arquivo de configuração do sistema
        param: form Form_Configuration
        '''
        dados = {
            'altura': 'form.getTxtAltura().getText()',
            'comprimento': 'form.getTxtComprimento().getText()',
            'icone': 'form.getTxtIconeSistema().getText()',
            'arquivos': 'form.getTxtPastaArquivo().getText()',
            'tempoArquivo': 'form.getTxtTempoArquivo().getText()',
            'tempoPagina': 'form.getTxtTempoPagina().getText()',
            'loopArquivo': 'String.valueOf(form.getCkLoopArquivo().isSelected())'
        }
        try:
            Utilidades().gravar_arquivo_configuracao(dados)
        except:
            messagebox.showerror('Error Message', Exception.__cause__)

    def confirmar(self, form):
        '''
        ->Método utilizado pelo botão de confirmar do formulário. Grava os dados do
        formulário no arquivo de configuração, fecha o formulário de configuração
        e abre o formulário de apresentação.

        param: form Form_Configuration
        '''
        if (messagebox.askyesno("Confirmar", "Deseja realmente confirmar?")):
            # gravar_dados(form)
            # Form_Slider slider = new Form_Slider()
            # slider.setVisible(true)
            # form.dispose()
            pass

    def criar_arquivo_configuracao(self):
        '''Cria o arquivo de configuração caso o mesmo não exista'''
        path = os.getcwd + "/configuration.conf"
        if (not os.path.exists(path)):
            Utilidades().gravar_arquivo_configuracao(
                Utilidades().get_initial_configuration())

    def selecionar_icone(self, form):
        '''
        ->Método utilizado pelo botão de selecionar icone no formulário de configuração.
        param: form Form_Configuration
        '''
        try:
            # form.getTxtIconeSistema().setText(Utilidades.selecionadorArquivos(form, "Selecionar ícone", JFileChooser.FILES_ONLY, "jpg", "jpeg", "gif"))
            pass
        except:
            pass

    def selecionar_pasta_arquivos(self, form):
        '''
        Método utilizado pelo botão de selecionar pasta de arquivos no formulário de configuração.
        param: form Form_Configuration
        '''
        try:
            # form.getTxtPastaArquivo().setText(Utilidades.selecionadorArquivos(form, "Selecionar", JFileChooser.FILES_AND_DIRECTORIES, "pdf"))
            pass
        except:
            pass
