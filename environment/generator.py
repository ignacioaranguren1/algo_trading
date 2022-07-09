from random import randint


class Generator(object):
    def __init__(self, id):
        self.id = id

    def gen_random(self) -> int:
        return randint(0, 10)
