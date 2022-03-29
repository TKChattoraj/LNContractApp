import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QCursor
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QMenu

from QtContractParent import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.contractView.customContextMenuRequested['QPoint'].connect(self.contract_view_right_click)

    def contract_view_right_click(self):
        self.contractView.copy() 
    
        menu_window=QMainWindow()
        top_bar = QMainWindow.menuBar(menu_window)
        menu =top_bar.addMenu("&Choose an Object")
        object1 = menu.addAction("Object1")
        object2 = menu.addAction("Object2")
        object3 = menu.addAction("Object3")
        
        sub_menu= menu.addMenu("Submenu")
        object4 = sub_menu.addAction("Object4")

        # top_menu = QMenu(self.parent)

        # menu = top_menu.addMenu("Menu")
        # config = menu.addMenu("Configuration ...")

        # _load = config.addAction("&Load ...")
        # _save = config.addAction("&Save ...")

        # config.addSeparator()

        # config1 = config.addAction("Config1")
        # config2 = config.addAction("Config2")
        # config3 = config.addAction("Config3")

        action = menu.exec(QCursor.pos())

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
        elif action == object4:
            cb=clipboard.text()
            clipboard.clear()
            print(cb)
            pass
    

app = QApplication(sys.argv)
clipboard=app.clipboard()
window = MainWindow()
window.show()
app.exec()  