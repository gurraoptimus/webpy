from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngine import *


class MyWebBrowser(QMainWindow):
   
    def __init__(self, *args, **kwargs):
        super(MyWebBrowser, self).__init__(*args, **kwargs)

        self.window = QWidget()
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
        self.forward_btn.setMaximumHeight(30)

        self.horizontal.addWindget(self.url_bar)
        self.horizontal.addWindget(self.go_btn)
        self.horizontal.addWindget(self.back_btn)
        self.horizontal.addWindget(self.forward_btn)
        
        self.browser = QtWebEngineView()

        self.layout.addLayout(self.horizontal)
        self.addWindget(self.browser)

        self.browser.setUrl(QUrl(""))

        self.window.setLayout(self.layout)
        self.window.show()

app = QApplication([])
window = MyWebBrowser()
app.exec_()