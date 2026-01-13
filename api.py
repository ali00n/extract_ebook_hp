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

        nomes = set()

        for row in cursor:
            # popula atributos (mantendo compatibilidade)
            self.titulo_livro = row.get("TITULO_LIVRO")
            self.preco_livro = row.get("PRECO_LIVRO")
            self.tipo_livro = row.get("TIPO_LIVRO")
            self.nome_livros_um = row.get("TIPO_LIVRO_UM")
            self.nome_livros_dois = row.get("TIPO_LIVRO_DOIS")

            # coleta os nomes fixos (pode repetir por causa do CROSS JOIN)
            if self.nome_livros_um:
                nomes.add(self.nome_livros_um)
            if self.nome_livros_dois:
                nomes.add(self.nome_livros_dois)

        # Se não encontrou nada no loop, tenta buscar diretamente de LIVRO_FIXO
        if not nomes:
            cursor2 = self.conexao.cursor(dictionary=True)
            cursor2.execute("SELECT TIPO_LIVRO_UM, TIPO_LIVRO_DOIS FROM LIVRO_FIXO LIMIT 1")
            row2 = cursor2.fetchone()
            if row2:
                if row2.get("TIPO_LIVRO_UM"):
                    nomes.add(row2.get("TIPO_LIVRO_UM"))
                if row2.get("TIPO_LIVRO_DOIS"):
                    nomes.add(row2.get("TIPO_LIVRO_DOIS"))
            try:
                cursor2.close()
            except Exception:
                pass

        try:
            cursor.close()
        except Exception:
            pass

        return nomes
