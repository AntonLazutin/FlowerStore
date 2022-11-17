from database import Database

from users.user import User
from users.user_handler import UserHandler

from flowers.flower import Flower
from flowers.flower_handler import FlowerHandler


if __name__ == "__main__":
    for flower in FlowerHandler.get_all():
        for elem in flower:
            print(elem)