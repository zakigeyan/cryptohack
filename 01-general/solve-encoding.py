#!/usr/bin/env python
from pwn import *
from Crypto.Util.number import long_to_bytes
import base64, json

print ''.join(map(chr, [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]))
print '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'.decode('hex')
print base64.b64encode('72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'.decode('hex'))
print long_to_bytes(11515195063862318899931685488813747395775516287289682636499965282714637259206269)

HOST = 'socket.cryptohack.org'
PORT = 13377
p = remote(HOST, PORT, level='warn')
while True:
    try:
        c1 = json.loads(p.recvline())
        if c1['type']=='base64':
            pload = base64.b64decode(c1['encoded'])
        elif c1['type']=='hex':
            pload = c1['encoded'].decode('hex')
        elif c1['type']=='rot13':
            pload = c1['encoded'].encode('rot13')
        elif c1['type']=='bigint':
            pload = long_to_bytes(eval(c1['encoded']))
        elif c1['type']=='utf-8':
            pload = ''.join(map(chr, c1['encoded']))
        pload = {'decoded': pload}
        p.sendline(json.dumps(pload))
    except:
        print c1['flag']
        break
