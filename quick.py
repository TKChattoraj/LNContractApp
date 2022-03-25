from curses import BUTTON1_CLICKED
import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# os.makedirs('./counterparty')
# mac_file = open(r'./counterparty/macfile.txt', 'w')
# mac_file.write("string")
# mac_file.close()




class window(QWidget):
    def __init__(self, parent=None):
        super(window,self).__init__(parent)
        self.setGeometry(10,10,500, 200)
        self.setWindowTitle("LNContract App")
        self.label = QLabel(self)
        self.label.setText("Contract will go here.")
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.move(50,20)
        self.b1 = QPushButton(self)
        self.b1.setText("Button1")
        self.b1.move(50,50)
        self.b1.clicked.connect(self.b1_clicked)


    def b1_clicked(self):
        self.label.setText("And this one belongs to the Reds!")


def main():
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())

if __name__ =='__main__':
    main()