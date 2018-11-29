from Macromodel import LWR_Model
import matplotlib.pyplot as plt
import numpy as np
import math

l = 10 * 8000          #m
vMax = 60 * 1000/3600   #m/s
pace = 20
timeTeta = 1
segments = math.ceil(l/pace)

def startDens(x):
    if x>=0 and x<=1500:
        return 0.17
    elif x > 1500 and x <= 5000:
        return  0.1
    # else:
    #     return 0.7
    elif x > 5000 and x < 20000:
        return 0.04
    elif x > 20000 and x <= 25500:
        return 0.15
    elif x > 25500 and x <= 34000:
        return 0.12
    elif x >34000 and x<=60000:
        return 0.05
    else:
        return 0.08

if __name__ == "__main__":
    model = LWR_Model(l, vMax, startDens, _segmNumb=segments)
    X = np.linspace(0, 800, segments)
    T = np.linspace(0, 5, 20)
    density2 = model.Godunov(0, l, timeTeta, segments, 1000, startDens)
    plt.figure(2)
    plt.imshow(density2)
    plt.colorbar()
    plt.ylabel("t, sec")
    plt.xlabel("x/20, meters")
    plt.title("Density")

    plt.show()