#!/usr/bin/env python3
"""Quick demo of PyQT line edits."""

# pylint: disable=invalid-name
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QLineEdit, QWidget


class LineEditsDemo(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.initUI()

    def initUI(self):
        """Initialize the UI using code."""
        layout = QGridLayout()

        self.lblFirstName = QLabel("First Name:", self)
        self.lblFirstName.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.lblLastName = QLabel("Last Name:", self)
        self.lblLastName.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        self.lblJob = QLabel("Job:", self)
        self.lblJob.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        self.lblUsername = QLabel("Username:", self)
        self.lblUsername.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        self.lblPassword = QLabel("Password:", self)
        self.lblPassword.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        self.lblEmail = QLabel("Email:", self)
        self.lblEmail.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        self.txtFirstName = QLineEdit("", self)
        self.txtLastName = QLineEdit("", self)
        self.txtJob = QLineEdit("", self)
        self.txtUsername = QLineEdit("", self)
        self.txtPassword = QLineEdit("", self)
        self.txtPassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.txtEmail = QLineEdit("", self)
        self.txtEmail.setPlaceholderText("example@example.com")

        layout.addWidget(self.lblFirstName, 0, 0)
        layout.addWidget(self.txtFirstName, 0, 1)
        layout.addWidget(self.lblLastName, 0, 2)
        layout.addWidget(self.txtLastName, 0, 3)
        layout.addWidget(self.lblJob, 1, 0)
        layout.addWidget(self.txtJob, 1, 1, 1, 3)
        layout.addWidget(self.lblUsername, 2, 0)
        layout.addWidget(self.txtUsername, 2, 1, 1, 3)
        layout.addWidget(self.lblEmail, 3, 0)
        layout.addWidget(self.txtEmail, 3, 1, 1, 3)
        layout.addWidget(self.lblPassword, 4, 0)
        layout.addWidget(self.txtPassword, 4, 1, 1, 3)

        self.setLayout(layout)

        self.setWindowTitle("Widgets - Line Edits")
        self.setGeometry(200, 200, 325, 0)
        self.show()


def main():
    app = QApplication(sys.argv)
    window = LineEditsDemo()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
