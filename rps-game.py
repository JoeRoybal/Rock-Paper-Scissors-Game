import sys
from PyQt5.QtWidgets import *


class Window (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Paper Scissors Game")
        self.setGeometry(350, 150, 1000, 500)
        self.UI()

    def UI(self):
        self.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
