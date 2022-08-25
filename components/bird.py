from utils import generate_key, getFakeFirstName, getRandomColor
import numpy as np


class Bird:
    def __init__(self):
        self.__name = getFakeFirstName()
        self.__color = getRandomColor()
        self.__key = generate_key()

    def getHidePlace(self, matrix):
        np.random.seed(self.__key)
        noise = np.random.rand(*matrix.shape)
        noise = noise * matrix
        x, y = np.unravel_index(np.argmax(noise, axis=None), noise.shape)
        return x, y
    
    def getColor(self):
        return self.__color
    
    def getName(self):
        return self.__name
