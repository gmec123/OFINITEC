import numpy as np
def D4D():
    import numpy as np
    # grados lib
    Nod = 6
    # matriz rig
    n = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    x = np.array([[0, 0], [0, 100], [0, 200], [100, 0], [100, 100], [100, 200], [200, 0], [200, 100], [200, 300], [300, 0], [300, 100], [300, 300]])
    El = 5
    En = np.array([1, 2])
    Enl = np.array([[1, 2, 4, 5], [2, 3, 5, 6], [4, 5, 7, 8], [7, 8, 10, 11], [8, 9, 11, 12]])
    #restricciones
    rx = np.array([1, -1])
    ry = np.array([1, 1])
    rn = np.array([2, 4])



    return x, En, Enl, El, n, Nod, rx, ry, rn
