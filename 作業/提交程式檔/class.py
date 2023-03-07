lil = [[0, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0]]
for alist in lil:
    print(alist)

import matplotlib.pyplot as plt

def plotlines(linelist, canvas=[-2, 2, -2, 2], finalize=True):
    plt.figure(figsize=(5, 5))
    plt.axis(canvas)    
    for aline in linelist:
        plt.plot([aline[0], aline[2]], [aline[1], aline[3]], linestyle='-', marker='o', color='b')
    plt.draw()
    plt.pause(.01)
    if finalize:
        plt.show()

fig1 = [[0, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0]]
plotlines(fig1)







def printlines(linelist):
    for i, aline in enumerate(linelist):
        print("Line%d: %0.3f %0.3f %0.3f %0.3f" % (i, aline[0], aline[1], aline[2], aline[3]))

printlines(fig1)

def plotshift(linelist, xshift=0, yshift=0):
    # 定義你的函數

    return something