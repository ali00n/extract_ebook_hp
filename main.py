from banco_de_dados import *
from chrome_manager import *
from classes import *


if __name__ == "__main__":
 config = Configuracoes()
 driver = config.iniciar_webdriver()

 banco = BancoDeDados
 banco.conexao_banco(driver)

 classes = Classes(driver)

 classes.entrar_site()

 classes.pesquisar_livro()

 classes.extracao()

