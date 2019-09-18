import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import sobol_seq as ss

# Since it reminds me of the data vis class
style.use('ggplot')

# Defining differend N
a = 100
b = 500
c = 1000
d = 2000
e = 5000


fig, axes = plt.subplots(2,5, sharex = True, sharey = True)


axes[0, 0].scatter(np.random.rand(a), np.random.rand(a), color = 'black', s = 1)
axes[0, 0].set_aspect('equal', 'box')
axes[0, 0].set_xlabel("N = " + str(a))
axes[0, 0].xaxis.set_label_position('top')
axes[0, 0].set_ylabel("Pseudo-Random")


axes[0, 1].scatter(np.random.rand(b), np.random.rand(b), color = 'black', s = 1)
axes[0, 1].set_aspect('equal', 'box')
axes[0, 1].set_xlabel("N = " + str(b))
axes[0, 1].xaxis.set_label_position('top')


axes[0, 2].scatter(np.random.rand(c), np.random.rand(c), color = 'black', s = 1)
axes[0, 2].set_aspect('equal', 'box')
axes[0, 2].set_xlabel("N = " + str(c))
axes[0, 2].xaxis.set_label_position('top')


axes[0, 3].scatter(np.random.rand(d), np.random.rand(d), color = 'black', s = 1)
axes[0, 3].set_aspect('equal', 'box')
axes[0, 3].set_xlabel("N = " + str(d))
axes[0, 3].xaxis.set_label_position('top')


axes[0, 4].scatter(np.random.rand(e), np.random.rand(e), color = 'black', s = 1)
axes[0, 4].set_aspect('equal', 'box')
axes[0, 4].set_xlabel("N = " + str(e))
axes[0, 4].xaxis.set_label_position('top')


axes[1, 0].scatter(ss.i4_sobol_generate(3, a), ss.i4_sobol_generate(3, a), color = 'black', s = 1)
axes[1, 0].set_aspect('equal', 'box')
axes[1, 0].set_ylabel("Quasi-Random")
axes[1, 1].scatter(ss.i4_sobol_generate(2, b), ss.i4_sobol_generate(2, b), color = 'black', s = 1)
axes[1, 1].set_aspect('equal', 'box')


axes[1, 2].scatter(ss.i4_sobol_generate(2, c), ss.i4_sobol_generate(2, c), color = 'black', s = 1)
axes[1, 2].set_aspect('equal', 'box')


axes[1, 3].scatter(ss.i4_sobol_generate(2, d), ss.i4_sobol_generate(2, d), color = 'black', s = 1)
axes[1, 3].set_aspect('equal', 'box')


axes[1, 4].scatter(ss.i4_sobol_generate(2, e), ss.i4_sobol_generate(2, e), color = 'black', s = 1)
axes[1, 4].set_aspect('equal', 'box')


plt.show()
