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


def pl(D, F, percent):

    full_name = "result-d-" + str(D).zfill(2) + "-f-" + str(F).zfill(2) + ".txt"

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

    print(full_name)
    print(full_name[:-4])
    plt.title(full_name[:-4] + ", " + str(lp * 100) + "%")
    name_result_file = DIR + full_name[:-4] + ".png"

    print(name_result_file)

    plt.semilogx([1], [1], 'k.')

    plt.semilogx(
        [a.n for a in al_bf],
        [a.t_b_f for a in al_bf],
        'ro', label='(Tb-Tf)/max')

    plt.semilogx(
        [a.n for a in al_hm],
        [a.t_h_m for a in al_hm],
        'bo', label='(Th-Tm)/max')

    plt.axhline(0, color='black')

    plt.xlabel('N')
    plt.ylabel('t')
    plt.legend(loc=3)
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

DIR = "plots/final-plots_all_point/"
IN_DIR = "experiments-2.2/"

pr = 0
for fi in [1, 2, 3, 5, 10, 20]:
    pl(5, fi, pr)


    # pl(100000, mi, "cube", pr)
#
# for mi in range(10, 31, 5):
#     # pl(100000, mi, "1fronts", 0.30)
#     pl(100000, mi, "2fronts", 0.30)
#     # pl(100000, mi, "cube", 0.30)
