from app.ui.mainwindow import MainWindow
import argparse
import logging
from PyQt5.QtWidgets import QApplication
import sys


def main(file):

    sys._excepthook = sys.excepthook

    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)

    sys.excepthook = exception_hook

    app = QApplication([])
    window = MainWindow(file)
    window.show()
    app.exec()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs='?', default='')
    args = parser.parse_args()

    main(args.file)
