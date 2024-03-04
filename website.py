from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qtcore import *
from PyQt5.QtWebEngine import *


class MyWebBrowser(QMainWindow):
   
    def __init__(self, *args, **kwargs):
        super(MyWebBrowser, self).__init__(*args, **kwargs)

        self.window = QtWidgets()
        self.window.setWindowTitle("webpy Web Browser")