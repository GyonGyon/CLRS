import random


def log(*arg):
    print('>>>', *arg)


def random_array(size=8):
    a = list(range(size))
    random.shuffle(a)
    return a
