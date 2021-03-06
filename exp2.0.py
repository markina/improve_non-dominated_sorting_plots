import math

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class T:
    def __init__(self, n, m, k, tf, tb):
        self.n = n
        self.m = m
        self.k = k
        self.tf = tf
        self.tb = tb
        # self.th = th
        # tm = min(tb, tf)
        self.t_b_f = (tb - tf) / max(tf, tb)
        # self.t_h_m = (th - tm) / max(tm, th)


def pl(D, F, percent):

    full_name = "result" + "-d-" + str(D).zfill(2) + "-f-" + str(F).zfill(2) + ".txt"
    out_file_name = "d-" + str(D).zfill(2) + "-f-" + str(F).zfill(2) + ".png"

    al = {}

    lp = percent
    rp = 1 - percent

    max_k = -1

    with open(IN_DIR + full_name) as f:
        for line in f:
            n, m, k = [int(i) for i in line.split()]
            Tf = float(next(f))
            Tb = float(next(f))
            max_k = max(max_k, k)
            if n not in al:
                al[n] = []
            al[n].append(T(n, m, k, Tf, Tb))

    al_bf = []
    # al_hm = []

    for (n, ls) in al.items():
        bf = sorted(ls, key=lambda e: e.t_b_f)
        sz = len(bf)
        left = int(sz * lp)
        right = int(math.ceil(sz * rp))
        al_bf.extend(bf[left:right + 1])
        #
        # hm = sorted(ls, key=lambda e: e.t_h_m)
        # sz = len(hm)
        # left = int(sz * lp)
        # right = int(math.ceil(sz * rp))
        # al_hm.extend(hm[left:right + 1])

    plt.title(" D = " + str(D).zfill(2) + ", F = " + str(F).zfill(2) + ", " + str(lp * 100) + "%")

    print(out_file_name)
    print("Cnt ranks = " + str(max_k))

    plt.semilogx([1], [1], 'k.')

    plt.semilogx(
        [a.n for a in al_bf],
        [a.t_b_f for a in al_bf],
        'ro', label='(Tb-Tf)/max')
    #
    # plt.semilogx(
    #     [a.n for a in al_hm],
    #     [a.t_h_m for a in al_hm],
    #     'bo', label='(Th-Tm)/max')

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
    plt.savefig(DIR + out_file_name, bbox_inches='tight')
    plt.close()
    # plt.show()
#

DIR = "plots/plot-delete/"
IN_DIR = "experiments-2.0/"

for mi in range(3, 8):
    for fi in range(1, 21):
        pl(mi, fi, 0.3)

for fi in range(1, 11):
    pl(8, fi, 0.3)

