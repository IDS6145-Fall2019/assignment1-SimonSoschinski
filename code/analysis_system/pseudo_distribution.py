import numpy as np
import matplotlib.pyplot as plt

# Defining differend N
a = 100
b = 500
c = 1000
d = 2000
e = 5000

# Bins
f = 50

# Creating the multiplot grid (3x5)
fig, axes = plt.subplots(3,5)

# 1st row 1st plot
axes[0, 0].hist(np.random.normal(size = a), bins = f)
axes[0, 0].set_xlabel("N = " + str(a))
axes[0, 0].xaxis.set_label_position('top')
axes[0, 0].set_ylabel("Normal")

# 1st row 2nd plot
axes[0, 1].hist(np.random.normal(size = b), bins = f)
axes[0, 1].set_xlabel("N = " + str(b))
axes[0, 1].xaxis.set_label_position('top')

# 1st row 3rd plot
axes[0, 2].hist(np.random.normal(size = c), bins = f)
axes[0, 2].set_xlabel("N = " + str(c))
axes[0, 2].xaxis.set_label_position('top')

# 1st row 4th plot
axes[0, 3].hist(np.random.normal(size = d), bins = f)
axes[0, 3].set_xlabel("N = " + str(d))
axes[0, 3].xaxis.set_label_position('top')

# 1st row 5th plot
axes[0, 4].hist(np.random.normal(size = e), bins = f)
axes[0, 4].set_xlabel("N = " + str(e))
axes[0, 4].xaxis.set_label_position('top')

# 2nd row 1st plot
axes[1, 0].hist(np.random.uniform(-3, 3, a), bins = f)
axes[1, 0].set_xlabel("N = " + str(a))
axes[1, 0].xaxis.set_label_position('top')
axes[1, 0].set_ylabel("Uniform")

# 2nd row 2nd plot
axes[1, 1].hist(np.random.uniform(-3, 3, b), bins = f)
axes[1, 1].set_xlabel("N = " + str(b))
axes[1, 1].xaxis.set_label_position('top')

# 2nd row 3rd plot
axes[1, 2].hist(np.random.uniform(-3, 3, c), bins = f)
axes[1, 2].set_xlabel("N = " + str(c))
axes[1, 2].xaxis.set_label_position('top')

# 2nd row 4th plot
axes[1, 3].hist(np.random.uniform(-3, 3, d), bins = f)
axes[1, 3].set_xlabel("N = " + str(d))
axes[1, 3].xaxis.set_label_position('top')

# 2nd row 5th plot
axes[1, 4].hist(np.random.uniform(-3 , 3, e), bins = f)
axes[1, 4].set_xlabel("N = " + str(e))
axes[1, 4].xaxis.set_label_position('top')

# 3rd row 1st plot
axes[2, 0].hist(np.random.exponential(1, a), bins = f)
axes[2, 0].set_xlabel("N = " + str(a))
axes[2, 0].xaxis.set_label_position('top')
axes[2, 0].set_ylabel("Exponential")

# 3rd row 2nd plot
axes[2, 1].hist(np.random.exponential(1, b), bins = f)
axes[2, 1].set_xlabel("N = " + str(b))
axes[2, 1].xaxis.set_label_position('top')

# 3rd row 3rd plot
axes[2, 2].hist(np.random.exponential(1, c), bins = f)
axes[2, 2].set_xlabel("N = " + str(c))
axes[2, 2].xaxis.set_label_position('top')

# 3rd row 4th plot
axes[2, 3].hist(np.random.exponential(1, d), bins = f)
axes[2, 3].set_xlabel("N = " + str(d))
axes[2, 3].xaxis.set_label_position('top')

# 3rd row 5th plot
axes[2, 4].hist(np.random.exponential(1, e), bins = f)
axes[2, 4].set_xlabel("N = " + str(e))
axes[2, 4].xaxis.set_label_position('top')


plt.show()