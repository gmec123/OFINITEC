import numpy as np
from bm import bm


def KE4(x, D):

    g = np.sqrt(1 / 3)
    z = np.array([-1, 1]) * g
    k = len(z)

    nne = len(x)


    e = 1
    KE4 = np.zeros([nne * 2, nne * 2])

    i = 0
    j = 0


    s = 0

    while i < k:
        r = z[i]

        while j < k:
            s = z[j]

            [BM, dJ] = bm([r, s], x)

            BMT = np.transpose(BM)
            C = np.dot(BMT, D)

            BM = BM * dJ

            G = np.dot(C, BM)
            KE4 = KE4 + G
            j = j + 1

        i = i + 1
        j = 0
    return KE4