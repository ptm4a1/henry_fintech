import numpy as np

K = 9100
Premium_Call = 60
Premium_Put = 45

Interval = 500
ST = np.arange(K - Interval, K + Interval)

x = np.maximum(ST - K, 0) + Premium_Call  
y = - (np.minimum(ST - K, 0) + Premium_Put)

import matplotlib.pyplot as plt
plt.plot(ST, x)
plt.plot(ST, y)
plt.show()