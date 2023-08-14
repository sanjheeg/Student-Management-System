from PyQt6.QtWidgets import QMainWindow, QApplication, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QLabel, QWidget
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


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())