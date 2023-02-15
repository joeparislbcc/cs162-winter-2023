#!/usr/bin/env python3

# noqa

# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,invalid-name,eval-used,broad-exception-caught,attribute-defined-outside-init,too-many-instance-attributes

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(400, 300)

        self.spinBoxLabel = QLabel("Value:", parent=self)
        self.spinBoxLabel.setAlignment(Qt.AlignmentFlag.AlignRight)
        # self.label.setStyleSheet("background-color: red;")
        self.spinBox = QSpinBox(parent=self)
        self.spinBox.setMinimum(-10)
        self.spinBox.setMaximum(10)
        self.spinBox.valueChanged.connect(self.onValueChanged)

        self.valueLabel = QLabel("0", parent=self)

        hBox = QHBoxLayout()
        hBox.addWidget(self.spinBoxLabel)
        hBox.addWidget(self.spinBox)

        vBox = QVBoxLayout()
        vBox.addLayout(hBox)
        vBox.addWidget(self.valueLabel)

        centralWidget = QWidget(parent=self)
        centralWidget.setLayout(vBox)

        self.setCentralWidget(centralWidget)

    def onValueChanged(self):
        self.valueLabel.setText(str(self.spinBox.value()))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()  # all top-level widgets are WINDOWS
    window.show()
    sys.exit(app.exec())  # start the event loop
