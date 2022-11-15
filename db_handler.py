import sqlite3
import contextlib

class Database:
    def __init__(self, db_name) -> None:
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def query(self, query):
        self.cursor.execute(query)

    def select(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self.cursor.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()

