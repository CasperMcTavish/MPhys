import numpy as np
import matplotlib.pyplot as plt

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
azi_rad = read_file("datapoints_115_0_270.txt")
vals = read_file("Efficiency")

azi, rad = splitter(azi_rad)
print(azi)
print("=================")
print(rad)
eff, err = splitter(vals)

print(eff)
print("=================")
print(err)
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

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_trisurf(np.array(azi), np.array(rad), np.array(eff), cmap=plt.cm.YlGnBu_r)
plt.show()
