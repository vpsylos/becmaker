import matplotlib.pyplot as plt

#Asks for input
clo = int(input("Insert current level of output: "))
tfc = int(input("Insert total fixed costs: "))
avc = int(input("Insert average variable costs: "))
pri = int(input("Insert price: "))

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
else:
    plt.fill(porlx, porly, "r", label = "Loss")
#Plot break-even point, current costs and revenues
plt.scatter(beq, bep)
plt.annotate("BEQ, (%s, %s)" % (str(beq), str(bep)), (beq, bep))
plt.scatter(clo, cc)
plt.annotate("(%s, %s)" % (str(clo), str(cc)), (clo, cc))
plt.scatter(clo, cr)
plt.annotate("(%s, %s)" % (str(clo), str(cr)), (clo, cr))
plt.grid(linestyle = "dotted")
leg = plt.legend(loc='upper center')
plt.show()
