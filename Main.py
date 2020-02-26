from graphics import *
import numpy as np
from D4D2 import D4D
from KG2DF import KG2D
from mesh2D3 import MESH2D
from KGR import KGR
import xlsxwriter
from KE4 import KE4
from condf import fij
from VNOD import nodv
from VNOD import nodv2
from VMAIL import vmai
from condForce import force




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






div = np.zeros([2])
div[0] = 2
div[1] = 2
[ENL2, X2, Y2, X, Y, nn] = MESH2D(x, y, Enl, El, div[0], div[1])
print("ENL, x, y")
print(ENL2)
print(Y)
print(X)
print("X2")
print("Y")
print(Y2)
print(X2)
print("mesh")
print(ENL2)
print("ENL2S")
print(ENL2.shape)

nodv(X, Y, nn)
vmai(X2, Y2, ENL2)
KG2 = KG2D(X2, Y2, ENL2, D, nn)


print(X2)
print(Y2)



[rn2, r] = fij(x, y, nn, X2, Y2, rx, ry, rn)

KG2R = KGR(KG2, rx, ry, rn2, r)

fn2 = force(x, y, nn, X2, Y2, fn, fx, fy, rx, ry, rn2, r)
print("KG2")
KGRI = np.linalg.inv(KG2R)
L = np.dot(KGRI, KG2R)
print("dta1, dt2")
print(np.linalg.det(KG2R), np.linalg.det(L))
workbook = xlsxwriter.Workbook('arrays.xlsx')
worksheet = workbook.add_worksheet()
col = 0
print("fn2")
print(fn2)
print("dtKG")

for row, data in enumerate(KG2R):
   worksheet.write_row(row, col, data)

de = np.linalg.solve(KG2R, fn2)
print("des")
print(de)



workbook.close()


nodv2(x, y, Enl)
vmai(x, y, Enl)

vmai(X2, Y2, ENL2)


