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
from db_methods import (
    select_entities,
    insert_goods_table,
    select_last_id,
    select_pn,
    select_contracts,
    get_db_id,
    insert_sale_goods,
    insert_contract,
    insert_contract_doc
)


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
        id_index=entities.record().indexOf("id")
        print("party_index")
        print(party_index)
        self.party_dict={}
        self.counterparty_dict={}
        while entities.next():
            if entities.value(party_index)==1:
                self.contract_party_comboBox.addItem(entities.value(name_index))
                self.party_dict[entities.value(id_index)]=entities.value(name_index)
            else:
                self.contract_counterparty_comboBox.addItem(entities.value(name_index))
                self.counterparty_dict[entities.value(id_index)]=entities.value(name_index)
        entities.finish()
        # load the contract doc
        self.contract_doc_browse_pushButton.clicked.connect(self.browse_contracts)
        
        self.contract_buttonBox.accepted.connect(self.create_contract)
        self.contract_buttonBox.rejected.connect(self.reject_contract)
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

    def create_contract(self):
        k_num=self.contract_number_LineEdit.text()
        desc=self.contract_description_LineEdit.text()
        party=self.contract_party_comboBox.currentText()
        counterparty=self.contract_counterparty_comboBox.currentText()
        k_doc=self.contract_document_LineEdit.text()
        party_id =self.get_key(self.party_dict, party)
        counterparty_id=self.get_key(self.counterparty_dict, counterparty)
        status=""
        data = [(k_num, party_id, counterparty_id, desc, status)]
        insert_contract(self.con, data)
        
        # connect the selected k doc to the contract
        k_id=select_last_id(self.con, "contracts")
        data = [(k_doc, k_id)]
        insert_contract_doc(self.con, data)

        
        self.reset_contract_form()

    def get_key(self, dict, val):
        for k, v in dict.items():
            if val==v:
                return k
            # else we'll need to account for the error that value isn't in the dict
            # but that shoulldn't happen because val is coming from the dict originally
            # still need to think.

    
    # reset the contract view

    def reset_contract_form(self):
        self.contract_number_LineEdit.setText("")
        self.contract_description_LineEdit.setText("")
        self.contract_counterparty_comboBox.currentText()
        self.contract_document_LineEdit.setText("")

    # Show display as "Working..." for 1.5 seconds and then show
    # "Done." message.  Time delay is to make the change and notice 
    # message noticable to user.

        timer = QTimer(self)
        timer.setSingleShot(True)       
        timer.timeout.connect(self.update_bottom_label)
        timer.start(500)
        
    def reject_contract(self):
        self.setVisible(False)
        
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
        
    # update the bootom lable of the sog form.    
    def update_bottom_label(self):
        self.contract_bottom_Label.setText("Done.  Enter another or quit.")
