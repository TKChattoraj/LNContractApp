import os

os.makedirs('./counterparty')
mac_file = open(r'./counterparty/macfile.txt', 'w')
mac_file.write("string")
mac_file.close()