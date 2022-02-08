import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def read_file(filename):
    with open(filename) as f:
        contents = f.readlines()

    if (len(contents) > 1):
        print("File read of length: " + str(len(contents)))
    else:
        print("File length is too short to process (please include more positions)")

    return contents


def splitter(array):
    # ASSUMES TWO DIFFERENT COMPONENTS OF THE ARRAY OF STRINGS, SO WILL SPLIT THEM
    list1 = []
    list2 = []
    # begin loop
    for i in range(len(array)):
        # split position
        spl_pos = str.split(array[i])
        # convert to floats here
        list1.append(float(spl_pos[0]))
        list2.append(float(spl_pos[1]))

    return list1, list2

# read in correct files
azi_rad = read_file("datapoints_115_0_270.txt_polar_mm")
vals = read_file("Efficiency")
# non polar
positions = read_file("datapoints_115_0_270.txt")

azi, rad = splitter(azi_rad)
eff, err = splitter(vals)
x, y = splitter(positions)


# two input arrays
#azimut = np.random.rand(3000)*2*np.pi
#radius = np.random.rayleigh(29, size=3000)

# define binning
#rbins = np.linspace(0,np.array(rad).max(), 30)
#abins = np.linspace(0,2*np.pi, 60)

#calculate histogram
#hist, _, _ = np.histogram2d(azi, rad, bins=(abins, rbins))
#A, R = np.meshgrid(abins, rbins)

# plot
#fig, ax = plt.subplots(subplot_kw=dict(projection="polar"))

#pc = ax.pcolormesh(A, R, eff, cmap="magma_r")
#fig.colorbar(pc)

#plt.show()

# Bar chart
fig = plt.figure()
ax1 = fig.add_subplot(projection='3d')

# Formatting for bar chart
x = np.array(x)
y = np.array(y)
eff = np.array(eff)
bottom = np.zeros_like(x)
top = x+y
width = depth = 250

# setting up colors for bars

# add a bit more sensitivity at higher values
colors = plt.cm.jet(eff.flatten()/float(eff.max()))

ax1.bar3d(x, y, np.zeros(len(eff)), width, depth, eff, shade=True, color=colors)
fig.colorbar(plt.cm.ScalarMappable(cmap = 'jet'), ax = ax1)
plt.show()



fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_trisurf(np.array(azi), np.array(rad), np.array(eff), cmap=plt.cm.YlGnBu_r)
plt.show()
