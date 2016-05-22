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
M = 30

name = "2fronts"
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
    [a.n for a in al if a.m == M and a.k == 1],
    [a.t for a in al if a.m == M and a.k == 1],
    'ro', label='m = ' + str(M) + ', k = 1')

# plt.semilogx(
#     [a.n for a in al if a.m == M and a.k == 2],
#     [a.t for a in al if a.m == M and a.k == 2],
#     'o', color=(1.0, 0.75, 0.0), label='m = ' + str(M) + ', k = 2')

# plt.semilogx(
#     [a.n for a in al if a.m == M and a.k == 3],
#     [a.t for a in al if a.m == M and a.k == 3],
#     'o', color=(1, 1, 0), label='m = ' + str(M) + ', k = 3')

# plt.semilogx(
#     [a.n for a in al if a.m == M and a.k == 4],
#     [a.t for a in al if a.m == M and a.k == 4],
#     'go', label='m = ' + str(M) + ', k = 4')
#
# plt.semilogx(
#     [a.n for a in al if a.m == M and a.k == 5],
#     [a.t for a in al if a.m == M and a.k == 5],
#     'co', label='m = ' + str(M) + ', k = 5')
#
# plt.semilogx(
#     [a.n for a in al if a.m == M and a.k == 6],
#     [a.t for a in al if a.m == M and a.k == 6],
#     'bo', label='m = ' + str(M) + ', k = 6')
#
# plt.semilogx(
#     [a.n for a in al if a.m == M and a.k == 7],
#     [a.t for a in al if a.m == M and a.k == 7],
#     'mo', label='m = ' + str(M) + ', k = 7')
#
# plt.semilogx(
#     [a.n for a in al if a.m == M and a.k == 8],
#     [a.t for a in al if a.m == M and a.k == 8],
#     'ko', label='m = ' + str(M) + ', k = 8')
#
# plt.semilogx(
#     [a.n for a in al if a.m == M and a.k == 9],
#     [a.t for a in al if a.m == M and a.k == 9],
#     'o', color=(0.5, 0.5, 0.5), label='m = ' + str(M) + ', k = 9')
#
# plt.semilogx(
#     [a.n for a in al if a.m == M and a.k == 10],
#     [a.t for a in al if a.m == M and a.k == 10],
#     'wo', label='m = ' + str(M) + ', k = 10')


plt.axhline(0, color='black')

plt.xlabel('N')
plt.ylabel('t')
plt.legend(loc=4)
plt.xlim(0, 110000)
plt.ylim(-1, 1)
plt.show()

