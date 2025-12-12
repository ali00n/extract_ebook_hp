import mysql.connector

class BancoDeDados:
    def __init__(self):
        self.cursor = None
        self.titulo = ''
        
        
    def conexao_banco(self, host='localhost', user='root', password='1234', database='extract'):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()