# containing the sub-classed Service Number Form with form specific slots and other handling.

from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6.QtCore import Qt, QDate, QTimer
from service_number_form import Ui_ServiceNumberForm
from db_methods import insert_services_table


class ServiceNumberForm(QWidget, Ui_ServiceNumberForm):
    
    def __init__(self, parent, con):
        # self is the window.sn_form_widget
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
        
        self.sn_entry_ButtonBox.accepted.connect(self.create_sn)
        self.sn_entry_ButtonBox.rejected.connect(self.reject_sn)
        self.setVisible(False)
        
    def create_sn(self):
        # retrieve the values from the form
        service_number = self.sn_entry_service_number_LineEdit.text()
        sn_description = self.sn_entry_description_LineEdit.text()
        sn_status = self.sn_entry_status_LineEdit.text()
        # create the data parameter amd inserting into db 
        data = [(service_number, sn_description, sn_status)]
        insert_services_table(self.con, data)

        #reset part number form()

        self.reset_sn_form()        
    
    def reject_sn(self):
        self.setVisible(False)

    def reset_sn_form(self):
        
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


        