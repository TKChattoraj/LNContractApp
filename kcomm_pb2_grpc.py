# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import kcomm_pb2 as kcomm__pb2


class KCommStub(object):
    """Service definition
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Transfer_Macaroon = channel.unary_unary(
                '/KComm/Transfer_Macaroon',
                request_serializer=kcomm__pb2.Inbound_Mac.SerializeToString,
                response_deserializer=kcomm__pb2.Mac_Response.FromString,
                )


class KCommServicer(object):
    """Service definition
    """

    def Transfer_Macaroon(self, request, context):
        """Method to receive Macaroon from counterparty appear
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KCommServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Transfer_Macaroon': grpc.unary_unary_rpc_method_handler(
                    servicer.Transfer_Macaroon,
                    request_deserializer=kcomm__pb2.Inbound_Mac.FromString,
                    response_serializer=kcomm__pb2.Mac_Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'KComm', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class KComm(object):
    """Service definition
    """

    @staticmethod
    def Transfer_Macaroon(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/KComm/Transfer_Macaroon',
            kcomm__pb2.Inbound_Mac.SerializeToString,
            kcomm__pb2.Mac_Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
