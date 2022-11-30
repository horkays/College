from Crypto.Util.number import getPrime, inverse, long_to_bytes

q, h = 7638232120454925879231554234011842347641017888219021175304217358715878636183252433454896490677496516149889316745664606749499241420160898019203925115292257, 2163268902194560093843693572170199707501787797497998463462129592239973581462651622978282637513865274199374452805292639586264791317439029535926401109074800
e = 5605696495253720664142881956908624307570671858477482119657436163663663844731169035682344974286379049123733356009125671924280312532755241162267269123486523

def inner_product(a, b):
	x = 0
	for i in range(2):
		x += a[i] * b[i]

	return x

def gauss(a, b):
	if inner_product(a, a) > inner_product(b, b):
		return gauss(b, a)

	m = inner_product(a, b) // inner_product(a, a)

	if m == 0:
		return [a, b]

	for i in range(2):
		b[i] -= m * a[i]

	return gauss(a, b)

def decrypt(q, h, f, g, e):
    a = (f*e) % q
    m = (a*inverse(f, g)) % g
    return m

v = [0, q]
u = [1, h]

x = gauss(u, v)

f = x[0][0]
g = x[0][1]

m = decrypt(q, h, f, g, e)

print(long_to_bytes(m).decode())