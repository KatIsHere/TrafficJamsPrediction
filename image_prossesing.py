from PIL import Image, ImageDraw
import networkx as nx
from map_config import getGraph
import Model
import math
# loacations
nodes = {1 : (510, 271), 2:(450, 390), 3:(708, 215), 4:(854, 177), 5:(932, 154), 6:(1013, 130), \
        7:(1210, 42), 8:(1241, 55), 9:(1123, 271), 10:(1052, 219), 11:(975, 257), 12:(1025, 342), \
        13:(877, 286), 14:(733, 320), 15:(959, 387), 16:(687, 554), 17:(671, 709), 18:(544, 642), \
        19:(346, 760), 20:(286, 795), 21:(316, 704)}
# connected = [(1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (20, 21), (21, 2), (2, 1), (4, 13), (13, 15), \
#                 (2, 14), (14, 13), (13, 11), (11, 10)]

problem_area = {(13, 15): [(906, 403), (910, 425), (928, 425)], \
                (8, 9) : [(1167, 215)], (17, 18) : [(570, 685)]}

# get traffic graph:
G = getGraph()
#t_start = [12, 0, 0]
pace = 30

# optimal path
t, path = Model.findPath(16, 4, G)
strTime = "Estimated time = " + str(t) + " seconds"

img1 = Image.open('Holosievo.png')
draw1 = ImageDraw.Draw(img1, mode='RGBA')
#draw.line()
for i in range(1, len(path)-1):
    if (nodes[path[i-1]], nodes[path[i]]) in problem_area:
        AllDots = problem_area[(path[i-1], path[i])]
        draw2.line([nodes[path[i-1]], AllDots[0]], fill = color, width=5)
        for j in range(1, len(AllDots) - 1):
            draw2.line([AllDots[j-1], AllDots[j]], fill = color, width=5)
        draw2.line([AllDots[-1], nodes[path[i]]], fill = color, width=5)
    elif (nodes[path[i]], nodes[path[i-1]]) in problem_area:
        AllDots = problem_area[(path[i-1], path[i])]
        draw2.line([nodes[path[i-1]], AllDots[0]], fill = color, width=5)
        for j in range(len(AllDots) - 1, 1):
            draw2.line([AllDots[j-1], AllDots[j]], fill = color, width=5)
        draw2.line([AllDots[-1], nodes[path[i]]], fill = color, width=5)
    else:
        draw1.line([nodes[path[i-1]], nodes[path[i]]], fill='blue', width=5)

draw1.text((75,50), strTime, fill='black', width = 10)
del draw1
img1.save('optimalPath_t4.png')

# pathsNeeded = [[20, 21, 2, 1, 3, 4, 5, 6, 7, 8], [8, 9, 12, 15, 16, 18, 19,20],     \
#             [2, 14, 13, 11, 10], [8, 9, 12, 15, 16, 17, 18, 19, 20],           \
#             [3, 14, 13, 4, 5, 11, 10, 6], [3, 14, 13, 15, 12, 11, 10, 9]]
# #allPaths, allDens = Model.findAllPaths(20, 7, G)
# # all paths for t = 12:00:00
# img2 = Image.open('Holosievo.png')
# draw2 = ImageDraw.Draw(img2, mode='RGBA')
# count = 0
# lengthMin = math.inf
# density = []
# for path in pathsNeeded:
#     saveMatr = "resoults//matrix" + str(count) + ".npy"
#     saveParams = "resoults//params" + str(count) + ".npy"
#     dens = Model.findDensOnPath(G, path, tosave=True, saveMatrTo=saveMatr, SaveValuesTo=saveParams)
#     density.append(dens)
#     count += 1
# count = 0
# for path in pathsNeeded:
#     dens = density[count]
#     if len(dens) < lengthMin:
#         lengthMin = len(dens)
#     L = 0
#     i = 1
#     for i in range(1, len(path)):
#         L += G.edges[path[i-1], path[i]]['L']
#         l = 0
#         #draw2.text(path[i-1], str(path[i-1]), fill='blue', width=2)
#         color = 'blue'
#         while True:
#             if l <= L: #and i < len(dens[0]):
#                 l += pace
#                 if dens[0][i-1] <= 0.05:
#                     color = 'green'
#                 elif dens[0][i-1] <= 0.12 and dens[0][i-1] > 0.07:
#                     color = 'yellow'
#                 elif dens[0][i-1] <= 0.16 and dens[0][i-1] > 0.12:
#                     color = 'orange'
#                 elif dens[0][i-1] > 0.16:
#                     color = 'red'
#                 if (path[i-1], path[i]) in problem_area:
#                     AllDots = problem_area[(path[i-1], path[i])]
#                     draw2.line([nodes[path[i-1]], AllDots[0]], fill = color, width=5)
#                     for j in range(1, len(AllDots) - 1):
#                         draw2.line([AllDots[j-1], AllDots[j]], fill = color, width=5)
#                     draw2.line([AllDots[-1], nodes[path[i]]], fill = color, width=5)
#                 else:
#                     draw2.line([nodes[path[i-1]], nodes[path[i]]], fill = color, width=5)
#             else:
#                 break
#     count+=1
        
