# Form implementation generated from reading ui file 'service_number_form.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ServiceNumberForm(object):
    def setupUi(self, ServiceNumberForm):
        ServiceNumberForm.setObjectName("ServiceNumberForm")
        ServiceNumberForm.resize(457, 300)
        self.service_entry_formWidget = QtWidgets.QWidget(ServiceNumberForm)
        self.service_entry_formWidget.setGeometry(QtCore.QRect(9, 60, 371, 161))
        self.service_entry_formWidget.setObjectName("service_entry_formWidget")
        self.formLayout = QtWidgets.QFormLayout(self.service_entry_formWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.sn_entery_name_Label = QtWidgets.QLabel(self.service_entry_formWidget)
        self.sn_entery_name_Label.setObjectName("sn_entery_name_Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.sn_entery_name_Label)
        self.service_entry_name_LineEdit = QtWidgets.QLineEdit(self.service_entry_formWidget)
        self.service_entry_name_LineEdit.setObjectName("service_entry_name_LineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.service_entry_name_LineEdit)
        self.service_entry_part_number_Label = QtWidgets.QLabel(self.service_entry_formWidget)
        self.service_entry_part_number_Label.setObjectName("service_entry_part_number_Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.service_entry_part_number_Label)
        self.sn_entry_pn_entry_service_number_LineEdit = QtWidgets.QLineEdit(self.service_entry_formWidget)
        self.sn_entry_pn_entry_service_number_LineEdit.setObjectName("sn_entry_pn_entry_service_number_LineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.sn_entry_pn_entry_service_number_LineEdit)
        self.sn_entry_description_Label = QtWidgets.QLabel(self.service_entry_formWidget)
        self.sn_entry_description_Label.setObjectName("sn_entry_description_Label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.sn_entry_description_Label)
        self.sn_entry_description_LineEdit = QtWidgets.QLineEdit(self.service_entry_formWidget)
        self.sn_entry_description_LineEdit.setObjectName("sn_entry_description_LineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.sn_entry_description_LineEdit)
        self.sn_entry_buttonBox = QtWidgets.QDialogButtonBox(self.service_entry_formWidget)
        self.sn_entry_buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Save)
        self.sn_entry_buttonBox.setObjectName("sn_entry_buttonBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.sn_entry_buttonBox)
        self.sn_entry_form_label = QtWidgets.QLabel(ServiceNumberForm)
        self.sn_entry_form_label.setGeometry(QtCore.QRect(10, 30, 141, 16))
        self.sn_entry_form_label.setObjectName("sn_entry_form_label")

        self.retranslateUi(ServiceNumberForm)
        QtCore.QMetaObject.connectSlotsByName(ServiceNumberForm)

    def retranslateUi(self, ServiceNumberForm):
        _translate = QtCore.QCoreApplication.translate
        ServiceNumberForm.setWindowTitle(_translate("ServiceNumberForm", "Form"))
        self.sn_entery_name_Label.setText(_translate("ServiceNumberForm", "Name"))
        self.service_entry_part_number_Label.setText(_translate("ServiceNumberForm", "Service Number"))
        self.sn_entry_description_Label.setText(_translate("ServiceNumberForm", "Description"))
        self.sn_entry_form_label.setText(_translate("ServiceNumberForm", "Service Number Entry"))