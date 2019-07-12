import os
import _thread
from util import Utilidades


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
