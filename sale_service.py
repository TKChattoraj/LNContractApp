# containing the sub-classed SaleServiceForm with form specific slots and other handling.

import sys, time
from datetime import date
from PyQt6.QtCore import Qt, QDate, QTimer
from PyQt6.QtGui import QAction, QCursor
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QMenu, QWidget
from PyQt6.QtSql import QSqlDatabase, QSqlDatabase, QSqlTableModel, QSqlQuery
from sale_service_form import Ui_SaleServiceForm
from db_methods import select_entities, select_sn, select_contracts, get_db_id, insert_sale_service


class SaleServiceForm(QWidget, Ui_SaleServiceForm):
    def __init__(self, parent, con):
        # parent is instance of MainWindow
        # con is the db connection
        # self is the sale of service widget being created

        super().__init__()
        self.setupUi(self)
        self.parent=parent
        self.con=con

        contracts=select_contracts(con)
        contracts_index=contracts.record().indexOf("contract_no")  #contract_no is the contract number column in contracts table.
        while contracts.next():
            self.sale_service_contractComboBox.addItem(contracts.value(contracts_index))
        contracts.finish()

        entities=select_entities(con)
        name_index=entities.record().indexOf("name")
        while entities.next():
            self.sale_service_obligorComboBox.addItem(entities.value(name_index))
        entities.finish()

        service_numbers=select_sn(con)
        sn_index=service_numbers.record().indexOf("service_number")
        while service_numbers.next():
            print(service_numbers.value(sn_index))
            self.sale_service_numberComboBox.addItem(service_numbers.value(sn_index))
        service_numbers.finish()

        self.sale_service_due_dateDateEdit.setCalendarPopup(True)
        today = QDate.currentDate()
        self.sale_service_due_dateDateEdit.setDate(today)

        self.sale_service_buttonBox.accepted.connect(self.create_sos)
        self.sale_service_buttonBox.rejected.connect(self.reject_sos)
        self.setVisible(False)

    def create_sos(self):
        # get the data from the form
        contract_num = self.sale_service_contractComboBox.currentText()
        obligor_name = self.sale_service_obligorComboBox.currentText()
        sn = self.sale_service_numberComboBox.currentText()
        quantity = self.sale_service_quantitySpinBox.value()
        description=self.sale_service_descriptionLineEdit.text()
        date= self.sale_service_due_dateDateEdit.date()
        status = self.sale_service_statusLineEdit.text()
        date_str = date.toString()
        tender=False
        
        # get the primary ids for the foregin keys for contracts, part number and entities
        contract_id=get_db_id(self.con,"contracts", "contract_no", contract_num)
        sn_id=get_db_id(self.con,"services", "service_number", sn)
        obligor_id=get_db_id(self.con, "entities", "name", obligor_name)

        # set the data for the call to inserting sales order into db
        data = [(contract_id, sn_id, obligor_id, quantity, date_str, tender, description, status)]
        insert_sale_service(self.con, data)

        #reset the form view
        self.reset_sos_form()
        
    def reject_sos(self):
        self.setVisible(False)
        
    def reset_sos_form(self):
        self.sale_service_quantitySpinBox.setValue(0)
        self.sale_service_descriptionLineEdit.setText("")
        self.sale_service_statusLineEdit.setText("")



        self.sale_service_bottom_Label.setText("Working...")
       
        # Show display as "Working..." for 1.5 seconds and then show
        # "Done." message.  Tiome delay is to make the change and notice 
        # message noticable to user.

        timer = QTimer(self)
        timer.setSingleShot(True)       
        timer.timeout.connect(self.update_bottom_label)
        timer.start(500)
        
    # update the bootom lable of the sog form.    
    def update_bottom_label(self):
        self.sale_service_bottom_Label.setText("Done.  Enter another or quit.")
