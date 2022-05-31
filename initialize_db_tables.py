# calls create table data functions and fills database tables

import os, sys, codecs
from PyQt6.QtCore import QSize, Qt, QByteArray
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QDataWidgetMapper,
    QDoubleSpinBox,
    QFormLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QSpinBox,
    QTableView,
    QWidget,
)
from PyQt6.QtGui import QAction, QCursor


from create_db_tables import (
    create_db_tables
    
)

from db_initialize_methods import(
    initialize_ln_node_table,
    initialize_kcomm_servers_table,
    initialize_entities_table,
    initialize_contracts_table,
    initialize_ktexts_table,
    initialize_goods_table,
    initialize_services_table,
    initialize_monetary_obligations_table,
    initialize_sale_goods_table,
    initialize_sale_services_table,
    initialize_signatures_table

)

# Create the connection
con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("lncontract_db.sqlite")

# Open the connection
if not con.open():
    print("Database Error: %s" % con.lastError().databaseText())
    sys.exit(1)

query= QSqlQuery()
query.exec("""PRAGMA foreign_keys = ON""")

# create the required db tables
create_db_tables(con)

# initialize db tables with certain data

initialize_ln_node_table(con)
initialize_kcomm_servers_table(con)
initialize_ktexts_table(con)
initialize_entities_table(con)

initialize_contracts_table(con)
initialize_goods_table(con)
initialize_services_table(con)
initialize_monetary_obligations_table(con)
initialize_sale_goods_table(con)
initialize_sale_services_table(con)
initialize_signatures_table(con)

#select_sig(con)
# select_entities(con)
con.close()

