#!/usr/bin/python

#Writing this so I can stress networking adapters and networks to their limit, using nothing but a few script, It's multithreaded and sends pregenerated data, so IO and CPU should not bottleneck.

#Usage example: python networktest.py --target=192.169.1.10 --threads=8


import sys
from thread import*
import socket
from random import randint

args=sys.argv
#Default settings
class networktest():
    def __init__(self):
        self.target=''
        self.bs=1024
        self.threads=2
        self.port=3333
        self.running=False
        self.blockcount=1
        self.s=None
config=networktest()
for arg in args:
    arg=arg.replace(" ", "")
    arglist=arg.split("=")
    if arglist[0].lower()=="--target":
        config.target=arglist[1]
    if arglist[0].lower()=="--bs":
        try:
            config.bs=int(arglist[1])
        except:
            print("bs must be int")
    if arglist[0].lower()=="--threads":
        try:
            config.threads=int(arglist[1])
        except:
            print("threads must be int")


def generateblock():
    block=[]
    print("Generating %sKB of data" % config.bs)
    for i in range (0, config.bs):
        data=str(randint(0,9)) * 1024
        block.append(data)
        data=''
    block=''.join(block)
    return block


config.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (config.target, config.port)
config.s.connect(server_address)
def sendblock(block):
    while config.running==True:   
        config.s.send(block)
        config.blockcount+=1

block=generateblock()

print("Starting network stress test")
config.running=True
for i in range(0, config.threads):
    start_new_thread(sendblock, (block,))
bc=0
while 1:
    if bc != config.blockcount:
        bc=config.blockcount
        print("%s blocks sent" % config.blockcount)




   
