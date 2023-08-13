from datetime import datetime
from PyQt6.QtWidgets import QApplication, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QLabel, QWidget
import sys


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        # create widgets
        grid = QGridLayout()
        name = QLabel("name: ")
        self.edit_name = QLineEdit()
        birth = QLabel("date of birth mm/dd/yyyy: ")
        self.edit_birth = QLineEdit()

        button = QPushButton("calculate age")
        button.clicked.connect(self.calculate)
        self.output = QLabel("")

        # add widgets to grid
        grid.addWidget(name, 0, 0)
        grid.addWidget(self.edit_name, 0, 1)
        grid.addWidget(birth, 1, 0)
        grid.addWidget(self.edit_birth, 1, 1)
        # button add [2,0] and we want it to span across 1 row and to columns
        grid.addWidget(button, 2, 0, 1, 2)
        grid.addWidget(self.output, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate(self):
        current = datetime.now().year
        date = self.edit_birth.text()
        name = self.edit_name.text()
        birth = datetime.strptime(date, "%m/%d/%Y").date().year
        age = current - birth
        self.output.setText(f"you are {age} years old, {name}")


app = QApplication(sys.argv)
calc = AgeCalculator()
calc.show()
sys.exit(app.exec())

