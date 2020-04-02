import numpy as np
from graphics import *
def nodv(x, y, nn):
    win2 = GraphWin(width=1000, height=1000)  # create a window
    win2.setCoords(-100, -100, 300, 200)
    e = 0
    while e < nn.shape[0]:
        i = 0
        while i < nn.shape[1]:
            j = 0
            while j < nn.shape[2]:
                x1 = (x[e][i][j]) / 2
                x2 = (y[e][i][j]) / 2
                n = nn[e][i][j]
                k = str(int(n))
                apoint = Point(x1, x2)
                message = Text(apoint, k)
                message.setTextColor('blue')
                message.setStyle('italic')
                message.setSize(10)
                message.draw(win2)
                apoint.draw(win2)
                j = j +1


            i = i + 1
        e = e + 1

    win2.getMouse()
    win2.close()
    return

def nodv2(x,y, Enl):
    win2 = GraphWin(width=1000, height=1000)  # create a window
    win2.setCoords(-100, -100, 300, 200)
    e = 0
    while e < Enl.shape[0]:
        i = 0
        while i < 4:
            x1 = (x[int(Enl[e][i])-1]) / 2
            x2 = (y[int(Enl[e][i])-1]) / 2
            n  = int(Enl[e][i]-1)
            j = str(int(n + 1))
            apoint = Point(int(x1), int(x2))
            message = Text(apoint, j)
            message.setTextColor('blue')
            message.setStyle('italic')
            message.setSize(10)
            message.draw(win2)
            apoint.draw(win2)

            i = i + 1
        e = e + 1

    win2.getMouse()
    win2.close()
    return


