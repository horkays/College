import math

for i in range(2048):
	if math.perm(2048, i) / (2048 ** i) < 0.25:
		print(i)
		break