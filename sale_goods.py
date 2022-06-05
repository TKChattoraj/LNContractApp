# containing the sub-classed SaleGoodsForm with form specific slots and other handling.

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


class SaleGoodsForm(QMainWindow, Ui_SaleGoodsForm):
    def __init__(self, parent, con):
        # parent is instance of MainWindow
        # con is the db connection
        # self is the sale of goods widget being created

        super().__init__()
        self.setupUi(self)
        self.parent=parent
        self.con=con

        contracts=select_contracts(con)
        contracts_index=contracts.record().indexOf("contract_no")  #contract_no is the contract number column in contracts table.
        while contracts.next():
            self.sale_goods_contractComboBox.addItem(contracts.value(contracts_index))
        contracts.finish()

        entities=select_entities(con)
        name_index=entities.record().indexOf("name")
        while entities.next():
            self.sale_goods_obligorComboBox.addItem(entities.value(name_index))
        entities.finish()

        part_numbers=select_pn(con)
        pn_index=part_numbers.record().indexOf("part_number")
        while part_numbers.next():
            print(part_numbers.value(pn_index))
            self.sale_goods_part_numberComboBox.addItem(part_numbers.value(pn_index))
        part_numbers.finish()

        self.sale_goods_due_dateDateEdit.setCalendarPopup(True)
        today = QDate.currentDate()
        self.sale_goods_due_dateDateEdit.setDate(today)

        self.sale_goods_buttonBox.accepted.connect(self.create_sog)
        self.sale_goods_buttonBox.rejected.connect(self.reject_sog)
        self.setVisible(False)
        
    def create_sog(self):
        # get the data from the form
        contract_num = self.sale_goods_contractComboBox.currentText()
        obligor_name = self.sale_goods_obligorComboBox.currentText()
        pn = self.sale_goods_part_numberComboBox.currentText()
        quantity = self.sale_goods_quantitySpinBox.value()
        description=self.sale_goods_descriptionLineEdit.text()
        date= self.sale_goods_due_dateDateEdit.date()
        status = self.sale_goods_statusLineEdit.text()
        date_str = date.toString()
        tender=False
        
        # get the primary ids for the foregin keys for contracts, part number and entities
        contract_id=get_db_id(self.con,"contracts", "contract_no", contract_num)
        pn_id=get_db_id(self.con,"goods", "part_number", pn)
        obligor_id=get_db_id(self.con, "entities", "name", obligor_name)

        # set the data for the call to inserting sales order into db
        data = [(contract_id, pn_id, obligor_id, quantity, date_str, tender, description, status)]
        insert_sale_goods(self.con, data)

        #reset the form view
        self.reset_sog_form()
        
    def reject_sog(self):
        self.parent.show_blank_verticalWidget_3()
        self.parent.show_blank_verticalWidget_4()
    
    def reset_sog_form(self):
        self.sale_goods_quantitySpinBox.setValue(0)

        self.sale_goods_bottom_Label.setText("Working...")
       
        # Show display as "Working..." for 1.5 seconds and then show
        # "Done." message.  Tiome delay is to make the change and notice 
        # message noticable to user.

        timer = QTimer(self)
        timer.setSingleShot(True)       
        timer.timeout.connect(self.update_bottom_label)
        timer.start(500)
        
    # update the bootom lable of the sog form.    
    def update_bottom_label(self):
        self.sale_goods_bottom_Label.setText("Done.  Enter another or quit.")
