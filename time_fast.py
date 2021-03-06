from matplotlib import pyplot as plt


class T:
    def __init__(self, n, m, k, t, Tf, Tb):
        self.n = n
        self.m = m
        self.k = k
        self.t = t
        self.Tf = Tf
        self.Tb = Tb

    def __repr__(self):
        return repr((self.n, self.m, self.k, self.t))


N = 100000
M = 20
zoom = 1E6

name = "cube"
prefix = "_result.txt"

full_name = name + "_" + str(N) + "_" + str(M) + prefix

al = []

map_cnt = {}
map_sum_fast = {}

with open("experiments/" + full_name) as f:
    for line in f:
        n, m, k = [int(i) for i in line.split()]
        Tf = float(next(f))
        Tb = float(next(f))
        al.append(T(n, m, k, (Tb - Tf) / max(Tf, Tb), Tf, Tb))
        if n in map_cnt:
            map_cnt[n] += 1
            map_sum_fast[n] += Tf
        else:
            map_cnt[n] = 1
            map_sum_fast[n] = Tf

map_average_fast = {}

for (i, x) in map_cnt.items():
    map_average_fast[i] = map_sum_fast[i] / x

plt.title(name + " M = " + str(M) + " - time")

plt.semilogx(
    [a.n for a in al],
    [a.Tf - map_average_fast[a.n] for a in al],
    'ro', label='fast')

plt.semilogx(
    [i for i in map_average_fast.keys()],
    [map_average_fast[i] for i in map_average_fast.keys()],
    'bo', label='average')


# plt.semilogx([1], [1], 'k.')

plt.axhline(0, color='black')

plt.xlabel('N')
plt.ylabel('tf - average(tf)')
plt.legend(loc=4)
if zoom:
    plt.ylim(-zoom, zoom)
# plt.ylim(-1, 1)
plt.show()

