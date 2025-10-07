import numpy as np
import matplotlib.pyplot as plt

k = 1.3807e-23
c = 299792458

GHz = np.array([0.6, 1.2, 2.4, 4.8, 9.6, 22.0])
depth = np.array([0, 50, 100, 170, 250, 375])
F = np.array([7.59342e-21, 6.15189e-20, 3.90419e-19, 1.86758e-18, 8.12656e-18, 4.14506e-17])
a = np.array([2.0e-4, 4.0e-4, 8.0e-4, 1.6e-3, 3.2e-3, 7.0e-3])
b = np.array([1.15, 1.18, 1.20, 1.23, 1.26, 1.30])
d = np.array([0.0025, 0.0027, 0.0030, 0.0033, 0.0036, 0.0040])

Hz = GHz * 1e9

def f_i(T, i):
    w = Hz[i]
    ai, bi, di = a[i], b[i], d[i]
    t1 = (2*k*w**2) / (c**2)
    t2 = T / (1 + di * np.sqrt(T))
    t3 = (1 - np.exp(-ai * T**bi))
    return t1 * t2 * t3

def bisection(function, i, F_target, T_low=1.0, T_high=1000.0, tolerance=1):
    while (T_high - T_low) > tolerance:
        T_mid = 0.5 * (T_low + T_high)
        F_mid = function(T_mid, i)
        if (F_mid - F_target) * (function(T_low, i) - F_target) < 0:
            T_high = T_mid
        else:
            T_low = T_mid
    return 0.5 * (T_low + T_high)
        
T_values = []
for i in range(len(GHz)):
    T_val = bisection(f_i, i, F[i])
    T_values.append(T_val)
    
T_values = np.array(T_values)
    
plt.figure(figsize=(6, 5))
plt.plot(T_values, depth, 'o-', color='blue', linewidth=2)
plt.xlabel('Temperature (K)')
plt.ylabel('Depth from 1 bar (km)')
plt.title('Temperature vs Depth (MWR)')
plt.grid(True)
plt.gca().invert_yaxis()  # depth increases downward
plt.tight_layout()
plt.savefig("mwrTemperature.png", dpi=300)
plt.show()