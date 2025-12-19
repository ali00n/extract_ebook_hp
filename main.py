from api import API
from banco_de_dados import BancoDeDados
from chrome_manager import Configuracoes
from classes import *

class Main:
    def __init__(self, conexao):
        self.conexao = conexao

    def main(self):
        config = Configuracoes()
        driver = config.iniciar_webdriver()

        banco = BancoDeDados()
        banco.conexao_banco()

        api = API(banco.conexao)
        api.invoke_dados_livro()

        classes = Classes(driver)
        classes.entrar_site()
        classes.pesquisar_livro()
        classes.extracao()


if __name__ == "__main__":
    main = Main(None)
    main.main()


