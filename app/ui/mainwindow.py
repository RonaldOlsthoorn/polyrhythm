from PyQt5 import QtGui, QtWidgets
from app.ui.base.mainwindow import Ui_MainWindow
import  app.model.polyrhythm.polyrhythm_pb2 as polyrhythm_pb2


def parse_file(file):

    # parse input file (if provided)
    pr = polyrhythm_pb2.PolyRhythm()

    if file:
        try:
            with open(file, 'rb') as f:
                file_content = f.read()
            pr.ParseFromString(file_content)
        except IOError:
            errorMessage = "Could not open file {}".format(file)
            logging.error(errorMessage)
            raise IOError(errorMessage)
        except DecodeError:
            errorMessage = "File {} in wrong format".format(file)
            logging.error(errorMessage)   
            raise IOError(errorMessage)

    return pr


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, file):
        super(MainWindow, self).__init__()

        # build ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionNew.triggered.connect(self.newRhythm)
        self.ui.actionExit.triggered.connect(self.close)
        self.savedChanges = False

        try:
            self.model = parse_file(file)
            self.file = file
        except IOError as e:
            a = QtGui.QMessageBox.critical(None,'Error!', repr(e) , QtGui.QMessageBox.Abort)
        
        if(self.model):
            self.setupModel()

    def setupModel(model):
        pass
    
    def newRhythm(self):
        if self.savedChanges:
            pass
        else:
            self.model = polyrhythm_pb2.PolyRhythm()
            
    def closeEvent(self, event):
        if not self.savedChanges:
            event.accept()
        else:
            event.ignore()

