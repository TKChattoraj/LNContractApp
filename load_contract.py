# containing the sub-classed SaleGoodsForm with form specific slots and other handling.

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
    select_party_with_id,
    select_ktext,
    select_ln_node,
    select_kcomm
)

from LNContract_classes import Party, LnNode, KCommServer


class LoadContractForm(QMainWindow, Ui_LoadContractForm):
    def __init__(self, parent, con):
        # parent is instance of MainWindow
        # con is the db connection
        # self is the load contract widget being created

        super().__init__()
        self.setupUi(self)
        self.parent=parent
        self.con=con

        self.contracts=select_contracts(con)
        self.contracts_no_index=self.contracts.record().indexOf("contract_no")  #contract_no is the contract number column in contracts table.
        self.contracts_id_index=self.contracts.record().indexOf("id")
        self.contracts_party_id_index=self.contracts.record().indexOf("party_id")
        self.contracts_counterparty_id_index=self.contracts.record().indexOf("counterparty_id")

        
        self.contracts_dict={}
        while self.contracts.next():
            
            self.contract_no_val=self.contracts.value(self.contracts_no_index)
            self.id_val=self.contracts.value(self.contracts_id_index)
            self.party_val=self.contracts.value(self.contracts_party_id_index)
            self.counterparty_val=self.contracts.value(self.contracts_counterparty_id_index)
            self.load_contract_contractComboBox.addItem(self.contract_no_val)
            # assuming with this dict that the contract number is unique--as it is used as the key
            self.contracts_dict[self.contract_no_val]=(
                self.id_val,  # contract id value will be in 0 position of the dictionary tuple
                self.party_val, # party value will be in 1 position of the dictionary tuple
                self.counterparty_val # counterparty value will be in 2 position of the dictionary tuple
            )
        self.contracts.finish()

        self.load_contract_buttonBox.accepted.connect(self.load_contract)
        self.load_contract_buttonBox.rejected.connect(self.reject_load_contract)
        self.setVisible(False)

    def load_contract(self):
        # get the data from the form
        contract_num = self.load_contract_contractComboBox.currentText()

        id=self.contracts_dict[contract_num][1]
        

        #  use the party_id_val to select the party then get the party name to display
        party_query=select_party_with_id(self.con, self.contracts_dict[contract_num][1] )
        # print("returned query")
        # print(party_query.value(0))  # id value
        # print(party_query.value(1))  # name value
        # print(party_query.value(2))  # ln_node id value
        # print(party_query.value(3))  # kcomm_server id value

        
        
        # print("ln_nodes")
        # print(party_ln_node_query.value(0))


        # create the ln_node object:
        party_ln_node_id=party_query.value(2)
        party_ln_node_query=select_ln_node(self.con, party_ln_node_id)
        
        ln_id= party_ln_node_query.value(0)
        ln_address= party_ln_node_query.value(1)
        ln_tls_path=party_ln_node_query.value(2)
        ln_macaroon_path=party_ln_node_query.value(3)
        ln_status=party_ln_node_query.value(4)
        ln_node=LnNode(
            ln_id,
            ln_address,
            ln_tls_path,
            ln_macaroon_path,
            ln_status
        )

        # create the kcomm_server object:
        party_kcomm_id=party_query.value(3)
        party_kcomm_query=select_kcomm(self.con, party_kcomm_id)
        
        k_id=party_kcomm_query.value(0)
        k_address=party_kcomm_query.value(1)
        k_tls_cert=party_kcomm_query.value(2)
        k_status=party_kcomm_query.value(3)

        kcomm_server=KCommServer(
            k_id,
            k_address,
            k_tls_cert,
            k_status
        )

        # create the party object:
        p_id=party_query.value(0)
        p_name=party_query.value(1)
        p_ln_node= ln_node
        p_kcomm=kcomm_server
        party=Party(p_id, p_name, p_ln_node, p_kcomm)
        print("Party:")
        print(party.id)
        print(party.name)
        print(party.ln_node.id)
        print(party.ln_node.address)
        print(party.ln_node.tls_path)
        print(party.ln_node.macaroon_path)
        print(party.kcom_server.id)
        print(party.kcom_server.address)
        

        #  use the counterparty_id_val to get the counterparty then get the counterparty name to display
        counterparty_query=select_party_with_id(self.con, self.contracts_dict[contract_num][2] )

        # print("returned query")
        # print(counterparty_query.value(0))
        # print(counterparty_query.value(1))
        # print(counterparty_query.value(2))
        # print(counterparty_query.value(3))
        

        #  use the id_val to get the contract text to display
        contract_text_path=select_ktext(self.con, self.contracts_dict[contract_num][0])
        # print("contract text")
        # print(contract_text_path.value(0))


        # #reset the form view
        self.reset_load_contract_form()
        
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
        
    # update the bootom label of the load contract form.    
    def update_bottom_label(self):
        self.load_contract_bottom_label.setText("Done.  Enter another or quit.")
