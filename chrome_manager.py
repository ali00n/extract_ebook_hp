import undetected_chromedriver as uc

class Configuracoes:
    def __init__(self):
        self.driver = None

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
        self.driver = uc.Chrome(options=options)

        return self.driver