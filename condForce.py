import numpy as np
def force(x, y, nn, X2, Y2, fn, fx, fy, rx, ry, rn, r):
    import numpy as np



    d = fn.shape[0]
    fn2 = np.zeros(d)
    e = 0
    e2 = 0
    rr = r
    xf = 0


    while e < fn.shape[0]:
        e2 = 0
        xf = x[int(fn[e]) - 1]
        yf = y[int(fn[e]) - 1]
        while e2 < nn.shape[0]:
            i = 0
            while i < nn.shape[1]:
                xf2 = X2[int(nn[e2][i])-1]
                yf2 = Y2[int(nn[e2][i]) - 1]
                if xf== xf2 and yf == yf2:
                    fn2[e] = nn[e2][i]
                i = i + 1
            e2 = e2 +1
        e = e + 1


    fn22 = np.zeros(2 * len(fn2))
    e = 0
    while e < len(fn2):
        fn22[2*e] = 2*fn2[e] - 1
        fn22[2*e + 1] = 2*fn2[e]
        e = e + 1

    v = nn[int(nn.shape[0])-1][int(nn.shape[1])-1]
    F = np.zeros(int(2*v))
    i = 0
    j = 0
    fr = np.zeros(len(fn22))
    e = 0


    while e < len(fn):
        fr[2*e] = fx[e]
        fr[2*e + 1] = fy[e]
        e = e + 1

    while j < len(fn22):
        i = 0
        while i < 2*v:
            if fn22[j] == i + 1:
                F[i] = fr[j]
            i = i + 1
        j = j + 1

    ####
    ##
    e = 0
    fI = np.zeros(int(2 * v))

    while e < len(rn):
        r1 = rx[e]
        r2 = ry[e]
        r = rn[e] - 1
        ru = 2 * r * r1
        rv = (2 * r + 1) * r2

        i = 0
        while i < 2*v:
            if i == ru:
                fI[i] = 1
            elif i == rv:
                fI[i] = 1
            i = i + 1
        e = e + 1

    fir = np.zeros(int(len(F)-rr))

    j = 0
    i = 0
    while i < 2*v:

        if fI[i] == 0:
            fir[j] = F[i]
            j = j + 1
        i = i + 1

    return fir
