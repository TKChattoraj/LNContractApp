import lightning_pb2 as ln
import lightning_pb2_grpc as lnrpc

import KComm_pb2_grpc
import KComm_pb2

import grpc
import os
import codecs

import KComm_server as kcomm

# Start the server
############ 
# Somehow we need to start the counterparty's server
# and then continue on.
############



# Due to updated ECDSA generated tls.cert we need to let gprc know that
# we need to use that cipher suite otherwise there will be a handhsake
# error when we communicate with the lnd rpc server.
os.environ["GRPC_SSL_CIPHER_SUITES"] = 'HIGH+ECDSA'


# Connect to Alice

# build the TLS credentials:# Normally Lnd cert is at ~/.lnd/tls.cert on Linux and
# ~/Library/Application Support/Lnd/tls.cert on Mac.
# That is if there is a local LN node.  
# Here we are using Polar and so the TLS cert is located at
# /home/tarun/.polar/networks/1/volumes/lnd/alice/tls.cert'

cert = open(os.path.expanduser('/home/tarun/.polar/networks/1/volumes/lnd/alice/tls.cert'), 'rb').read()

cert_creds = grpc.ssl_channel_credentials(cert)

# Build the meta data for the macaroon credentials:
# Normally Lnd admin macaroon is at ~/.lnd/data/chain/bitcoin/simnet/admin.macaroon on Linux and
# ~/Library/Application Support/Lnd/data/chain/bitcoin/simnet/admin.macaroon on Mac.  
# That is if there is a local LN node.
# Here we are using Polar and so the macaroon will be located at: 
# /home/tarun/.polar/networks/1/volumes/lnd/alice/data/chain/bitcoin/regtest/admin.macaroon

with open(os.path.expanduser('/home/tarun/.polar/networks/1/volumes/lnd/alice/data/chain/bitcoin/regtest/admin.macaroon'), 'rb') as f:
    macaroon_bytes = f.read()
    macaroon = codecs.encode(macaroon_bytes, 'hex')

# Metadata callback
def metadata_callback(context, callback):
    # for more info see grpc docs
    callback([('macaroon', macaroon)], None)

auth_creds = grpc.metadata_call_credentials(metadata_callback)


# Combine the certa dn macaroon auth credentials.
# Every call will be encrypted and authenticated.

combined_creds = grpc.composite_channel_credentials(cert_creds, auth_creds)


#127.0.0.1:10004.
channel = grpc.secure_channel('localhost:10004', combined_creds, options=(('grpc.enable_http_proxy', 0),('grpc.enable_https_proxy', 0)))
stub = lnrpc.LightningStub(channel)


# Retrieve and display the wallet balance.
response = stub.WalletBalance(ln.WalletBalanceRequest())
print(response.total_balance)


# # Get Info of node.
# request = ln.GetInfoRequest()
# response = stub.GetInfo(request)
# print(response)

# # List Peers
# request = ln.ListPeersRequest(
#     latest_error=True
# )
# response = stub.ListPeers(request)
# print(response)



# # List Permissions.
# request = ln.ListPermissionsRequest()
# response = stub.ListPermissions(request)
# print(response)

# Fee Report
request = ln.FeeReportRequest()
response = stub.FeeReport(request)
print(response)


# Prepare Bake Macaroon request
permissions = [{"entity":"info", "action":"read"}, {"entity":"offchain", "action":"read"}]
key = 0xffffffffffffffff
#key = 1
external_permissions = False
request = ln.BakeMacaroonRequest(
    permissions=permissions,
    root_key_id=key,
    allow_external_permissions=external_permissions
)
# The response from the request is a strng hex macaroon
response= stub.BakeMacaroon(request)
print(response)


# request = ln.ListMacaroonIDsRequest()
# response = stub.ListMacaroonIDs(request)
# print(response)

# Connect with the counterparty server

def transfer_macaroon(stub, mac_hex_str):
    mac_request = KComm_pb2.Inbound_Mac(MacStr=mac_hex_str)
    result = stub.Transfer_Macaroon(mac_request)
    print(result.MacResp)


    


port = input("Enter port number of counterparty:  (50051)")
with grpc.insecure_channel('localhost:'+port) as channel:
    stub = KComm_pb2_grpc.KCommStub(channel)
    transfer_macaroon(stub, response.macaroon)


print("Finished.")