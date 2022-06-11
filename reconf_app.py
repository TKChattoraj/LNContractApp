import sys, time
from datetime import date
from PyQt6.QtCore import Qt, QDate, QTimer
from PyQt6.QtGui import QAction, QCursor
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QMenu, QDialog, QFileDialog
from PyQt6.QtSql import QSqlDatabase, QSqlDatabase, QSqlTableModel, QSqlQuery

from reconfigured import Ui_MainWindow
from contract_view import ContractView
from sale_goods_form import Ui_SaleGoodsForm
from sale_service_form import Ui_SaleServiceForm
from part_number_form import Ui_PartNumberForm
from service_number_form import Ui_ServiceNumberForm
from entity_form import Ui_EntityForm
from contract_form import Ui_ContractForm


from db_methods import (
    insert_contract_doc,
    select_entities,
    insert_goods_table,
    select_pn,
    select_contracts,
    get_db_id,
    insert_sale_goods,
    insert_contract_doc
)

from sale_goods import SaleGoodsForm
from sale_service import SaleServiceForm
from part_number import PartNumberForm
from service_number import ServiceNumberForm
from entity import EntityForm
from contract import ContractForm
        

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, con):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.con = con
        
        # set up the contract_view_widget to display contract 
        self.contract_view_widget = ContractView(self, self.con)
        # set up the sale of goods form:
        self.sale_goods_form_widget = SaleGoodsForm(self, self.con)
        # set up the sale of service form:
        self.sale_service_form_widget = SaleServiceForm(self,self.con)
        # set up the part number form:
        self.pn_form_widget = PartNumberForm(self, self.con)
        # set up the service number form:
        self.sn_form_widget=ServiceNumberForm(self,self.con)
        # set up the enitity form:
        self.entity_form_widget=EntityForm(self, self.con)
        # set up the contract form:
        self.contract_form_widget=ContractForm(self,self.con)

        
        # add various widgets to the middle_layout
        self.middle_layout.addWidget(self.contract_view_widget)
        self.middle_layout.addWidget(self.sale_goods_form_widget)
        self.middle_layout.addWidget(self.sale_service_form_widget)
        self.middle_layout.addWidget(self.pn_form_widget)
        self.middle_layout.addWidget(self.sn_form_widget)
        self.middle_layout.addWidget(self.entity_form_widget)
        self.middle_layout.addWidget(self.contract_form_widget)


        # connect action triggers to slots
        self.actionOpen.triggered.connect(self.open_) 
        self.actionSale_of_Goods.triggered.connect(self.show_sale_of_goods_form)
        self.actionSale_of_Services.triggered.connect(self.show_sale_of_service_form)
        self.actionPart_Number.triggered.connect(self.show_part_number_form)
        self.actionService_Number.triggered.connect(self.show_service_number_form)
        self.actionEntity.triggered.connect(self.show_entity_form)
        self.actionLoad_Contract_Docs.triggered.connect(self.load_contract_docs)
        self.actionContract.triggered.connect(self.show_contract_form)


    def open_(self):
        # will eventually take the selected contract name/description
        # and load the TextEdit with the appropriate html
        # and then make visible.

        with open("./contract.html", 'r', encoding='utf-8') as k:
            html=k.read()
        self.contract_view_widget.textEdit.setHtml(html)

        # the the desired view to True and others to False
        self.contract_view_widget.setVisible(True)
        self.sale_goods_form_widget.setVisible(False)
        self.sale_service_form_widget.setVisible(False)
        self.pn_form_widget.setVisible(False)
        self.sn_form_widget.setVisible(False)
        self.entity_form_widget.setVisible(False)
        self.contract_form_widget.setVisible(False)
    
    def show_sale_of_goods_form (self):
        self.contract_view_widget.setVisible(False)
        self.sale_goods_form_widget.setVisible(True)
        self.sale_service_form_widget.setVisible(False)
        self.pn_form_widget.setVisible(False)
        self.sn_form_widget.setVisible(False)
        self.entity_form_widget.setVisible(False)
        self.contract_form_widget.setVisible(False)

    def show_sale_of_service_form (self):
        self.contract_view_widget.setVisible(False)
        self.sale_goods_form_widget.setVisible(False)
        self.sale_service_form_widget.setVisible(True)
        self.pn_form_widget.setVisible(False)
        self.sn_form_widget.setVisible(False)
        self.entity_form_widget.setVisible(False)
        self.contract_form_widget.setVisible(False)

    def show_part_number_form(self):
        self.contract_view_widget.setVisible(False)
        self.sale_goods_form_widget.setVisible(False)
        self.sale_service_form_widget.setVisible(False)
        self.pn_form_widget.setVisible(True)
        self.sn_form_widget.setVisible(False)
        self.entity_form_widget.setVisible(False)
        self.contract_form_widget.setVisible(False)

    def show_service_number_form(self):
        self.contract_view_widget.setVisible(False)
        self.sale_goods_form_widget.setVisible(False)
        self.sale_service_form_widget.setVisible(False)
        self.pn_form_widget.setVisible(False)
        self.sn_form_widget.setVisible(True)
        self.entity_form_widget.setVisible(False)
        self.contract_form_widget.setVisible(False)

    def show_entity_form(self):
        self.contract_view_widget.setVisible(False)
        self.sale_goods_form_widget.setVisible(False)
        self.sale_service_form_widget.setVisible(False)
        self.pn_form_widget.setVisible(False)
        self.sn_form_widget.setVisible(False)
        self.entity_form_widget.setVisible(True)
        self.contract_form_widget.setVisible(False)

    def show_contract_form(self):
        self.contract_view_widget.setVisible(False)
        self.sale_goods_form_widget.setVisible(False)
        self.sale_service_form_widget.setVisible(False)
        self.pn_form_widget.setVisible(False)
        self.sn_form_widget.setVisible(False)
        self.entity_form_widget.setVisible(False)
        self.contract_form_widget.setVisible(True)

    def load_contract_docs(self):
        file_dialog=QFileDialog(self, "Select Contract", "home/tarun/LNContractApp")
        print(file_dialog)
        if file_dialog.exec():
            contract_file=file_dialog.selectedFiles()
            data=[(contract_file)]
            insert_contract_doc(self.con, data)




# application    

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


app.exec()  
