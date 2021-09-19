import os
import math
from PyQt5 import QtCore, QtGui
import app.model.model as model


class EditorTreeModel(QtCore.QAbstractItemModel):

    CHILD_METHODS = {
        model.ViewPolyRhythm:
        lambda polyrhythm, row: polyrhythm.rhythms[row],
        model.ViewRhythm:
        lambda rhythm, row: rhythm.notes[row],
        model.ViewNote:
        lambda note, row: None}

    ROW_COUNT_METHODS = {
        model.ViewPolyRhythm: lambda polyrhythm: len(polyrhythm.rhythms),
        model.ViewRhythm: lambda rhythm: len(rhythm.notes),
        model.ViewNote: lambda note: 0}

    COLUMN_COUNT_METHODS = {
        model.ViewPolyRhythm: lambda polyrhythm: 0,
        model.ViewRhythm: lambda rhythm: 2,
        model.ViewNote: lambda note: 4}

    def __init__(self, model=None):
        super(EditorTreeModel, self).__init__()
        self.polyRhythm = model

    def nodeFromIndex(self, index):
        if index.isValid():
            return index.internalPointer()
        else:
            return self.polyRhythm

    def data(self, index, role):
        if not index.isValid():
            return QVariant()

        node = self.nodeFromIndex(index)

        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if type(node) == model.ViewRhythm:
                if index.column() == 0:
                    return QtCore.QVariant(node.name)
                else:
                    return QtCore.QVariant()
            elif type(node) == model.ViewNote:
                if index.column() == 0:
                    return QtCore.QVariant("Note {}".format(index.row()))
                elif index.column() == 1:
                    return QtCore.QVariant()
                elif index.column() == 2:
                    return QtCore.QVariant(
                        "{} / {}".format(
                            node.position.representation[0],
                            node.position.representation[1]))
                elif index.column() == 3:
                    return QtCore.QVariant(
                        "{}%".format(math.floor(node.volume * 100)))

        elif role == QtCore.Qt.ItemDataRole.BackgroundColorRole:
            if type(node) == model.ViewRhythm and index.column() == 1:
                return QtGui.QColor(
                    node.color[0],
                    node.color[1],
                    node.color[2])
            return QtCore.QVariant()
        return QtCore.QVariant()

    def headerData(self, section, orientation, role):
        if orientation != QtCore.Qt.Orientation.Horizontal or\
           role != QtCore.Qt.ItemDataRole.DisplayRole:
            return QtCore.QVariant()
        if section == 0:
            return QtCore.QVariant("Name")
        elif section == 1:
            return QtCore.QVariant("Color")
        elif section == 2:
            return QtCore.QVariant("Position")
        elif section == 3:
            return QtCore.QVariant("Volume")

    def index(self, row, column, parent):

        if (not self.polyRhythm or row < 0 or column < 0):
            return QModelIndex()

        parentNode = self.nodeFromIndex(parent)
        childNode = self.CHILD_METHODS[type(parentNode)](parentNode, row)

        if (not childNode):
            return QModelIndex()

        return self.createIndex(row, column, childNode)

    def parent(self, index):
        node = self.nodeFromIndex(index)

        if(type(node) == model.ViewNote):
            for i, rhythm in enumerate(self.polyRhythm.rhythms):
                for note in rhythm.notes:
                    if note == node:
                        return self.createIndex(i, 0, rhythm)

        return QtCore.QModelIndex()

    def rowCount(self, parent):
        if parent.column() > 0:
            return 0
        else:
            node = self.nodeFromIndex(parent)
            if not node:
                return 0
            else:
                return self.ROW_COUNT_METHODS[type(node)](node)

    def columnCount(self, parent):
        return 4
