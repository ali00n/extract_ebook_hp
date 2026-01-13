import mysql.connector
import time

class BancoDeDados:
    def __init__(self, var):
        self.conexao = None
        self.cursor = None
        self.var = var

    def conexao_banco(self, host='localhost', user='root', password='1234', database='extract'):
        tentativas = 0

        while tentativas < 5:
            try:
                self.conexao = mysql.connector.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=database
                )

                if self.conexao.is_connected():
                    self.cursor = self.conexao.cursor()
                    print('Conexão com banco de dados bem-sucedida')
                    return

            except mysql.connector.Error as e:
                tentativas += 1
                print(f'Erro ao conectar ({tentativas}/5): {e}')
                time.sleep(2)

        raise Exception('Não foi possível conectar ao banco de dados')

    def inserir_dados(self, titulo_livro, preco_livro, tipo_livro):
        """Insere um registro na tabela DADOS_LIVRO.

        Args:
            titulo_livro (str): título do livro
            preco_livro (int | float): preço do livro
            tipo_livro (str): tipo/descrição do livro

        Returns:
            int: id do registro inserido (quando aplicável) ou None

        Raises:
            Exception: quando não há conexão com o banco ou ocorre erro na inserção
        """
        print('Inserir dados...')

        if not self.conexao or not self.conexao.is_connected():
            raise Exception('Sem conexão com o banco. Chame conexao_banco() antes de inserir dados.')

        try:
            # Usa query parametrizada para evitar SQL injection
            sql = (
                "INSERT INTO DADOS_LIVRO (TITULO_LIVRO, PRECO_LIVRO, TIPO_LIVRO) "
                "VALUES (%s, %s, %s)"
            )

            params = (titulo_livro, preco_livro, tipo_livro)

            cursor = self.conexao.cursor()
            cursor.execute(sql, params)
            self.conexao.commit()

            try:
                inserted_id = cursor.lastrowid
            except Exception:
                inserted_id = None

            print(f'Registro inserido com sucesso (id={inserted_id})')
            cursor.close()
            return inserted_id

        except mysql.connector.Error as e:
            # Faz rollback em caso de erro
            try:
                self.conexao.rollback()
            except Exception:
                pass
            print(f'Erro ao inserir dados: {e}')
            raise

    def fechar_conexao(self):
        """Fecha cursor e conexão com o banco, se existirem."""
        try:
            if self.cursor:
                try:
                    self.cursor.close()
                except Exception:
                    pass
            if self.conexao and self.conexao.is_connected():
                self.conexao.close()
                print('Conexão fechada')
        except Exception as e:
            print(f'Erro ao fechar conexão: {e}')
