import mysql.connector

class BancoDeDados:
    def __init__(self, conexao):
        self.cursor = None
        self.conexao = conexao

    def conexao_banco(self, host='localhost', user='root', password='1234', database='extract'):
        self.conexao = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conexao.cursor()