import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Classes:
    def __init__(self, driver):
        self.nome_livros = ''
        self.driver = driver
        self.preco_livro = 0
        self.index = 0
        self.titulo_do_livro = ''
        self.tipo_do_livro = ''
        self.tipo_livro_um = ''

    def find_element_with_wait(self, by, value, timeout=10, parent=None):
        if parent is None:
            parent = self.driver
        return WebDriverWait(parent, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def find_elements_with_wait(self, by, value, timeout=10, parent=None):
        if parent is None:
            parent = self.driver
        return WebDriverWait(parent, timeout).until(
            EC.presence_of_all_elements_located((by, value))
        )

    def atribuir_variaveis(self, nomes_iteravel=None):
        """Atribui as variáveis iniciais; se for passado um iterável de nomes, usa-o como `self.nome_livros`.

        Args:
            nomes_iteravel (iterable[str] | None): nomes de livros vindos do banco; se None usa conjunto padrão.
        """
        if nomes_iteravel:
            try:
                # converte para set para manter comportamento de iteração única
                self.nome_livros = set(nomes_iteravel)
            except Exception:
                # fallback para string
                self.nome_livros = nomes_iteravel
        else:
            self.nome_livros = {'Harry Potter e a Pedra Filosofal', 'Alice no Pais das Maravilhas'}

        self.preco_livro = 0
        self.index = 0
        self.titulo_do_livro = ''
        self.tipo_do_livro = ''

    ''' FUNÇÃO APENAS PARA ENTRAR NO SITE '''
    def entrar_site(self):
        self.driver.get('https://www.amazon.com.br/Livros/b/?ie=UTF8&node=6740748011&ref_=nav_cs_books')

    def pesquisar_livro(self):
        print('Aqui iremos pesquisar o livro...')

        for tipo in self.nome_livros:

            '''ESSE PROJETO IRA PESQUISAR 2 TIPOS DE LIVROS DIFERENTES'''

            self.find_element_with_wait(By.XPATH, '//input[contains(@id, "twotabsearchtextbox")]').send_keys(tipo)
            time.sleep(1)

            # APÓS INSERIDO O TIPO DO LIVRO IREMOS PESQUISAR
            self.find_element_with_wait(By.XPATH, '//input[contains(@id, "search-submit")]').click()
            time.sleep(1)

            # VERIFICA SE O TEXT QUE FOI ENVIADO É O MESMO DO INDEX = 0
            verifica_texto = self.find_element_with_wait(By.XPATH, "//div[contains(@class, 'a-section a-spacing-none s-breadcrumb-header-text')]")
            texto = verifica_texto.text

            if tipo in texto:
                print(f'Livro verificado: {tipo} !')
                return
            else:
                print('Livro nao verificado!')
                raise

    def extracao(self):
        print('Aqui iremos extrair valores...')

        # AQUI IREMOS ITERAR SOBRE CADA 'TABLE'

        index_tabela = 2

        index_titulo = 1

        items_tabela = self.find_elements_with_wait(By.XPATH, f'//div[contains(@role, "listitem") and contains(@data-index, "{index_tabela}")]')

        for item in items_tabela:
            index_tabela += 1


            preco_capa_dura = self.find_element_with_wait(By.XPATH, f'(//span[contains(@class, "a-price")]//span[contains(@class, "a-price-whole")])[{index_titulo}]')
            index_titulo += 1
            texto_do_preco_capa = preco_capa_dura.text

            converter_para_int = int(texto_do_preco_capa)

            print(f'Preço livro: {converter_para_int}R$')

            if converter_para_int < 50 and converter_para_int > 20:
                self.preco_livro = converter_para_int

                titulo_livro = self.find_element_with_wait(By.XPATH, f'(//a[contains(@class, "a-link-normal s-line-clamp-2")])[{index_titulo}]')
                self.titulo_do_livro = titulo_livro.text

                print(f'Titulo do livro: {titulo_livro.text}')

                tipo_do_livro = self.find_element_with_wait(By.XPATH, f'(//a[contains(@class, "a-size-base a-link-normal s-underline-")])[{index_titulo}]')
                self.tipo_do_livro = tipo_do_livro.text

                print(f'Tipo do livro: {tipo_do_livro.text}')
