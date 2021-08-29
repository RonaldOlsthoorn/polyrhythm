from PyQt5 import QtGui, QtWidgets


class RhythmPlayerWidget(QtWidgets.QOpenGLWidget):

    def __init__(self):
        super(RhythmPlayerWidget, self).__init__()

        self.labelHello = QtGui.QLabel(self)
        self.labelHello.setText("This is My Widget")

        self.layout = QtGui.QHBoxLayout(self)
        self.layout.addWidget(self.labelHello)