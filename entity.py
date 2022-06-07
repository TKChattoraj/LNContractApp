# containing the sub-classed Service Number Form with form specific slots and other handling.

from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6.QtCore import Qt, QDate, QTimer
from entity_form import Ui_EntityForm
from db_methods import insert_ln_nodes_table, insert_kcomm_server_table


class EntityForm(QWidget, Ui_EntityForm):
    
    def __init__(self, parent, con):
        # self is the window.entity_form_widget
        # parent is instance of MainWindow
        # con is the db connection

        # note on naming convention:
        # instant variables related to Qt elements will be
        # lower_case_seperated_and_QtElementsCapitalized

        super().__init__()
        self.setupUi(self)
        self.parent=parent
        self.con=con
        #maybe define default input for various view widget elements that need it?
        
        self.entity_buttonBox.accepted.connect(self.create_entity)
        self.entity_buttonBox.rejected.connect(self.reject_entity)
        self.setVisible(False)
        
    def create_entity(self):
        # retrieve the values from the form
        entity_name = self.entity_name_LineEdit.text()
        lnd_location=self.entity_lnd_address_port_LineEdit.text()
        lnd_tls=self.entity_lnd_tls_LineEdit.text()
        lnd_macaroon=self.entity_macaroon_LineEdit.text()
        contract_server=self.enitity_server_address_port_LineEdit.text()
        contract_tls=self.enitity_server_tls_LineEdittext()
        entity_status= ""

        # insert lnd data into ln_nodes table of db: 
        status = ""
        data = [(lnd_location, lnd_tls, lnd_macaroon, status)]
        ln_node_id=insert_ln_nodes_table(self.con, data)
        print("ln node id:")
        print(ln_node_id)

        # insert k comm server data into kcomm_servers table of db:
        status = ""
        data = [(contract_server, contract_tls, status)]
        insert_kcomm_server_table(self.con, data)

        # get the lnd and kcomm server ids for what was just input





        #reset part number form()

        self.reset_entity_form()        
    
    def reject_entity(self):
        self.setVisible(False)

    def reset_entity_form(self):
        
        self.sn_bottem_Label.setText("Working...")
        self.sn_entry_service_number_LineEdit.setText("")
        self.sn_entry_description_LineEdit.setText("")
        self.sn_entry_status_LineEdit.setText("")
        
        # Show display as "Working..." for 1.5 seconds and then show
        # "Done." message.  Tiome delay is to make the change and notice 
        # message noticable to user.
        timer = QTimer(self)
        timer.setSingleShot(True)   
        timer.timeout.connect(self.update_bottom_label)
        timer.start(500)

    # update the bottom lable of the sos form.    
    def update_bottom_label(self):
        self.sn_bottem_Label.setText("Done.  Enter another or quit.")


        