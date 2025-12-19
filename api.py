

class API:
    def __init__(self, conexao):
        self.driver = None
        self.conexao = conexao
        self.titulo_livro = None
        self.preco_livro = None
        self.tipo_livro = None
        self.nome_livros_um = None
        self.nome_livros_dois = None

    def invoke_dados_livro(self):
        # AQUI IREMOS DAR GET EM DADOS DO BANCO

        cursor = self.conexao.cursor(dictionary=True)

        cursor.execute("""
               SELECT 
                   d.TITULO_LIVRO,
                   d.PRECO_LIVRO,
                   d.TIPO_LIVRO,
                   f.TIPO_LIVRO_UM,
                   f.TIPO_LIVRO_DOIS
               FROM DADOS_LIVRO d
               CROSS JOIN LIVRO_FIXO f
           """)

        for row in cursor:
            self.titulo_livro = row.get("TITULO_LIVRO")
            self.preco_livro = row.get("PRECO_LIVRO")
            self.tipo_livro = row.get("TIPO_LIVRO")
            self.nome_livros_um = row.get("TIPO_LIVRO_UM")
            self.nome_livros_dois = row.get("TIPO_LIVRO_DOIS")


