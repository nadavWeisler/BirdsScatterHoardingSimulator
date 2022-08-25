from PyQt6 import QtGui, QtWidgets
import sys
from PyQt6.QtWidgets import QApplication, QTabWidget, QDialog
import numpy as np
from bird import Bird
from components.birds import Birds

from components.board import Board
from map import Map
import random
import names

from utils import rgb2hex


class App(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'CryptoBirds'
        self.birds = [self.generateRandomBird(), self.generateRandomBird(),
                      self.generateRandomBird()]
        self.maps = [self.generateRandomMap(), self.generateRandomMap(),
                     self.generateRandomMap()]
        self.currentMap = None
        self.initUI()

    def generateRandomMap(self):
        randomNumber = np.random.randint(20, 50)
        return Map(np.random.randint(low=0, high=255,
                                     size=(randomNumber, randomNumber)))

    def generateRandomBird(self):
        randomNumber = np.random.randint(1, 1000)
        randomColor = random.choices(range(256), k=3)
        return Bird(names.get_first_name(), rgb2hex(randomColor[0], randomColor[1], randomColor[2]),
                    randomNumber)

    def getMapIcon(self, index):
        m = QtWidgets.QPushButton(QtGui.QIcon(
            "icons/map.png"), "Map " + str(index))
        m.clicked.connect(lambda: self.setCurrentMap(index))
        m.setFixedSize(200, 200)
        return m

    def setCurrentMap(self, index):
        self.currentMap = self.maps[index]
        self.layout.addWidget(self.currentMap.board, 1, 1, 3, 3)

    def getNewMapIcon(self):
        newMapButton = QtWidgets.QPushButton(
            QtGui.QIcon("icons/new.png"), "New Map")
        newMapButton.clicked.connect(lambda: self.createNewMap())
        newMapButton.setFixedSize(200, 200)
        return newMapButton

    def addMaps(self):
        m1 = QtWidgets.QPushButton(QtGui.QIcon(
            "icons/map.png"), "Map " + str(1))
        m1.clicked.connect(lambda: self.setCurrentMap(0))
        self.layout.addWidget(m1, 1, 0)

        m2 = QtWidgets.QPushButton(QtGui.QIcon(
            "icons/map.png"), "Map " + str(2))
        m2.clicked.connect(lambda: self.setCurrentMap(1))
        self.layout.addWidget(m2, 2, 0)

        m3 = QtWidgets.QPushButton(QtGui.QIcon(
            "icons/map.png"), "Map " + str(3))
        m3.clicked.connect(lambda: self.setCurrentMap(2))
        self.layout.addWidget(m3, 3, 0)

    def addBirds(self):
        randomNumber = np.random.randint(1, 8)
        m1 = QtWidgets.QPushButton(QtGui.QIcon(
            "icons/bird" + str(randomNumber) + ".png"), "Map " + str(1))
        m1.clicked.connect(lambda: self.setCurrentMap(0))
        self.layout.addWidget(m1, 0, 1)

        randomNumber = np.random.randint(1, 8)
        m2 = QtWidgets.QPushButton(QtGui.QIcon(
            "icons/bird" + str(randomNumber) + ".png"), "Map " + str(2))
        m2.clicked.connect(lambda: self.setCurrentMap(1))
        self.layout.addWidget(m2, 0, 2)

        randomNumber = np.random.randint(1, 8)
        m3 = QtWidgets.QPushButton(QtGui.QIcon(
            "icons/bird" + str(randomNumber) + ".png"), "Map " + str(3))
        m3.clicked.connect(lambda: self.setCurrentMap(2))
        self.layout.addWidget(m3, 0, 3)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.layout = QtWidgets.QGridLayout()
        self.addBirds()
        self.addMaps()
        self.setLayout(self.layout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.resize(650, 500)
    sys.exit(app.exec_())
