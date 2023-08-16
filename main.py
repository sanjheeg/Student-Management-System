from PyQt6.QtWidgets import QTableWidget, QMainWindow, QApplication, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QLabel, QWidget
import sys
from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        file_menu = self.menuBar().addMenu("&File")
        help_menu = self.menuBar().addMenu("&Help")

        add_student = QAction("add student", self)
        file_menu.addAction(add_student)

        about = QAction("about", self)
        help_menu.addAction(about)
        about.setMenuRole(QAction.MenuRole.NoRole)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("ID", "name", "course", "mobile"))
        # a layout is used when you use QWidgets and you have multiple widgets, with QMainWindow we have a lot of
        # different structures so we need to specify the central widget
        self.setCentralWidget(self.table)

    def load_data(self):
        self.table


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())