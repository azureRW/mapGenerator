import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

def blending(t):
    return 6 * (t ** 5) - 15 * (t ** 4) + 10 * (t ** 3)


def perlin(x, y,matrix):
    x1 = np.floor(x).astype(int)
    x2 = np.floor(x+1).astype(int)
    y1 = np.floor(y).astype(int)
    y2 = np.floor(y+1).astype(int)
    return (
        (matrix[x1][y1]*blending(x2-x)+matrix[x2][y1]*blending(x-x1))*blending(y2-y)
        +
        (matrix[x1][y2]*blending(x2-x)+matrix[x2][y2]*blending(x-x1))*blending(y-y1)
    )
    
    
unit=100
random2D = np.random.randint(-256, 256, size=(12, 12))
xArray = np.linspace(0, 10, unit)
yArray = np.linspace(0, 10, unit)
X, Y = np.meshgrid(xArray, yArray)
Z = np.empty((unit, unit))
for i, x in enumerate(xArray):
    for j, y in enumerate(yArray):
        Z[i,j] = perlin(x, y,random2D)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap = cm.gist_earth) 
plt.show()
