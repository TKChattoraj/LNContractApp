# containing the sub-classed SaleGoodsForm with form specific slots and other handling.

import sys, time
from datetime import date
from PyQt6.QtCore import Qt, QDate, QTimer
from PyQt6.QtGui import QAction, QCursor
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QMenu, QFileDialog
from PyQt6.QtSql import QSqlDatabase, QSqlDatabase, QSqlTableModel, QSqlQuery

from QtContractParent import Ui_MainWindow
from contract_form import Ui_ContractForm
from db_methods import select_entities, insert_goods_table, select_pn, select_contracts, get_db_id, insert_sale_goods


class ContractForm(QMainWindow, Ui_ContractForm):
    def __init__(self, parent, con):
        # parent is instance of MainWindow
        # con is the db connection
        # self is the contract widget being created

        super().__init__()
        self.setupUi(self)
        self.parent=parent
        self.con=con


        # populate the party and counterparty comboboxes
        entities=select_entities(con)
        name_index=entities.record().indexOf("name")
        print("name index:")
        print(name_index)
        party_index=entities.record().indexOf("party")
        print("party_index")
        print(party_index)
        while entities.next():
            if entities.value(party_index)==1:
                self.contract_party_comboBox.addItem(entities.value(name_index))
            else:
                self.contract_counterparty_comboBox.addItem(entities.value(name_index))
        entities.finish()
        self.contract_doc_browse_pushButton.clicked.connect(self.browse_contracts)
        self.contract_buttonBox.accepted.connect(self.create_contract)
        self.contract_buttonBox.rejected.connect(self.reject_contract)
        self.setVisible(False)
        self.setVisible(False)

    def browse_contracts(self):
        file_dialog=QFileDialog(self, "Select Contract", "home/tarun/LNContractApp")
        if file_dialog.exec():
            contract_file=file_dialog.selectedFiles()
            # To Do:  Will need to handle the multiple file selection
            self.contract_document_LineEdit.setText(contract_file[0])
            print(contract_file)
            # if the selected file isn't already a contract then create a new contract file entry in the db
            # one way to test is to hash each contract doc and store the hash digest in the db
            # hash the new doc--does its digetst eaqual any of the existing contracts?  This way the content
            # can be checked and don't need to rely unique file names
            #data=[(contract_file)]
            #insert_contract_doc(self.con, data)

    # def create_sog(self):
    #     # get the data from the form
    #     contract_num = self.sale_goods_contractComboBox.currentText()
    #     obligor_name = self.sale_goods_obligorComboBox.currentText()
    #     pn = self.sale_goods_part_numberComboBox.currentText()
    #     quantity = self.sale_goods_quantitySpinBox.value()
    #     description=self.sale_goods_descriptionLineEdit.text()
    #     date= self.sale_goods_due_dateDateEdit.date()
    #     status = self.sale_goods_statusLineEdit.text()
    #     date_str = date.toString()
    #     tender=False
        
    #     # get the primary ids for the foreign keys for contracts, part number and entities
    #     contract_id=get_db_id(self.con,"contracts", "contract_no", contract_num)
    #     pn_id=get_db_id(self.con,"goods", "part_number", pn)
    #     obligor_id=get_db_id(self.con, "entities", "name", obligor_name)

    #     # set the data for the call to inserting sales order into db
    #     data = [(contract_id, pn_id, obligor_id, quantity, date_str, tender, description, status)]
    #     insert_sale_goods(self.con, data)

    #     #reset the form view
    #     self.reset_sog_form()
        
    # def reject_sog(self):
    #     self.setVisible(False)
        
    # def reset_sog_form(self):
    #     self.sale_goods_quantitySpinBox.setValue(0)
    #     self.sale_goods_descriptionLineEdit.setText("")
    #     self.sale_goods_statusLineEdit.setText("")

    #     self.sale_goods_bottom_Label.setText("Working...")
       
    #     # Show display as "Working..." for 1.5 seconds and then show
    #     # "Done." message.  Tiome delay is to make the change and notice 
    #     # message noticable to user.

    #     timer = QTimer(self)
    #     timer.setSingleShot(True)       
    #     timer.timeout.connect(self.update_bottom_label)
    #     timer.start(500)
        
    # # update the bootom lable of the sog form.    
    # def update_bottom_label(self):
    #     self.sale_goods_bottom_Label.setText("Done.  Enter another or quit.")
