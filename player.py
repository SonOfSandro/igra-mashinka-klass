from PyQt5 import uic
from PyQt5.QtWidgets import *
from main import your_score


class ToLeaderList(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("end.ui", self)
        self.enter.clicked.connect(self.write())
        self.name = self.input_name.text()

    def write(self):
        with open("PlayerResults.txt") as file:
            file.write(f"{self.name}: {your_score}")
            file.close()
