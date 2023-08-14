from datetime import datetime
from PyQt6.QtWidgets import QComboBox, QApplication, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QLabel, QWidget
import sys

class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("average speed calculator")

        grid = QGridLayout()
        distance_l = QLabel("distance:")
        self.distance = QLineEdit()
        time_l = QLabel("time (hours):")
        self.time = QLineEdit()
        self.output = QLabel("")
        calculate = QPushButton("calculate")
        calculate.clicked.connect(self.speed)
        self.unit = QComboBox()
        self.unit.addItem("miles")
        self.unit.addItem("kilometer")

        grid.addWidget(distance_l, 0, 0)
        grid.addWidget(self.distance, 0, 1)
        grid.addWidget(self.time, 1, 1)
        grid.addWidget(self.output, 3, 0, 1, 2)
        grid.addWidget(self.unit, 0, 2)
        grid.addWidget(time_l, 1, 0)
        grid.addWidget(calculate, 2, 1)

        self.setLayout(grid)

    def speed(self):
        avg = 0
        len = self.unit.currentText()
        if len == "miles":
            avg = float(self.distance.text()) / float(self.time.text())
            self.output.setText(f"the average speed is {avg} miles/hour")
        else:
            avg = float(self.distance.text()) / float(self.time.text())
            self.output.setText(f"the average speed is {avg} km/hour")

app = QApplication(sys.argv)
calc = SpeedCalculator()
calc.show()
sys.exit(app.exec())

