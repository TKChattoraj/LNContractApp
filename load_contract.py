# containing the sub-classed SaleGoodsForm with form specific slots and other handling.

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtSql import QSqlTableModel

from load_contract_form import Ui_LoadContractForm

from LNContract_classes import Entity, LnNode, KCommServer, Contract, KText

from setup_db_objects import (
    
    set_up_entity_object,
    set_up_contract_object
)
from db_methods import get_model
from ln_connect import LNConnection

class LoadContractForm(QMainWindow, Ui_LoadContractForm):
    def __init__(self, parent, con):
        # parent is instance of MainWindow
        # con is the db connection
        # self is the load contract widget being created

        super().__init__()
        self.setupUi(self)
        self.parent=parent
        self.con=con

        table="contracts"
        self.contract_model=get_model(table)

        for i in range(self.contract_model.rowCount()):
            row=self.contract_model.record(i)
            print(row.value("contract_no"))
            phrase=row.value("contract_no")+": "+row.value("description")
            # load each contract into the combo box widget
            self.load_contract_contractComboBox.addItem(phrase)
      
        self.load_contract_buttonBox.accepted.connect(self.load_contract)
        self.load_contract_buttonBox.rejected.connect(self.reject_load_contract)
        self.setVisible(False)

    def load_contract(self):
        # get the data from the form
        self.chosen_contract = self.load_contract_contractComboBox.currentText()
        
        ### get contracts record corresponding to the contract chosen
        # isolate the chosen contract number
        chosen_k_no = self.chosen_contract.split(": ")[0]
        
        # make the WHERE phrase, use the model to get the appropriate record
        where_phrase="contract_no = '"+chosen_k_no +"'"
        self.contract_model.setFilter(where_phrase)
        self.contract_model.select()
        contract_record=self.contract_model.record(0)

        # get the party and counterparty ids from the selected record
        party_id=contract_record.value("party_id")
        counterparty_id=contract_record.value("counterparty_id")
        description=contract_record.value("description")
        status=contract_record.value("status")
        if not status:
            status=""

        contract_obj=set_up_contract_object(
            chosen_k_no,
            contract_record,
            party_id,
            counterparty_id,
            description,
            status
            )
        
        print("The Contract")       
        print(contract_obj.party.name)
        print(contract_obj.contract_texts[0].filename)
        print(contract_obj.counterparty.name)

        ln_n=contract_obj.party.ln_node
        ln_connection = LNConnection(ln_n.tls_path, ln_n.macaroon_path, ln_n.address)
        print("Should be done with the ln_connection instantiation.")

        node_info=ln_connection.get_node_info()


        balance_info=ln_connection.get_node_info()
        print("Node info:")
        print(node_info)
        print("Node Balance:")
        print(balance_info)

        # open a channel to Bob--alis for the counterparty in the contract (Charlie)
        # assume for now that party (Titan) knows the pubkey of its counterparty (Charlie)
        node_pubkey = "02fae819273fd07726778f92bbe8f7f4f89d8e5b46b4f51129f94b88ff7ebf798e"
        amount=2001
        channel=ln_connection.open_channel(node_pubkey, amount)
        print("Channel: {}".format(channel))


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
        
    # update the bottom label of the load contract form.    
    def update_bottom_label(self):
        self.load_contract_bottom_label.setText("Done.  Enter another or quit.")
