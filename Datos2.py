import numpy as np
def D4D():
    import numpy as np
    # grados lib
    Nod = 4
    # matriz rig

    n = np.array([1, 2, 3, 4])
    x = np.array([0, 20, 60, 0])
    y = np.array([20, 0, 0, 60])
    El = 1
    Enl = np.array([[1, 2, 3, 4]])
    #restricciones
    rx = np.array([1, 1])
    ry = np.array([1, 1])
    rn = np.array([1, 2])
    fx = np.array([20])
    fy = np.array([50])
    fn = np.array([3])
    E = 2100000
    nu = 0.3
    D = (E / (1 - nu * nu)) * np.array([[1, nu, 0], [nu, 1, 0], [0, 0, (1 - nu) / 2]])
    t = 1
    print(D)





    return x, y, Enl, El, rx, ry, rn, n, fx, fy, fn, D, t
