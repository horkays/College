import time
from Crypto.Util.number import *
import hashlib
from pwn import *
import json
import codecs

r = remote('socket.cryptohack.org', 13372)

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

r.recvline()

flag_len = len(b'crypto{????????????????????}')

while 1:
	json_send({
		"option": "get_flag"
		})
	enc_flag = bytes.fromhex(json_recv()["encrypted_flag"])
	json_send({
		"option": "encrypt_data",
		"input_data": bytes.hex(b"\x00" * flag_len)
		})
	key = bytes.fromhex(json_recv()["encrypted_data"])

	pt = xor(enc_flag, key)
	if pt[:6] == b"crypto":
		print(pt)
		break

r.interactive()