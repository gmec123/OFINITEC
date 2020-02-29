import numpy as np

def KGR(KG, rx, ry, rn, r):
    import numpy as np


    nr = r
    ng = KG.shape[0]
    ngr = ng - nr
    FI = np.zeros([ng, ng])
    i = 0
    j = 0
    e = 0
    r1 = 0
    r2 = 0
    r = 0
    ru = 0
    rv = 0



    while e < len(rn):
        r1 = rx[e]
        r2 = ry[e]
        r = rn[e] - 1
        ru = 2 * r * r1
        rv = (2 * r + 1) * r2
        i = 0
        while i < ng:
            j = 0
            while j < ng:
                if i == ru:
                    FI[i][j] = 1
                elif j == ru:
                    FI[i][j] = 1
                elif i == rv:
                    FI[i][j] = 1
                elif j == rv:
                    FI[i][j] = 1

                j = j + 1
            i = i + 1
        e = e + 1
    KGR = np.zeros([ngr, ngr])


    FI = FI
    FR = np.zeros([ngr])
    FR = FI[FI.shape[0]-1]


    i = 0
    j = 0
    u = 0
    v = 0


    while i < ng:
        j = 0
        v = 0
        while j < ng:
            if FI[i][j] == 0 and v < ngr-1:
                KGR[u][v] = int(KG[i][j])

                v = v + 1

            elif FI[i][j] == 0 and v == ngr-1:
                KGR[u][v] = int(KG[i][j])
                u = u +1


            j = j + 1

        i = i + 1

    kgr = KGR

    return kgr, FR
