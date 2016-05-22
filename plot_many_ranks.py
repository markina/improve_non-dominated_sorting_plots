from matplotlib import pyplot as plt
from collections import namedtuple


class T:
    def __init__(self, n, m, k, t):
        self.n = n
        self.m = m
        self.k = k
        self.t = t

    def __repr__(self):
        return repr((self.n, self.m, self.k, self.t))


N = 100000
M = 7

name = "cube"
prefix = "_result.txt"

# full_name = name + "_" + str(N) + "_" + str(M) + "_" + str(A) + prefix
full_name = name + "_" + str(N) + "_" + str(M) + prefix

al = []
max_k = -1

with open("experiments/" + full_name) as f:
    for line in f:
        n, m, k = [int(i) for i in line.split()]
        max_k = max(max_k, k)
        Tf = float(next(f))
        Tb = float(next(f))
        al.append(T(n, m, k, (Tb - Tf) / max(Tf, Tb)))

print("Cnt ranks = " + str(max_k))

plt.title(name + " M = " + str(M))

plt.semilogx([1], [1], 'k.')


plt.semilogx(
    [a.n for a in al if a.m == M and 1 < a.k <= 2],
    [a.t for a in al if a.m == M and 1 < a.k <= 2],
    'ro', label='m = ' + str(M) + ',  1 < k <= 2')

plt.semilogx(
    [a.n for a in al if a.m == M and 2 < a.k <= 4],
    [a.t for a in al if a.m == M and 2 < a.k <= 4],
    'o', color=(1.0, 0.75, 0.0), label='m = ' + str(M) + ',  2 < k <= 4')

plt.semilogx(
    [a.n for a in al if a.m == M and 4 < a.k <= 8],
    [a.t for a in al if a.m == M and 4 < a.k <= 8],
    'o', color=(1, 1, 0), label='m = ' + str(M) + ',  4 < k <= 8')

plt.semilogx(
    [a.n for a in al if a.m == M and 8 < a.k <= 16],
    [a.t for a in al if a.m == M and 8 < a.k <= 16],
    'go', label='m = ' + str(M) + ',  8 < k <= 16')

plt.semilogx(
    [a.n for a in al if a.m == M and 16 < a.k <= 32],
    [a.t for a in al if a.m == M and 16 < a.k <= 32],
    'co', label='m = ' + str(M) + ', 16 < k <= 32')

plt.semilogx(
    [a.n for a in al if a.m == M and 32 < a.k <= 64],
    [a.t for a in al if a.m == M and 32 < a.k <= 64],
    'bo', label='m = ' + str(M) + ', 32 < k <= 64')

plt.semilogx(
    [a.n for a in al if a.m == M and a.k > 64],
    [a.t for a in al if a.m == M and a.k > 64],
    'mo', label='m = ' + str(M) + ', k > 64')


plt.axhline(0, color='black')

plt.xlabel('N')
plt.ylabel('t')
plt.legend(loc=4)
plt.xlim(0, 110000)
plt.ylim(-1, 1)
# plt.savefig("ex.png")
# plt.savefig('foo.png', bbox_inches='tight')

plt.show()


