import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

def blending(t):
    return 6 * (t ** 5) - 15 * (t ** 4) + 10 * (t ** 3)

random2D = np.random.randint(-256, 256, size=(12, 12))

def mapi(xx,yy,mox,moy):
    return random2D[xx][yy] *(
        blending((mox**2+moy**2)/2**0.5)
    )
    
    
    

def perlin(x, y):
    x1 = np.floor(x).astype(int)
    x2 = np.floor(x+1).astype(int)
    y1 = np.floor(y).astype(int)
    y2 = np.floor(y+1).astype(int)
    return mapi(x1, y1, x2-x, y2-y) + mapi(x2, y1, x-x1, y2-y) + mapi(x1, y2, x2-x, y-y1) - mapi(x2, y2, x-x1, y-y1)

unit=100
xArray = np.linspace(0, 10, unit)
yArray = np.linspace(0, 10, unit)
X, Y = np.meshgrid(xArray, yArray)
Z = np.empty((unit, unit))
for i, x in enumerate(xArray):
    for j, y in enumerate(yArray):
        Z[i,j] = perlin(x, y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap = cm.gist_earth) 
plt.show()
