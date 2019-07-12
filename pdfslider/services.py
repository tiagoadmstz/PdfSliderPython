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

    """
    -> Pega lista de arquivo dentro da pasta indicada no arquivo de configuração
    return: List com path dos arquivos
    """

    def get_files(self):
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

    '''
     ->Pega o tamanho da tela do usuário e seta nos campos do formulário de configuração
     param: form Form_Configuration
    '''

    def get_default_screen_size(self, form):
        # Dimension d = Toolkit.getDefaultToolkit().getScreenSize()
        # form.getTxtAltura().setText(String.valueOf(d.height))
        # form.getTxtComprimento().setText(String.valueOf(d.width))
        pass

    '''
    ->Pega os dados de configuração do arquivo e mostrar nos campos do formulário.
    param: form Form_Configuration
    '''

    def set_dados(self, form):
        dados = Utilidades().get_configuration()
        # form.getTxtAltura().setText(dados.get("altura"))
        # form.getTxtComprimento().setText(dados.get("comprimento"))
        # form.getTxtIconeSistema().setText(dados.get("icone"))
        # form.getTxtPastaArquivo().setText(dados.get("arquivos"))
        # form.getTxtTempoArquivo().setText(dados.get("tempoArquivo"))
        # form.getTxtTempoPagina().setText(dados.get("tempoPagina"))
        #form.getCkLoopArquivo().setSelected('true' == dados.get("loopArquivo"))

    '''
    Grava os dados do formulário no arquivo de configuração do sistema
    param: form Form_Configuration
    '''

    def gravar_dados(self, form):
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
            Utilidades.gravarArquivoConfiguracao(dados)
        except:
            messagebox.showerror('Error Message', Exception.__cause__)

    '''
    ->Método utilizado pelo botão de confirmar do formulário. Grava os dados do
    formulário no arquivo de configuração, fecha o formulário de configuração
    e abre o formulário de apresentação.

    param: form Form_Configuration
    '''

    def confirmar(self, form):
        if (messagebox.askyesno("Confirmar", "Deseja realmente confirmar?")):
            # gravar_dados(form)
            # Form_Slider slider = new Form_Slider()
            # slider.setVisible(true)
            # form.dispose()
            pass

    '''Cria o arquivo de configuração caso o mesmo não exista'''

    def criar_arquivo_configuracao(self):
        path = os.getcwd + "/configuration.conf"
        if (not os.path.exists(path)):
            Utilidades().gravar_arquivo_configuracao(
                Utilidades().get_initial_configuration())

    '''
    ->Método utilizado pelo botão de selecionar icone no formulário de configuração.
    param: form Form_Configuration
    '''

    def selecionar_icone(self, form):
        try:
            #form.getTxtIconeSistema().setText(Utilidades.selecionadorArquivos(form, "Selecionar ícone", JFileChooser.FILES_ONLY, "jpg", "jpeg", "gif"))
            pass
        except:
            pass

    '''
    Método utilizado pelo botão de selecionar pasta de arquivos no formulário de configuração.
    param: form Form_Configuration
    '''

    def selecionar_pasta_arquivos(self, form):
        try:
            #form.getTxtPastaArquivo().setText(Utilidades.selecionadorArquivos(form, "Selecionar", JFileChooser.FILES_AND_DIRECTORIES, "pdf"))
            pass
        except:
            pass