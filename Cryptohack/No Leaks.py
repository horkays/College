import time
from Crypto.Util.number import *
import hashlib
from pwn import *
import json
import codecs
import base64

r = remote('socket.cryptohack.org', 13370)

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

r.recvline()

flag_len = len("crypto{????????????}")

poss = []

for i in range(20):
	line = [i for i in range(256)]
	poss.append(line)

while 1:

	json_send({
		"msg": "request"
		})
	res = json_recv()
	if not "ciphertext" in res:
		continue

	ct = base64.b64decode(res["ciphertext"].encode())
	
	for i in range(20):
		if ct[i] in poss[i]:
			poss[i].remove(ct[i])

	current = ""
	for i in range(20):
		current += str(len(poss[i])) + " "

	print(current)

	tot = 0
	for i in range(20):
		tot += len(poss[i])

	if tot == 20:
		break

flag = ""
for i in range(20):
	flag += chr(poss[i][0])

print(flag)

r.interactive()