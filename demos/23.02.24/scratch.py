#!/usr/bin/env python3
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QLabel, QMainWindow, QVBoxLayout, QWidget


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(800, 600)

        label1 = QLabel("Label 1", parent=self)
        label1.setStyleSheet("background-color: red;")
        label2 = QLabel("Label 2", parent=self)
        label2.setStyleSheet("background-color: red;")
        label3 = QLabel("Label 3", parent=self)
        label3.setStyleSheet("background-color: red;")

        centralWidget = QWidget()
        centralWidget.setStyleSheet("background-color: blue;")
        self.setCentralWidget(centralWidget)

        vbox = QVBoxLayout()
        centralWidget.setLayout(vbox)
        vbox.addWidget(label3)
        vbox.addWidget(label2)
        vbox.addWidget(label1)

        label4 = QLabel("Label 4", parent=self)
        label4.setStyleSheet("background-color: green")
        label4.setMinimumWidth(100)
        label5 = QLabel("Label 5", parent=self)
        label5.setStyleSheet("background-color: green")
        label5.setMinimumWidth(100)

        hbox = QHBoxLayout()
        hbox.setAlignment(Qt.AlignmentFlag.AlignLeft)
        hbox.addWidget(label4)
        hbox.addWidget(label5)

        vbox.addLayout(hbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()  # all top-level widgets are WINDOWS
    window.show()
    sys.exit(app.exec())  # start the event loop