# del draw2
# img2.save('allPath_start_t25.png')

# # all paths for t = 12:00:00
# img2 = Image.open('Holosievo.png')
# draw2 = ImageDraw.Draw(img2, mode='RGBA')
# count = 0
# for path in pathsNeeded:
#     dens = density[count]
#     L = 0
#     i = 1
#     for i in range(1, len(path)):
#         L += G.edges[path[i-1], path[i]]['L']
#         l = 0
#         #draw2.text(path[i-1], str(path[i-1]), fill='blue', width=2)
#         color = 'blue'
#         while True:
#             if l <= L: #and i < len(dens[0]):
#                 l += pace
#                 if dens[lengthMin//2][i-1] <= 0.05:
#                     color = 'green'
#                 elif dens[lengthMin//2][i-1] <= 0.12 and dens[lengthMin//2][i-1] > 0.07:
#                     color = 'yellow'
#                 elif dens[lengthMin//2][i-1] <= 0.16 and dens[lengthMin//2][i-1] > 0.12:
#                     color = 'orange'
#                 elif dens[lengthMin//2][i-1] > 0.16:
#                     color = 'red'
#                 if (path[i-1], path[i]) in problem_area:
#                     AllDots = problem_area[(path[i-1], path[i])]
#                     draw2.line([nodes[path[i-1]], AllDots[0]], fill = color, width=5)
#                     for j in range(1, len(AllDots) - 1):
#                         draw2.line([AllDots[j-1], AllDots[j]], fill = color, width=5)
#                     draw2.line([AllDots[-1], nodes[path[i]]], fill = color, width=5)
#                 else:
#                     draw2.line([nodes[path[i-1]], nodes[path[i]]], fill = color, width=5)
#             else:
#                 break
#     count+=1
        
# del draw2
# img2.save('allPath_start.png')

# # all paths for t = 12:05:00
# img2 = Image.open('Holosievo.png')
# draw2 = ImageDraw.Draw(img2, mode='RGBA')
# count = 0
# for path in pathsNeeded:
#     dens = density[count]
#     L = 0
#     i = 1
#     for i in range(1, len(path)):
#         L += G.edges[path[i-1], path[i]]['L']
#         l = 0
#         #draw2.text(path[i-1], str(path[i-1]), fill='blue', width=2)
#         color = 'blue'
#         while True:
#             if l <= L: #and i < len(dens[0]):
#                 lengh = len(dens)
#                 l += pace
#                 if dens[lengthMin - 1][i-1] <= 0.05:
#                     color = 'green'
#                 elif dens[lengthMin - 1][i-1] <= 0.12 and dens[lengthMin - 1][i-1] > 0.07:
#                     color = 'yellow'
#                 elif dens[lengthMin - 1][i-1] <= 0.16 and dens[lengthMin - 1][i-1] > 0.12:
#                     color = 'orange'
#                 elif dens[lengthMin - 1][i-1] > 0.16:
#                     color = 'red'
#                 if (path[i-1], path[i]) in problem_area:
#                     AllDots = problem_area[(path[i-1], path[i])]
#                     draw2.line([nodes[path[i-1]], AllDots[0]], fill = color, width=5)
#                     for j in range(1, len(AllDots) - 1):
#                         draw2.line([AllDots[j-1], AllDots[j]], fill = color, width=5)
#                     draw2.line([AllDots[-1], nodes[path[i]]], fill = color, width=5)
#                 else:
#                     draw2.line([nodes[path[i-1]], nodes[path[i]]], fill = color, width=5)
#             else:
#                 break
#     count+=1
        
# del draw2
# img2.save('allPath_start_t5.png')

