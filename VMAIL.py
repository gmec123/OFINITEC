import numpy as np
from graphics import *
def vmai(x,y, ENL2):
    win2 = GraphWin(width=1000, height=1000)  # create a window
    win2.setCoords(-100, -100, 300, 200)
    e = 0
    h = np.zeros(4)
    k = np.zeros(4)
    while e < ENL2.shape[0]:
        x1x = x[int((ENL2[e][0])) - 1]
        x1y = y[int((ENL2[e][0])) - 1]
        pt1 = Point(x1x / 4, x1y / 4)

        x2x = x[int((ENL2[e][1])) - 1]
        x2y = y[int((ENL2[e][1])) - 1]
        pt2 = Point(x2x / 4, x2y / 4)

        x3x = x[int((ENL2[e][2])) - 1]
        x3y = y[int((ENL2[e][2])) - 1]
        pt3 = Point(x3x / 4, x3y / 4)

        x4x = x[int((ENL2[e][3])) - 1]
        x4y = y[int((ENL2[e][3])) - 1]
        pt4 = Point(x4x / 4, x4y / 4)
        h[0] = x1x
        h[1] = x2x
        h[2] = x3x
        h[3] = x4x
        k[0] = x1y
        k[1] = x2y
        k[2] = x3y
        k[3] = x4y
        hm = min(h)
        hmax = max(h)
        km = min(k)
        kmax = max(k)
        l1 = Line(pt1, pt2)
        l2 = Line(pt2, pt3)
        l3 = Line(pt3, pt4)
        l4 = Line(pt4, pt1)

        xh = (hmax+hm)/8
        yk = (kmax + km)/8


        apoint = Point(int(xh), int(yk))
        message = Text(apoint, str(e+1))
        message.setTextColor('blue')
        message.setStyle('italic')
        message.setSize(10)
        message.draw(win2)

        l1.draw(win2)
        l2.draw(win2)
        l3.draw(win2)
        l4.draw(win2)
        e = e + 1

    win2.getMouse()
    win2.close()
    return



