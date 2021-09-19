import os
from google.protobuf.message import DecodeError
import math
from PyQt5 import QtCore, QtGui, QtWidgets
from app.ui.base.mainwindow import Ui_MainWindow
from app.ui.rhythmplayerwidget import RhythmPlayerWidget, PlayState
from app.ui.editortreemodel import EditorTreeModel
import app.model.polyrhythm.polyrhythm_pb2 as polyrhythm_pb2
import app.model.model


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
    else:
        pr.bpm = 120
        pr.time_signature.num = 4
        pr.time_signature.denom = 4

    return pr


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, file):
        super(MainWindow, self).__init__()

        # build ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.leftSplitter = QtWidgets.QSplitter(
            QtCore.Qt.Orientation.Vertical, self)

        self.ui.rhythmPlayerWidget = RhythmPlayerWidget(self.ui.leftSplitter)
        self.ui.rhythmModelViewer = QtWidgets.QTreeView(self.ui.leftSplitter)
        self.ui.rhythmModelViewer.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)

        self.ui.leftSplitter.addWidget(self.ui.rhythmPlayerWidget)
        self.ui.leftSplitter.addWidget(self.ui.rhythmModelViewer)

        self.ui.leftPane.insertWidget(0, self.ui.leftSplitter)

        self.openFile(file)

        self.selection = {}
        self.savedChanges = False

        self.ui.editorTreeModel = EditorTreeModel(self.model)
        self.ui.rhythmModelViewer.setModel(self.ui.editorTreeModel)
        self.connectSignals()

    def connectSignals(self):
        self.ui.actionNew.triggered.connect(self.newPolyRhythmEvent)
        self.ui.actionOpen.triggered.connect(self.openPolyRhythmEvent)
        self.ui.actionSave.triggered.connect(self.savePolyRhythmEvent)
        self.ui.actionSave.triggered.connect(self.savePolyRhythmAsEvent)
        self.ui.actionExit.triggered.connect(self.closeEvent)
        self.ui.actionPlay.triggered.connect(self.playPolyRhythmEvent)
        self.ui.actionPlay.triggered.connect(self.pausePolyRhythmEvent)
        self.ui.actionPlay.triggered.connect(self.stopPolyRhythmEvent)
        self.ui.actionAdd_rhythm.triggered.connect(self.addPolyRhythmEvent)
        self.ui.actionDelete_rhythm.triggered.connect(
            self.deletePolyRhythmEvent)
        self.ui.actionAdd_note.triggered.connect(self.addNoteEvent)
        self.ui.actionDelete_note.triggered.connect(
            self.deleteNoteEvent)

        self.ui.polyNameText.textChanged.connect(self.polyRhythmNameChanged)
        self.ui.rhythmNameText.textChanged.connect(self.rhythmNameChanged)
        self.ui.bpmSpinner.valueChanged.connect(self.bpmChanged)
        self.ui.timeSignatureNumSpinner.valueChanged.connect(
            self.timeSignatureNumChanged)
        self.ui.timeSignatureDenomSpinner.valueChanged.connect(
            self.timeSignatureDenomChanged)
        self.ui.notePositionNumSpinner.valueChanged.connect(
            self.notePositionNumChanged)
        self.ui.notePositionDenomSpinner.valueChanged.connect(
            self.notePositionDenomChanged)
        self.ui.volumeSlider.valueChanged.connect(self.volumeChanged)

        self.ui.rhythmModelViewer.selectionModel().selectionChanged.connect(
            self.mvSelectionChanged)

        self.ui.openMidiButton.clicked.connect(self.selectMidiFile)

    def setupModel(model):
        pass

    def newPolyRhythmEvent(self):
        if self.savedChanges:
            pass
        else:
            self.model = polyrhythm_pb2.PolyRhythm()

    def openPolyRhythmEvent(self):
        if self.savedChanges:
            pass
        else:
            file, _ = QtWidgets.QFileDialog.getOpenFileName(
                self, "Save File",
                os.path.expanduser("~"), "Polyrhythm (*.pr)")
            if file:
                self.openFile(file)
                self.onModelUpdate()

    def savePolyRhythmEvent(self):
        if self.savedChanges:
            with open(self.file, "wb") as f:
                f.write(self.model.__pb__().SerializeToString())
            self.savedChanges = False

    def savePolyRhythmAsEvent(self):
        path = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save File", os.path.expanduser("~"), "Polyrhythm (*.pr)")

    def closeEvent(self, event):
        if not self.savedChanges:
            event.accept()
        else:
            event.ignore()

    def playPolyRhythmEvent(self, event):
        pass

    def pausePolyRhythmEvent(self, event):
        pass

    def stopPolyRhythmEvent(self, event):
        pass

    def addPolyRhythmEvent(self, event):
        pass

    def deletePolyRhythmEvent(self, event):
        pass

    def addNoteEvent(self, event):
        rhythmPosition = app.model.model.RhythmPosition(0, self.model.time_signature[1])

        viewPosition = QtCore.QPointF(
            0, -self.ui.rhythmPlayerWidget.baselineGuiProps.radius)

        note = app.model.model.ViewNote(
            rhythmPosition, .5, viewPosition,
            self.ui.rhythmPlayerWidget.baselineGuiProps.noteRadius * 1.5)
        self.selection["rhythm"].notes.append(note)
        self.ui.rhythmModelViewer.model().layoutChanged.emit()
        self.updateVisualPane()

    def deleteNoteEvent(self, event):
        self.selection["rhythm"].notes.remove(self.selection["note"])
        self.ui.rhythmModelViewer.model().layoutChanged.emit()
        self.updateVisualPane()

    def openFile(self, file):
        try:
            pb_model = parse_file(file)
            self.model = app.model.model.ViewPolyRhythm(
                pb_model,
                self.ui.rhythmPlayerWidget.baselineGuiProps)
            self.selection = {"rhythm": None, "note": None}
            self.file = file
        except IOError as e:
            a = QtGui.QMessageBox.critical(
                None, 'Error!', repr(e), QtGui.QMessageBox.Abort)
            return

        if(self.model):
            self.setupModel()

    def onModelUpdate(self):
        self.ui.rhythmModelViewer.model().polyRhythm = self.model
        self.ui.rhythmModelViewer.model().layoutChanged.emit()
        self.updateEditorpane()
        self.updateVisualPane()

    def mvSelectionChanged(self, newSelection, oldSelection):
        node = newSelection.indexes()[0].internalPointer()
        if type(node) == app.model.model.ViewRhythm:
            self.selection["rhythm"] =\
                newSelection.indexes()[0].internalPointer()
            self.selection["note"] = None
        elif type(node) == app.model.model.ViewNote:
            self.selection["rhythm"] =\
                newSelection.indexes()[0].parent().internalPointer()
            self.selection["note"] =\
                newSelection.indexes()[0].internalPointer()
        self.updateEditorpane()

        self.ui.actionAdd_note.setEnabled(
            True if self.selection["rhythm"] else False)
        self.ui.actionDelete_note.setEnabled(
            True if self.selection["note"] else False)

    def selectMidiFile(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(
                self, "Open File",
                os.path.expanduser("~"), "Midi (*.midi)")
        if file:
            self.selection["rhythm"].sound_path = file
            self.updateEditorpane()

    def polyRhythmNameChanged(self, text):
        self.model.name = text

    def rhythmNameChanged(self, text):
        self.selection["rhythm"].name = text
        self.ui.rhythmModelViewer.model().layoutChanged.emit()

    def bpmChanged(self, value):
        self.model.bpm = value

    def timeSignatureNumChanged(self, value):
        self.model.time_signature = (value, self.model.time_signature[1])
        self.model.updateDrawArea(self.ui.rhythmPlayerWidget.baselineGuiProps)
        self.ui.rhythmModelViewer.model().layoutChanged.emit()
        self.updateVisualPane()

    def timeSignatureDenomChanged(self, value):
        self.model.time_signature = (self.model.time_signature[0], value)
        self.model.updateDrawArea(self.ui.rhythmPlayerWidget.baselineGuiProps)
        self.ui.rhythmModelViewer.model().layoutChanged.emit()
        self.updateVisualPane()

    def notePositionNumChanged(self, value):
        self.selection["note"].position.representation =\
            (value, self.selection["note"].position.representation[1])
        self.model.updateDrawArea(self.ui.rhythmPlayerWidget.baselineGuiProps)
        self.ui.rhythmModelViewer.model().layoutChanged.emit()
        self.updateVisualPane()

    def notePositionDenomChanged(self, value):
        self.selection["note"].position.representation =\
            (self.selection["note"].position.representation[0], value)
        self.model.updateDrawArea(self.ui.rhythmPlayerWidget.baselineGuiProps)
        self.ui.rhythmModelViewer.model().layoutChanged.emit()
        self.updateVisualPane()

    def volumeChanged(self, value):
        self.selection["note"].volume = value / 100
        self.ui.rhythmModelViewer.model().layoutChanged.emit()

    def updateGuiElement(self, element, value, enabled=True):
        element.blockSignals(True)
        if(type(element) == QtWidgets.QLineEdit):
            element.setText(value)
        else:
            element.setValue(value)
        element.blockSignals(False)
        element.setEnabled(enabled)

    def updateEditorpane(self):
        self.updateGuiElement(self.ui.polyNameText, self.model.name)
        self.updateGuiElement(
            self.ui.timeSignatureNumSpinner, self.model.time_signature[0])
        self.updateGuiElement(
            self.ui.timeSignatureDenomSpinner, self.model.time_signature[1])

        if self.selection["rhythm"]:
            self.updateGuiElement(
                self.ui.midiPathText,
                self.selection["rhythm"].sound_path)

        if self.selection["note"]:
            self.updateGuiElement(
                self.ui.notePositionNumSpinner,
                self.selection["note"].position.representation[0])
            self.updateGuiElement(
                self.ui.notePositionDenomSpinner,
                self.selection["note"].position.representation[1])
            self.updateGuiElement(
                self.ui.volumeSlider,
                math.floor(self.selection["note"].volume * 100))
        else:
            self.updateGuiElement(self.ui.notePositionNumSpinner, 0, False)
            self.updateGuiElement(self.ui.notePositionDenomSpinner, 1, False)
            self.updateGuiElement(self.ui.volumeSlider, 50, False)

    def updateVisualPane(self):
        self.ui.rhythmPlayerWidget.changeModel(self.model)
