#!/usr/bin/env python
from pwn import xor
from PIL import Image

#1
print 'crypto{%s}' % (xor('label', chr(13)))

#2
enc = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'.decode('hex')
keys = xor('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'.decode('hex'), 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'.decode('hex'))
print xor(enc, keys)

#3
enc = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'.decode('hex')
for i in range(256):
    if xor(enc, chr(i)).startswith('crypto'):
        print xor(enc, chr(i))
        break

#4
enc = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'.decode('hex')
# print xor(enc, 'crypto{')
print xor(enc, 'myXORkey')

#5
img1 = Image.open('flag.png')
img2 = Image.open('lemur.png')
img3 = Image.new('RGB', img1.size)
data = img3.load()
pixels = []
for i in range(img1.size[0]):
    for j in range(img1.size[1]):
        a,b,c = img1.getpixel((i, j))
        d,e,f = img2.getpixel((i, j))
        data[i, j] = (a^d, b^e, c^f)
img3.save('result.png')
