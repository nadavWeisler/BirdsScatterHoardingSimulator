

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QGridLayout, QPushButton, QWidget)

import qtawesome as qta

from bird import Bird

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 100


class Birds(QWidget):
    def __init__(self, birds_list):
        super().__init__()
        mainLayout = QGridLayout()
        for i in range(len(birds_list)):
            mainLayout.addWidget(self.createIcon(
                "fa5s.kiwi-bird", birds_list[i].name, birds_list[i].getHideOut), 0, i)

        mainLayout.setAlignment(Qt.AlignTop)
        self.setLayout(mainLayout)

    @staticmethod
    def createIcon(iconName, iconText, executeFunction):
        icon = qta.icon(iconName)
        btn = QPushButton(icon, iconText)
        btn.setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
        btn.clicked.connect(executeFunction)
        return btn
