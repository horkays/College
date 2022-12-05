from Crypto.PublicKey import RSA
from Crypto.Util.number import *
from factordb.factordb import FactorDB
import math
import sympy

p = 28151

for i in range(2, p):
	chk = 1
	for j in range(1, p - 1):
		if pow(i, j, p) == 1:
			chk = 0
			break
	if chk == 1:
		print(i)
		break
