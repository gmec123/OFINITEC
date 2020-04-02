from graphics import *
import numpy as np
from esfdef import  esdef
from Datos1 import D4D
from KGlobal import KG2D
from Mesh import MESH2D
from KGlobalRed import KGR
from Fijar import fij
from VisNod import nodv2
from VisRes import vmaiR
from Fuerzas import force




V = D4D()
x = V[0]
y = V[1]
Enl = V[2]
El = V[3]
rx = V[4]
ry = V[5]
rn = V[6]
n = V[7]
fx = V[8]
fy = V[9]
fn = V[10]
D = V[11]
t = V[12]
r = 4





nodv2(x, y, Enl)
div = np.zeros([2])
div[0] = 6
div[1] = 6

[ENL2, ENL, X2, Y2, X, Y, nn] = MESH2D(x, y, Enl, El, div[0], div[1])


[KG2, B1, B2, B3, B4, a] = KG2D(X2, Y2, ENL2, D, nn)



[rn2, r] = fij(x, y, nn, X2, Y2, rx, ry, rn)

[KG2R, FR] = KGR(KG2, rx, ry, rn2, r)
print("nn")
print(nn)
fn2 = force(x, y, nn, X2, Y2, fn, fx, fy, rx, ry, rn2, r)



de = np.linalg.solve(KG2R, fn2)

[dep, depe, esfvonE] = esdef(de, FR, B1, B2, B3, B4, ENL2, D)






vmaiR(X2, Y2, ENL2, esfvonE)



