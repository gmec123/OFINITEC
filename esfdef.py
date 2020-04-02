import numpy as np

def esdef(de, FR, B1, B2, B3, B4, ENL2, D):

    i = 0
    z = 0
    frr = FR.shape[0]
    dep = np.zeros([frr])
    while i < frr:
        if FR[i] == 0:
            dep[i] = de[z]
            z = z + 1
        else:
            dep[i] = 0
        i = i + 1

    depe = np.zeros([ENL2.shape[0], 8])
    e = 0
    i = 0

    while e < ENL2.shape[0]:
        i = 0
        while i < 4:
            depe[e][2*i] = dep[2*(int(ENL2[e][i])-1)]
            depe[e][2*i+1] = dep[2*(int(ENL2[e][i])-1)+1]
            i = i +1
        e = e + 1

    e = 0
    deff1 = np.zeros([ENL2.shape[0], 3])
    deff2 = np.zeros([ENL2.shape[0], 3])
    deff3 = np.zeros([ENL2.shape[0], 3])
    deff4 = np.zeros([ENL2.shape[0], 3])
    esf1 = np.zeros([ENL2.shape[0], 3])
    esf2 = np.zeros([ENL2.shape[0], 3])
    esf3 = np.zeros([ENL2.shape[0], 3])
    esf4 = np.zeros([ENL2.shape[0], 3])
    esfp1 = np.zeros([ENL2.shape[0], 2])
    esfp2 = np.zeros([ENL2.shape[0], 2])
    esfp3 = np.zeros([ENL2.shape[0], 2])
    esfp4 = np.zeros([ENL2.shape[0], 2])
    esfvon1 = np.zeros([ENL2.shape[0]])
    esfvon2 = np.zeros([ENL2.shape[0]])
    esfvon3 = np.zeros([ENL2.shape[0]])
    esfvon4 = np.zeros([ENL2.shape[0]])
    esfvonE = np.zeros([ENL2.shape[0]])
    while e <  ENL2.shape[0]:

        deff1[e] = np.dot(B1[e], depe[e])
        esf1[e] = np.dot(D, deff1[e])
        esfp1[e][0] = (esf1[e][0] + esf1[e][1])/2 + pow(pow((esf1[e][0] - esf1[e][1])/2, 2)+pow(esf1[e][2] ,2), 0.5)
        esfp1[e][1] = (esf1[e][0] + esf1[e][1])/2 - pow(pow((esf1[e][0] - esf1[e][1])/2, 2)+pow(esf1[e][2] ,2), 0.5)
        esfvon1[e] = pow(1/2*(pow((esfp1[e][0] - esfp1[e][1]), 2)+pow(esfp1[e][0] ,2) + pow(esfp1[e][1] ,2)), 0.5)
        deff2[e] = np.dot(B2[e], depe[e])
        esf2[e] = np.dot(D, deff2[e])
        esfp2[e][0] = (esf2[e][0] + esf2[e][1]) / 2 + pow(pow((esf2[e][0] - esf2[e][1]) / 2, 2) + pow(esf2[e][2], 2), 0.5)
        esfp2[e][1] = (esf2[e][0] + esf2[e][1]) / 2 - pow(pow((esf2[e][0] - esf2[e][1]) / 2, 2) + pow(esf2[e][2], 2), 0.5)
        esfvon2[e] = pow(1 / 2 * (pow((esfp2[e][0] - esfp2[e][1]), 2) + pow(esfp2[e][0], 2) + pow(esfp2[e][1], 2)), 0.5)
        deff3[e] = np.dot(B3[e], depe[e])
        esf3[e] = np.dot(D, deff3[e])
        esfp3[e][0] = (esf3[e][0] + esf3[e][1]) / 2 + pow(pow((esf3[e][0] - esf3[e][1]) / 2, 2) + pow(esf3[e][2], 2), 0.5)
        esfp3[e][1] = (esf3[e][0] + esf3[e][1]) / 2 - pow(pow((esf3[e][0] - esf3[e][1]) / 2, 2) + pow(esf3[e][2], 2), 0.5)
        esfvon3[e] = pow(1 / 2 * (pow((esfp3[e][0] - esfp3[e][1]), 2) + pow(esfp3[e][0], 2) + pow(esfp3[e][1], 2)), 0.5)
        deff4[e] = np.dot(B4[e], depe[e])
        esf4[e] = np.dot(D, deff4[e])
        esfp4[e][0] = (esf4[e][0] + esf4[e][1]) / 2 + pow(pow((esf4[e][0] - esf4[e][1]) / 2, 2) + pow(esf4[e][2], 2), 0.5)
        esfp4[e][1] = (esf4[e][0] + esf4[e][1]) / 2 - pow(pow((esf4[e][0] - esf4[e][1]) / 2, 2) + pow(esf4[e][2], 2), 0.5)
        esfvon4[e] = pow(1 / 2 * (pow((esfp4[e][0] - esfp4[e][1]), 2) + pow(esfp4[e][0], 2) + pow(esfp4[e][1], 2)), 0.5)
        esfvonE = (esfvon1 + esfvon2 + esfvon3 + esfvon4)/4
        e = e + 1



    return dep, depe, esfvonE
