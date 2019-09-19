import chaospy as cp
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

# Creating Normal Distribution and samplesizes
db = cp.Normal(mu = 0, sigma = 1)
samplesa = db.sample(a, rule = 'S')
samplesb = db.sample(b, rule = 'S')
samplesc = db.sample(c, rule = 'S')
samplesd = db.sample(d, rule = 'S')
samplese = db.sample(e, rule = 'S')

# 1st row 1st plot
axes[0, 0].hist(samplesa, bins = f)
axes[0, 0].set_xlabel("N = " + str(a))
axes[0, 0].xaxis.set_label_position('top')
axes[0, 0].set_ylabel("Normal")

# 1st row 2nd plot
axes[0, 1].hist(samplesb, bins = f)
axes[0, 1].set_xlabel("N = " + str(b))
axes[0, 1].xaxis.set_label_position('top')

# 1st row 3rd plot
axes[0, 2].hist(samplesc, bins = f)
axes[0, 2].set_xlabel("N = " + str(c))
axes[0, 2].xaxis.set_label_position('top')

# 1st row 4th plot
axes[0, 3].hist(samplesc, bins = f)
axes[0, 3].set_xlabel("N = " + str(c))
axes[0, 3].xaxis.set_label_position('top')

# 1st row 5th plot
axes[0, 4].hist(samplese, bins = f)
axes[0, 4].set_xlabel("N = " + str(e))
axes[0, 4].xaxis.set_label_position('top')


# Creating Uniform Distribution and samplesizes
db2 = cp.Uniform(-3, 3)
samples2a = db2.sample(a, rule = 'S')
samples2b = db2.sample(b, rule = 'S')
samples2c = db2.sample(c, rule = 'S')
samples2d = db2.sample(d, rule = 'S')
samples2e = db2.sample(e, rule = 'S')

# 2nd row 1st plot
axes[1, 0].hist(samples2a, bins = f)
axes[1, 0].set_xlabel("N = " + str(a))
axes[1, 0].xaxis.set_label_position('top')
axes[1, 0].set_ylabel("Uniform")

# 2nd row 2nd plot
axes[1, 1].hist(samples2b, bins = f)
axes[1, 1].set_xlabel("N = " + str(b))
axes[1, 1].xaxis.set_label_position('top')

# 2nd row 3rd plot
axes[1, 2].hist(samples2c, bins = f)
axes[1, 2].set_xlabel("N = " + str(c))
axes[1, 2].xaxis.set_label_position('top')

# 2nd row 4th plot
axes[1, 3].hist(samples2c, bins = f)
axes[1, 3].set_xlabel("N = " + str(c))
axes[1, 3].xaxis.set_label_position('top')

# 2nd row 5th plot
axes[1, 4].hist(samples2e, bins = f)
axes[1, 4].set_xlabel("N = " + str(e))
axes[1, 4].xaxis.set_label_position('top')


# Creating Exponential Distribution and samplesizes
db3 = cp.Exponential(1, 0)
samples3a = db3.sample(a, rule = 'S')
samples3b = db3.sample(b, rule = 'S')
samples3c = db3.sample(c, rule = 'S')
samples3d = db3.sample(d, rule = 'S')
samples3e = db3.sample(e, rule = 'S')

# 3rd row 1st plot
axes[2, 0].hist(samples3a, bins = f)
axes[2, 0].set_xlabel("N = " + str(a))
axes[2, 0].xaxis.set_label_position('top')
axes[2, 0].set_ylabel("Uniform")

# 3rd row 2nd plot
axes[2, 1].hist(samples3b, bins = f)
axes[2, 1].set_xlabel("N = " + str(b))
axes[2, 1].xaxis.set_label_position('top')

# 3rd row 3rd plot
axes[2, 2].hist(samples3c, bins = f)
axes[2, 2].set_xlabel("N = " + str(c))
axes[2, 2].xaxis.set_label_position('top')

# 3rd row 4th plot
axes[2, 3].hist(samples3c, bins = f)
axes[2, 3].set_xlabel("N = " + str(c))
axes[2, 3].xaxis.set_label_position('top')

# 3rd row 5th plot
axes[2, 4].hist(samples3e, bins = f)
axes[2, 4].set_xlabel("N = " + str(e))
axes[2, 4].xaxis.set_label_position('top')


plt.show()