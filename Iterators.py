import numpy as np


def sinx_x(x):
    if x == 0:
        return 1
    return np.sin(x) / x


def cosx_x(x):
    if x == 0:
        return 1
    return np.cos(x) / x


t_range = list(np.arange(-100, 100, 0.01))
sinx = list()
cosx = list()
for t in t_range:
    sinx.append(sinx_x(t))
    cosx.append(cosx_x(t))

# result_sin = sinx_x(-2)
# print('sin(x)/x', result_sin)
# result_cos = cosx_x(8)
# print('cos(x)/x', result_cos)
# print(sinx)
# print(cosx)
