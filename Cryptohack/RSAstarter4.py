p = 857504083339712752489993810777
q = 1029224947942998075080348647219

e = 65537

a = (p - 1) * (q - 1)
N = p * q

d = pow(e, -1, a)

print(d)