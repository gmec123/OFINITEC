import numpy as np
from graphics import *
def MESH2D(x, y, Enl, El, div1, div2):
    import numpy as np
    i = 0
    x1 = 0
    x2 = 0

    i = 0
    j = 0

    x2 = np.zeros([El, 4])
    y2 = np.zeros([El, 4])
    XX = np.zeros([El, 4])
    YY = np.zeros([El, 4])

    N = np.shape(x)
    e = 0
    i = 0
    while e < Enl.shape[0]:
        i = 0
        while i < 4:
            x2[e][i] = x[int(Enl[e][i]) - 1]
            y2[e][i] = y[int(Enl[e][i]) - 1]
            i = i + 1
        e = e + 1

    e = 0
    i = 0
    while e < El:
        i = 0
        while i < 4:
            XX[e][i] = x2[e][i]
            YY[e][i] = y2[e][i]
            i = i + 1
        e = e + 1

    e = 0
    Xm = np.zeros(El)
    Ym = np.zeros(El)
    Xmin = np.zeros(El)
    Ymin = np.zeros(El)
    while e < El:
        Xm[e] = max(XX[e])
        Ym[e] = max(YY[e])
        Xmin[e] = min(XX[e])
        Ymin[e] = min(YY[e])
        e = e + 1


    e = 0
    i = 0
    j = 0
    X = np.zeros([El, ((int(div1) + 1) * (int(div2) + 1))])
    Y = np.zeros([El, ((int(div1) + 1) * (int(div2) + 1))])

    ENL = np.zeros([El, int(div1 * div2), 4])

    xx = 0
    xy = 0
    ss = 0
    u = 0
    v = 0
    n = 0
    nn = np.zeros([El, (int(div1) + 1) * (int(div2) + 1)])
    tt = 0
    h = 0

    while e < El:
        i = 0
        ss = 0
        tt = 0
        while i < div1 + 1:
            j = 0
            while j < div2 + 1:
                if e > 0:
                    X[e][ss] = ((Xm[e] - Xmin[e]) / div1) * i + Xmin[e]
                    Y[e][ss] = ((Ym[e] - Ymin[e]) / div2) * j + Ymin[e]
                else:
                    X[e][ss] = (Xm[e] / div1) * i
                    Y[e][ss] = (Ym[e] / div2) * j
                g = 0
                if e > 0:
                    tt = tt + 1
                    v = 0
                    nn[e][ss] = nn[e - 1][(int(div1) + 1) * (int(div2) + 1) - 1] + tt
                    while v < e:
                        if g == 0:
                            v = v + 1
                            u = 0
                            while u < (int(div1) + 1) * (int(div2) + 1):
                                u = u + 1
                                if X[v - 1][u - 1] == X[e][ss] and Y[v - 1][u - 1] == Y[e][ss]:
                                    nn[e][ss] = nn[v - 1][u - 1]
                                    X[e][ss] = 0
                                    Y[e][ss] = 0
                                    h = h + 1
                                    u = 10
                                    tt = tt - 1
                                    g = g + 1

                        else:
                            v = El + 1
                else:
                    tt = tt + 1
                    nn[e][ss] = tt
                ss = ss + 1
                j = j + 1
            i = i + 1
        e = e + 1

    g = 0
    nnm = np.zeros(El)
    while g < El:
        nnm[g] = max(nn[g])
        g = g + 1
    NNm = max(nnm)

    X2 = np.zeros([int(NNm)])
    Y2 = np.zeros([int(NNm)])

    e = 0
    i = 0
    j = 0

    while e < El:
        i = 0
        while i < (int(div1) + 1) * (int(div2) + 1):
            if X[e][i] == 0 and Y[e][i] == 0 and e > 0:
                j = j
            else:
                X2[j] = X[e][i]
                Y2[j] = Y[e][i]
                j = j + 1

            i = i + 1
        e = e + 1
    e = 0
    i = 0
    j = 0
    s = 0

    u1 = 0
    u2 = 0
    u3 = 0
    u4 = 0

    while e < El:
        i = 0
        u1 = 0
        u2 = 0
        u3 = 0
        u4 = 0
        s = 0
        w = 0
        while i < div1:
            j = 0
            while j < div2:

                u1 = j + (div1+1)*i
                u2 = j + div2 + 1 + (div1+1)*i
                u3 = j + div2 + 2 + (div1+1)*i
                u4 = j + 1 + (div1+1)*i

                ENL[e][s][0] = nn[e][int(u1)]
                ENL[e][s][1] = nn[e][int(u2)]
                ENL[e][s][2] = nn[e][int(u3)]
                ENL[e][s][3] = nn[e][int(u4)]
                s = s +1
                j = j + 1
            i = i + 1
        e = e + 1

    ENL2 = np.zeros([El * int(div1) * int(div2), 4])
    e = 0
    i = 0
    j = 0
    s = 0

    while e < El:
        i = 0
        while i < div1*div2:
            j = 0
            while j < 4:
                ENL2[s][j] = ENL[e][i][j]
                j = j + 1

            i = i + 1
            s = s + 1
        e = e + 1
    e = 0

    #############
    ###########3
    ########################################grafic


    return ENL2, ENL, X2, Y2, X, Y, nn
#################
