import matplotlib.pyplot as plt
from numpy.random import exponential
dt = 0.01
def sir(t_end):
    t = 0
    s_0 = 0.99
    i_0 = 1 - s_0
    r_0 = 0
    beta = 0.5
    gamma = 0.33333
    T = [0]
    S = [s_0]
    I = [i_0]
    R = [r_0]
    dS = [-beta * s_0 * i_0]
    dI = [beta * s_0 * i_0 - gamma * i_0]
    dR = [gamma * i_0]
    while t < t_end:
        T.append(t)
        ds = dS[-1]
        di = dI[-1]
        dr = dR[-1]
        s = S[-1] + dt * ds
        i = I[-1] + dt * di
        r = R[-1] + dt * dr
        dS.append(-beta * s * i)
        dI.append(beta * s * i - gamma * i)
        dR.append(gamma * i)
        S.append(s)
        I.append(i)
        R.append(r)
        
        t += dt
    return T, S, I, R

t, s, i, r = sir(100)
plt.plot(t, s, label='suspect')
plt.plot(t, i, label='infected')
plt.plot(t, r, label='recovered / dead')
plt.legend()
plt.savefig('sir.png')