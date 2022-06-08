# db initializer methods
import sys
import os
import codecs

from PyQt6.QtCore import QSize, Qt, QByteArray, QVariant
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



# Get the sample tls cert and sample macaroon
# cert = open(os.path.expanduser('/home/tarun/.polar/networks/1/volumes/lnd/alice/tls.cert'), 'rb').read()
# print("Cert")
# print(cert)
# print(type(cert))
# cert_qb=QByteArray(cert)
tls_path="/home/tarun/.polar/networks/1/volumes/lnd/alice/tls.cert"

# with open(os.path.expanduser('/home/tarun/.polar/networks/1/volumes/lnd/alice/data/chain/bitcoin/regtest/admin.macaroon'), 'rb') as f:
#     macaroon_bytes = f.read()
#     print("macaroon bytes")
#     print(macaroon_bytes)
#     print(type(cert))
#     print("macaroon encode")
#     macaroon = codecs.encode(macaroon_bytes, 'hex')
#     print(macaroon)
#     print(type(macaroon))
#     macaroon_qb=QByteArray(macaroon)
macaroon_path="/home/tarun/.polar/networks/1/volumes/lnd/alice/data/chain/bitcoin/regtest/admin.macaroon"
address_port="https://192.168.1.16:8500"
address_port2="https://192.168.1.16:8501"
# initialize the ln_node table
def initialize_ln_node_table(con):
    # Populate the kcomm_server table
    query_text = """
        INSERT INTO ln_nodes (
            address,
            tls_path,
            macaroon_path,
            status
        )
        VALUES (?, ?, ?, ?)
        """
    data = [(address_port, tls_path, macaroon_path, "status1"), (address_port2, tls_path, macaroon_path, "status2")]
    initialize_table(con, query_text, data)


# initialize the kcomm_server table
def initialize_kcomm_servers_table(con):
    query_text ="""
        INSERT INTO kcomm_servers (
            address,
            tls_cert,
            status
        )
        VALUES (?, ?, ?)
        """
    data = [("http://192.168.1.15/", tls_path, "status3"), ("http://192.168.1.12/", tls_path, "status4")]
    initialize_table(con, query_text, data)

# initialize the entities table
def initialize_entities_table(con):
    query_text="INSERT INTO entities (name, ln_node_id, kcomm_server_id, party, status) VALUES (?, ?, ?, ?, ?)"
    
    id1=1
    id2=2
    p1=True
    p2=False
    print("id1: {id1}")
    print("id2: {id2}")
    data=[("Titan", id1, id2, p1, "status7"), ("Champ", id2, id1, p2, "status8")]
    initialize_table(con, query_text, data)

# initialize the contracts table
def initialize_contracts_table(con):
    query_text="INSERT INTO contracts (contract_no, description, party_id, counterparty_id, status) VALUES (?, ?, ?, ?, ?)"
    id1=QVariant(1)
    id2=QVariant(2)
    data =[("K001","contract description", id1, id2, "status6-will likely be enums for active, inactive, complete"),("K002", "contract description2", id2, id1, "status7-will likely be enums for active, inactive, complete")  ]
    initialize_table(con, query_text, data)


# initialize the ktexts table
# Note-the contracts table doesn't exist yet and so need to leave the contracts_id null
def initialize_ktexts_table(con):

    query_text="""
        INSERT INTO ktexts (            
            filename,
            contract_id,
            status
        )
        VALUES (?, ?, ?)
        """
    data = [("contract_file1.txt", 1, "status5"), ("contract_file2.doc", 2, "status5")]
    initialize_table(con, query_text, data)

def initialize_goods_table(con):
    query_text="INSERT INTO goods (part_number, description, status) VALUES (?, ?, ?)"
    data = [("PN001", "goods description 1", "status 8"), ("PN002", "goods description 2", "status9")]
    initialize_table(con, query_text, data)

def initialize_services_table(con):
    query_text="INSERT INTO services (service_number, description, status) VALUES (?, ?, ?)"
    data = [("SN001", "services description 1", "status 8"), ("SN002", "services description 2", "status9")]
    initialize_table(con, query_text, data)

def initialize_monetary_obligations_table(con):
    query_text="INSERT INTO monetary_obligations (contract_id, amount, unit, due_date, tender, status) VALUES (?, ?, ?, ?, ?, ?)"
    amount1=10.20
    amount2=13.99
    data=[(1, amount1, "Satoshi", "5-16-2022", QVariant(False), "status 10"), (2, amount2, "Satoshi", "2-17-2022", QVariant(True), "status 11")]
    initialize_table(con, query_text, data)

def initialize_sale_goods_table(con):
    query_text="INSERT INTO sale_goods (contract_id, goods_id, entity_id, quantity, due_date, tender, description, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    data=[(1, 1, 1, 10, "1-04-2023", QVariant(False), "description 15", "status 19"), (2, 2, 2, 13, "1-04-2022", QVariant(True), "description 15", "status 19")]
    initialize_table(con, query_text, data)

def initialize_sale_services_table(con):
    query_text="INSERT INTO sale_services (contract_id, service_id, entity_id, quantity, due_date, tender, description, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    data=[(1, 1, 1, 10, "1-04-2023", QVariant(False), "description 18", "status 19"), (2, 2, 2, 13, "1-04-2022", QVariant(True), "description 21", "status 20")]
    initialize_table(con, query_text, data)

def initialize_signatures_table(con):
    query_text="INSERT INTO signatures (r, s, sig_hash, ktext_id, status) VALUES (?, ?, ?, ?, ?)"
    data=[("r", "s", "sig_hash", 1, "status 22"), ("rr", "ss", "sig_hash2", 2, "status 23")]
    initialize_table(con, query_text, data)

def initialize_table(con, query_text, data):
    print(f"query_texts: {query_text}")
    print(f"data: {data}")
    query=QSqlQuery(con)
    query.prepare(query_text)
    for t in data:
        for e in t:
            query.addBindValue(e)
        query.exec()
    #love you dad

def select_last_id(con, table):
    query=QSqlQuery(con)
    # think about injection risk?  table doesn't come from user
    # but is internal to the app
    query_text="SELECT id FROM {} WHERE id = (SELECT MAX(id) FROM {})".format(table, table)
    query.exec(query_text)
    query.first()
    return query.value(0)

def last_row_id(con):
    query=QSqlQuery(con)
    query_text="SELECT last_insert_rowid()"
    query.exec(query_text)
    query.first()
    id=query.value(0)
    query.finish()
    return id

# application    

con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("lncontract_db.sqlite")

initialize_methods = [
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
    ]

# Open the connection
if not con.open():
    print("Database Error: %s" % con.lastError().databaseText())
    sys.exit(1)
for m in initialize_methods:
    m(con)

# q=select_last_id(con, "ln_nodes")

# # i=last_row_id(con)
# # print(i)

#print(q)



