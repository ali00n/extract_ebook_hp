import undetected_chromedriver as uc

class Configuracoes:
    def __init__(self, var):
        self.driver = None
        self.var = var

    def iniciar_webdriver(self, headless=False):
        # Inicia com o undetected_chromedriver
        options = uc.ChromeOptions()

        # Configurações básicas
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # Inicializa o navegador (sem precisar de chromedriver instalado)
        driver = uc.Chrome(options=options)

        # guarda no objeto e retorna o driver diretamente
        self.driver = driver
        return driver
