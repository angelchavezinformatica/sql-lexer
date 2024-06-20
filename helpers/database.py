from sqlite3 import connect


class ConnectDB:
    def __init__(self):
        self.connection = connect('dbVivero.db')
        self.cursor = self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def execute(self, sql: str):
        result = self.cursor.execute(sql).fetchall()
        self.connection.commit()
        return result
