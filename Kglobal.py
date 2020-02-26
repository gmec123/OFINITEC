import numpy as np
from KEG3 import  KEG2
def KG2D(x, y, Enl, D, nn):


    a = Enl.shape[0]
    b = Enl.shape[1]


    e = 0
    g = 0
    while e < a:
        i = 0
        while i < b:
            u = -1
            while u < a - 1:
                if Enl[e][i] == Enl[u][i] and u >= 0:
                    g = g + 1
                    u = u + 1
                else:
                    u = u + 1
            i = i + 1
        e = e + 1
    x1 = np.zeros([a, b])
    y1 = np.zeros([a, b])

    j = 0


    while j < a:
        j = j + 1
        s = 0
        for f in x:
            s = s + 1
            i = 0
            while i < b:
                i = i + 1
                if Enl[j-1][i-1] == s:
                    x1[j-1][i-1] = x[s - 1]
                    y1[j - 1][i - 1] = y[s - 1]







    v = np.zeros([a, 2*b])
    i = 0
    while i < 4:
        j = 0
        while j < a:
            v[j][2 * i] = 2 * Enl[j][i] - 2
            v[j][2 * i + 1] = 2 * Enl[j][i] - 1
            j = j + 1
        i = i + 1


    e = 0
    i = 0
    print("nn")
    print(nn)
    nmax = np.zeros(nn.shape[0])
    while e < nn.shape[0]:
        print("nn")
        print(nn[e])
        nmax[e] = max(nn[e])
        e = e + 1

    nmmax = max(nmax)
    print("nmax")
    print(nmmax)


    i = 0
    j = 0
    s = 0
    e = 0
    K = np.zeros([2*b, 2*b])
    Kg = np.zeros([int(2*nmmax), int(2*nmmax)])
    KG = np.zeros([int(2*nmmax), int(2*nmmax)])



    while e < a:
        i = 0
        K = KEG2(x1[e], y1[e], D)

        while i < 2 * b:
            j = 0
            while j < 2*b:

                Kg[int(v[e][i])][int(v[e][j])] = int(K[i][j])

                j = j + 1
            i = i +1
        e = e +1
        Kg = Kg

        KG = Kg + KG
        Kg = np.zeros([int(2*nmmax), int(2*nmmax)])


    return KG



