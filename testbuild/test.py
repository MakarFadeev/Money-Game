import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton
from interface import Ui_MainWindow

app = QApplication(sys.argv)
window=QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

ui.pushButton.clicked.connect(lambda:ui.label.setText('text2'))
window.show()
sys.exit(app.exec_())