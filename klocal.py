import numpy as np
from klocal0 import KEG


def KEG2(x, y, D):
    t1 = 0.57735
    s1 = 0.57735
    t2 = - 0.57735
    s2 = 0.57735
    t3 = 0.57735
    s3 = -0.57735
    t4 = -0.57735
    s4 = -0.57735

    [ke1, b1] = KEG(x, y, D, t1, s1)
    [ke2, b2] = KEG(x, y, D, t2, s2)
    [ke3, b3] = KEG(x, y, D, t3, s3)
    [ke4, b4] = KEG(x, y, D, t4, s4)
    kee = ke1 + ke2 + ke3 + ke4

    return kee, b1, b2, b3, b4
