import numpy as np
def bm(z,x):

    [nn, dim] = x.shape


    dNi = 0.25 * np.array([[z[1] - 1, -z[1] + 1, 1 + z[1], -1 - z[1]],
                           [z[0] - 1, -z[0] - 1, 1 + z[0], 1 - z[0]]])


    J = dNi.dot(x)

    dJ = np.linalg.det(J)

    Ji = (np.linalg.inv(J))

    dNxy = np.dot(Ji, dNi)

    bm = np.zeros((3, nn*dim))

    bm[0][0:7:2] = dNxy[0][:]
    bm[1][1:8:2] = dNxy[1][:]
    bm[2][0:7:2] = dNxy[1][:]
    bm[2][1:8:2] = dNxy[0][:]


    return bm, dJ



