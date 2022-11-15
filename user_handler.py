from user import User
from db_handler import Database
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
    def get(username):
        with Database(DB_PATH) as db:
            return db.select(f"""
                SELECT * FROM USER
                WHERE username="{username}";
            """)

    def delete(self):
        pass

    def update(self):
        with Database(DB_PATH) as db:
            return db.query(f"""
                UPDATE USER
                SET username = "{self.User.username}"
                    first_name = ""
                    last_name = ""
                    hashed_pass = ""
                    is_staff = ""
            """)



if __name__ == "__main__":    
    for elem in UserHandler.get("palemale")[0]:
        print(elem)


Yulia = User("yulkamur", "Yulia", "Zhur", "1234", 0)

print(Yulia.password)

#UserHandler.save_user(Yulia)

print(UserHandler.get(username='yulkamur')[0])