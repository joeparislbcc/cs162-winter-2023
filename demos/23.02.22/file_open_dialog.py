#!/usr/bin/env python3

# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,invalid-name
import sys
from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QKeySequence
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QLabel,
    QMainWindow,
    QToolBar,
    QVBoxLayout,
    QWidget,
)


class FileOpenDialogDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        # region: build the main parts of the GUI
        self.setWindowTitle("File Open Dialog Demo")
        self.setMinimumSize(800, 600)

        self.mainLayout = QVBoxLayout()
        self.pathLabel = QLabel("Spam spam spam", parent=self)
        self.pathLabel.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        self.mainLayout.addWidget(self.pathLabel)

        centralWidget = QWidget()
        centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(centralWidget)
        # endregion

        # region build actions
        self.actionFileOpen = QAction("&Open...", parent=self)
        self.actionFileOpen.setShortcut(QKeySequence("Ctrl+o"))
        self.actionFileOpen.setStatusTip("Opens a file you select")
        self.actionFileOpen.setToolTip("Open a file")
        self.actionFileOpen.triggered.connect(self.onFileOpenClicked)

        self.actionFileSaveAs = QAction("Save &As...", parent=self)
        self.actionFileSaveAs.setShortcut(QKeySequence("Ctrl+Shift+s"))
        self.actionFileSaveAs.setStatusTip("Save the file with a name you specify")
        self.actionFileSaveAs.setToolTip("Save the current file")
        self.actionFileSaveAs.triggered.connect(self.onFileSaveAsClicked)

        self.actionFileExit = QAction("E&xit", parent=self)
        self.actionFileExit.setStatusTip("Quit the program")
        self.actionFileExit.triggered.connect(self.onFileExitClicked)
        # endregion

        # region: build the menu
        self.menuMain = self.menuBar()
        self.menuFile = self.menuMain.addMenu("&File")
        self.menuFile.addAction(self.actionFileOpen)
        self.menuFile.addAction(self.actionFileSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionFileExit)
        # endregion

        # region: build status bar
        self.statusbar = self.statusBar()
        # endregion

        # region: build toolbar
        self.toolbarMain = QToolBar("Main Toolbar", parent=self)
        self.addToolBar(self.toolbarMain)
        self.toolbarMain.addAction(self.actionFileOpen)
        self.toolbarMain.addAction(self.actionFileSaveAs)
        self.toolbarMain.addAction(self.actionFileExit)
        # endregion

    def onFileOpenClicked(self):
        if sys.platform.startswith("win32"):
            # we're on windows
            initial_directory = Path.home() / "Documents"
        else:
            # we're on a unix-like os
            initial_directory = Path.home()

        filePath = QFileDialog().getOpenFileName(
            directory=str(initial_directory),
            filter="Text files (*.txt);;Python Source files (*.py);;All file types (*.*)",
            parent=self,
        )[0]

        if filePath:
            self.pathLabel.setText(filePath)
            # open the file, read its contents into a str, set the text of the
            # QPlainTextEdit widget to that str
            # reverse the process for Save As

    def onFileSaveAsClicked(self):
        self.pathLabel.setText("You clicked Save As...")

    def onFileExitClicked(self):
        QApplication.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileOpenDialogDemo()
    window.show()
    sys.exit(app.exec())
