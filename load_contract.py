# containing the sub-classed SaleGoodsForm with form specific slots and other handling.

from contextlib import nullcontext
from html.entities import entitydefs
import sys, time
from datetime import date
from turtle import setheading
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

from LNContract_classes import Entity, LnNode, KCommServer, Contract, KText


class LoadContractForm(QMainWindow, Ui_LoadContractForm):
    def __init__(self, parent, con):
        # parent is instance of MainWindow
        # con is the db connection
        # self is the load contract widget being created

        super().__init__()
        self.setupUi(self)
        self.parent=parent
        self.con=con

        

    #####################################

        # self.model = QSqlTableModel(self)
        # self.model.setTable("contracts")
        # self.model.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit) #changes are cached until submitAll() or revertAll()
        # #self.model.setHeaderData(0,Qt.Orientation.Horizontal, "id")
        # #self.model.setHeaderData(1,Qt.Orientation.Horizontal, "contract_no")
        # self.model.select() # populates the model
        
        # row=self.model.record(0)
        # for j in range(row.count()):
        #     column_names.append(row.fieldName(j))
        # print("model column and values")

        table="contracts"
        self.contract_model, column_names =self.get_model(table)
        # self.contract_model.setFilter("id=4")
        # self.contract_model.select()
        # row=self.contract_model.record(0)
        # print("filtered row")
        # print(row.value("contract_no"))
        # print(self.contract_model.filter())


        # print("printing the contract numbers:")
        for i in range(self.contract_model.rowCount()):
            row=self.contract_model.record(i)
            print(row.value("contract_no"))
            phrase=row.value("contract_no")+": "+row.value("description")
            # load each contract into the combo box widget
            self.load_contract_contractComboBox.addItem(phrase)
        

        # contract_object=ContractObject(row)
        # print("contract object")
        # print(contract_object.contract_no)
        



    #####################################


    #00000000000000000000000000000000000000
        # self.contracts=select_contracts(con) # query object for all contracts from contracts table
        # # create the index for various query values
        
        # self.contracts_no_index=self.contracts.record().indexOf("contract_no")  #contract_no is the contract number column in contracts table.
        # self.contracts_id_index=self.contracts.record().indexOf("id")
        # self.contracts_party_id_index=self.contracts.record().indexOf("party_id")
        # self.contracts_counterparty_id_index=self.contracts.record().indexOf("counterparty_id")

        # # contract query indices:
        # # id -> 0
        # # contract_no-> 1
        # # party_id -> 2
        # # counterparty_id -> 3
        # # description -> 4
        # # status -> 5
        
        
        # self.contracts_dict={}

        # # go through each contracts query record
        # # prepare the dict for that record with contract name as the key
        # # put name into the combo box widget

        # while self.contracts.next():
            
        #     self.contract_no_val=self.contracts.value(self.contracts_no_index)  # contract number value that was selected in the form
        #     print("type for contract_no_val")
        #     print(type(self.contract_no_val))

        #     self.id_val=self.contracts.value(self.contracts_id_index)
        #     self.party_val=self.contracts.value(self.contracts_party_id_index)
        #     self.counterparty_val=self.contracts.value(self.contracts_counterparty_id_index)

        #     # load each contract into the combo box widget
        #     self.load_contract_contractComboBox.addItem(self.contract_no_val)

        #     # assuming with this dict that the contract number is unique--as it is used as the key
        #     self.contracts_dict[self.contract_no_val]={
        #         "id":self.id_val,  
        #         "party":self.party_val, 
        #         "counterparty":self.counterparty_val  
        #     }
        #     print("dict")
        #     print(self.contracts_dict[self.contract_no_val]["id"])
        #     print(self.contracts_dict[self.contract_no_val]["party"])
        #     print(self.contracts_dict[self.contract_no_val]["counterparty"])
        # self.contracts.finish()
    #00000000000000000000000000000000000000
        self.load_contract_buttonBox.accepted.connect(self.load_contract)
        self.load_contract_buttonBox.rejected.connect(self.reject_load_contract)
        self.setVisible(False)

    def get_column_names(self, model):
        column_names=[]
        row=model.record(0)  #assume the table is non empty
        if row:
            for j in range(row.count()):
                column_names.append(row.fieldName(j))
            return column_names
        else:
            print("error in getting columns")
            return None


    def get_model(self, table):
        model = QSqlTableModel()
        model.setTable(table)
        model.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit) #changes are cached until submitAll() or revertAll()
        model.select() # populates the model
        col_names=self.get_column_names(model)
        return model, col_names

    class ContractObject():
            print("in modelobject")
            def __init__(self, row):
                self.id=row.value("id")
                self.contract_no=row.value("contract_no")
                self.party=row.value("party_id")
                self.counterparty=row.value("counterparty_id")
                self.description=row.value("description")
                

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

        contract_obj=self.set_up_contract_model(
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

        # #reset the form view
        self.reset_load_contract_form()

    def set_up_contract_model(self, chosen_k_no, contract_record, party_id, counterparty_id, description, status):
        # create the party and counterparty objects/models
        party=self.set_up_entity_model(party_id)
        counterparty=self.set_up_entity_model(counterparty_id)

        contract_id=contract_record.value("id")
        contract_texts=self.get_ktexts(contract_id)
        print("contract texts:")
        print(contract_texts)
       
        # create the contract model object
        contract=Contract(contract_id, chosen_k_no, party, counterparty, contract_texts, description, status)
        return contract

    def get_ktexts(self, k_id):
        # use the id_val to get the contract text to display
        k_text_model, col = self.get_model("ktexts")
        where_clause="contract_id={}".format(k_id)
        k_text_model.setFilter(where_clause)
        k_text_model.select()
        rows=k_text_model.rowCount()
        k_text_list=[]
        for i in range(rows):
            record=k_text_model.record(i)
            id=record.value("id")
            filename=record.value("filename")
            contract_id=record.value("contract_id")
            status=record.value("satus")
            ktext=KText(id, filename, contract_id, status)
            k_text_list.append(ktext)
        return k_text_list

        # ktexts_query=select_record_with_column_value(self.con, "ktexts", "contract_id", id)
        
        # print("contract text")
        # contract_texts=[]
        # while ktexts_query.next():
        #     contract_texts.append(ktexts_query.value(1))
        # return contract_texts

    def set_up_entity_model(self, entity_id):

        # entity_type is party or counterparty

        ##### create the party object:
        #entity_query=select_record_with_id(self.con, self.contracts_dict[self.contract_num][entity_type], "entities")
        entity_model, columns =self.get_model("entities")
        where_phrase="id={}".format(entity_id)
        entity_model.setFilter(where_phrase)
        entity_model.select()
        entity_record=entity_model.record(0)

        #### create the party's ln_node object:

        # select the ln_node record
        #entity_ln_node_id=entity_query.value(2)  
        entity_ln_node_id=entity_record.value("ln_node_id")

        print("within entity setutp")
        print(entity_ln_node_id)
        # think about refactoring the "2 indices to be more robust"
        # the 2 indices corresponds to the placement in the query which corresponds to the placement in the SELECT.
        # The SELECT text is assembled from the get column names.  Does the order of column
        # names it return ever change?
        #  

        # create the LnNode object:
        ln_node=self.set_up_ln_node_model(entity_ln_node_id)

        # create the kcomm_server object:
        # select the kcomm record
        entity_kcomm_id=entity_record.value("kcomm_server_id")
        
        ### create the party's kcomm_server object:
        kcomm_server=self.set_up_kcomm_model(entity_kcomm_id)
        
        # create the party object:
        id=entity_record.value("id")
        name=entity_record.value("name")
        ln_node= ln_node
        kcomm=kcomm_server
        entity=Entity(id, name, ln_node, kcomm)  
        return entity

    def set_up_ln_node_model(self, entity_ln_node_id):
        ln_node_model, columns =self.get_model("ln_nodes")
        where_phrase="id={}".format(entity_ln_node_id)
        ln_node_model.setFilter(where_phrase)
        ln_node_model.select()
        ln_node_record=ln_node_model.record(0)

        ############
        #entity_ln_node_query=select_record_with_id(self.con, entity_ln_node_id, "ln_nodes")
        
        ln_id= ln_node_record.value("id")
        ln_address= ln_node_record.value("address")
        ln_tls_path=ln_node_record.value("tls_path")
        ln_macaroon_path=ln_node_record.value("macaroon_path")
        ln_status=ln_node_record.value("status")

        # create the actual LnNode object:
        ln_node=LnNode(
            ln_id,
            ln_address,
            ln_tls_path,
            ln_macaroon_path,
            ln_status
        )
        return ln_node

    def set_up_kcomm_model(self, kcomm_id ):
        #  Need to think about abstracting the creation of these models into objects.
        #  Also need to think about how to make less fragile in case of a database change.
        #  That would require obtaining the values based on the specific column names for the table
        #  And so need to think about the use of the "columns" variable in the get_model() function.

        # entity_kcomm_query=select_record_with_id(self.con, entity_kcomm_id, "kcomm_servers")
        
        kcomm_model, col = self.get_model("kcomm_servers")
        where_phrase="id={}".format(kcomm_id)
        kcomm_model.setFilter(where_phrase)
        kcomm_model.select()
        kcomm_record=kcomm_model.record(0)
        
        k_id=kcomm_record.value("id")
        k_address=kcomm_record.value("address")
        k_tls_cert=kcomm_record.value("tls_cert")
        k_status=kcomm_record.value("status")

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
