import math
from matplotlib import pyplot as plt


class T:
    def __init__(self, n, m, k, t):
        self.n = n
        self.m = m
        self.k = k
        self.t = t

    def __repr__(self):
        return repr((self.n, self.m, self.k, self.t))


N = 100000
M = 30

name = "1fronts"
prefix = "_result.txt"

full_name = name + "_" + str(N) + "_" + str(M) + prefix

al_f = {}
max_k = -1

with open("experiments-3/" + full_name) as f:
    for line in f:
        n, m, k = [int(i) for i in line.split()]
        max_k = max(max_k, k)
        Tf = float(next(f))
        Tb = float(next(f))
        Th = float(next(f))
        if n not in al_f:
            al_f[n] = []
        al_f[n].append(T(n, m, k, (Th - Tf) / max(Tf, Th)))

print("Cnt ranks = " + str(max_k))

lp = 0.25
rp = 0.75

al_new_f = {}
for (n, ls) in al_f.items():
    al_new_f[n] = sorted(ls, key=lambda e: e.t)

al_f = []
for (n, ls) in al_new_f.items():
    sz = len(ls)
    left = int(sz * lp)
    right = int(math.ceil(sz * rp))
    al_f.extend(ls[left:right + 1])


plt.title(name + " M = " + str(M) + " " + str(lp * 100) + "%")

plt.semilogx([1], [1], 'k.')

# plt.semilogx(
#     [a.n for a in al_f if a.m == M],
#     [a.t for a in al_f if a.m == M],
#     'ro', label='(Th-Tf)/max')


############################################################


al_b = {}
max_k = -1

with open("experiments-3/" + full_name) as f:
    for line in f:
        n, m, k = [int(i) for i in line.split()]
        Tf = float(next(f))
        Tb = float(next(f))
        Th = float(next(f))
        if n not in al_b:
            al_b[n] = []
        al_b[n].append(T(n, m, k, (Th - Tb) / max(Th, Tb)))


al_new_b = {}
for (n, ls) in al_b.items():
    al_new_b[n] = sorted(ls, key=lambda e: e.t)

al_b = []
for (n, ls) in al_new_b.items():
    sz = len(ls)
    left = int(sz * lp)
    right = int(math.ceil(sz * rp))
    al_b.extend(ls[left:right + 1])


plt.title(name + " M = " + str(M) + " " + str(lp * 100) + "%")

plt.semilogx([1], [1], 'k.')
#
# plt.semilogx(
#     [a.n for a in al_b if a.m == M],
#     [a.t for a in al_b if a.m == M],
#     'bo', label='(Th-Tb)/max')

################################

al = {}

with open("experiments-3/" + full_name) as f:
    for line in f:
        n, m, k = [int(i) for i in line.split()]
        Tf = float(next(f))
        Tb = float(next(f))
        Th = float(next(f))
        if n not in al:
            al[n] = []
        al[n].append(T(n, m, k, (Tb - Tf) / max(Tf, Tb)))

al_new = {}
for (n, ls) in al.items():
    al_new[n] = sorted(ls, key=lambda e: e.t)

al = []
for (n, ls) in al_new.items():
    sz = len(ls)
    left = int(sz * lp)
    right = int(math.ceil(sz * rp))
    al.extend(ls[left:right + 1])


plt.title(name + " M = " + str(M) + " " + str(lp * 100) + "%")

plt.semilogx([1], [1], 'k.')

plt.semilogx(
    [a.n for a in al if a.m == M],
    [a.t for a in al if a.m == M],
    'ro', label='(Tb-Tf)/max')

################################

al_m = {}

with open("experiments-3/" + full_name) as f:
    for line in f:
        n, m, k = [int(i) for i in line.split()]
        Tf = float(next(f))
        Tb = float(next(f))
        Th = float(next(f))
        Tm = min(Tb, Tf)
        if n not in al_m:
            al_m[n] = []
        al_m[n].append(T(n, m, k, (Th - Tm) / max(Tm, Th)))

al_new_m = {}
for (n, ls) in al_m.items():
    al_new_m[n] = sorted(ls, key=lambda e: e.t)

al_m = []
for (n, ls) in al_new_m.items():
    sz = len(ls)
    left = int(sz * lp)
    right = int(math.ceil(sz * rp))
    al_m.extend(ls[left:right + 1])


plt.title(name + " M = " + str(M) + " " + str(lp * 100) + "%")

plt.semilogx([1], [1], 'k.')

plt.semilogx(
    [a.n for a in al_m if a.m == M],
    [a.t for a in al_m if a.m == M],
    'go', label='(Th-Tm)/max')

################################

plt.axhline(0, color='black')

plt.xlabel('N')
plt.ylabel('t')
plt.legend(loc=4)
plt.xlim(0, 110000)
plt.ylim(-1, 1)
plt.show()
