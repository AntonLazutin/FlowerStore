import bcrypt

"""
    Hashing and then later checking that a password matches the previous hashed password is very simple:

    import bcrypt

    password = b"super secret password"
    # Hash a password for the first time, with a randomly-generated salt
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    # Check that an unhashed password matches one that has previously been hashed
    if bcrypt.checkpw(password, hashed):
        print("It Matches!")
    else:
        print("It Does not Match :(")
"""

class User:
    def __init__(self, username=None, f_name=None, l_name=None, password=None, status=False) -> None:
        self.__id = None
        self.username = username
        self.__f_name = f_name
        self.__l_name = l_name
        self.__password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.__is_staff = status

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def f_name(self):
        return self.__f_name
    
    @f_name.setter
    def f_name(self, f_name):
        self.__f_name = f_name

    @property
    def l_name(self):
        return self.__l_name
    
    @l_name.setter
    def l_name(self, l_name):
        self.__l_name = l_name

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def is_staff(self):
        return self.__is_staff
    
    @is_staff.setter
    def is_staff(self, is_staff):
        self.__is_staff = is_staff
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

palemale = User('abobaabobus', 'aboba', 'abobus', '1313141', 0)

print(palemale.f_name)
print(palemale.password)