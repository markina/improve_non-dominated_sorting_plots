import math

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class T:
    def __init__(self, n, m, k, tf, tb, th):
        self.n = n
        self.m = m
        self.k = k
        self.tf = tf
        self.tb = tb
        self.th = th
        tm = min(tb, tf)
        self.t_b_f = (tb - tf) / max(tf, tb)
        self.t_h_m = (th - tm) / max(tm, th)


def pl(N, M, name, percent):

    # N = 100000
    # M = 30
    #
    # name = "1fronts"
    prefix = "_result.txt"

    full_name = name + "_" + str(N) + "_" + str(M) + prefix

    al = {}
    max_k = -1

    lp = percent
    rp = 1 - percent

    with open(IN_DIR + full_name) as f:
        for line in f:
            n, m, k = [int(i) for i in line.split()]
            max_k = max(max_k, k)
            Tf = float(next(f))
            Tb = float(next(f))
            Th = float(next(f))
            if n not in al:
                al[n] = []
            al[n].append(T(n, m, k, Tf, Tb, Th))

    print("Cnt ranks = " + str(max_k))

    al_bf = []
    al_hm = []

    for (n, ls) in al.items():
        bf = sorted(ls, key=lambda e: e.t_b_f)
        sz = len(bf)
        left = int(sz * lp)
        right = int(math.ceil(sz * rp))
        al_bf.extend(bf[left:right + 1])

        hm = sorted(ls, key=lambda e: e.t_h_m)
        sz = len(hm)
        left = int(sz * lp)
        right = int(math.ceil(sz * rp))
        al_hm.extend(hm[left:right + 1])

    plt.title(name + " M = " + str(M).zfill(2) + ", " + str(lp * 100) + "%")
    name_result_file = DIR + name + "_m=" +  str(M).zfill(2) + ".png"

    print(name_result_file)

    plt.semilogx([1], [1], 'k.')

    plt.semilogx(
        [a.n for a in al_bf if a.m == M],
        [a.t_b_f for a in al_bf if a.m == M],
        'ro', label='(Tb-Tf)/max')

    plt.semilogx(
        [a.n for a in al_hm if a.m == M],
        [a.t_h_m for a in al_hm if a.m == M],
        'bo', label='(Th-Tm)/max')

    plt.axhline(0, color='black')

    plt.xlabel('N')
    plt.ylabel('t')
    plt.legend(loc=4)
    plt.xlim(0, 110000)
    plt.ylim(-1, 1)
    # plt.grid()
    # fig = plt.figure()
    # fig.canvas.manager.window.attributes('-topmost', 1)
    # After placing figure window on top, allow other windows to be on top of it later
    # fig.canvas.manager.window.attributes('-topmost', 0)
    plt.savefig(name_result_file, bbox_inches='tight')
    plt.close()
    # plt.show()
#

DIR = "plots/plot-3_new_test/"
IN_DIR = "experiments-3/"

for mi in range(3, 11):
    if mi < 5:
        pr = 0.40
    else:
        pr = 0.30
    pl(100000, mi, "1fronts", pr)
    # pl(100000, mi, "2fronts", pr)
    pl(100000, mi, "cube", pr)

for mi in range(10, 31, 5):
    pl(100000, mi, "1fronts", 0.30)
    # pl(100000, mi, "2fronts", 0.30)
    pl(100000, mi, "cube", 0.30)
