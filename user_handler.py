from user import User
from db_handler import Database
from config import DB_PATH

class UserHandler:
    """
    Class for the connection between User class and DB
    """

    def __init__(self, User: User=None) -> None:
        self.User = User

    def save_user(self):
        with Database(DB_PATH) as db:
            db.query("")

    @staticmethod
    def get(username):
        with Database(DB_PATH) as db:
            return db.select(f"""
                SELECT * FROM USER
                WHERE username="{username}";
            """)

    def delete(self):
        pass

    def update(self):
        pass



if __name__ == "__main__":    
    for elem in UserHandler.get("palemale")[0]:
        print(elem)