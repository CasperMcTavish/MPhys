import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys


#file_name_grid = "grid_positions_197.txt"
#file_name_polar = "grid_positions_197.txt_polar"
#file_name_value = "Efficiency"

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


# takes files and plots in polar and as box
def plot_and_save(file_name_polar = "grid_positions_197.txt_polar", file_name_grid = "grid_positions_197.txt", file_name_value = "Efficiency"):

    # read in correct files

    azi_rad = read_file(file_name_polar)
    vals = read_file(file_name_value)
    # non polar
    positions = read_file(file_name_grid)

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

    # Changes size of boxes'
    width = depth = 200

    # setting up colors for bars
    colors = plt.cm.jet(eff.flatten()/float(eff.max()))


    # Create string name for prints
    title_name = file_name_value + "_" + file_name_grid + "_"

    ax1.bar3d(x, y, np.zeros(len(eff)), width, depth, eff, shade=True, color=colors)
    fig.colorbar(plt.cm.ScalarMappable(cmap = 'jet'), ax = ax1)
    plt.savefig(title_name + "bar_plot.png")
    plt.show()



    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot_trisurf(np.array(azi), np.array(rad), np.array(eff), cmap=plt.cm.YlGnBu_r)
    plt.savefig(title_name + "trisurf_plot.png")
    plt.show()

# Collect arguments to run, if you dont have enough, stop the code

if len(sys.argv) == 4:
    # ignoring the name of the python script
    plot_and_save(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    print("collect_data takes exactly 3 arguments (" + str(len(sys.argv)-1) + ") given.\nPlease input polar position text file, grid position text file, and values text file to continue...")
