# various class for LNContract App

from enum import Enum
import datetime


class MonetaryUnit(Enum):
    SATOSHI=1
    BITCOIN=2
    DOLLAR=3

class ConsiderationType():
    def __init__(self, description="A nominal consideration", qty=1):
        self.description=description
        self.qty=qty

class Good(ConsiderationType):
    def __init__(self, part_number=None, description="A nominal good", qty=1):
        super().__init__(description=description, qty=qty)
        self.part_number = part_number
        print("Good created:")
        print(self.description)
        print(self.part_number)
        print(self.qty)

class MonetaryPayment(ConsiderationType):
    def __init__(self, description="A nominal monetary payment", qty=0, unit=MonetaryUnit.SATOSHI):
        super().__init__(description=description, qty=qty)
        self.unit=unit
        print("MonetaryPayment created:")
        print(self.description)
        print(self.qty) #qty is the amount of the monetary units, e.g. 500 Satoshis.  
        print(self.unit.name)

class Service(ConsiderationType):
    def __init__(self, description="A nominal service", qty=1):
        super().__init__(description=description, qty=qty)
        print("Service created:")
        print(self.description)
        print(self.qty)

class Consideration():
    def __init__(self, type=MonetaryPayment(), due_date=datetime.datetime.now()):
        self.type=type  # this will be a ConsiderationType, either Good, MonetaryPayment or Service
        self.due_date=due_date
        print("Consideration Object:")
        print(self.type.description)
        print(self.due_date)

class Party():
    def __init__(self, id, name, ln_node, kcomm_server):
        # need id, name, ln_node, kcomm_server
        self.id=id
        self.name=name
        self.ln_node=ln_node
        self.kcom_server=kcomm_server

class LnNode():
    def __init__(self, id, address, tls_path, macaroon_path, status="" ):
        self.id=id
        self.address=address
        self.tls_path=tls_path
        self.macaroon_path=macaroon_path
        self.status=status

class KCommServer():
    def __init__(self, id, address, tls_cert, status=""):
        self.id=id
        self.address=address
        self.tls_cert=tls_cert
        self.status=status



# if __name__ == "__main__":
#     import sys
#     g = Good()
#     gg = Good(part_number="x1q44", description="An upgrade to a nomimal good", qty=3)
  
#     # s=MonetaryPayment()
#     # b=MonetaryPayment(description="A Bitcoin payment", qty=1, unit=MonetaryUnit.BITCOIN)
#     # d=MonetaryPayment(description="A Dollar payment", qty=2, unit=MonetaryUnit.DOLLAR)

#     sv = Service()
#     sv1 = Service(description="An improved servce", qty=2)

#     # review = Service(description="Legal review of case", qty=1)
#     # due = datetime.datetime(2022, 5, 16)
#     # con = Consideration(type=review, due_date=due)
