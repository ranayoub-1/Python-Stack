import random

def randInt(min=0, max=100):
    if min > max:
        min, max = max, min

    num = random.random()
    return round(num * (max - min) + min)

# BONUS
import random

def randInt(min=0, max=100):
    if min > max:
        min, max = max, min

    if min == max:
        return min

    num = random.random()
    return round(num * (max - min) + min)