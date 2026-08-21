from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
              QPushButton, QLabel, QLineEdit)

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        label = QLabel("Индекс Руфье: 0.0\nСостояние вашего здоровья: Отличное")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        
        layout.addWidget(label)

        self.setLayout(layout)
    
    def set_appear(self):
        
        self.setWindowTitle("Результат")
        self.resize(400, 300)
        self.show

def age_rate(self):

    age = int(self.line_edit_age.text())

    index = self.calculate_ruffier()

    if age == 7 or age == 8:

        if index >= 21:
            return "Низький"
        elif index >= 17:
            return "Задовільний"
        elif index >= 12:
            return "Середній"
        elif index >= 6.5:
            return "Вище среднього"
        else:
            return "Високий"

    elif age == 9 or age == 10:
        if index >= 19.5:
            return "Низький"
        elif index >= 15.5: 
            return "Задовільний"
        elif index >= 10.5:
            return "Середній"
        elif index >= 5:
            return "Вище середнього"
        else:
            return "Високий"

    elif age == 11 or age == 12:

        if index >= 18:
            return "Низький"

        elif index >= 14:
            return "Задовільний"
        elif index >= 9:
            return "Середній"
        elif index >= 3.5:
            return "Вище середнього"
        else:
            return "Високий"

    elif age == 13 or age == 14:

        if index >= 16.5:
            return "Низький"
        elif index >= 12.5:
            return "Задовільний"
        elif index >= 7.5:
            return "Середній"
        elif index >= 2:
            return "Вище середнього"
        else:
            return "Високий"

    elif age >= 15:
        if index >= 15:
            return "Низький"
        elif index >= 11:
            return "Задовільний"
        elif index >= 6:
            return "Середній"
        elif index >= 0.5:
            return "Вище середнього"
        else:
            return "Високий"
    
app = QApplication([])
fw = FinalWin()
fw.show()
app.exec_()