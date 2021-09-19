import app.model.polyrhythm.polyrhythm_pb2 as polyrhythm_pb2
import math
from PyQt5 import QtCore, QtGui


class DrawAreaProperties:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.midRadius = max(5, math.floor(min(height, width) / 50))
        self.noteRadius = max(3, math.floor(min(height, width) / 100))
        self.radius = math.floor(min(height, width) / 2.5)


class RhythmPosition:

    def __init__(self, num, denom):
        self.representation = (num, denom)
        self.value = num / denom


class Note:

    def __init__(self, position, volume):
        self.position = position
        self.volume = volume

    def __pb__(self):
        pr_note = polyrhythm_pb2.Note()
        pr_note.position.value = self.position
        pr_note.volume = self.volume


class Rhythm:

    def __init__(self, name, sound_path, color):
        self.name = name
        self.sound_path = sound_path
        self.color = color
        self.notes = []

    def __pb__(self, pr_rhythm):
        pr_rhythm.name = self.name
        pr_rhythm.sound_path = self.sound_path
        pr_rhythm.color.r = self.color[0]
        pr_rhythm.color.g = self.color[1]
        pr_rhythm.color.b = self.color[2]

        for note in self.notes:
            note.__pb__(pr_rhythm.notes.add())


class PolyRhythm:

    def __init__(self, name, bpm, time_signature):
        self.name = name
        self.bpm = bpm
        self.time_signature = time_signature
        self.period = self.time_signature[0] * (60.0 / self.bpm)
        self.rhythms = []


class ViewNote(Note):

    def __init__(self, position, volume, viewPosition, viewRadius):
        super(ViewNote, self).__init__(position, volume)
        self.viewPosition = viewPosition
        self.viewRadius = viewRadius


class ViewRhythm(Rhythm):

    def __init__(self, name, sound_path, color, viewColor):
        super(ViewRhythm, self).__init__(name, sound_path, color)
        self.viewColor = viewColor


class ViewPolyRhythm(PolyRhythm):

    def __init__(self, pr_pb2, drawAreaProperties):
        super(ViewPolyRhythm, self).__init__(
            pr_pb2.name,
            pr_pb2.bpm,
            (pr_pb2.time_signature.num, pr_pb2.time_signature.denom))

        for pb_rhythm in pr_pb2.rhythms:
            color = (
                pb_rhythm.color.r,
                pb_rhythm.color.g,
                pb_rhythm.color.b)

            viewColor = QtGui.QColor(
                pb_rhythm.color.r,
                pb_rhythm.color.g,
                pb_rhythm.color.b)

            rhythm = ViewRhythm(pb_rhythm.name, pb_rhythm.sound_path,
                                color, viewColor)

            for pb_note in pb_rhythm.notes:

                p = pb_note.position.representation.num /\
                     pb_note.position.representation.denom

                viewPosition = QtCore.QPointF(
                    drawAreaProperties.radius * math.sin(
                        2 * math.pi * p /
                        (self.time_signature[0] / self.time_signature[1])),
                    -drawAreaProperties.radius * math.cos(
                        2 * math.pi * p /
                        (self.time_signature[0] / self.time_signature[1])))

                rhythmPosition = RhythmPosition(
                    pb_note.position.representation.num,
                    pb_note.position.representation.denom)

                note = ViewNote(
                    rhythmPosition,
                    pb_note.volume,
                    viewPosition,
                    drawAreaProperties.noteRadius * (1 + pb_note.volume))
                rhythm.notes.append(note)

            self.rhythms.append(rhythm)

    def updateDrawArea(self, drawAreaProperties):

        for rhythm in self.rhythms:
            for note in rhythm.notes:
                note.viewPosition = QtCore.QPointF(
                        drawAreaProperties.radius * math.sin(2 * math.pi *
                        (note.position.representation[0] / note.position.representation[1]) /
                            (self.time_signature[0] / self.time_signature[1])),
                        -drawAreaProperties.radius * math.cos(2 * math.pi *
                        (note.position.representation[0] / note.position.representation[1]) /
                            (self.time_signature[0] / self.time_signature[1]))
                    )
                note.viewRadius = drawAreaProperties.noteRadius * (1 + note.volume)
