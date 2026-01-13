from api import API
from banco_de_dados import BancoDeDados
from chrome_manager import Configuracoes
from classes import *

class Main:
    def __init__(self, conexao):
        self.conexao = conexao

    def main(self, var=None):

        config = Configuracoes(var)
        driver = config.iniciar_webdriver()


        banco = BancoDeDados(var)
        banco.conexao_banco()

        api = API(banco.conexao)
        nomes = api.invoke_dados_livro()  # obtém nomes de livros do banco

        classes = Classes(driver)
        # popula nomes vindos do banco (se houver)
        classes.atribuir_variaveis(nomes)

        classes.entrar_site()
        classes.pesquisar_livro()
        classes.extracao()



if __name__ == "__main__":
    main = Main(None)
    main.main()
