import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

def blending(t):
    return 6 * (t ** 5) - 15 * (t ** 4) + 10 * (t ** 3)
def normalBlending(t):
    return t
yVector = np.random.randint(-256,256,size=11)

def normalNoise(x):
    f=math.floor(x)
    c=math.ceil(x)
    moveFromX1 = x-f
    moveFromX2 = c-x
    return round(normalBlending(moveFromX2)*yVector[f] + normalBlending(moveFromX1)*yVector[c])

def perlinNoise(x):
    f=math.floor(x)
    c=math.ceil(x)
    moveFromX1 = x-f
    moveFromX2 = c-x
    return round(blending(moveFromX2)*yVector[f] + blending(moveFromX1)*yVector[c]) 

xArray = np.linspace(0, 10, 500)
yArray = [perlinNoise(i) for i in xArray]
zArray = [normalNoise(i) for i in xArray]

fig, axs = plt.subplots(2, 1, figsize=(8, 8))
axs[0].plot(xArray, yArray)
axs[0].set_xlim(0, 10)
axs[0].set_ylim(-256, 256)
axs[0].set_title('y')
axs[1].plot(xArray, zArray)
axs[1].set_xlim(0, 10)
axs[1].set_ylim(-256, 256)
axs[1].set_title('z')

plt.tight_layout()
plt.show()
