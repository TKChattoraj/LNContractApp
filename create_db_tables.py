from readline import insert_text
import sys
import os
import codecs

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

services= """
    CREATE TABLE IF NOT EXISTS services (
        id INTEGER PRIMARY KEY UNIQUE NOT NULL,
        service_number VARCHAR(40) UNIQUE NOT NULL,
        description VARCHAR(50),
        status VARCHAR(50)
    )
    """
goods="""
    CREATE TABLE IF NOT EXISTS goods (
        id INTEGER PRIMARY KEY UNIQUE NOT NULL,
        part_number VARCHAR(50) UNIQUE NOT NULL,
        description VARCHAR(50),
        status VARCHAR(50)
    )
    """

contracts="""
    CREATE TABLE IF NOT EXISTS contracts (
        id INTEGER PRIMARY KEY UNIQUE NOT NULL,
        contract_no VARCHAR UNIQUE NOT NULL,
        party_id INTEGER,
        counterparty_id INTEGER,
        description VARCHAR(50),
        status VARCHAR(50)
    )
    """

entities="""
    CREATE TABLE IF NOT EXISTS entities (
        id INTEGER PRIMARY KEY UNIQUE NOT NULL,
        name VARCHAR(50) UNIQUE NOT NULL,
        ln_node_id INTEGER,
        kcomm_server_id INTEGER,
        status VARCHAR(50)
    )
    """

ln_nodes="""
    CREATE TABLE IF NOT EXISTS ln_nodes (
        id INTEGER PRIMARY KEY UNIQUE NOT NULL,
        address VARCHAR(50) NOT NULL,
        tls_path VARCHAR(500),
        macaroon_path VARCHAR(500),
        status VARCHAR(50)
    )
    """
kcomm_servers="""
    CREATE TABLE IF NOT EXISTS kcomm_servers (
        id INTEGER PRIMARY KEY UNIQUE NOT NULL,
        address VARCHAR(50) NOT NULL,
        tls_cert VARCHAR(500),
        status VARCHAR(50)
    )
    """
sale_goods="""
    CREATE TABLE IF NOT EXISTS sale_goods (
        id INTEGER PRIMARY KEY UNIQUE NOT NULL,
        contract_id INTEGER NOT NULL,
        goods_id INTEGER NOT NULL,
        entity_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        due_date TEXT NOT NULL,
        tender BOOL NOT NULL,
        description VARCHAR(50),
        status VARCHAR(50)
    )
    """
sale_services="""
    CREATE TABLE IF NOT EXISTS sale_services (
        id INTEGER PRIMARY KEY UNIQUE NOT NULL,
        contract_id INTEGER NOT NULL,
        service_id INTEGER NOT NULL,
        entity_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        due_date TEXT NOT NULL,
        tender BOOL NOT NULL,
        description VARCHAR(50),
        status VARCHAR(50)
    )
    """

monetary_obligations="""
    CREATE TABLE IF NOT EXISTS monetary_obligations (
        id INTEGER PRIMARY KEY UNIQUE NOT NULL,
        contract_id INTEGER NOT NULL,
        amount REAL,
        unit VARCHAR(10) NOT NULL,
        due_date TEXT NOT NULL,
        tender BOOL NOT NULL,
        status VARCHAR(50)
    )
"""

ktexts="""
    CREATE TABLE IF NOT EXISTS ktexts (
        id INTEGER PRIMARY KEY UNIQUE NOT NULL,
        filename VARCHAR(50),
        contract_id INTEGER,
        status VARCHAR(50)
    )
    """

signatures="""
    CREATE TABLE IF NOT EXISTS signatures (
        id INTEGER PRIMARY KEY UNIQUE NOT NULL,
        r VARCHAR(100),
        s VARCHAR(100),
        sig_hash VARCHAR(100),
        ktext_id INTEGER NOT NULL,
        status VARCHAR(50)
    )
    """

# create the required db tables if not already exists
def create_db_tables(con):
    createTableQuery = QSqlQuery(con)
    table_list = [goods, services, contracts, entities, sale_goods, sale_services, monetary_obligations, ln_nodes, kcomm_servers, ktexts, signatures]
    print(con.tables())
    for t in table_list:
        createTableQuery.exec(t)     
    print(con.tables())

# application    

con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("lncontract_db.sqlite")

# Open the connection
if not con.open():
    print("Database Error: %s" % con.lastError().databaseText())
    sys.exit(1)
create_db_tables(con)
