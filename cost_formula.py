from numpy import *
import numpy as np

it = np.array([[14.2, 215], [16.4, 325], [11.9, 185], [15.2, 332], [18.5, 406], [22.1, 522], [19.4, 412], [25.1, 614],
               [23.4, 544], [18.1, 421], [22.6, 445], [17.2, 408]])
print(it)
avx = sum([item[0] for item in it]) / 12
avy = sum([item[1] for item in it]) / 12
alpha = sum([(a[0] - avx) * (a[1] - avy) for a in it])
beta = sqrt(sum([power(a[0] - avx, 2) for a in it]) * sum([power(a[1] - avy, 2) for a in it]))
theta = alpha / beta
print(theta)
