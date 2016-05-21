from matplotlib import pyplot as plt
from collections import namedtuple


# постоение графика по name N M

class T:
    def __init__(self, n, m, k, t):
        self.n = n
        self.m = m
        self.k = k
        self.t = t

    def __repr__(self):
        return repr((self.n, self.m, self.k, self.t))


N = 100000
M = 10

name = "cube"
prefix = "_result.txt"

# full_name = name + "_" + str(N) + "_" + str(M) + "_" + str(A) + prefix
full_name = name + "_" + str(N) + "_" + str(M) + prefix

al = []

with open("experiments/" + full_name) as f:
    for line in f:
        n, m, k = [int(i) for i in line.split()]
        Tf = float(next(f))
        Tb = float(next(f))
        al.append(T(n, m, k, (Tb - Tf) / max(Tf, Tb)))

plt.title(name + " M = " + str(M))

plt.semilogx([1], [1], 'k.')  # это костыть, пусть пока будет


# plt.semilogx(
#     [a.n for a in al if a.m == 10 and a.k == 0],
#     [a.t for a in al if a.m == 10 and a.k == 0],
#     'ro', label='m = 10, k = 1')
#
# plt.semilogx(
#     [a.n for a in al if a.m == 10 and a.k == 1],
#     [a.t for a in al if a.m == 10 and a.k == 1],
#     'o', color=(1.0, 0.75, 0.0), label='m = 10, k = 2')
#
# plt.semilogx(
#     [a.n for a in al if a.m == 10 and a.k == 2],
#     [a.t for a in al if a.m == 10 and a.k == 2],
#     'o', color=(1, 1, 0), label='m = 10, k = 3')
#
# plt.semilogx(
#     [a.n for a in al if a.m == 10 and a.k == 3],
#     [a.t for a in al if a.m == 10 and a.k == 3],
#     'go', label='m = 10, k = 4')
#
# plt.semilogx(
#     [a.n for a in al if a.m == 10 and a.k == 4],
#     [a.t for a in al if a.m == 10 and a.k == 4],
#     'co', label='m = 10, k = 5')

plt.semilogx(
    [a.n for a in al if a.m == 10 and a.k == 6],
    [a.t for a in al if a.m == 10 and a.k == 6],
    'mo', label='m = 10, k = 7')


plt.axhline(0, color='black')

plt.xlabel('N')
plt.ylabel('t')
plt.legend(loc=4)
plt.xlim(0, 110000)
plt.ylim(-1, 1)
plt.show()
