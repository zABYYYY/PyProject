
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
QPushButton, QLabel, QLineEdit)

from instr import *

win_x, win_y = 200, 100
win_width, win_height = 1000, 600

class testWin(QWidget):
    def __init__(self):
        super().__init__()
    # створюємо та налаштовуємо графічні елементи:
        self.initUI()
    # Встановлює зв'язки між елементами
        self.connects()
    # Встановлює, як виглядатиме вікно (напис, розмір, місце)
        self.set_appear()
    # старт:
        self.show()

    def initUI(self):
        self.txt_hello = QLabel(txt_hello)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.txt_hello, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.btn_next, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()


    def set_appear(self):

        self.resize(win_width, win_height)
        self.move(win_x, win_y)


app = QApplication([])
test_Win = testWin()
test_Win.show()
app.exec_()


