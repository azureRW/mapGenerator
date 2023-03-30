import json
with open('output.json', 'r') as file:
    data = json.load(file)
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from random import randint
from math import floor
from array import array


Z= np.array( data.get("map"))
print(Z.shape)
xArray = np.linspace(0, 10, 100)
yArray = np.linspace(0, 10, 100)
X, Y = np.meshgrid(xArray, yArray)
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap = cm.gist_earth) # 用地形高度顏色來著色
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title('map')
plt.show()
