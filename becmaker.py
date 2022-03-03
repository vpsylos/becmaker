#!/usr/bin/env python3

import PySimpleGUIQt as sg
import matplotlib.pyplot as plt

def createbec(values):
    #Input values defined
    clo = int(values[1])
    tfc = int(values[2])
    avc = int(values[3])
    pri = int(values[4])

    #Calculates break-even point, costs and revenues at the current level of output
    beq = tfc // (pri - avc)
    bep = tfc + (avc * beq)
    cc = tfc + (avc * clo)
    cr = pri * clo

    #If the break-even point is larger than the current level of output, then the lines are extrapolated a bit further from the break-even point
    if beq > clo:
        rangenums = int(((11/10) * beq) + 1)
        x = list(range(rangenums))
    #Else, the lines stop at the current level of output
    else:
        x = list(range(clo+1))

    #Calculate the two lines
    y0 = [tfc] * len(x)
    y1 = [tfc + (avc * num) for num in x]
    y2 = [pri * num for num in x]

    #Calculate the shape indicating profit or loss
    porlx = [beq, clo, clo, beq]
    porly = [bep, cc, cr, bep]

    #Plot the two lines
    plt.plot(x, y0, label = "Total Fixed Costs")
    plt.plot(x, y1, label = "Total Costs")
    plt.plot(x, y2, label = "Total Revenues")
    #Plot the shape indicating profit or loss
    if beq < clo:
        plt.fill(porlx, porly, "g", label = "Profit")
    elif beq > clo:
        plt.fill(porlx, porly, "r", label = "Loss")

    #Plot break-even point, current costs and revenues
    plt.scatter(beq, bep)
    if beq == clo:
        plt.annotate("BEQ, CLO, (%s, %s)" % (str(beq), str(bep)), (beq, bep))
    else:
        plt.annotate("BEQ, (%s, %s)" % (str(beq), str(bep)), (beq, bep))
        plt.scatter(clo, cc)
        plt.annotate("CLO (Costs), (%s, %s)" % (str(clo), str(cc)), (clo, cc))
        plt.scatter(clo, cr)
        plt.annotate("CLO (Revenues), (%s, %s)" % (str(clo), str(cr)), (clo, cr))
    plt.grid(linestyle = "dotted")
    plt.axvspan(beq, clo, facecolor="lightcyan", alpha=0.5, label = "Margin of safety")
    leg = plt.legend(loc='upper center')
    plt.show()

#GUI created
sg.theme("Default1")
layout = [
            [sg.Text('Current level of output:', size = (20, 1)), sg.In(key=1)],
            [sg.Text('Total fixed costs:', size = (20, 1)), sg.In(key=2)],
            [sg.Text('Average variable costs:', size = (20, 1)), sg.In(key=3)],
            [sg.Text('Price:', size = (20, 1)), sg.In(key=4)],
            [sg.Button('Create break-even chart'), sg.Button('Exit')]
        ]
window = sg.Window('BECMaker', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    createbec(values)

window.close()
