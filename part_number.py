# containing the sub-classed SaleGoodsForm with form specific slots and other handling.

from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt, QDate, QTimer
from part_number_form import Ui_PartNumberForm
from db_methods import insert_goods_table


class PartNumberForm(QMainWindow, Ui_PartNumberForm):
    
    def __init__(self, parent, con):
        # self is the window.pn_entry_form_widget
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
        parent.verticalLayout_4.addWidget(self)
        self.pn_entry_ButtonBox.accepted.connect(self.create_pn)
        self.pn_entry_ButtonBox.rejected.connect(self.reject_pn)
        
    def create_pn(self):
        # retrieve the values from the form
        part_number = self.pn_entry_part_number_LineEdit.text()
        pn_description = self.pn_entry_description_LineEdit.text()
        pn_status = self.pn_entry_part_number_LineEdit.text()
        # create the data parameter amd inserting into db 
        data = [(part_number, pn_description, pn_status)]
        insert_goods_table(self.con, data)

        #reset part number form()

        self.reset_pn_form()        
    
    def reject_pn(self):
        self.parent.show_blank_verticalWidget_3()
        self.parent.show_blank_verticalWidget_4()

    def reset_pn_form(self):
        
        self.pn_bottem_Label.setText("Working...")
        self.pn_entry_part_number_LineEdit.setText("")
        self.pn_entry_description_LineEdit.setText("")
        self.part_number_status_LineEdit.setText("")
        
        # Show display as "Working..." for 1.5 seconds and then show
        # "Done." message.  Tiome delay is to make the change and notice 
        # message noticable to user.
        timer = QTimer(self)
        timer.setSingleShot(True)   
        timer.timeout.connect(self.update_bottom_label)
        timer.start(500)

    # update the bootom lable of the sog form.    
    def update_bottom_label(self):
        self.pn_bottem_Label.setText("Done.  Enter another or quit.")


        