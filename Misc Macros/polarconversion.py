import numpy as np
from numpy import exp, abs, angle
import matplotlib.pyplot as plt

def read_positions(filename):
    with open(filename) as f:
        contents = f.readlines()

    if (len(contents) > 1):
        print("File read of length: " + str(len(contents)))
    else:
        print("File length is too short to process (please include more positions)")

    return contents

# CONVERTS CARTESIAN COORDINATES TO POLAR AROUND A CENTRAL POINT
def conversion(filename, centre):

    # collect file data
    positional = read_positions(filename)
    new_positional = []
    theta_list = []
    R_list = []

    # begin loop
    for i in range(len(positional)):
        theta = 0
        R = 0
        # split position
        spl_pos = str.split(positional[i])
        # take away centre from each
        spl_pos[0] = (int(spl_pos[0]) - int(centre[0]))
        spl_pos[1] = (int(spl_pos[1]) - int(centre[1]))

        # Apply polar conversion to give correct theta and R components
        # due to how polar works, this is a bit more complex (quadrant based)
        
        # convert to z = x+iy
        z = spl_pos[0] + 1j*spl_pos[1]
        theta = angle(z)
        R = abs(z)
        
        # central point
        #if (spl_pos[0] == 0) and (spl_pos[1] == 0):
        #    theta = 0
        # if along y axis
        #if (spl_pos[0] == 0)
        #    theta = np.arctan(spl_pos[1]/spl_pos[0])
        # R
        #R = np.sqrt(spl_pos[0]**2 + spl_pos[1]**2)
        # Append
        new_positional.append([theta,R])
        theta_list.append(theta)
        R_list.append(R)

    # write
    file_name_mm = filename + "_polar"
    with open(file_name_mm, "w") as f:
        for i in range(len(new_positional)):
            # reformatting
            pos = str(new_positional[i])
            pos = pos.strip("[]")
            pos = pos.replace(",","")
            f.write(pos + "\n")

    fig = plt.figure()
    ax = fig.add_subplot(projection='polar')
    c = ax.scatter(theta_list, R_list, cmap='hsv')
    plt.savefig("examplefig.png")

# current centre and textfile
conversion("datapoints_115_0_270.txt", [4946, 5595])

