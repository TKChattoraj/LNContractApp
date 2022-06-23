# containing the sub-classed SaleGoodsForm with form specific slots and other handling.

from html.entities import entitydefs
import sys, time
from datetime import date
from PyQt6.QtCore import Qt, QDate, QTimer
from PyQt6.QtGui import QAction, QCursor
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QMenu
from PyQt6.QtSql import QSqlDatabase, QSqlDatabase, QSqlTableModel, QSqlQuery

from load_contract_form import Ui_LoadContractForm
from sale_goods_form import Ui_SaleGoodsForm
from part_number_form import Ui_PartNumberForm
from db_methods import (
    select_entities,
    select_contracts,
    get_db_id,
    insert_sale_goods,
    select_entity_with_id,
    select_ktext,
    select_ln_node,
    select_kcomm,
    get_column_names,
    select_record_with_id,
    select_record_with_column_value
)

from LNContract_classes import Entity, LnNode, KCommServer, Contract


class LoadContractForm(QMainWindow, Ui_LoadContractForm):
    def __init__(self, parent, con):
        # parent is instance of MainWindow
        # con is the db connection
        # self is the load contract widget being created

        super().__init__()
        self.setupUi(self)
        self.parent=parent
        self.con=con

        self.contracts=select_contracts(con) # query object for all contracts from contracts table
        # create the index for various query values
        
        self.contracts_no_index=self.contracts.record().indexOf("contract_no")  #contract_no is the contract number column in contracts table.
        self.contracts_id_index=self.contracts.record().indexOf("id")
        self.contracts_party_id_index=self.contracts.record().indexOf("party_id")
        self.contracts_counterparty_id_index=self.contracts.record().indexOf("counterparty_id")

        # contract query indices:
        # id -> 0
        # contract_no-> 1
        # party_id -> 2
        # counterparty_id -> 3
        # description -> 4
        # status -> 5
        
        
        self.contracts_dict={}

        # go through each contracts query record
        # prepare the dict for that record with contract name as the key
        # put name into the combo box widget

        while self.contracts.next():
            
            self.contract_no_val=self.contracts.value(self.contracts_no_index)  # contract number value that was selected in the form
            print("type for contract_no_val")
            print(type(self.contract_no_val))

            self.id_val=self.contracts.value(self.contracts_id_index)
            self.party_val=self.contracts.value(self.contracts_party_id_index)
            self.counterparty_val=self.contracts.value(self.contracts_counterparty_id_index)

            # load each contract into the combo box widget
            self.load_contract_contractComboBox.addItem(self.contract_no_val)

            # assuming with this dict that the contract number is unique--as it is used as the key
            self.contracts_dict[self.contract_no_val]={
                "id":self.id_val,  
                "party":self.party_val, 
                "counterparty":self.counterparty_val  
            }
            print("dict")
            print(self.contracts_dict[self.contract_no_val]["id"])
            print(self.contracts_dict[self.contract_no_val]["party"])
            print(self.contracts_dict[self.contract_no_val]["counterparty"])
        self.contracts.finish()

        self.load_contract_buttonBox.accepted.connect(self.load_contract)
        self.load_contract_buttonBox.rejected.connect(self.reject_load_contract)
        self.setVisible(False)

    def load_contract(self):
        # get the data from the form
        self.contract_num = self.load_contract_contractComboBox.currentText()
        print("load contract type")
        print(type(self.contract_num))

        contract_model=self.set_up_contract_model()
        print("Created the contract model")
        print(contract_model.party.kcomm_server.address)

        # #reset the form view
        self.reset_load_contract_form()

    def set_up_contract_model(self):
        # create the party and counterparty objects/models
        party=self.set_up_entity_model("party")
        counterparty=self.set_up_entity_model("counterparty")

        id=self.contracts_dict[self.contract_num]["id"]
        contract_texts=self.get_ktexts(id)
       
        # create the contract model object
        contract=Contract(id, self.contract_num, party, counterparty, contract_texts)
        return contract

    def get_ktexts(self, id):
        # use the id_val to get the contract text to display
        ktexts_query=select_record_with_column_value(self.con, "ktexts", "contract_id", id)
        
        print("contract text")
        contract_texts=[]
        while ktexts_query.next():
            contract_texts.append(ktexts_query.value(1))
        return contract_texts

    def set_up_entity_model(self, entity_type):
        # entity_type is party or counterparty

        ##### create the party object:
        entity_query=select_record_with_id(self.con, self.contracts_dict[self.contract_num][entity_type], "entities")

        #### create the party's ln_node object:

        # select the ln_node record
        entity_ln_node_id=entity_query.value(2)  
        # think about refactoring the "2 indices to be more robust"
        # the 2 indices corresponds to the placement in the query which corresponds to the placement in the SELECT.
        # The SELECT text is assembled from the get column names.  Does the order of column
        # names it return ever change?
        #  

        # create the LnNode object:
        ln_node=self.set_up_ln_node_model(entity_ln_node_id)

        # create the kcomm_server object:
        # select the kcomm record
        entity_kcomm_id=entity_query.value(3)
        
        ### create the party's kcomm_server object:
        kcomm_server=self.set_up_kcomm_model(entity_kcomm_id)
        
        # create the party object:
        id=entity_query.value(0)
        name=entity_query.value(1)
        ln_node= ln_node
        kcomm=kcomm_server
        entity=Entity(id, name, ln_node, kcomm)  
        return entity

    def set_up_ln_node_model(self, entity_ln_node_id):
        entity_ln_node_query=select_record_with_id(self.con, entity_ln_node_id, "ln_nodes")
        
        ln_id= entity_ln_node_query.value(0)
        ln_address= entity_ln_node_query.value(1)
        ln_tls_path=entity_ln_node_query.value(2)
        ln_macaroon_path=entity_ln_node_query.value(3)
        ln_status=entity_ln_node_query.value(4)

        # create the actual LnNode object:
        ln_node=LnNode(
            ln_id,
            ln_address,
            ln_tls_path,
            ln_macaroon_path,
            ln_status
        )
        return ln_node

    def set_up_kcomm_model(self, entity_kcomm_id ):
        entity_kcomm_query=select_record_with_id(self.con, entity_kcomm_id, "kcomm_servers")
        
        k_id=entity_kcomm_query.value(0)
        k_address=entity_kcomm_query.value(1)
        k_tls_cert=entity_kcomm_query.value(2)
        k_status=entity_kcomm_query.value(3)

        # create the actual KCommServer object
        kcomm_server=KCommServer(
            k_id,
            k_address,
            k_tls_cert,
            k_status
        )
        return kcomm_server


    def reject_load_contract(self):
        self.setVisible(False)
        
    def reset_load_contract_form(self):

        self.load_contract_bottom_label.setText("Loading Contract...")
       
        # Show display as "Working..." for 1.5 seconds and then show
        # "Done." message.  Time delay is to make the change and notice 
        # message noticable to user.

        timer = QTimer(self)
        timer.setSingleShot(True)       
        timer.timeout.connect(self.update_bottom_label)
        timer.start(500)
        
    # update the bottom label of the load contract form.    
    def update_bottom_label(self):
        self.load_contract_bottom_label.setText("Done.  Enter another or quit.")
