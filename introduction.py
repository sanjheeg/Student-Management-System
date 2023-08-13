import sys
from PyQt6.QtWidgets import QApplication, QGridLayout, QLineEdit, QVBoxLayout, QLabel, QWidget


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        name = QLabel("name: ")
        edit_name = QLineEdit()
        birth = QLabel("date of birth mm/dd/yyyy: ")
        edit_birth = QLineEdit()

        grid.addWidget(name, 0, 0)
        grid.addWidget(edit_name, 0, 1)
        grid.addWidget(birth, 1, 0)
        grid.addWidget(edit_birth, 1, 1)

        self.setLayout(grid)


app = QApplication(sys.argv)
calc = AgeCalculator()
calc.show()
sys.exit(app.exec())
