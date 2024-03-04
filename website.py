from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qtcore import *
from PyQt5.QtWebEngine import *


class MyWebBrowser(QMainWindow):
   
    def __init__(self, *args, **kwargs):
        super(MyWebBrowser, self).__init__(*args, **kwargs)

        self.window = QWidgets()
        self.window.setWindowTitle("webpy Web Browser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximunHeight(30)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMaximunHeight(30)

        self.back_btn = QPushButton("<")
        self.back_btn.setMaximunHeight(30)

        self.forward_btn = QPushButton(">")
        self.forward_btn.setMaximunHeight(30)

        self.