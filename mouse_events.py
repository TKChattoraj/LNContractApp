import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QCursor
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
            self.label.setText("mouseMoveEvent")
    def mousePressEvent(self, e):
            self.label.setText("mousePressEvent")
    def mouseReleaseEvent(self, e):
            self.label.setText("mouseReleaseEvent")
    def mouseDoubleClickEvent(self, e):
            self.label.setText("mouseDoubleClickEvent")

    def contextMenuEvent(self, e):
        context = QMenu(self)
        object1=context.addAction(QAction("test 1", self))
        object2=context.addAction(QAction("test 2", self))
        object3=context.addAction(QAction("test 3", self))
        #context.exec(e.globalPos())
        action=context.exec(e.globalPos())
        #action = menu.exec_(QtGui.QCursor.pos())

        if action == object1:
            print("object1")
            
        elif action == object2:
            print("Object2")
        
        elif action == object3:
            print("Object3")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()  