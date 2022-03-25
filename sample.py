# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sample.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(540, 300)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit = QtWidgets.QTextEdit(Frame)
        self.textEdit.setGeometry(QtCore.QRect(140, 20, 261, 241))
        self.textEdit.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayoutWidget = QtWidgets.QWidget(Frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 21))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(310, 270, 80, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Frame)
        self.pushButton.clicked.connect(self.textEdit.clear)
        self.textEdit.customContextMenuRequested['QPoint'].connect(self.right_click)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.textEdit.setHtml(_translate("Frame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is the Contract</p></body></html>"))
        self.pushButton.setText(_translate("Frame", "Change"))

    def right_click(self):
        self.textEdit.copy() 
    

        menu_window=QtWidgets.QMainWindow()
        top_bar = QtWidgets.QMainWindow.menuBar(menu_window)
        menu =top_bar.addMenu("Choose an Object")
        object1 = menu.addAction("Object1")
        object2 = menu.addAction("Object2")
        object3 = menu.addAction("Object3")

        # top_menu = QMenu(self.parent)

        # menu = top_menu.addMenu("Menu")
        # config = menu.addMenu("Configuration ...")

        # _load = config.addAction("&Load ...")
        # _save = config.addAction("&Save ...")

        # config.addSeparator()

        # config1 = config.addAction("Config1")
        # config2 = config.addAction("Config2")
        # config3 = config.addAction("Config3")

        action = menu.exec_(QtGui.QCursor.pos())

        if action == object1:
            cb=clipboard.text()
            clipboard.clear()
            print(cb)
            
        elif action == object2:
            print("Object2")
            pass
        elif action == object3:
            print("Object3")
            pass
       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    clipboard=app.clipboard()
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())

