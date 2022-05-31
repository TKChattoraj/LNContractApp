import sys, time
from datetime import date
from PyQt6.QtCore import Qt, QDate, QTimer
from PyQt6.QtGui import QAction, QCursor
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QMenu
from PyQt6.QtSql import QSqlDatabase, QSqlDatabase, QSqlTableModel, QSqlQuery

from QtContractParent import Ui_MainWindow
from sale_goods_form import Ui_SaleGoodsForm
from part_number_form import Ui_PartNumberForm
from db_methods import select_entities, insert_goods_table, select_pn, select_contracts, get_db_id, insert_sale_goods

from sale_goods import SaleGoodsForm
from part_number import PartNumberForm
        

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, con):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.con = con
        # self.contract_view_widget = QtWidgets()
        # self.contract_view_layout = 
        self.contractView.customContextMenuRequested['QPoint'].connect(self.contract_view_right_click)


        self.horizontalLayoutWidget_2a = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2a.setGeometry(QtCore.QRect(149, 9, 471, 541))
        self.horizontalLayoutWidget_2a.setObjectName("horizontalLayoutWidget_2")
        
        self.verticalWidget_4 = QtWidgets.QWidget(self.horizontalLayoutWidget_2)
        self.verticalWidget_4.setObjectName("verticalWidget4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalWidget_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        
        self.horizontalLayout_2.addWidget(self.verticalWidget_4)
        self.verticalWidget_4.setVisible(False)
        self.verticalWidget_3.setVisible(False)

        
        # set up the sale of goods form:
        self.sale_goods_form_widget = SaleGoodsForm(self, self.con)
        #self.verticalLayout_4.addWidget(self.sale_goods_form_widget)
        
        
        # set up the part number entry form:
        self.pn_entry_form_widget = PartNumberForm(self, self.con) 
        
        # set up the Manage Menubar actions:
        self.actionSale_of_Goods.triggered.connect(self.show_sale_of_goods_form) 
        self.actionPart_Number.triggered.connect(self.show_part_number_form)

        # set up the Contract Menubar actions
        self.actionImport.triggered.connect(self.import_)   
    
    
    def import_(self):
        self.verticalWidget_4.setVisible(False)     
        self.verticalWidget_3.setVisible(True)

    def show_sale_of_goods_form (self):
        self.verticalWidget_4.setVisible(True)
        self.sale_goods_form_widget.setVisible(True)
        self.pn_entry_form_widget.setVisible(False)
        self.verticalWidget_3.setVisible(False)

    def show_part_number_form(self):
        self.verticalWidget_4.setVisible(True)
        self.pn_entry_form_widget.setVisible(True)
        self.sale_goods_form_widget.setVisible(False)
        self.verticalWidget_3.setVisible(False)   

    def show_blank_verticalWidget_4(self):
        self.verticalWidget_4.setVisible(False)
        self.pn_entry_form_widget.setVisible(False)
        self.sale_goods_form_widget.setVisible(False)

    def show_blank_verticalWidget_3(self):
        #  Will need to likely inlcude setVisible(False for widgets contained in verticalWidget_3)
        self.verticalWidget_3.setVisible(False) 


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

        action = menu.exec(QCursor.pos())

        if action == object1:
            cb=clipboard.text()
            clipboard.clear()
            print(cb)
            
        elif action == object2:
            print("Object2")
            self.verticalWidget_3.setVisible(False)     
            self.verticalWidget_4.setVisible(True)
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
con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("lncontract_db.sqlite")

# Open the connection
if not con.open():
    print("Database Error: %s" % con.lastError().databaseText())
    sys.exit(1)
window = MainWindow(con)
window.show()
# Create the connection


app.exec()  
