# From:
# https://codingshiksha.com/python/python-3-pyqt5-script-to-draw-over-image-canvas-with-mouse-and-drawing-pen-gui-desktop-app-full-project-for-beginners/



import sys
from PyQt6.QtCore import Qt, QPoint, QRect
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QMenuBar, QMenu
from PyQt6.QtGui import QPixmap, QPainter, QPen, QPainterPath, QAction


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(0,0, 300, 300 )

        # self.menu_file=self.menuBar().addMenu('file')
        # self.menu_file_open=self.menu_file.addAction('open')
        # self.menu_file_save=self.menu_file.addAction('save')
        
        self.menubar = QMenuBar(self)
        self.FileMenu = QMenu("File")
        self.OpenAction=QAction("Open", self)
        self.SaveAction=QAction("Save", self)
        self.OpenAction.triggered.connect(self.open_triggered)
        self.SaveAction.triggered.connect(self.save_triggered)
        self.FileMenu.addAction(self.OpenAction)
        self.FileMenu.addAction(self.SaveAction)
        self.menubar.addMenu(self.FileMenu)
        self.setMenuBar(self.menubar)
        

        self.label = QLabel("Sign Here")
        self.setCentralWidget(self.label)
        self.drawing = False
        self.lastPoint = QPoint()
        
        self.current_point = QPoint()
        self.image = QPixmap(300,300)
        self.label.setPixmap(self.image)
        
        
        #self.resize(self.image.width(), self.image.height())
        self.show()

    def save_triggered(self):   
        self.label.pixmap().save("./pix.png", "PNG")
        print("Saved!")

    def open_triggered(self):
        self.painter.end()
        self.image=QPixmap("pix.png", "PNG")
        self.label.setPixmap(self.image)
        self.painter.begin(self)
        print("Opened!")

    def paintEvent(self, event):        
        self.painter = QPainter(self.image) 
        #self.painter.drawPixmap(self.rect(), self.label.pixmap())
        self.painter.begin(self)
        self.painter.setPen(QPen(Qt.GlobalColor.white, 3, Qt.PenStyle.SolidLine))
        #self.painter.end()

    def drawTo(self):
        #self.painter.begin(self)
        self.painter.drawLines(self.lastPoint, self.current_point)
        self.painter.end()
        self.lastPoint = self.current_point
        self.label.setPixmap(self.image)
        
        
    def mousePressEvent(self, event):
        print("Enter mousePressEvent")
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
            return
            
    def mouseMoveEvent(self, event):
        
        if event.buttons() and Qt.MouseButton.LeftButton and self.drawing:
            self.current_point=event.pos()
            self.drawTo()
            self.update()
       
    def mouseReleaseEvent(self, event):
        if event.button == Qt.MouseButton.LeftButton:
            self.drawing = False
            self.lastPoint= None
            
          



app = QApplication(sys.argv)
mainWindow = MainWindow()
#mainMenu.show()
sys.exit(app.exec())



# import sys
# from PyQt6 import QtCore, QtGui, QtWidgets, uic
# from PyQt6.QtCore import Qt, QPoint, QPointF


# class MainWindow(QtWidgets.QMainWindow):

#     def __init__(self):
#         super().__init__()

#         self.label = QtWidgets.QLabel()
#         self.canvas = QtGui.QPixmap(400, 300)
#         self.label.setPixmap(self.canvas)
#         print("pixmap")
#         print(self.label.pixmap())
        
#         self.setCentralWidget(self.label)

#         self.last_x, self.last_y = None, None

#     def mouseMoveEvent(self, e):
#         if self.last_x is None: # First event.
#             self.last_x = e.position().x()
#             print("type:")
#             print(type(self.last_x))
#             self.last_y = e.position().y()
#             self.last_p = QPointF(self.last_x, self.last_y)
#             print("point1")
#             print(self.last_p)
#             self.update()
#             return # Ignore the first time.
#         print("line 107")
#         print("pixmap")
#         print(self.label.pixmap())
#         painter = QtGui.QPainter(self.canvas)
#         pen = QtGui.QPen(Qt.GlobalColor.white)
#         painter.setPen(pen)
#         print("painter")
#         print(painter)
#         print("device")
#         #print(painter.device())
#         print("line 109")
#         point = QPointF(e.position().x(), e.position().y())
#         print("point2")
#         print(point)
#         print("line111")
#         painter.drawLine(self.last_p, point)

#         print("line 112")
        
#         print("line 114")
#         painter.end()
#         self.label.setPixmap(self.canvas)
#         self.update()
#         # Update the origin for next time.
#         self.last_x = e.position().x()
#         self.last_y = e.position().y()
#         self.last_p = QPointF(self.last_x, self.last_y)

#     def mouseReleaseEvent(self, e):
#         self.last_x = None
#         self.last_y = None


# app = QtWidgets.QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()
