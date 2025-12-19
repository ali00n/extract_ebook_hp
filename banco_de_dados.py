import mysql.connector
import time

class BancoDeDados:
    def __init__(self):
        self.conexao = None
        self.cursor = None

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
