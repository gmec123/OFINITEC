import numpy as np
from bm import bm


def KEG(x, y, D, t, s):
    dNIs = 0.25 * np.array([t - 1, -t + 1, t + 1, -1 - t])
    dNIt = 0.25 * np.array([s - 1, -s - 1, 1 + s, 1 - s])

    dxds = np.dot(x, dNIs)
    dxdt = np.dot(x, dNIt)
    dyds = np.dot(y, dNIs)
    dydt = np.dot(y, dNIt)

    J = np.zeros([2, 2])
    J[0][0] = dxds
    J[1][0] = dyds
    J[0][1] = dxdt
    J[1][1] = dydt


    dJ = np.linalg.det(J)


    A = np.zeros([3, 4])
    A[0][0] = dydt
    A[0][1] = -dyds
    A[1][2] = -dxdt
    A[1][3] = dxds
    A[2][0] = -dxdt
    A[2][1] = dxds
    A[2][2] = dydt
    A[2][3] = -dyds
    A = A / dJ

    G = np.zeros([4, 8])
    i = 0
    while i < 4:
        G[0][i * 2] = dNIs[i]
        G[1][i * 2] = dNIt[i]
        G[2][1 + i * 2] = dNIs[i]
        G[3][1 + i * 2] = dNIt[i]
        i = i + 1


    B = np.dot(A, G)

    Bt = np.transpose(B)
    KE4 = dJ * np.dot(np.dot(Bt, D), B)

    return KE4