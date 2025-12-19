from api import API
from banco_de_dados import *
from chrome_manager import *
from classes import *

class Main:
    def __init__(self, conexao):
        self.conexao = conexao

    def main(self):
        config = Configuracoes()
        driver = config.iniciar_webdriver()

        banco = BancoDeDados(driver)

        api = API(driver, conexao)

        api.invoke_dados_livro()

        banco.conexao_banco(driver)

        classes = Classes(driver)

        classes.entrar_site()

        classes.pesquisar_livro()

        classes.extracao()


if __name__ == "__main__":
    main = Main(conexao)


