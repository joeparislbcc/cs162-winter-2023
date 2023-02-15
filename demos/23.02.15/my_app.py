#!/usr/bin/env python3

import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)

window = QMainWindow()  # all top-level widgets are WINDOWS
# the QPushButton is the top-level widget because it has no parent attribute
window.show()
sys.exit(app.exec())  # start the event loop
