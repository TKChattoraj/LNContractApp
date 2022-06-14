# db methods
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


def select_sig(con):
    query=QSqlQuery(con)
    query_text="SELECT * FROM signatures WHERE id=1"
    
    query.exec(query_text)
    query.first()
    sig_hash_index=query.record().indexOf("sig_hash")
    print(query.value(sig_hash_index))
    query.finish()

def select_entities(con):
    query=QSqlQuery(con)
    query_text="SELECT id, name, ln_node_id, kcomm_server_id, party, status FROM entities"
    query.exec(query_text)
    return query

def select_pn(con):
    query=QSqlQuery(con)
    query_text="SELECT id, part_number, description, status FROM goods"
    query.exec(query_text)
    return query

def select_sn(con):
    query=QSqlQuery(con)
    query_text="SELECT id, service_number, description, status FROM services"
    query.exec(query_text)
    return query

def select_contracts(con):
    query=QSqlQuery(con)
    query_text="SELECT id, contract_no, party_id, counterparty_id, description, status FROM contracts"
    query.exec(query_text)
    return query

def select_last_id(con, table):
    query=QSqlQuery(con)
    # think about injection risk?  table doesn't come from user
    # but is internal to the app
    query_text="SELECT id FROM {} WHERE id = (SELECT MAX(id) FROM {})".format(table, table)
    query.exec(query_text)
    query.first()
    return query.value(0)

def select_party_with_id(con, id):
    query=QSqlQuery(con)
    # think about injection risk?  table doesn't come from user
    # but is internal to the app
    query_text="SELECT id, name, ln_node_id, kcomm_server_id, party FROM entities WHERE id={}".format(id)
    query.exec(query_text)
    print("last query")
    print(query.lastQuery())
    print ("party query active?")
    print(query.isActive())
    query.next()
    return query

def select_ktext(con,k_id):
    query=QSqlQuery(con)
    # think about injection risk?  table doesn't come from user
    # but is internal to the app
    query_text="SELECT filename FROM ktexts WHERE contract_id={}".format(k_id)
    query.exec(query_text)
    print("last query")
    print(query.lastQuery())
    print ("party query active?")
    print(query.isActive())
    query.next()
    return query

def select_ln_node(con, id):
    query=QSqlQuery(con)
    # think about injection risk?  table doesn't come from user
    # but is internal to the app
    query_text="SELECT id, address, tls_path, macaroon_path, status FROM ln_nodes WHERE id={}".format(id)
    query.exec(query_text)
    print("last query")
    print(query.lastQuery())
    print ("party query active?")
    print(query.isActive())
    query.next()
    return query

def select_kcomm(con, id):
    query=QSqlQuery(con)
    # think about injection risk?  table doesn't come from user
    # but is internal to the app
    query_text="SELECT id, address, tls_cert, status FROM kcomm_servers WHERE id={}".format(id)
    query.exec(query_text)
    print("last query")
    print(query.lastQuery())
    print ("party query active?")
    print(query.isActive())
    query.next()
    return query


def insert_goods_table(con, data):
    query_text="INSERT INTO goods (part_number, description, status) VALUES (?, ?, ?)"
    insert_in_table(con, query_text, data)

def insert_services_table(con, data):
    query_text="INSERT INTO services (service_number, description, status) VALUES (?, ?, ?)"
    insert_in_table(con, query_text, data)

def insert_sale_goods(con, data):
    query_text="INSERT INTO sale_goods (contract_id, goods_id, entity_id, quantity, due_date, tender, description, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    insert_in_table(con, query_text, data)

def insert_sale_service(con, data):
    query_text="INSERT INTO sale_services (contract_id, service_id, entity_id, quantity, due_date, tender, description, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    insert_in_table(con, query_text, data)

def insert_ln_nodes_table(con, data):
    query_text="INSERT INTO ln_nodes (address, tls_path, macaroon_path, status) VALUES (?, ?, ?, ?)"
    insert_in_table(con, query_text, data)

def insert_kcomm_servers_table(con, data):
    query_text="INSERT INTO kcomm_servers (address, tls_cert, status) VALUES (?, ?, ?)"
    insert_in_table(con, query_text, data)

def insert_entities_table(con, data):
    query_text="INSERT INTO entities (name, ln_node_id, kcomm_server_id, party, status) VALUES (?, ?, ?, ?, ?)"
    insert_in_table(con, query_text, data)

def insert_contract_doc(con, data):
    query_text= "INSERT INTO ktexts (filename, contract_id) VALUES (?, ?)"
    insert_in_table(con,query_text,data)

def insert_contract(con, data):
    query_text="INSERT INTO contracts (contract_no, party_id, counterparty_id, description, status) VALUES (?, ?, ?, ?, ?)"
    insert_in_table(con, query_text, data)

def insert_in_table(con, query_text, data):
    print(f"query_texts: {query_text}")
    print(f"data: {data}")
    query=QSqlQuery(con)
    query.prepare(query_text)
    for t in data:
        for e in t:
            query.addBindValue(e)
        query.exec()

def get_db_id(con, table, column, value):
    
    query=QSqlQuery(con)
    query_text=f"SELECT id FROM {table} WHERE {column} = '{value}'"
    query.exec(query_text)
    query.first()
    id=query.value(0) #returning the value in 0 position of the query
    query.finish()
    return id

def last_row_id(con):
    query=QSqlQuery(con)
    query_text="SELECT last_insert_rowid()"
    query.exec(query_text)
    query.first()
    id=query.value(0)
    query.finish()
    return id