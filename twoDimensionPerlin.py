import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import cv2


def blending(t):
    return 6 * (t ** 5) - 15 * (t ** 4) + 10 * (t ** 3)


def noise(frequentIndictor):
    unit=frequentIndictor*100
    matrix = np.random.uniform(-5, 5, size=(np.floor(unit/10).astype(int)+2, np.floor(unit/10).astype(int)+2))
    xArray = np.linspace(0, unit/10, unit)
    yArray = np.linspace(0, unit/10, unit)
    X, Y = np.meshgrid(xArray, yArray)
    Z = np.empty((unit, unit))
    for i, x in enumerate(xArray):
        for j, y in enumerate(yArray):
                x1 = np.floor(x).astype(int)
                x2 = np.floor(x+1).astype(int)
                y1 = np.floor(y).astype(int)
                y2 = np.floor(y+1).astype(int)
                Z[i,j] = (
                    (matrix[x1][y1]*blending(x2-x)+matrix[x2][y1]*blending(x-x1))*blending(y2-y)
                    +
                    (matrix[x1][y2]*blending(x2-x)+matrix[x2][y2]*blending(x-x1))*blending(y-y1)
                )
    if frequentIndictor==1:
        return Z
    else:
        return cv2.resize(Z, (100, 100), interpolation=cv2.INTER_AREA)

    
    

Z=noise(3)
xArray = np.linspace(0, 10, 100)
yArray = np.linspace(0, 10, 100)
X, Y = np.meshgrid(xArray, yArray)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap = cm.gist_earth) 
plt.show()
