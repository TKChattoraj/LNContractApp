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
from db_initialize_methods import initialize_table

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
    query_text="SELECT id, name, ln_node_id, kcomm_server_id, status FROM entities"
    query.exec(query_text)
    return query

def select_pn(con):
    query=QSqlQuery(con)
    query_text="SELECT id, part_number, description, status FROM goods"
    query.exec(query_text)
    return query

def select_contracts(con):
    query=QSqlQuery(con)
    query_text="SELECT id, contract_no, party_id, counterparty_id, description, status FROM contracts"
    query.exec(query_text)
    return query


def insert_goods_table(con, data):
    query_text="INSERT INTO goods (part_number, description, status) VALUES (?, ?, ?)"
    initialize_table(con, query_text, data)

def insert_sale_goods(con, data):
    query_text="INSERT INTO sale_goods (contract_id, goods_id, entity_id, quantity, due_date, tender, description, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
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

def get_db_id(con,table, column, value):
    
    query=QSqlQuery(con)
    query_text=f"SELECT id FROM {table} WHERE {column} = '{value}'"
    query.exec(query_text)
    query.first()
    id=query.value(0) #returning the value in 0 position of the query
    query.finish()
    return id