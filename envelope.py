import random


class Envelope:

    def __init__(self):
        self.money = random.randint(0, 100000)
        self.used = False
