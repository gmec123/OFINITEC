import numpy as np
from bm import bm
from KEG2 import KEG


def KEG2(x, y, D):
    t1 = 0.57735
    s1 = 0.57735
    t2 = - 0.57735
    s2 = 0.57735
    t3 = 0.57735
    s3 = -0.57735
    t4 = -0.57735
    s4 = -0.57735

    ke1 = KEG(x, y, D, t1, s1)
    ke2 = KEG(x, y, D, t2, s2)
    ke3 = KEG(x, y, D, t3, s3)
    ke4 = KEG(x, y, D, t4, s4)
    kee = ke1 + ke2 + ke3 + ke4

    return kee