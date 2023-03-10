#!/usr/bin/env python3

# icons by p.yusukekamiyamane (https://p.yusukekamiyamane.com/)
# and used under CC BY 3.0 (https://creativecommons.org/licenses/by/3.0/)

# noqa
# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,invalid-name,eval-used,broad-exception-caught,attribute-defined-outside-init,too-many-instance-attributes

import sys
from pathlib import Path

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPlainTextEdit,
    QPushButton,
    QSpinBox,
    QStatusBar,
    QToolBar,
    QVBoxLayout,
    QWidget,
)


class CaesarView(QMainWindow):
    FILE_FILTERS = ["Text files (*.txt)", "Comma Separated Values (*.csv)"]

    def __init__(self) -> None:
        super().__init__()

        self.initActions()
        self.initUI()
        self.model = CaesarModel()

    def initActions(self):
        print(Path(__file__).parent)
        basedir = Path(__file__).parent
        print(basedir)

        self.actionFileOpen = QAction(QIcon("icons/open-document-text.png"), "&Open...", self)
        self.actionFileOpen.setShortcut(QKeySequence("Ctrl+o"))
        self.actionFileOpen.setStatusTip("Open file...")
        self.actionFileOpen.triggered.connect(self.onFileOpenClick)

        self.actionFileSaveAs = QAction(QIcon("icons/disk.png"), "Save &As...", self)
        self.actionFileSaveAs.setShortcut(QKeySequence("Ctrl+Shift+s"))
        self.actionFileSaveAs.setStatusTip("Save file...")
        self.actionFileSaveAs.triggered.connect(self.onFileSaveAsClick)

        self.actionExit = QAction("E&xit", self)
        self.actionExit.triggered.connect(self.onFileExitClick)

        self.actionEncrypt = QAction(QIcon("icons/minus-button.png"), "&Encrypt", self)
        self.actionEncrypt.setShortcut(QKeySequence("Ctrl+e"))
        self.actionEncrypt.setStatusTip("Encrypt file")
        self.actionEncrypt.triggered.connect(self.onEncryptClick)

        self.actionDecrypt = QAction(QIcon("icons/plus-button.png"), "&Decrypt", self)
        self.actionDecrypt.setShortcut(QKeySequence("Ctrl+d"))
        self.actionDecrypt.setStatusTip("Decrypt file")
        self.actionDecrypt.triggered.connect(self.onDecryptClick)

        self.actionClear = QAction("Clear", self)
        # self.actionClear.setShortcut(QKeySequence("Alt+Delete"))
        self.actionClear.triggered.connect(self.onClearClick)

    def initUI(self):
        self.setWindowTitle("Caesar Cipher")
        self.setFixedSize(700, 550)
        self.setStyleSheet("font-size: 16px;")

        self.appIcon = QIcon()
        self.appIcon.addFile("icons/lock-16x16.png", QSize(16, 16))
        self.appIcon.addFile("icons/lock-24x24.png", QSize(24, 24))
        self.appIcon.addFile("icons/lock-32x32.png", QSize(32, 32))
        self.appIcon.addFile("icons/lock-32x32.png", QSize(256, 256))
        self.setWindowIcon(self.appIcon)

        self.vbox = QVBoxLayout()
        centralWidget = QWidget()
        centralWidget.setLayout(self.vbox)
        self.setCentralWidget(centralWidget)

        # build menu
        self.menu = self.menuBar()
        self.fileMenu = self.menu.addMenu("&File")
        self.fileMenu.addAction(self.actionFileOpen)
        self.fileMenu.addAction(self.actionFileSaveAs)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.actionEncrypt)
        self.fileMenu.addAction(self.actionDecrypt)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.actionExit)

        # build toolbar
        self.toolbarMain = QToolBar("Main Toolbar", parent=self)
        self.addToolBar(self.toolbarMain)
        self.toolbarMain.addAction(self.actionFileOpen)
        self.toolbarMain.addAction(self.actionFileSaveAs)
        self.toolbarMain.addAction(self.actionEncrypt)
        self.toolbarMain.addAction(self.actionDecrypt)

        # build status bar
        self.setStatusBar(QStatusBar(self))

        # build controls
        self.plainTextEdit = QPlainTextEdit(parent=self)
        self.plainTextEdit.textChanged.connect(self.onTextChanged)

        ## add clear action (and its keyboard shortcut) to WIDGET to enable it (the custom context menu and its clear
        ## entry exist ONLY while the menu is being displayed)
        ## https://stackoverflow.com/questions/74916829/how-to-activate-shortcut-key-in-context-menu-in-pyqt5
        self.plainTextEdit.addAction(self.actionClear)

        ## create custom context menu
        self.plainTextEdit.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.plainTextEdit.customContextMenuRequested.connect(self.plainTextEditCustomContextMenu)

        self.vbox.addWidget(self.plainTextEdit)

        self.controlsLayout = QHBoxLayout()
        self.controlsLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.encryptButton = QPushButton("&Encrypt", parent=self)
        self.encryptButton.setFixedSize(100, 55)
        self.encryptButton.clicked.connect(self.actionEncrypt.trigger)
        self.decryptButton = QPushButton("&Decrypt", parent=self)
        self.decryptButton.setFixedSize(100, 55)
        self.decryptButton.clicked.connect(self.actionDecrypt.trigger)

        self.controlsLayout.addWidget(self.encryptButton)
        self.controlsLayout.addWidget(self.decryptButton)

        self.rotationsLabel = QLabel("Rotation:", parent=self)
        self.rotationsLabel.setStyleSheet("margin-left:30")
        self.rotationsSpinBox = QSpinBox(parent=self)
        self.rotationsSpinBox.setMinimum(1)
        self.rotationsSpinBox.setMaximum(26)
        self.rotationsSpinBox.setValue(13)

        self.controlsLayout.addWidget(self.rotationsLabel)
        self.controlsLayout.addWidget(self.rotationsSpinBox)

        self.vbox.addLayout(self.controlsLayout)

    def plainTextEditCustomContextMenu(self, point):
        self.customContextMenu = self.plainTextEdit.createStandardContextMenu()
        self.customContextMenu.addSeparator()
        self.customContextMenu.addAction(self.actionClear)
        if len(self.plainTextEdit.toPlainText()) == 0:
            self.actionClear.setEnabled(False)
        else:
            self.actionClear.setEnabled(True)
        self.customContextMenu.exec(self.mapToGlobal(point))

    def onClearClick(self):
        self.plainTextEdit.clear()

    def onDecryptClick(self):
        LETTER_COUNT = 26
        rotations = LETTER_COUNT - self.rotationsSpinBox.value()
        ciphertext = self.plainTextEdit.toPlainText()

        self.model.plainText = ""
        for _, char in enumerate(ciphertext):
            if char.isupper():
                self.model.plainText += chr(
                    (ord(char) + rotations - ord("A")) % LETTER_COUNT + ord("A")
                )
            elif char.islower():
                self.model.plainText += chr(
                    (ord(char) + rotations - ord("a")) % LETTER_COUNT + ord("a")
                )
            else:
                self.model.plainText += char

        self.plainTextEdit.clear()
        self.plainTextEdit.setPlainText(self.model.plainText)

    def onEncryptClick(self):
        rotations = self.rotationsSpinBox.value()
        plaintext = self.model.text

        self.model.cipherText = ""
        for _, char in enumerate(plaintext):
            if char.isupper():
                self.model.cipherText += chr((ord(char) + rotations - ord("A")) % 26 + ord("A"))
            elif char.islower():
                self.model.cipherText += chr((ord(char) + rotations - ord("a")) % 26 + ord("a"))
            else:
                self.model.cipherText += char

        self.plainTextEdit.clear()
        self.plainTextEdit.setPlainText(self.model.cipherText)

    def onFileExitClick(self):
        QApplication.quit()

    def onFileOpenClick(self):
        filePath = QFileDialog().getOpenFileName(
            self, "Open", directory=str(Path.home()), filter="Text files (*.txt)"
        )[0]
        # openDlg = QFileDialog(parent=self)
        # filePath = openDlg.getOpenFileName(
        #     self, "Open", directory=str(Path.home()), filter="Text files (*.txt)"
        # )[0]

        if filePath:
            with open(filePath, mode="r", encoding="utf-8") as inputFile:
                text = inputFile.read()
            self.plainTextEdit.setPlainText(text)

    def onFileSaveAsClick(self):
        saveDlg = QFileDialog(parent=self)
        filePath = saveDlg.getSaveFileName(
            self, "Save As", directory=str(Path.home()), filter="Text files (*.txt)"
        )[0]

        if filePath:
            if not filePath.endswith(".txt"):
                filePath += ".txt"
            with open(filePath, mode="w", encoding="utf-8") as outputFile:
                outputFile.write(self.plainTextEdit.toPlainText())

    def onTextChanged(self):
        self.model.text = self.plainTextEdit.toPlainText()


class CaesarModel:
    def __init__(self) -> None:
        self.__text: str = ""
        self.__plainText: str = ""
        self.__cipherText: str = ""

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, newText):
        self.__text = newText

    @property
    def plainText(self):
        return self.__plainText

    @plainText.setter
    def plainText(self, newText):
        self.__plainText = newText

    @property
    def cipherText(self):
        return self.__cipherText

    @cipherText.setter
    def cipherText(self, newText):
        self.__cipherText = newText


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CaesarView()
    window.show()
    sys.exit(app.exec())
