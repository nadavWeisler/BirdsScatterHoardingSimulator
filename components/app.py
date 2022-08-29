
from PyQt6.QtWidgets import QDialog, QGridLayout, QPushButton, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import numpy as np
from components.bird import Bird
from components.map import Map
import os
import sys
import ctypes

from constants import BUTTON_LENGTH, ROW_BUTTON_HEIGHT, ROW_BUTTON_WIDTH


class App(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'Scatter Hoarding Simulator'
        self.birds = [Bird(), Bird(), Bird(), Bird()]
        self.maps = [Map(), Map(), Map(), Map(), Map()]
        self.initUI()

    def hideAllprevMaps(self):
        for map in self.maps:
            if map != self.currentMap:
                map.board.hide()

    def setCurrentMap(self, index):
        self.currentMap = self.maps[index]
        self.hideAllprevMaps()
        self.currentMap.board.show()
        self.layout.addWidget(self.currentMap.board, 1, 1, 5, 4)

    def drawBirdHideplace(self, index):
        x, y = self.birds[index].getHidePlace(self.currentMap.matrix)
        self.currentMap.board.draw_food_place(
            x, y, self.birds[index].getColor())

    def addMaps(self):
        m1 = QPushButton(QIcon(
            "icons/map.png"), self.maps[0].name)
        m1.clicked.connect(lambda: self.setCurrentMap(0))
        m1.setFixedSize(250, 100)
        m1.setIconSize(QSize(50, 50))
        m1.setContentsMargins(0, 0, 0, 0)
        m1.setStyleSheet("QPushButton { text-align: left; padding-left: 10px;}")
        self.layout.addWidget(m1, 1, 0)

        m2 = QPushButton(QIcon(
            "icons/map.png"), self.maps[1].name)
        m2.clicked.connect(lambda: self.setCurrentMap(1))
        m2.setFixedSize(250, 100)
        m2.setIconSize(QSize(50, 50))
        m2.setStyleSheet("QPushButton { text-align: left; padding-left: 10px;}")
        self.layout.addWidget(m2, 2, 0)

        m3 = QPushButton(QIcon(
            "icons/map.png"), self.maps[2].name)
        m3.clicked.connect(lambda: self.setCurrentMap(2))
        m3.setFixedSize(250, 100)
        m3.setIconSize(QSize(50, 50))
        m3.setStyleSheet("QPushButton { text-align: left; padding-left: 10px;}")
        self.layout.addWidget(m3, 3, 0)

        m4 = QPushButton(QIcon(
            "icons/map.png"), self.maps[3].name)
        m4.clicked.connect(lambda: self.setCurrentMap(3))
        m4.setFixedSize(250, 100)
        m4.setIconSize(QSize(50, 50))
        m4.setStyleSheet("QPushButton { text-align: left; padding-left: 10px;}")
        self.layout.addWidget(m4, 4, 0)

        m5 = QPushButton(QIcon(
            "icons/map.png"), self.maps[4].name)
        m5.clicked.connect(lambda: self.setCurrentMap(4))
        m5.setFixedSize(250, 100)
        m5.setIconSize(QSize(50, 50))
        m5.setStyleSheet("QPushButton { text-align: left; padding-left: 10px; }")
        self.layout.addWidget(m5, 5, 0)

    def addBirds(self):
        existing_birds = []
        randomNumber = np.random.randint(1, 48)

        while randomNumber in existing_birds:
            randomNumber = np.random.randint(1, 48)

        existing_birds.append(randomNumber)

        m1 = QPushButton(
            QIcon("icons/bird" + str(randomNumber) + ".png"), self.birds[0].getName())
        m1.clicked.connect(lambda: self.drawBirdHideplace(0))
        m1.setFixedSize(ROW_BUTTON_WIDTH, ROW_BUTTON_HEIGHT)
        m1.setIconSize(QSize(BUTTON_LENGTH, BUTTON_LENGTH))
        m1.setFont(QFont('Times', 15))
        m1.setStyleSheet("background-color: " + self.birds[0].getColor())
        self.layout.addWidget(m1, 0, 1)

        while randomNumber in existing_birds:
            randomNumber = np.random.randint(1, 48)

        existing_birds.append(randomNumber)

        m2 = QPushButton(QIcon(
            "icons/bird" + str(randomNumber) + ".png"), self.birds[1].getName())
        m2.clicked.connect(lambda: self.drawBirdHideplace(1))
        m2.setFixedSize(ROW_BUTTON_WIDTH, ROW_BUTTON_HEIGHT)
        m2.setIconSize(QSize(BUTTON_LENGTH, BUTTON_LENGTH))
        m2.setFont(QFont('Times', 15))
        m2.setStyleSheet("background-color: " + self.birds[1].getColor())
        self.layout.addWidget(m2, 0, 2)

        while randomNumber in existing_birds:
            randomNumber = np.random.randint(1, 48)

        existing_birds.append(randomNumber)

        m3 = QPushButton(QIcon(
            "icons/bird" + str(randomNumber) + ".png"), self.birds[2].getName())
        m3.setFixedSize(ROW_BUTTON_WIDTH, ROW_BUTTON_HEIGHT)
        m3.setIconSize(QSize(BUTTON_LENGTH, BUTTON_LENGTH))
        m3.clicked.connect(lambda: self.drawBirdHideplace(2))
        m3.setFont(QFont('Times', 15))
        m3.setStyleSheet("background-color: " + self.birds[2].getColor())
        self.layout.addWidget(m3, 0, 3)

        while randomNumber in existing_birds:
            randomNumber = np.random.randint(1, 48)
        existing_birds.append(randomNumber)

        m4 = QPushButton(QIcon(
            "icons/bird" + str(randomNumber) + ".png"), self.birds[3].getName())
        m4.setFixedSize(ROW_BUTTON_WIDTH, ROW_BUTTON_HEIGHT)
        m4.setIconSize(QSize(BUTTON_LENGTH, BUTTON_LENGTH))
        m4.clicked.connect(lambda: self.drawBirdHideplace(3))
        m4.setFont(QFont('Times', 15))
        m4.setStyleSheet("background-color: " + self.birds[3].getColor())
        self.layout.addWidget(m4, 0, 4)

    def addMainButtons(self):
        mainButtonWidget = QWidget()
        currentLayout = QGridLayout()
        restartButton = QPushButton(QIcon("icons/restart.png"), "")
        restartButton.clicked.connect(lambda: os.execl(
            sys.executable, sys.executable, *sys.argv))
        restartButton.setFixedSize(100, 100)
        restartButton.setIconSize(QSize(BUTTON_LENGTH, BUTTON_LENGTH))
        restartButton.setToolTip("Restart")
        currentLayout.addWidget(restartButton)
        mainButtonWidget.setLayout(currentLayout)
        self.layout.addWidget(mainButtonWidget, 0, 0)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('icons/bird48.png'))
        self.layout = QGridLayout()
        self.addBirds()
        self.addMaps()
        self.layout.setSpacing(0)
        self.setCurrentMap(0)
        self.addMainButtons()
        self.setLayout(self.layout)
        myappid = 'scatter.hoarding.birds.1.0'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.show()
 