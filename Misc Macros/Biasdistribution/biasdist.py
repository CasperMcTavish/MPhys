import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import matplotlib as mpl


# Calculate and plot the distribution of bias values as a histogram

# read and write, read formats into float array now with tuples
def read_file(filename):
    with open(filename) as f:
        contents = f.readlines()

    if (len(contents) > 1):
        print("File read of length: " + str(len(contents)))
    else:
        print("File length is too short to process (please include more positions)")

    contents = [contents[i].rstrip().lstrip() for i in range(len(contents))]
    contents = [contents[i].split() for i in range(len(contents))]
    contents = (np.array(contents)).astype(float)
    return contents

def stripper(contents):
    # strips strings with tuple and converts into np array of ints
    contents = [contents[i].rstrip().lstrip() for i in range(len(contents))]
    contents = [contents[i].split() for i in range(len(contents))]
    contents = (np.array(contents)).astype(int)
    return contents

def main(filename1, filename2, positionalfile):
    # take file for mu, efficiency, for 0 and 90. Find the different and plot histogram. Then maybe fit shit to the hist?

    vals1 = read_file(filename1)
    vals2 = read_file(filename2)
    positional = read_file(positionalfile)

    # remove erros
    vals_full1 = vals1[:,0]
    vals_full2 = vals2[:,0]

    # take differences
    diffs = vals_full1 - vals_full2

    # remove values above radius 90mm
    for i in range(len(diffs)):
        radius = np.sqrt((float(positional[i][0]))**2 + (float(positional[i][1]))**2)
        if radius > 90:
            diffs[i] = 0
    # return
    return diffs


def looper():
    # loop through all our relevant files to make a nice bias plot
    diffs_ef = main("efficiency.txt", "efficiency90.txt", "grid_positions_317.txt")
    diffs_fwhm = main("fwhm.txt", "fwhm90.txt", "grid_positions_317.txt")
    diffs_LED = main("LED_delay.txt","LED_delay90.txt", "grid_positions_317.txt")
    diffs_PV = main("P_V.txt", "P_V90.txt", "grid_positions_317.txt")
    diffs_g = main("gain.txt", "gain90.txt", "grid_positions_317.txt")


    # font nonsense
    mpl.rcParams['font.family']='serif'
    #hfont = {'fontname':'Computer Modern'}
    cmfont = font_manager.FontProperties(fname=mpl.get_data_path() + '/fonts/ttf/cmr10.ttf')
    mpl.rcParams['font.serif']=cmfont.get_name()
    mpl.rcParams['mathtext.fontset']='cm'
    mpl.rcParams['axes.unicode_minus']=False


    # plot the histograms
    #plt.gcf().subplots_adjust(left=0.15)
    plt.figure(figsize = (8,8))
    plt.hist(diffs_ef, density = False, histtype = "step", linewidth=2, bins=50, label = "Efficiency")
    plt.hist(diffs_fwhm, density = False, histtype = "step", linewidth=2, bins=50, label= "FWHM")
    plt.hist(diffs_g, density = False, histtype = "step", linewidth=2, bins=50, label= "Gain")
    plt.xlabel("Difference (%)", fontsize = (28))
    plt.ylabel("Counts", fontsize = (28))
    plt.title("Distribution of bias values", fontsize = (30))
    #plt.hist(diffs_LED, density = True, histtype = "step", linewidth=2, bins=25, label = "LED delay")
    plt.hist(diffs_PV, density = False, histtype = "step", linewidth=2, bins=50, label = "P:V ratio")
    plt.xlim(-0.3, 0.3)
    plt.legend(loc = 2, prop={'size': 25})
    plt.xticks(fontsize=25)
    plt.yticks(fontsize=25)
    plt.savefig("biasdist.pdf", bbox_inches="tight")
    plt.show()

    # extra bit, calculating stdev
    types = ["Efficiency", "FWHM", "Gain", "PV", "LED_delay"]
    types_data = [diffs_ef, diffs_fwhm, diffs_g, diffs_PV, diffs_LED]
    for i in range(len(types)):
        # collect hist, find midpoints of all bins
        n, bins = np.histogram(types_data[i])
        mids = 0.5*(bins[1:] + bins[:-1])
        # mean
        mean = np.average(mids, weights = n)
        # var
        var = np.average((mids-mean)**2, weights = n)
        st = np.sqrt(var)

        print("{} mean: {:.4f}\n{} std:{:.4f}".format(types[i],mean,types[i],st))



looper()
##if len(sys.argv) == 3:
    # ignoring the name of the python script
#    main(sys.argv[1], sys.argv[2])
#else:
#    print("collect_data takes exactly 2 arguments. (" + str(len(sys.argv)-1) + ") given\nPlease input filename1, filename2")
