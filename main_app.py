# main_app.py

import sys
from PyQt5 import QtWidgets

from main_window import MainWindow # Still imports MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
