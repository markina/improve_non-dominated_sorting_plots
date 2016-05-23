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
M = 10
zoom = 0  # 1E4

name = "cube"
prefix = "_result.txt"

full_name = name + "_" + str(N) + "_" + str(M) + prefix

al = []

map_cnt = {}
map_sum_bos = {}

with open("experiments/" + full_name) as f:
    for line in f:
        n, m, k = [int(i) for i in line.split()]
        Tf = float(next(f))
        Tb = float(next(f))
        al.append(T(n, m, k, (Tb - Tf) / max(Tf, Tb), Tf, Tb))
        if n in map_cnt:
            map_cnt[n] += 1
            map_sum_bos[n] += Tb
        else:
            map_cnt[n] = 1
            map_sum_bos[n] = Tb

map_average_bos = {}

for (i, x) in map_cnt.items():
    map_average_bos[i] = map_sum_bos[i] / x

plt.title(name + " M = " + str(M) + " - time")

plt.semilogx(
    [a.n for a in al],
    [a.Tb - map_average_bos[a.n] for a in al],
    'ro', label='bos')

plt.semilogx(
    [i for i in map_average_bos.keys()],
    [map_average_bos[i] for i in map_average_bos.keys()],
    'bo', label='average')

plt.axhline(0, color='black')

plt.xlabel('N')
plt.ylabel('tb - average(tb)')
plt.legend(loc=4)
if zoom:
    plt.ylim(-zoom, zoom)

plt.show()

