import numpy as np
def D4D():
    import numpy as np
    # grados lib
    Nod = 6
    # matriz rig
    n = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    x = np.array([0, 0, 0, 100, 100, 100, 200, 200, 200, 300, 300, 400])
    y = np.array([0, 100, 200, -10, 100, 200, 0, 100, 200, 0, 100, 250])
    El = 5
    Enl = np.array([[1, 4, 5, 2], [2, 5, 6, 3], [4, 7, 8, 5], [7, 10, 11, 8], [8, 11, 12, 9]])
    #restricciones
    rx = np.array([1, 1])
    ry = np.array([1, 1])
    rn = np.array([1, 2])
    fx = np.array([20, 40])
    fy = np.array([50, 10])
    fn = np.array([6, 12])
    E = 2100000
    nu = 0.3
    D = (E / (1 - nu * nu)) * np.array([[1, nu, 0], [nu, 1, 0], [0, 0, (1 - nu) / 2]])
    t = 1
    print(D)





    return x, y, Enl, El, rx, ry, rn, n, fx, fy, fn, D, t
