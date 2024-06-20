from sqlite3 import connect


class ConnectDB:
    def __init__(self):
        self.connection = connect('dbVivero.db')
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def execute(self, sql: str, parameters: tuple = tuple()):
        result = self.cursor.execute(sql, parameters)
        self.connection.commit()
        return result
