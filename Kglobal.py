import numpy as np
from KE4 import KE4
def KG2D(x, Enl):


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
    x1 = np.zeros([a, b, 2])
    s = 0
    v = 0
    i = 0
    j = 0
    t = 0
    l1 = 0
    l2 = 0
    j = 0
    fi = 2
## adaptación coordenadas globables a coordenadas por elementos

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



    m = Enl[a-1][b-1]
    K = np.zeros([2*b, 2*b])
    Kg = np.zeros([int(2*m), int(2*m)])
    KG = np.zeros([int(2*m), int(2*m)])


    v = np.zeros([a, 2*b])
    i = 0
    while i < 4:
        j = 0
        while j < a:
            v[j][2 * i] = 2 * Enl[j][i] - 2
            v[j][2 * i + 1] = 2 * Enl[j][i] - 1
            j = j + 1
        i = i + 1

    i = 0
    j = 0
    s = 0
    e = 0


    print("x1")
    print(x1)
    np.set_printoptions(formatter={"float": lambda x:"%0.1f"%(x)})
    ## ensamble de matrices de rigidez de los elementos
    while e < a:
        i = 0
        K = KE4(x1[e])

        while i < 2 * b:
            j = 0
            while j < 2*b:
                Kg[int(v[e][i])][int(v[e][j])] = K[i][j]
                j = j + 1
            i = i +1
        e = e +1
        Kg = Kg

        KG = Kg + KG
        Kg = np.zeros([int(2*m), int(2*m)])

    return KG



