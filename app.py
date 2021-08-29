from app.ui.mainwindow import MainWindow
import app.model.polyrhythm.polyrhythm_pb2 as polyrhythm_pb2
import argparse
from google.protobuf.message import DecodeError
import logging
from PyQt5.QtWidgets import QApplication


def main(file):

    app = QApplication([])
    window = MainWindow(file)
    window.show()
    app.exec()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs='?', default='')
    args = parser.parse_args()

    main(args.file)