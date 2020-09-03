# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc

import helloworld_pb2
import helloworld_pb2_grpc

import os

class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        #print ('%s'% request.name)
        #print ("prepe: " + request.name)
        
        #os.remove() 
        #f = open('PSconfig.txt')
        #f.write(' \n' + request.name2 + ' \n')
        #os.system("python3 DPS_Control.py PSconfig.txt --port /dev/ttyUSB0 --speed 9600")

        #obtener respuesta: a- fuente 1 configurada exitosamente. b- fuente 2 configurada exitosamente. c- error  
        #en lugar de -hello-
        return helloworld_pb2.HelloReply(message='La fuente 1 ha sido configurada exitosamente.\nDetalle: %s' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()


# cd ~/Escritorio/ITeDA/grpc/examples/python/helloworld
# source venv/bin/activate
# python3 greeter_server.py
