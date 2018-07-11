import math


def encrypt(num):
    return (num ** 2 - 10) * 7 - 3


def decrypt(num):
    x = math.sqrt(abs((num + 3) / 7 + 10))
    if x == int(x):
        return int(x)
    else:
        return 0


print(encrypt(0))