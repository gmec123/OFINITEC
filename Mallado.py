from graphics import *
import numpy as np
from D4D import D4D
from KGG2D import KG2D
import xlsxwriter



V = D4D()
x = V[0]
Enl = V[2]
El = V[3]

i = 0
x1 = 0
x2 = 0

i = 0
j = 0

x2 = np.zeros([El, 4, 2])
XX = np.zeros([El, 4])
YY = np.zeros([El, 4])

N = np.shape(x)
e = 0
i = 0
while e < El:
    i = 0
    while i < 4:

        x2[e][i] = x[int(Enl[e][i])-1]
        i = i +1
    e = e +1

e = 0
i = 0
while e < El:
    i = 0
    while i < 4:
        XX[e][i] = x2[e][i][0]
        YY[e][i] = x2[e][i][1]
        i = i + 1
    e = e +1


e = 0
Xm = np.zeros(El)
Ym = np.zeros(El)
Xmin = np.zeros(El)
Ymin = np.zeros(El)
while e < El:
    Xm[e] = max(XX[e])
    Ym[e] = max(YY[e])
    Xmin[e] = min(XX[e])
    Ymin[e] = min(YY[e])
    e = e + 1

print("Xm y Ym")
print(Xm)
print(Ym)
e = 0
l = np.zeros([El, 4, 2])

while e < El:
    i = 0
    while i < 2:
        j = 0
        while j < 2:

            if j < 1:
                l[e][i][0] = Enl[e][2 * i]
                l[e][i][1] = Enl[e][2 * i + 1]

                j = j + 1
            else:
                l[e][i + 2][0] = Enl[e][i]
                l[e][i + 2][1] = Enl[e][i + 2]
                j = j + 1

        i = i + 1
    e = e + 1

i = 0
e = 0

e = 0
i = 0
Dl = np.zeros([El, 4])
while e < El:
    i = 0
    while i < 4:

            x1 = x[int(l[e][i][0])-1][0]
            x2 = x[int(l[e][i][0])-1][1]

            x3 = x[int(l[e][i][1]) - 1][0]
            x4 = x[int(l[e][i][1]) - 1][1]

            Dl[e][i] = np.sqrt((x1 - x3)**2 + (x2 -x4)**2)

            i = i + 1
    e = e + 1

div = np.zeros([2])
div[0] = 2
div[1] = 2
DlD = np.zeros([El, 4])
e = 0
while e < El:
    i = 0
    while i < 4:
        s = 0
        if i < 2:
            DlD[e][i] = Dl[e][i]/div[0]
        else:
            DlD[e][i] = Dl[e][i]/div[1]
        i = i + 1
    e = e + 1


e = 0
i = 0
j = 0
X = np.zeros([El, ((int(div[0]) + 1)*(int(div[1])+1)), 2])

ENL = np.zeros([El, int(div[0]*div[1]), 4])

xx = 0
xy = 0
ss = 0
u = 0
v = 0
n = 0
nn = np.zeros([El, (int(div[0])+1)*(int(div[1])+1)])
tt = 0
h = 0
print("XF")
print(x)
print("xmin")
print(Xmin)
while e < El:
    i = 0
    ss = 0
    tt = 0
    while i < div[0] + 1:
        j = 0
        while j < div[1] + 1:
            if e > 0:
                X[e][ss][0] = ((Xm[e]-Xmin[e])/div[0]) * i + Xmin[e]
                X[e][ss][1] = ((Ym[e]-Ymin[e])/div[1]) * j + Ymin[e]

            else:
                X[e][ss][0] = (Xm[e]/div[0])*i
                X[e][ss][1] = (Ym[e]/div[1])*j

            g = 0
            if e > 0:
                tt = tt + 1
                v = 0
                nn[e][ss] = nn[e-1][(int(div[0])+1)*(int(div[1])+1)-1] + tt

                while v < e:
                    if g == 0:
                        v = v + 1
                        u = 0
                        while u < (int(div[0])+1)*(int(div[1])+1):
                            u = u + 1
                            if X[v-1][u-1][0] == X[e][ss][0] and X[v-1][u-1][1] == X[e][ss][1]:
                                nn[e][ss] = nn[v-1][u-1]
                                X[e][ss][0] = 0
                                X[e][ss][1] = 0
                                h = h + 1
                                u = 10
                                tt = tt - 1
                                g = g + 1

                    else:
                        v = El + 1
            else:
                tt = tt + 1
                nn[e][ss] = tt
            ss = ss + 1
            j = j + 1
        i = i +1
    e = e + 1

print("nn")
print(nn)
print("X")
print(X)
g = 0
nnm = np.zeros(El)
while g < El:
    nnm[g] = max(nn[g])
    g = g +1
NNm =max(nnm)
print(NNm)
X2 = np.zeros([int(NNm), 2])

e = 0
i = 0
j = 0
print("El")
print(El)
while e < El:
    i = 0
    while i < (int(div[0])+1)*(int(div[1])+1):
        if X[e][i][0] == 0 and X[e][i][1] == 0 and e > 0:
            j = j
        else:
            X2[j][0] = X[e][i][0]
            X2[j][1] = X[e][i][1]
            j = j + 1

        i = i + 1
    e = e +1



e = 0
i = 0
j = 0
s = 0

u1 = 0
u2 = 0
u3 = 0
u4 = 0
while e < El:
    i = 0
    u1 = 0
    u2 = 0
    u3 = 0
    u4 = 0
    s = 0
    while i < div[0]*div[1]:

        if s < div[0]:
            s = s + 1
            u1 = u1 + 0
            u2 = u1 + 1
            u3 = u1 + 3
            u4 = u1 + 4

            ENL[e][i][0] = nn[e][u1]
            ENL[e][i][1] = nn[e][u2]
            ENL[e][i][2] = nn[e][u3]
            ENL[e][i][3] = nn[e][u4]
            u1 = u1 + 1
        else:
            s = 0
            u1 = u1 + 1
            u2 = u1 + 1
            u3 = u1 + 3
            u4 = u1 + 4

            ENL[e][i][0] = nn[e][u1]
            ENL[e][i][1] = nn[e][u2]
            ENL[e][i][2] = nn[e][u3]
            ENL[e][i][3] = nn[e][u4]
            u1 = u1 + 1
        i = i +1


    e = e +1

ENL2 = np.zeros([El*int(div[0])*int(div[1]), 4])
e = 0
i = 0
j = 0
s = 0
while e < El:
    i = 0
    while i < 4:
        j = 0
        while j < 4:
            ENL2[s][j] = ENL[e][i][j]
            j = j + 1

        i = i +1
        s = s + 1
    e = e +1
e = 0
print("X2")
print(X2)

print("X2")
print(X2)
print("nn")
print(nn)
print("ENl2")
print(ENL2)
KG = KG2D(X2, ENL2)

#while i < a:
 #   j = 0
  #  while j < b:
   #     KG[i][j] = [KG[i][j]]
    #    j = 0
    #i = i +1


workbook = xlsxwriter.Workbook('arrays.xlsx')
worksheet = workbook.add_worksheet()



row = 0

for col, data in enumerate(KG):
    worksheet.write_column(row, col, data)

workbook.close()




#mallado
win = GraphWin(width = 700, height = 700) # create a window
win.setCoords(-100, -100, 300, 300) # set the coordinates of the window; bottom left is (0, 0) and top right is (10, 10)