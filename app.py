from PyQt5.QtWidgets import QApplication
from app.ui.mainwindow import MainWindow


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()