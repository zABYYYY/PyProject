class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Результат")
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel()
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        self.setLayout(layout)