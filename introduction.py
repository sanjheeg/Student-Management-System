import sys
from PyQt6.QtWidgets import QApplication, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QLabel, QWidget


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()

        # create widgets
        grid = QGridLayout()
        name = QLabel("name: ")
        edit_name = QLineEdit()
        birth = QLabel("date of birth mm/dd/yyyy: ")
        edit_birth = QLineEdit()

        button = QPushButton("calculate age")
        output = QLabel("")

        grid.addWidget(name, 0, 0)
        grid.addWidget(edit_name, 0, 1)
        grid.addWidget(birth, 1, 0)
        grid.addWidget(edit_birth, 1, 1)
        # button add [2,0] and we want it to span across 1 row and to columns
        grid.addWidget(button, 2, 0, 1, 2)
        grid.addWidget(output, 3, 0, 1, 2)

        self.setLayout(grid)


app = QApplication(sys.argv)
calc = AgeCalculator()
calc.show()
sys.exit(app.exec())
