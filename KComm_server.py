#Server functionality


from concurrent import futures
import logging
import math
import time

import os

import grpc


import KComm_pb2
import KComm_pb2_grpc

class KCommServicer(KComm_pb2_grpc.KCommServicer):
    def Transfer_Macaroon(self, request, context):
        mac_string = request.MacStr
        print(mac_string)
        # save macaroon string to a file

        if not os.path.exists('./counterparty'):
            os.makedirs('./counterparty')
        mac_file = open(r"./counterparty/macfile.txt", "w")
        mac_file.write(mac_string)
        mac_file.close()
        print("mac_file closed")

        # read macaroon string from the file
        mac_file_read=open(r"./counterparty/macfile.txt", "r")
        macaroon_r = mac_file_read.read()
        print("macaroon read: ")
        print(macaroon_r)
        mac_file_read.close()


        return KComm_pb2.Mac_Response(MacResp="Got it!")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    KComm_pb2_grpc.add_KCommServicer_to_server(KCommServicer(), server)

    # Get the port for the server
    port = input("Enter the port number: (50051):")

    #server.add_insecure_port('[::]:50051')
    server.add_insecure_port('[::]:'+port)
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
