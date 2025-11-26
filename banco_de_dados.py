import mysql.connector

class BancoDeDados:
    def __init__(self, host='localhost', user='root', password='1234', database='automation_fipe'):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
