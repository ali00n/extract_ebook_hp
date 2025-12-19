from classes import *

class API:
    def __init__(self, conexao):
        self.driver = None
        self.conexao = conexao

    def invoke_dados_livro(self):
        # AQUI IREMOS DAR GET EM DADOS DO BANCO

        cursor = self.conexao.cursor()

        query = '''
        SELECT TITULO_LIVRO,
         PRECO_LIVRO,
          TIPO_LIVRO
        FROM DADOS_LIVRO
        '''
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            self.titulo_livro = row.get("TITULO_LIVRO")
            self.preco_livro = row.get("PRECO_LIVRO")
            self.tipo_livro = row.get("TIPO_LIVRO")


