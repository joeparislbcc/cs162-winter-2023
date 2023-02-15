#!/usr/bin/env python3

# noqa
# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,invalid-name,eval-used,broad-exception-caught,attribute-defined-outside-init,too-many-instance-attributes

import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(400, 300)

        button = QPushButton("Click me!", parent=self)

        self.setCentralWidget(button)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()  # all top-level widgets are WINDOWS
    window.show()
    sys.exit(app.exec())  # start the event loop
