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
    L = np.zeros([Enl.shape[0], Enl.shape[1], 2])
    while e < Enl.shape[0]:
        i = 0
        while i < 4:
            x2[e][i] = x[int(Enl[e][i]) - 1]
            y2[e][i] = y[int(Enl[e][i]) - 1]
            if i < 3:
                L[e][i][0] = Enl[e][i]
                L[e][i][1] = Enl[e][i + 1]
            else:
                L[e][i][0] = Enl[e][i]
                L[e][i][1] = Enl[e][0]
            i = i + 1
        e = e + 1
    print("L")
    x33 = np.zeros([2])
    y33 = np.zeros([2])
    XX2 = np.zeros([int(L.shape[0]), int(L.shape[1]), int(div1) + 1])
    YY2 = np.zeros([int(L.shape[0]), int(L.shape[1]), int(div1) + 1])
    print(L)
    e = 0
    i = 0
    j = 0
    print("x,y")
    print(x)
    print(y)
    while e < El:
        i = 0
        while i < L.shape[1]:
            x1 =  x[int(L[e][i][0]) - 1]
            y1 = y[int(L[e][i][0]) - 1]
            x2 =  x[int(L[e][i][1]) - 1]
            y2 = y[int(L[e][i][1]) - 1]

            x33[0] = x1
            x33[1] = x2
            y33[0] = y1
            y33[1] = y2
            xma = max(x33)
            xmi = min(x33)
            yma = max(y33)
            ymi = min(y33)
            print("e,i, xmi, ma")
            print(x33)
            print(e,i,xmi,xma)

            j = 0
            xx = np.zeros([int(div1) + 1])
            yy = np.zeros([int(div1) + 1])
            xld = np.zeros([int(div2 - 1)])
            yld = np.zeros([int(div2) - 1])
            while j < div1 - 1:
                xld[j] = xmi + (j+1) * (xma - xmi) / div2
                yld[j] = ymi + (j+1) * (yma - ymi) / div2
                j = j + 1

            k = 0

            xx[0] = xmi
            xx[int(xx.shape[0]) - 1] = xma
            xx[1:int(xx.shape[0]) - 1] = xld
            yy[0] = ymi
            yy[int(yy.shape[0]) - 1] = yma
            yy[1:int(yy.shape[0]) - 1] = yld


            print("i")
            print(i)
            while k < xx.shape[0]:
                XX2[e][i][k] = xx[k]
                YY2[e][i][k] = yy[k]
                k = k + 1
            i = i + 1
        e = e +1
    e = 0
    i = 0


    print("XX2")
    print(XX2, XX2.shape)
    print("YY2")
    print(YY2, YY2.shape)
    XM = np.zeros([El, XX2.shape[2], XX2.shape[2]])
    YM = np.zeros([El, XX2.shape[2], XX2.shape[2]])
    nnM = np.zeros([El, XX2.shape[2], XX2.shape[2]])
    x44 = np.zeros([2])
    e = 0
    i = 0
    j = 0
    nM = 0
    while e < El:
        i = 0
        while i < XX2.shape[2]:
            j = 0
            x1 = XX2[e][0][i]
            x2 = XX2[e][2][i]
            y1 = YY2[e][0][i]
            y2 = YY2[e][2][i]
            while j < YY2.shape[2]:
                x3 = XX2[e][1][j]
                x4 = XX2[e][3][j]
                y3 = YY2[e][1][j]
                y4 = YY2[e][3][j]
                nr1 = 0
                nr2 = 0
                m1 = 0
                m2 = 0
                if x1 - x2 == 0 or x4 - x3 == 0:
                    XM[e][i][j] = (x1 * x4 - x3 * x2) / (x4 - x3 - x2 + x1)
                    YM[e][i][j] = (y1 * y4 - y3 * y2) / (y4 - y3 - y2 + y1)
                else:
                    m1 = (y2-y1)/(x2 - x1)
                    m2 = (y4 - y3)/(x4- x3)
                    nr1 = ((x2-x1)*y1 - x1 * (y2-y1))/(x2-x1)
                    nr2 = (y3*(x4-x3)-x3*(y4-y3))/(x4-x3)
                    x = (nr1 - nr2)/(m2-m1)
                    y = x * m1 + nr1
                    XM[e][i][j] = x
                    YM[e][i][j] = y

                nM = nM + 1
                nnM[e][i][j] = nM
            #XM[e][i] = sorted(XM[e][i])


                j = j + 1
            i = i +1
        e = e +1
    #XM.sort()
    #YM.sort()
    print("XM")
    e = 0
    i = 0
    X = np.zeros([El, int((div1+1)*(div2+1))])
    Y = np.zeros([El, int((div1+1) * (div2+1))])
    nn = np.zeros([El, int((div1+1) * (div2+1))])
    print(XM)
    print("YM")
    print(YM)
    print("nnM")
    print(nnM)
    h = 0

    print("x")
    print(X.shape)
    while e < El:
        i = 0
        ss = 0
        tt = 0

        while i < XM.shape[1]:
            j = 0
            while j < XM.shape[2]:
                print("ss")
                print(ss, i, j)

                X[e][ss] = XM[e][i][j]
                Y[e][ss] = YM[e][i][j]
                nn[e][ss] = nnM[e][i][j]
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
                j = j +1
            i = i + 1
        e = e + 1
    print("X")
    print(X)
    print("X")
    print(Y)
    print("nn")
    print(nn)
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
    print("X2")
    print(X2)
    print("Y2")
    print(Y2)
    e = 0
    i = 0
    j = 0
    s = 0

    u1 = 0
    u2 = 0
    u3 = 0
    u4 = 0
    ENL = np.zeros([El, int(div1 * div2), 4])
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
                u1 = j + (div1 + 1) * i
                u2 = j + div2 + 1 + (div1 + 1) * i
                u3 = j + div2 + 2 + (div1 + 1) * i
                u4 = j + 1 + (div1 + 1) * i

                ENL[e][s][0] = nn[e][int(u1)]
                ENL[e][s][1] = nn[e][int(u2)]
                ENL[e][s][2] = nn[e][int(u3)]
                ENL[e][s][3] = nn[e][int(u4)]
                s = s + 1
                j = j + 1
            i = i + 1
        e = e + 1
    print("ENL")
    print(ENL)
    ENL2 = np.zeros([El * int(div1) * int(div2), 4])
    e = 0
    i = 0
    j = 0
    s = 0

    while e < El:
        i = 0
        while i < div1 * div2:
            j = 0
            while j < 4:
                ENL2[s][j] = ENL[e][i][j]
                j = j + 1

            i = i + 1
            s = s + 1
        e = e + 1
    e = 0
    print("ENL2")
    print(ENL2)

    return ENL2, ENL, X2, Y2, X, Y, nn
#################
