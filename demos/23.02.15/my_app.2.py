#!/usr/bin/env python3

# noqa

# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,invalid-name,eval-used,broad-exception-caught,attribute-defined-outside-init,too-many-instance-attributes

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(400, 300)

        self.button = QPushButton("Click me!", parent=self)
        self.button.clicked.connect(self.onButtonClicked)

        self.label = QLabel("I'm a label!", parent=self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        self.label.setStyleSheet("background-color: red;")

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        centralWidget = QWidget(parent=self)
        centralWidget.setLayout(layout)

        self.setCentralWidget(centralWidget)

    def onButtonClicked(self):
        self.label.setText("You clicked the button.")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()  # all top-level widgets are WINDOWS
    window.show()
    sys.exit(app.exec())  # start the event loop
