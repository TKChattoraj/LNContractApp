# Form implementation generated from reading ui file 'part_number_form.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PartNumberForm(object):
    def setupUi(self, PartNumberForm):
        PartNumberForm.setObjectName("PartNumberForm")
        PartNumberForm.resize(389, 300)
        self.pn_entry_form_Widget = QtWidgets.QWidget(PartNumberForm)
        self.pn_entry_form_Widget.setGeometry(QtCore.QRect(10, 70, 371, 121))
        self.pn_entry_form_Widget.setObjectName("pn_entry_form_Widget")
        self.formLayout = QtWidgets.QFormLayout(self.pn_entry_form_Widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.pn_entry_part_number_Label = QtWidgets.QLabel(self.pn_entry_form_Widget)
        self.pn_entry_part_number_Label.setObjectName("pn_entry_part_number_Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.pn_entry_part_number_Label)
        self.pn_entry_part_number_LineEdit = QtWidgets.QLineEdit(self.pn_entry_form_Widget)
        self.pn_entry_part_number_LineEdit.setObjectName("pn_entry_part_number_LineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pn_entry_part_number_LineEdit)
        self.pn_entry_description_Label = QtWidgets.QLabel(self.pn_entry_form_Widget)
        self.pn_entry_description_Label.setObjectName("pn_entry_description_Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.pn_entry_description_Label)
        self.pn_entry_description_LineEdit = QtWidgets.QLineEdit(self.pn_entry_form_Widget)
        self.pn_entry_description_LineEdit.setObjectName("pn_entry_description_LineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pn_entry_description_LineEdit)
        self.pn_entry_ButtonBox = QtWidgets.QDialogButtonBox(self.pn_entry_form_Widget)
        self.pn_entry_ButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Save)
        self.pn_entry_ButtonBox.setObjectName("pn_entry_ButtonBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pn_entry_ButtonBox)
        self.pn_entry_status_LineEdit = QtWidgets.QLineEdit(self.pn_entry_form_Widget)
        self.pn_entry_status_LineEdit.setObjectName("pn_entry_status_LineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pn_entry_status_LineEdit)
        self.part_number_status_Label = QtWidgets.QLabel(self.pn_entry_form_Widget)
        self.part_number_status_Label.setObjectName("part_number_status_Label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.part_number_status_Label)
        self.pn_entry_form_Label = QtWidgets.QLabel(PartNumberForm)
        self.pn_entry_form_Label.setGeometry(QtCore.QRect(10, 30, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pn_entry_form_Label.setFont(font)
        self.pn_entry_form_Label.setObjectName("pn_entry_form_Label")
        self.pn_bottem_Label = QtWidgets.QLabel(PartNumberForm)
        self.pn_bottem_Label.setGeometry(QtCore.QRect(20, 210, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pn_bottem_Label.setFont(font)
        self.pn_bottem_Label.setText("")
        self.pn_bottem_Label.setObjectName("pn_bottem_Label")

        self.retranslateUi(PartNumberForm)
        QtCore.QMetaObject.connectSlotsByName(PartNumberForm)
        PartNumberForm.setTabOrder(self.pn_entry_part_number_LineEdit, self.pn_entry_description_LineEdit)
        PartNumberForm.setTabOrder(self.pn_entry_description_LineEdit, self.pn_entry_status_LineEdit)

    def retranslateUi(self, PartNumberForm):
        _translate = QtCore.QCoreApplication.translate
        PartNumberForm.setWindowTitle(_translate("PartNumberForm", "Form"))
        self.pn_entry_part_number_Label.setText(_translate("PartNumberForm", "Part Number"))
        self.pn_entry_description_Label.setText(_translate("PartNumberForm", "Description"))
        self.part_number_status_Label.setText(_translate("PartNumberForm", "Status"))
        self.pn_entry_form_Label.setText(_translate("PartNumberForm", "Part Number Entry:"))
