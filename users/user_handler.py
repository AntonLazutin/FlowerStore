from .user import User
from database.db_handler import Database
from config import DB_PATH

class UserHandler:
    """
    Class for the connection between User class and DB
    """

    def __init__(self, user) -> None:
        self.user = user

    def save_user(self):
        with Database(DB_PATH) as db:
            db.query(f"""
                INSERT INTO User(username, first_name, last_name, hashed_pass, is_staff)
                VALUES(
                    "{self.username}", "{self.f_name}", "{self.l_name}",
                    "{self.password}", "{self.is_staff}"
                    );
            """)

    @staticmethod
    def get_id(user):
        with Database(DB_PATH) as db:
            return db.select(f"""
                SELECT id FROM User
                WHERE username="{user.username}";
            """)[0][0]

    @staticmethod
    def get(username):
        with Database(DB_PATH) as db:
            return db.select(f"""
                SELECT * FROM USER
                WHERE username="{username}";
            """)

    def delete(self):
        pass

    @staticmethod
    def update(user):
        with Database(DB_PATH) as db:
            return db.query(f"""
                UPDATE OR REPLACE USER
                SET username = "{user.username}",
                    first_name = "{user.f_name}",
                    last_name = "{user.l_name}",
                    is_staff = "{user.is_staff}"
                WHERE id="{user.id}";
            """)


Yulia = User("bagsea", "Yulia", "Zhur", "1234", 0)


#UserHandler.save_user(Yulia)


#print(UserHandler.get(username='bagsea'))
Yulia.id = UserHandler.get_id(Yulia)

Yulia.username = "yulkamur"

UserHandler.update(Yulia)


