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
        Pega lista de arquivo dentro da pasta indicada no arquivo de configuração
        return List com path dos arquivos
    """
    def get_files(self):
        try:
            dir = Utilidades().getConfiguration().get("arquivos")
            if(os.path.isdir(dir)):  # dir.isDirectory():
                for f in dir.readline:
                    lista.append(f)
                # Arrays.asList(dir.listFiles(new PdfFilter())).forEach(f -> lista.add(f.getPath()))
            else:
                lista.append(dir.name)
                # lista.add(dir.getPath())
        except:
            print(Exception().with_traceback())
    #return lista


print(Utilidades().getConfiguration())