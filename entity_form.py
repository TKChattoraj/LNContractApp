# Form implementation generated from reading ui file 'entity_form.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_EntityForm(object):
    def setupUi(self, EntityForm):
        EntityForm.setObjectName("EntityForm")
        EntityForm.resize(439, 549)
        self.entity_form_Widget = QtWidgets.QWidget(EntityForm)
        self.entity_form_Widget.setGeometry(QtCore.QRect(20, 40, 371, 501))
        self.entity_form_Widget.setObjectName("entity_form_Widget")
        self.formLayout = QtWidgets.QFormLayout(self.entity_form_Widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.enitty_name_Label = QtWidgets.QLabel(self.entity_form_Widget)
        self.enitty_name_Label.setObjectName("enitty_name_Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.enitty_name_Label)
        self.entity_name_LineEdit = QtWidgets.QLineEdit(self.entity_form_Widget)
        self.entity_name_LineEdit.setObjectName("entity_name_LineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.entity_name_LineEdit)
        self.entity_party_radioButton = QtWidgets.QRadioButton(self.entity_form_Widget)
        self.entity_party_radioButton.setObjectName("entity_party_radioButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.entity_party_radioButton)
        self.entity_counterparty_radioButton = QtWidgets.QRadioButton(self.entity_form_Widget)
        self.entity_counterparty_radioButton.setObjectName("entity_counterparty_radioButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.entity_counterparty_radioButton)
        self.label = QtWidgets.QLabel(self.entity_form_Widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.ItemRole.LabelRole, spacerItem)
        self.label_2 = QtWidgets.QLabel(self.entity_form_Widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.ItemRole.LabelRole, spacerItem1)
        self.entity_lnd_address_port_LineEdit = QtWidgets.QLineEdit(self.entity_form_Widget)
        self.entity_lnd_address_port_LineEdit.setObjectName("entity_lnd_address_port_LineEdit")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.entity_lnd_address_port_LineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(11, QtWidgets.QFormLayout.ItemRole.LabelRole, spacerItem2)
        self.label_3 = QtWidgets.QLabel(self.entity_form_Widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(14, QtWidgets.QFormLayout.ItemRole.LabelRole, spacerItem3)
        self.entity_lnd_tls_LineEdit = QtWidgets.QLineEdit(self.entity_form_Widget)
        self.entity_lnd_tls_LineEdit.setObjectName("entity_lnd_tls_LineEdit")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.ItemRole.FieldRole, self.entity_lnd_tls_LineEdit)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(16, QtWidgets.QFormLayout.ItemRole.LabelRole, spacerItem4)
        self.label_4 = QtWidgets.QLabel(self.entity_form_Widget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(18, QtWidgets.QFormLayout.ItemRole.LabelRole, spacerItem5)
        self.entity_macaroon_LineEdit = QtWidgets.QLineEdit(self.entity_form_Widget)
        self.entity_macaroon_LineEdit.setObjectName("entity_macaroon_LineEdit")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.ItemRole.FieldRole, self.entity_macaroon_LineEdit)
        self.label_5 = QtWidgets.QLabel(self.entity_form_Widget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label_5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(21, QtWidgets.QFormLayout.ItemRole.LabelRole, spacerItem6)
        self.label_6 = QtWidgets.QLabel(self.entity_form_Widget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(22, QtWidgets.QFormLayout.ItemRole.LabelRole, spacerItem7)
        self.entity_server_address_port_LineEdit = QtWidgets.QLineEdit(self.entity_form_Widget)
        self.entity_server_address_port_LineEdit.setObjectName("entity_server_address_port_LineEdit")
        self.formLayout.setWidget(22, QtWidgets.QFormLayout.ItemRole.FieldRole, self.entity_server_address_port_LineEdit)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(23, QtWidgets.QFormLayout.ItemRole.LabelRole, spacerItem8)
        self.label_7 = QtWidgets.QLabel(self.entity_form_Widget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(23, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_7)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(24, QtWidgets.QFormLayout.ItemRole.LabelRole, spacerItem9)
        self.entity_server_tls_LineEdit = QtWidgets.QLineEdit(self.entity_form_Widget)
        self.entity_server_tls_LineEdit.setObjectName("entity_server_tls_LineEdit")
        self.formLayout.setWidget(24, QtWidgets.QFormLayout.ItemRole.FieldRole, self.entity_server_tls_LineEdit)
        self.entity_buttonBox = QtWidgets.QDialogButtonBox(self.entity_form_Widget)
        self.entity_buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.entity_buttonBox.setObjectName("entity_buttonBox")
        self.formLayout.setWidget(26, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.entity_buttonBox)
        self.entity_bottom_Label = QtWidgets.QLabel(self.entity_form_Widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.entity_bottom_Label.setFont(font)
        self.entity_bottom_Label.setText("")
        self.entity_bottom_Label.setObjectName("entity_bottom_Label")
        self.formLayout.setWidget(27, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.entity_bottom_Label)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(19, QtWidgets.QFormLayout.ItemRole.SpanningRole, spacerItem10)
        self.entity_form_Label = QtWidgets.QLabel(EntityForm)
        self.entity_form_Label.setGeometry(QtCore.QRect(10, 10, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.entity_form_Label.setFont(font)
        self.entity_form_Label.setObjectName("entity_form_Label")

        self.retranslateUi(EntityForm)
        QtCore.QMetaObject.connectSlotsByName(EntityForm)

    def retranslateUi(self, EntityForm):
        _translate = QtCore.QCoreApplication.translate
        EntityForm.setWindowTitle(_translate("EntityForm", "Form"))
        self.enitty_name_Label.setText(_translate("EntityForm", "Name"))
        self.entity_party_radioButton.setText(_translate("EntityForm", "Party"))
        self.entity_counterparty_radioButton.setText(_translate("EntityForm", "Counterparty"))
        self.label.setText(_translate("EntityForm", "LND Node:"))
        self.label_2.setText(_translate("EntityForm", "Address:Port"))
        self.label_3.setText(_translate("EntityForm", "TLS Cert Location"))
        self.label_4.setText(_translate("EntityForm", "Macaroon Location"))
        self.label_5.setText(_translate("EntityForm", "Contract Server"))
        self.label_6.setText(_translate("EntityForm", "Address:Port"))
        self.label_7.setText(_translate("EntityForm", "TLS Cert Location"))
        self.entity_form_Label.setText(_translate("EntityForm", "Entity Entry:"))
