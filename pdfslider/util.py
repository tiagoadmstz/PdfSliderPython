import os


class Utilidades:

    def get_configuration(self):
        """
        -> Pega as configurações do arquivo
        return: retorna dicionário com valores de configuração
        """
        values = {}
        try:
            path = os.getcwd() + '\\configuration.conf'
            if(not os.path.exists(path)):
                self.gravar_arquivo_configuracao(self.get_initial_configuration())
            for ln in open(path, 'r').readlines():
                itens = ln.split('::')
                values[itens[0]] = itens[1].replace('\n', '')
        except Exception as ex:
            print(ex.__cause__)
        return values

    def get_initial_configuration(self):
        return {
            'icone': 'null',
            'arquivos': 'null',
            'tempoPagina': '00h00m10s',
            'tempoArquivo': '00h01m00s',
            'comprimento': '800',
            'altura': '600',
            'loopArquivo': 'true'
        }

    def gravar_arquivo_configuracao(self, configuracoes):
        try:
            path = os.getcwd() + '\\configuration.conf'
            if(not os.path.exists(path)):
                path = open(path, 'x+', encoding='utf-8')
            for k, v in configuracoes.items():
                try:
                    path.write(k + "::" + v + "\n")
                except Exception as ex:
                    print(ex.__cause__)
            path.close()
        except Exception as ex:
            print(ex.__cause__)
