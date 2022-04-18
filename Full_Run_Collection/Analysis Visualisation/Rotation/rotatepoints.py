import numpy as np
import matplotlib.pyplot as plt
import sys

# Rotate the individual PMT points by X degrees to allow for simple translation back into same initial frame.
# Takes position list as steps, as its easier to verify if it worked correctly (steps are always integer)
# FORMAT OF CENTRE -> 100 100


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
    contents = (np.array(contents)).astype(int)
    return contents

def stripper(contents):
    # strips strings with tuple and converts into np array of ints
    contents = [contents[i].rstrip().lstrip() for i in range(len(contents))]
    contents = [contents[i].split() for i in range(len(contents))]
    contents = (np.array(contents)).astype(int)
    return contents

def pos_write(file_name, positions):
    '''
    Writes the data points to file 'ring_positions.txt' in the correct format for XY-table automation
    eg.
    3002 2200
    3232 2400
    ...

    :param positions:       The list of positions to be written to the file
    '''
    # write file in the correct format
    # eg:
    # 3430 2323
    # 3232 0202
    # ...

    # creates a file if it doesnt already exist
    with open(file_name, "w") as f:
        for i in range(len(positions)):
            # reformatting for the format our automation system uses
            pos = str(positions[i])
            pos = pos.strip("[]")
            pos = pos.replace(",", "")
            f.write(pos + "\n")


def rotator(point, centre, degrees):
    # rotate 90 degrees anticlockwise

    # take away centres
    rotated_point = [point[0]- centre[0], point[1]-centre[1]]

    # apply rotation
    rotated_point = [-rotated_point[1], rotated_point[0]]

    # add centres
    rotated_point = [rotated_point[0] + centre[0], rotated_point[1] + centre[1]]
    return rotated_point

def main(file_name, degrees, centreX, centreY):

    centre = np.array([int(centreX), int(centreY)])
    # read in file
    data = read_file(file_name)
    print(len(data))
    # process specific data point
    newpoints = np.array([rotator(data[i], centre, degrees) for i in range(len(data))])

    # plot new point and data
    plt.title("New and Rotated points")
    plt.scatter(newpoints[:,0], newpoints[:,1], label=("New data"))
    plt.scatter(data[:,0], data[:,1], label=("Old data"))
    plt.scatter(centre[0], centre[1], label=("Centre"))
    plt.legend()
    plt.show()

    file_name_new = file_name + "_rotated90"

    pos_write(file_name_new, newpoints)

if len(sys.argv) == 5:
    # ignoring the name of the python script
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
else:
    print("collect_data takes exactly 4 arguments. (" + str(len(sys.argv)-1) + ") given\nPlease input file name, rotation in degrees, and centre positions X and Y")
