from PyQt5 import QtGui, QtWidgets
from app.ui.base.mainwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # build ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
