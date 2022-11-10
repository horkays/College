v = [2, 6, 3]
w = [1, 0, 0]
u = [7, 7, 2]

a = 0
for i in range(3):
	a += 3 * (2 * v[i] - w[i]) * 2 * u[i]

print(a)