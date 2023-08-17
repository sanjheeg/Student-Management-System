from PyQt6.QtWidgets import QComboBox, QVBoxLayout, QTableWidgetItem, QDialog, QTableWidget, QMainWindow, QApplication, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QLabel, QWidget
import sys
from PyQt6.QtGui import QAction
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        file_menu = self.menuBar().addMenu("&File")
        help_menu = self.menuBar().addMenu("&Help")

        add_student = QAction("add student", self)
        add_student.triggered.connect(self.insert_student)
        file_menu.addAction(add_student)

        about = QAction("about", self)
        help_menu.addAction(about)
        about.setMenuRole(QAction.MenuRole.NoRole)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("ID", "name", "course", "mobile"))
        self.table.verticalHeader().setVisible(False)
        # a layout is used when you use QWidgets and you have multiple widgets, with QMainWindow we have a lot of
        # different structures so we need to specify the central widget
        self.setCentralWidget(self.table)

    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students")
        self.table.setRowCount(0)
        for row_num, row_data in enumerate(result):
            self.table.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                self.table.setItem(row_num, column_num, QTableWidgetItem(str(data)))
        connection.close()

    def insert_student(self):
        dialog = InsertDialog()
        dialog.exec()


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("insert student data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()
        name = QLineEdit()
        name.setPlaceholderText("name: ")
        layout.addWidget(name)

        course = QComboBox()
        options = ["Biology", "Math", "Astronomy", "Physics"]
        course.addItems(options)
        layout.addWidget(course)

        phone = QLineEdit()
        phone.setPlaceholderText("phone number: ")
        layout.addWidget(phone)

        self.setLayout(layout)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
window.load_data()
sys.exit(app.exec())