import math

def inner_product(a, b):
	c = 0.0
	for i in range(4):
		c += a[i] * b[i]

	return c

v = [0] * 4
v[0] = [4.0, 1.0, 3.0, -1.0]
v[1] = [2.0, 1.0, -3.0, 4.0]
v[2] = [1.0, 0.0, -2.0, 7.0]
v[3] = [6.0, 2.0, 9.0, -5.0]

for i in range(4):
	for j in range(i):
		size = inner_product(v[j], v[j])
		inner = inner_product(v[i], v[j])

		for k in range(4):
			v[i][k] -= v[j][k] * inner / size

print(v[3][1])