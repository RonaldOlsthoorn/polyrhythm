import app.model.polyrhythm.polyrhythm_pb2 as polyrhythm_pb2
import contextlib
from enum import Enum
import math
import numpy as np
from PyQt5 import QtGui, QtWidgets, QtCore
import app.model.model as viewmodel


NOTE_LENGTH_MILLISECONDS = 200
HALF_NOTE_LENGTH_MILLISECONDS = 100


class PlayState(Enum):
    NEUTRAL = 1,
    PLAYING = 2,
    PAUSED = 3


class State:

    def __init__(self, play_state=PlayState.NEUTRAL,
                 elapsed_time_ms=0, relative_time=0):
        self.play_state = play_state
        self.elapsed_time_ms = elapsed_time_ms
        self.relative_time = relative_time


class DrawingAssistant:
    MIDPOINT_PEN = QtGui.QPen()
    PERIMETER_PEN = QtGui.QPen(QtCore.Qt.PenStyle.DashLine)
    METRONOME_PEN = QtGui.QPen()
    NOTE_PEN = QtGui.QPen()

    def drawStaticObjects(self, painter, properties):

        painter.save()
        painter.translate(
            properties.width / 2, properties.height / 2)

        # Draw midpoint
        painter.setPen(self.MIDPOINT_PEN)

        painter.drawEllipse(QtCore.QPointF(),
                            properties.midRadius,
                            properties.midRadius)

        # Draw perimeter
        painter.setPen(self.PERIMETER_PEN)
        painter.drawEllipse(QtCore.QPointF(),
                            properties.radius,
                            properties.radius)

        painter.restore()

    def drawDynamicObjects(self, painter, properties, viewmodel, state):

        painter.save()
        painter.translate(
            properties.width / 2, properties.height / 2)

        # Draw metronome line
        painter.setPen(self.METRONOME_PEN)
        painter.drawLine(QtCore.QPointF(),
                         QtCore.QPointF(
                            properties.radius *
                            math.sin(state.relative_time * 2 * math.pi),
                            -properties.radius *
                            math.cos(state.relative_time * 2 * math.pi)))

        period = viewmodel.time_signature[0] / viewmodel.time_signature[1]

        # Draw notes
        for rhythm in viewmodel.rhythms:
            painter.setBrush(QtGui.QBrush(rhythm.viewColor))

            for note in rhythm.notes:
                diff = state.relative_time - (note.position.value / period)

                if diff < 0:
                    self.drawNote(painter, note, 1.0)
                elif diff < HALF_NOTE_LENGTH_MILLISECONDS:
                    scale = 1 + diff / HALF_NOTE_LENGTH_MILLISECONDS
                    self.drawNote(painter, note, scale)
                elif diff < NOTE_LENGTH_MILLISECONDS:
                    scale = 2 - diff / HALF_NOTE_LENGTH_MILLISECONDS
                    self.drawNote(painter, note, scale)

        painter.restore()

    def drawNote(self, painter, note, scale):
        painter.drawEllipse(
            note.viewPosition,
            note.viewRadius * scale,
            note.viewRadius * scale)


class RhythmPlayerWidget(QtWidgets.QWidget):

    def __init__(self, parent=None, model=None):
        super(RhythmPlayerWidget, self).__init__(parent)
        self.baselineGuiProps = viewmodel.DrawAreaProperties(
            self.height(), self.width())
        self.state = State()

        if not model:
            model = polyrhythm_pb2.PolyRhythm()
            model.bpm = 120
            model.time_signature.num = 4
            model.time_signature.denom = 4

        self.viewmodel = viewmodel.ViewPolyRhythm(
            model,
            self.baselineGuiProps)
        self.assistant = DrawingAssistant()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(15)
        self.timer.timeout.connect(self.animate)

    def updateElapsedTime(self, elapsed_time_ms):
        period = self.viewmodel.time_signature[0] / self.viewmodel.time_signature[1]
        self.state.elapsed_time_ms =\
            (self.state.elapsed_time_ms + elapsed_time_ms) %\
            math.floor(1000 * period)
        self.state.relative_time = self.state.elapsed_time_ms / \
            (1000 * period)

    def animate(self):
        self.updateElapsedTime(self.sender().interval())
        self.update()

    def paintEvent(self, event):

        with self.getPainter() as painter:
            self.assistant.drawStaticObjects(painter, self.baselineGuiProps)
            self.assistant.drawDynamicObjects(
                painter, self.baselineGuiProps, self.viewmodel, self.state)

    @contextlib.contextmanager
    def getPainter(self):
        painter = QtGui.QPainter()
        painter.begin(self)
        yield painter
        painter.end()

    def resizeEvent(self, event):
        self.baselineGuiProps = viewmodel.DrawAreaProperties(
            event.size().height(), event.size().width())
        self.viewmodel.updateDrawArea(self.baselineGuiProps)
        self.update()

    def onPlay(self):
        if self.state.play_state == PlayState.NEUTRAL:
            self.play()
        elif self.state.play_state == PlayState.PLAYING:
            pass
        else:
            self.play()

    def onPause(self):
        if self.state.play_state == PlayState.NEUTRAL:
            pass
        elif self.state.play_state == PlayState.PLAYING:
            self.pause()
        else:
            pass

    def onStop(self):
        if self.state.play_state == PlayState.NEUTRAL:
            pass
        elif self.state.play_state == PlayState.PLAYING:
            self.stop()
        else:
            self.stop()

    def play(self):
        self.state.play_state = PlayState.PLAYING
        self.timer.start()

    def pause(self):
        self.state.play_state = PlayState.PAUSED
        self.timer.stop()
        self.updateElapsedTime(self.timer.remainingTime())
        self.update()

    def stop(self):
        self.state.play_state = State()
        self.timer.stop()
        self.update()

    def changeModel(self, model):
        if model:
            self.viewmodel = model
        self.update()
