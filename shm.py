import matplotlib.pyplot as plt
import numpy as np
from math import sin
# try with shm first
dt = 0.001
dphi_0 = 0
L = 10
g = 10

def y(t_end):
    y0 = 1
    i = 0
    yi = [[0, y0]]
    dyi = [[0, dphi_0]]
    while i < t_end:
        i += dt
        dyi.append([i, dyi[-1][-1] - g/L * sin(yi[-1][-1]) * dt])
        yi.append([i, yi[-1][-1] + dyi[-2][-1] * dt])
        
    return yi, dyi

ys, dys = y(np.pi * 4)
array_ys = np.array(ys).T[1, :]
array_dys = np.array(dys).T[1, :]
print(array_ys)
plt.plot(array_ys)
plt.plot(np.cos(np.arange(0, np.pi * 4, 0.001)))
plt.show()