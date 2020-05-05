#!/usr/bin/env python
import libnum

print libnum.gcd(66528, 52920)
print libnum.xgcd(26513, 32321)[:-1]
print min(11 % 6, 8146798528947 % 17)
print pow(273246787654, 65536, 65537)
print libnum.invmod(3, 13)
