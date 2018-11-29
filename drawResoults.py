import numpy as np
import matplotlib.pyplot as plt
import Model
from map_config import getGraph

G = getGraph()
path = [[20, 21, 2, 1, 3, 4, 5, 6, 7, 8], [8, 9, 12, 15, 16, 18, 19,20]]


loadMatr0 = "pics//matrix0.npy"
loadParams0 = "pics//params0.npy"
loadMatr1 = "pics//matrix1.npy"
loadParams1 = "pics//params1.npy"
#density1 = Model.path_prossesing(G, path[0], paceX=20, teta=1 ,save=True, saveMatrix=loadMatr0, saveParams=loadParams0)[0]
#density2 =  Model.path_prossesing(G, path[1], paceX=20, teta=1 ,save=True, saveMatrix=loadMatr1, saveParams=loadParams1)[0]
density1 np.load(loadMatr0)
density2 = np.load(loadMatr1)

plt.figure(1)
plt.imshow(density1)
plt.colorbar()

plt.figure(2)
plt.imshow(density2)
plt.colorbar()

plt.show()