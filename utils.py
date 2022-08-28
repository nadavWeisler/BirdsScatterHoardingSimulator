from enum import Enum
from random import choices
from faker import Faker
import numpy as np
from math import floor


def rgb2hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


faker = Faker()


def getFakeFirstName():
    return faker.first_name()


def getFakeAddress():
    return faker.address()


def generate_key(minValue=0, maxValue=1000):
    return np.random.randint(minValue, maxValue)


def generate_matrix(minLength=20, maxLength=50):
    length = np.random.randint(minLength, maxLength)
    return np.random.randint(low=0, high=255, size=(length, length))

def bird_choise(mat, field_shape, key):
    np.random.seed(key)
    noise = np.random.rand(*field_shape)
    noise = noise * mat
    idx = np.unravel_index(np.argmax(noise, axis=None), noise.shape)
    return idx

def getRandomColor():
    randomColor = choices(range(256), k=3)
    return rgb2hex(randomColor[0], randomColor[1], randomColor[2])

class Colors(Enum):
    GreenBrown = 1
    Blue = 2
    
def getRandomColorPalette():
    return np.random.randint(1, 3)

def getRandomBoardColor(value):
    randomNumber = np.random.randint(1, 3)
    if randomNumber == 1:
        return rgb2hex(floor(value / 2.7), value, 0)
    else:
        return rgb2hex(value, floor(value / 2), 0)
