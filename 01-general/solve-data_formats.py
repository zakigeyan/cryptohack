#!/usr/bin/env python
from Crypto.PublicKey import RSA

#1
keypair = open('keypair.pem').read()
print RSA.importKey(keypair).d

#2
# openssl x509 -in 2048b-rsa-example-cert.der -inform der -noout -text
n = int('''
00:b4:cf:d1:5e:33:29:ec:0b:cf:ae:76:f5:fe:2d:
c8:99:c6:78:79:b9:18:f8:0b:d4:ba:b4:d7:9e:02:
52:06:09:f4:18:93:4c:d4:70:d1:42:a0:29:13:92:
73:50:77:f6:04:89:ac:03:2c:d6:f1:06:ab:ad:6c:
c0:d9:d5:a6:ab:ca:cd:5a:d2:56:26:51:e5:4b:08:
8a:af:cc:19:0f:25:34:90:b0:2a:29:41:0f:55:f1:
6b:93:db:9d:b3:cc:dc:ec:eb:c7:55:18:d7:42:25:
de:49:35:14:32:92:9c:1e:c6:69:e3:3c:fb:f4:9a:
f8:fb:8b:c5:e0:1b:7e:fd:4f:25:ba:3f:e5:96:57:
9a:24:79:49:17:27:d7:89:4b:6a:2e:0d:87:51:d9:
23:3d:06:85:56:f8:58:31:0e:ee:81:99:78:68:cd:
6e:44:7e:c9:da:8c:5a:7b:1c:bf:24:40:29:48:d1:
03:9c:ef:dc:ae:2a:5d:f8:f7:6a:c7:e9:bc:c5:b0:
59:f6:95:fc:16:cb:d8:9c:ed:c3:fc:12:90:93:78:
5a:75:b4:56:83:fa:fc:41:84:f6:64:79:34:35:1c:
ac:7a:85:0e:73:78:72:01:e7:24:89:25:9e:da:7f:
65:bc:af:87:93:19:8c:db:75:15:b6:e0:30:c7:08:
f8:59'''.strip().replace(':', '').replace('\n', ''), 16)
print n
