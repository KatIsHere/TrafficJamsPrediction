import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from Macromodel import LWR_Model
from tempfile import TemporaryFile
import math
outfilenp = 'matrix.npy'
outfiletxt = 'matrix.txt'
G = nx.Graph()
# 29 m/s -> 65 mph
VelocityMax = 0.2

def SpeedToDensity(v, vMax):
    return VelocityMax*(1 - v/vMax)


def path_prossesing(Gr, nodes, paceX = 30, teta = 0.2, TMIN = math.inf, save = False, saveMatrix = None, saveParams = None):
    def startingDensity(x, lMap, nodes):
        for i in range(len(lMap) - 1):
            if x >= lMap[i] and x < lMap[i + 1]:
                maxSpeed = Gr.edges[nodes[i], nodes[i+1]]['maxSpeed']
                sp = Gr.edges[nodes[i], nodes[i+1]]['Speed']
                dens = SpeedToDensity(sp, maxSpeed)
                return dens
    L = 0
    maxSp = []
    tmin = 0 
    density0 = []
    Lmap = [0]
    for i in range(len(nodes) - 1):
        maxSpeed = Gr.edges[nodes[i], nodes[i+1]]['maxSpeed']
        maxSp.append(maxSpeed)
        leng = Gr.edges[nodes[i], nodes[i+1]]['L']
        L += leng
        Lmap.append(L)
        sp = Gr.edges[nodes[i], nodes[i+1]]['Speed']
        tmin += leng/sp
    if tmin > TMIN:
        return None
    maxSp = max(maxSp)
    model = LWR_Model(L, maxSp)
    segments = math.ceil(L/paceX)
    timeSegm = math.ceil(tmin/teta)
    x0 = 0
    for i in range(segments):
        density0.append(startingDensity(x0 + i*paceX, Lmap, nodes))
    teta = tmin/timeSegm
    dens = model.Godunov(0, L, teta, segments, timeSegm, None, density0)
    values = [dens, L, tmin, segments, teta, maxSp]
    if save:
        np.save(saveMatrix, dens)
        values = np.array([dens, L, tmin, segments, teta, maxSp])
        np.save(saveParams, values)
    return values

def speed(p, vMax):
    return vMax*(1 - p/VelocityMax)

def time_calc(L, tmax, segments, teta, dens, vMax):
    tSum = 0
    n = 0
    paceX = L//segments
    for i in range(segments):
        if n <= tmax/teta:
            p = dens[n][i]
        else:
            return math.inf
        t = paceX/speed(p, vMax)
        n = math.floor(t / teta)
        tSum += t
    print(tSum)
    return tSum

#nx.draw(G, with_labels = True, font_weight = 'bold')

def path_load(loadMatrix, loadParams):
    density = np.load(loadMatrix)
    params = np.load(loadParams)
    return density, params

def findPath(start, finish, Gr):
    Paths = nx.all_simple_paths(Gr, source=start, target=finish)
    i = 0
    timeMin = math.inf
    optimalPath = 0
    pathLenght = 0
    paths = list(Paths)
    paths.sort(key = lambda t: len(t), reverse= False)
    for p in paths:
        saveMatrixTo = 'matrix' + str(i) + '.npy'
        saveValuesTo = 'values' + str(i) + '.npy'    
        i+=1       
        res = path_prossesing(Gr, p, TMIN=timeMin, save=True, saveMatrix=saveMatrixTo, saveParams=saveValuesTo)
        if res is None:
            continue
        else:     
            dens, L, tmin, segments, teta, maxSp = res[0], res[1], res[2], res[3], res[4], res[5]
        t = time_calc(L, tmin, segments, teta, dens, maxSp)
        print("On path", p, "\n")
        if t < timeMin:
            timeMin = t
            optimalPath = p
            pathLenght = L
    return timeMin, optimalPath
 

def findAllPaths(start, finish, Gr):
    Paths = nx.all_simple_paths(Gr, source=start, target=finish)
    i = 0
    paths = list(Paths)
    paths.sort(key = lambda t: len(t), reverse= False)
    pathList = []
    density = []
    for p in paths:
        saveMatrTo = 'matrixes//matrix' + str(i) + '.npy' 
        saveValuesTo = 'matrixes//values' + str(i) + '.npy'
        i+=1       
        #res = path_prossesing(Gr, p, save=True, saveMatrix=saveMatrTo, saveParams=saveValuesTo)
        #if res is None:
        #    continue
        #else:     
        #    dens, L, tmin, segments, teta, maxSp = res[0], res[1], res[2], res[3], res[4], res[5]
        #dens = np.load(saveMatrTo)
        dens, L, tmin, segments, teta, maxSp = np.load(saveValuesTo) 
        t = time_calc(L, tmin, segments, teta, dens, maxSp)
        print("On path", p, "\n")
        pathList.append(p)
        density.append(dens)
    return pathList, density


def findDensOnPath(Gr, path, tosave = False, saveMatrTo = None, SaveValuesTo= None):
    res = path_prossesing(Gr, path, save=tosave, saveMatrix=saveMatrTo, saveParams=SaveValuesTo)
    if res is None:
        return None
    else:     
        dens, L, tmin, segments, teta, maxSp = res[0], res[1], res[2], res[3], res[4], res[5]
    t = time_calc(L, tmin, segments, teta, dens, maxSp)
    print("On path", path, "\n")
    return dens


def drawMatrix(i):
    plt.figure(i)
    outfilenp = "matrix" + str(i-1) + ".npy"
    dens = np.load(outfilenp)
    plt.imshow(dens)
    plt.colorbar()


# for i in range(6, 9):
#     drawMatrix(i)
# plt.show()

#t, path = findPath(1, 10, G)
#print(t, 'seconds on path', path)