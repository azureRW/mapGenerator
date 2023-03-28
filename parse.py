import json
with open('output.json', 'r') as file:
    data = json.load(file)
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from random import randint
from math import floor

def blending(t):
    return 6 * (t ** 5) - 15 * (t ** 4) + 10 * (t ** 3)

def lerp(g1, g2, t):
    return g1 + t * (g2 - g1)

def grad2(hashvalue, dx, dy):
    return [dy, dx + dy, dx, dx - dy, -dy, -dx - dy, -dx, -dx + dy][hashvalue % 8];

rand_table = np.random.randint(255, size = 256).tolist()
def _perlin2(x, y):
    xi = floor(x)
    yi = floor(y)

    aa = rand_table[
        (rand_table[xi % 256] + yi) % 256
    ]
    ba = rand_table[
        (rand_table[(xi + 1) % 256] + yi) % 256
    ]
    ab = rand_table[
        (rand_table[xi % 256] + yi + 1) % 256
    ]
    bb = rand_table[
        (rand_table[(xi + 1) % 256] + yi + 1) % 256
    ]

    dx = x - xi
    dy = y - yi    

    u = blending(dx)
    v = blending(dy)

    g1 = lerp(grad2(aa, dx, dy), grad2(ba, dx - 1, dy), u)
    g2 = lerp(grad2(ab, dx, dy - 1), grad2(bb, dx - 1, dy - 1), u)

    return lerp(g1, g2, v)
_perlin2 = np.frompyfunc(_perlin2, 2, 1)

def perlin2(x, y):
    cx, cy = np.meshgrid(x, y)
    return _perlin2(cx, cy).astype(np.cfloat)

width = 100
x = np.arange(width)
y = np.arange(width)

X, Y = np.meshgrid(x, y) 
Z = perlin2(x / 25, y / 25)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap = cm.gist_earth) # 用地形高度顏色來著色
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_box_aspect((1, 1, 25 / width))
plt.title('Perlin noise')
plt.show()
