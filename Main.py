from graphics import *
import numpy as np
from esfdef import  esdef
from D4D2 import D4D
from KG2DF import KG2D
from mesh2D66 import MESH2D
from KGR import KGR
import xlsxwriter
from KE4 import KE4
from condf import fij
from VNOD import nodv
from VNOD import nodv2
from VMAIL import vmai
from VMAILR import vmaiR
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





nodv2(x, y, Enl)
div = np.zeros([2])
div[0] = 6
div[1] = 6
#[XM, YM, nnM] = MESH2D(x, y, Enl, El, div[0], div[1])
[ENL2, ENL, X2, Y2, X, Y, nn] = MESH2D(x, y, Enl, El, div[0], div[1])

#nodv(XM, YM, nnM)
vmai(X2, Y2, ENL2)
[KG2, B1, B2, B3, B4, a] = KG2D(X2, Y2, ENL2, D, nn)



[rn2, r] = fij(x, y, nn, X2, Y2, rx, ry, rn)

[KG2R, FR] = KGR(KG2, rx, ry, rn2, r)
print("nn")
print(nn)
fn2 = force(x, y, nn, X2, Y2, fn, fx, fy, rx, ry, rn2, r)

#workbook = xlsxwriter.Workbook('arrays.xlsx')
#worksheet = workbook.add_worksheet()
#col = 0


#for row, data in enumerate(KG2R):
   #worksheet.write_row(row, col, data)

de = np.linalg.solve(KG2R, fn2)

[dep, depe, esfvonE] = esdef(de, FR, B1, B2, B3, B4, ENL2, D)




#workbook.close()




vmaiR(X2, Y2, ENL2, esfvonE)



