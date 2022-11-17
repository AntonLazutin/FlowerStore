import sys
import os
 
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to
# the sys.path.
sys.path.append(parent)

import database.db_handler as db_handler
from config import DB_PATH
from .flower import Flower

class FlowerHandler:
    """
    Class for the connection between Flower class and DB
    """

    def __init__(self, flower: Flower) -> None:
        self.flower = flower

    def save_flower(self):
        with db_handler.Database(DB_PATH) as db:
            db.query(f"""
                INSERT INTO Flower(name, price, quantity)
                VALUES(
                        "{self.flower.name}", "{self.flower.price}", "{self.flower.quantity}"
                    );
            """)

    @staticmethod
    def get(name):
        with db_handler.Database(DB_PATH) as db:
            return db.select(f"""
                SELECT * FROM Flower
                WHERE name="{name}";
            """)

    @staticmethod
    def get_all():
        with db_handler.Database(DB_PATH) as db:
            return db.select(f"""
                SELECT * FROM Flower;
            """)

    def delete(self):
        pass

    def update(self):
        with db_handler.Database(DB_PATH) as db:
            return db.query(f"""
               
            """)

# chrysanthemum = Flower("Хризантема", 22, 27)
# chrysanthemumHandler = FlowerHandler(chrysanthemum)
# chrysanthemumHandler.save_flower()
print(FlowerHandler.get_all())
