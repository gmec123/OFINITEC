import numpy as np
def fij(x, y, nn, X2, Y2, rx, ry, rn):
    import numpy as np



    d = rn.shape[0]
    rn2 = np.zeros(d)
    e = 0
    e2 = 0
    r = 0

    while e < rn.shape[0]:
        if rx[e] == 1:
            r = r + 1
        if ry[e] ==1:
            r = r + 1
        e = e + 1
    e = 0


    xr = np.zeros([d])
    yr = np.zeros([d])



    while e < rn.shape[0]:
        e2 = 0
        xr = x[int(rn[e]) - 1]
        yr = y[int(rn[e]) - 1]
        while e2 < nn.shape[0]:
            i = 0
            while i < nn.shape[1]:
                xr2 = X2[int(nn[e2][i])-1]
                yr2 = Y2[int(nn[e2][i]) - 1]

                if xr == xr2 and yr == yr2:
                    rn2[e] = nn[e2][i]





                i = i + 1
            e2 = e2 +1
        e = e + 1
    print("rn, rn2")
    print(rn, rn2)



    return rn2, r
