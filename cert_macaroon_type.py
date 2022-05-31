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
print("Cert")
print(cert)
print(type(cert))


# cert_creds = grpc.ssl_channel_credentials(cert)

# Build the meta data for the macaroon credentials:
# Normally Lnd admin macaroon is at ~/.lnd/data/chain/bitcoin/simnet/admin.macaroon on Linux and
# ~/Library/Application Support/Lnd/data/chain/bitcoin/simnet/admin.macaroon on Mac.  
# That is if there is a local LN node.
# Here we are using Polar and so the macaroon will be located at: 
# /home/tarun/.polar/networks/1/volumes/lnd/alice/data/chain/bitcoin/regtest/admin.macaroon

with open(os.path.expanduser('/home/tarun/.polar/networks/1/volumes/lnd/alice/data/chain/bitcoin/regtest/admin.macaroon'), 'rb') as f:
    macaroon_bytes = f.read()
    print("macaroon bytes")
    print(macaroon_bytes)
    print(type(cert))
    print("macaroon encode")
    macaroon = codecs.encode(macaroon_bytes, 'hex')
    print(macaroon)
    print(type(macaroon))

