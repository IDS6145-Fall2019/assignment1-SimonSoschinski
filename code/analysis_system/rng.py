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


# Creating the multiplot grid (2x5)
fig, axes = plt.subplots(2,5, sharex = True, sharey = True)

# 1st row 1st plot
axes[0, 0].scatter(np.random.rand(a), np.random.rand(a), color = 'black', s = 1)
axes[0, 0].set_aspect('equal', 'box')
axes[0, 0].set_xlabel("N = " + str(a))
axes[0, 0].xaxis.set_label_position('top')
axes[0, 0].set_ylabel("Pseudo-Random")

# 1st row 2nd plot
axes[0, 1].scatter(np.random.rand(b), np.random.rand(b), color = 'black', s = 1)
axes[0, 1].set_aspect('equal', 'box')
axes[0, 1].set_xlabel("N = " + str(b))
axes[0, 1].xaxis.set_label_position('top')

# 1st row 3rd plot
axes[0, 2].scatter(np.random.rand(c), np.random.rand(c), color = 'black', s = 1)
axes[0, 2].set_aspect('equal', 'box')
axes[0, 2].set_xlabel("N = " + str(c))
axes[0, 2].xaxis.set_label_position('top')

# 1st row 4th plot
axes[0, 3].scatter(np.random.rand(d), np.random.rand(d), color = 'black', s = 1)
axes[0, 3].set_aspect('equal', 'box')
axes[0, 3].set_xlabel("N = " + str(d))
axes[0, 3].xaxis.set_label_position('top')

# 1st row 5th plot
axes[0, 4].scatter(np.random.rand(e), np.random.rand(e), color = 'black', s = 1)
axes[0, 4].set_aspect('equal', 'box')
axes[0, 4].set_xlabel("N = " + str(e))
axes[0, 4].xaxis.set_label_position('top')


# Generating Quasi-Random numbers
soba = ss.i4_sobol_generate(2, a)
sobb = ss.i4_sobol_generate(2, b)
sobc = ss.i4_sobol_generate(2, c)
sobd = ss.i4_sobol_generate(2, d)
sobe = ss.i4_sobol_generate(2, e)

# 2nd row 1st plot
axes[1, 0].scatter(soba[:, 0], soba[:, 1], color = 'black', s = 1)
axes[1, 0].set_aspect('equal', 'box')
axes[1, 0].set_ylabel("Quasi-Random")

# 2nd row 2nd plot
axes[1, 1].scatter(sobb[:, 0], sobb[:, 1], color = 'black', s = 1)
axes[1, 1].set_aspect('equal', 'box')

# 2nd row 3rd plot
axes[1, 2].scatter(sobc[:, 0], sobc[:, 1], color = 'black', s = 1)
axes[1, 2].set_aspect('equal', 'box')

# 2nd row 4th plot
axes[1, 3].scatter(sobd[:, 0], sobd[:, 1], color = 'black', s = 1)
axes[1, 3].set_aspect('equal', 'box')

# 2nd row 5th plot
axes[1, 4].scatter(sobe[:, 0], sobe[:, 1], color = 'black', s = 1)
axes[1, 4].set_aspect('equal', 'box')


plt.show()




