# containing the sub-classed SaleGoodsForm with form specific slots and other handling.

import sys, time
from datetime import date
from PyQt6.QtCore import Qt, QDate, QTimer
from PyQt6.QtGui import QAction, QCursor
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QMenu, QFrame, QWidget
from PyQt6.QtSql import QSqlDatabase, QSqlDatabase, QSqlTableModel, QSqlQuery

from QtContractParent import Ui_MainWindow
from contract_text_view import Ui_ContractView
from db_methods import select_entities, insert_goods_table, select_pn, select_contracts, get_db_id, insert_sale_goods


class ContractView(QWidget, Ui_ContractView):
    def __init__(self, parent, con):
        # parent is instance of QMainWindow 
        # con is the db connection
        # self is the contract_view_widget

        super().__init__()
        self.setupUi(self)
        self.parent=parent
        self.con=con

        self.setVisible(False)
        
    
    