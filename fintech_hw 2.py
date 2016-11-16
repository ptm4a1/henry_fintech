import numpy as np

K = 9000
K2 = 9200
Premium_Put = 10
Premium_Put2 = 80


Interval = 500
ST = np.arange(K - Interval, K + Interval)
ST2 = np.arange(K2 - Interval, K2 + Interval)
A = np.minimum(ST - K, 0) + Premium_Put
B = -(np.minimum(ST2 - K2, 0) + Premium_Put2)

import matplotlib.pyplot as plt
plt.plot(ST, A)
plt.plot(ST2, B)
plt.show()