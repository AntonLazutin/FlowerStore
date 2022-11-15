from ..db_handler import Database
from ..config import DB_PATH

class FlowerHandler:
    """
    Class for the connection between User class and DB
    """

    def __init__(self, user) -> None:
        self.user = user

    def save_flower(self):
        with Database(DB_PATH) as db:
            db.query(f"""
                INSERT INTO Flower()
                VALUES(

                    );
            """)

    @staticmethod
    def get():
        with Database(DB_PATH) as db:
            return db.select(f"""
                SELECT * FROM Flower
                WHERE ;
            """)

    def delete(self):
        pass

    def update(self):
        with Database(DB_PATH) as db:
            return db.query(f"""
               
            """)
