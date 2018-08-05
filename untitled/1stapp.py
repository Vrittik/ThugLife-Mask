import sys
from PyQt5 import QtWidgets

def window():
    app=QtWidgets.QApplication(sys.argv)
    w=QtWidgets.QWidget()
    w.setWindowTitle("Google")
    l1=QtWidgets.QLabel(w)
    l1.setText("Hello hi")
    l1.move(100,30)
    w.show()
    sys.exit(app.exec_())

window()