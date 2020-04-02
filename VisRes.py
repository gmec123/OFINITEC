import numpy as np
from graphics import *
def vmaiR(x,y, ENL2, esvo):
    win2 = GraphWin(width=1000, height=1000)  # create a window
    win2.setCoords(-100, -100, 300, 200)
    e = 0
    h = np.zeros(4)
    k = np.zeros(4)
    emin = min(esvo)
    emax = max(esvo)
    em = (emin + emax)/2
    emim = (em + emin)/2
    emam = (em + emax)/2

    while e < ENL2.shape[0]:
        x1x = x[int((ENL2[e][0])) - 1]
        x1y = y[int((ENL2[e][0])) - 1]
        pt1 = Point(x1x / 2, x1y / 2)

        x2x = x[int((ENL2[e][1])) - 1]
        x2y = y[int((ENL2[e][1])) - 1]
        pt2 = Point(x2x / 2, x2y / 2)

        x3x = x[int((ENL2[e][2])) - 1]
        x3y = y[int((ENL2[e][2])) - 1]
        pt3 = Point(x3x / 2, x3y / 2)

        x4x = x[int((ENL2[e][3])) - 1]
        x4y = y[int((ENL2[e][3])) - 1]
        pt4 = Point(x4x / 2, x4y / 2)


        if esvo[e] <= emax and esvo[e] >= em:
            if esvo[e] < emam:
                r = ((esvo[e]-em)/(emam-em))*250
                g = 250
                b = 0
            elif esvo[e] >= emam:
                r = 250
                g = ((emax - esvo[e])/(emax-emam))*250
                print("esvo, emam, emax, emax-esvo, emax-emam")
                print(esvo[e],emam, emax, emax-esvo[e], emax-emam)
                b = 0
                print("r,g,b")
                print(r, g, b)
        elif esvo[e] >= emin and esvo[e] < em:
            if esvo[e] >= emim:
                r = 0
                g = 250
                b = ((em - esvo[e])/(em-emim))*250
            elif esvo[e] <= emim:
                r = 0
                g = ((esvo[e]-emin)/(em-emin))*250
                b = 250



        #r = int(250 * (esvo[e]) / emax)
        #g = 0
        #b =70



        aPolygon = Polygon(pt1, pt2, pt3, pt4)
        color = color_rgb(int(r), int(g), int(b))
        aPolygon.setFill(color)
        aPolygon.draw(win2)
        e = e + 1

    win2.getMouse()
    win2.close()
    return



