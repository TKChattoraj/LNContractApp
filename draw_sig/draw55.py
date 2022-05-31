
import sys
from PyQt6 import uic
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class Canvas(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.GlobalColor.white)
        self.setAutoFillBackground(True)
        self.setPalette(p)
        self.myPixmap = QPixmap(200,200)
        self.setMinimumSize(200,200)
        self.painter = QPainter(self.myPixmap)
        self.pen = QPen(Qt.GlobalColor.black)
        self.painter.setPen(self.pen)
        self.painter.fillRect(0,0,200,200, Qt.GlobalColor.white)
        self.setPixmap(self.myPixmap)
        self.last = None

    def mouseMoveEvent(self, event):
        if self.last:
            self.painter.drawLine(self.last, event.pos())

            self.last = event.pos()
            self.setPixmap(self.myPixmap)
            self.update()

    def mousePressEvent(self, event):
        self.last = event.pos()

    def mouseReleaseEvent(self, event):
        self.last = None

    def updateSize(self, width, height):
        pm = QPixmap(width, height)
        pm.fill(Qt.GlobalColor.white)
        old = self.myPixmap
        self.myPixmap = pm
        self.pen = QPen(Qt.GlobalColor.black)
        self.painter = QPainter(pm)
        self.painter.drawPixmap(0,0,old)
        self.setPixmap(pm)

    def resizeEvent(self, event):
        if event.oldSize().width() > 0:
            self.updateSize(event.size().width(), event.size().height())


app = QApplication(sys.argv)
c = Canvas()
c.show()
app.exec()  