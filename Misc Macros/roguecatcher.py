import numpy as np
import sys
import math
import matplotlib.pyplot as plt

# THIS CODE IS MADE TO SKIM THROUGH THE DIFFERENT FILE TYPES FROM OUTPUT DATA, AND CORRECT ANY ROGUE VARIABLES
# SHOWN BELOW

# PV
# VALUES BELOW 0, OR ABOVE 7 ARE SET TO 1

# GAIN
# VALUES ABOUT 2E07 AND BELOW 0 ARE SET TO 0.5E07

# EFFICIENCY
# VALUES BELOW 0 OR ABOVE 0.2 ARE SET TO 0

# MU
# VALUES BELOW 0 OR ABOVE 0.2 ARE SET TO 0

# LED_DELAY
# VALUES BELOW 80 AND ABOVE 120 ARE SET TO 100

# LED_DELAY WIDTH
# UNCHANGED, NORMALLY FINE

# Plotting function
def plot_points(positions, radius, centre):
    '''
    Plots a circle with radius R to represent the PMT, then plots each datapoint within the circle from the position list obtained via collate_datapoints

    :param positions:    List of the [x,y] positions across the entire PMT
    :param radius:       Radius of the PMT (126.5mm which is approximately 1796 steps on XY-table)
    :param centre:       [x,y] position for the centre axis
    '''
    # plot the points on the sphere of set radius in matplot lib
    # good way to visualise the points, as otherwise its hard to understand where they are just by the numbers

    # create linspace of angles
    angle = np.linspace(0, 2 * math.pi, 150)

    # create x and y positions for circle
    x_circ = radius * np.cos(angle) + centre[0]
    y_circ = radius * np.sin(angle) + centre[1]

    figure, axes = plt.subplots(1)
    for i in range(len(positions)):
        axes.scatter(positions[i][0],positions[i][1])

    axes.plot(x_circ, y_circ)
    axes.set_aspect (1)

    plt.title("Rogue Data points taken across PMT")
    #file_name = "rogues"
    #file_name += str(len(positions))
    #file_name += ".pdf"
    #plt.savefig(file_name)
    plt.show()


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



def read_file(filename):
    with open(filename) as f:
        contents = f.readlines()

    if (len(contents) > 1):
        print("File read of length: " + str(len(contents)))
    else:
        print("File length is too short to process (please include more positions)")

    # convert to floats in this case
    return contents

def write_file(filename, data, errors, suffix):
    """
    Hand over standard array of data and write to file
    eg File:
    1313
    23232
    242151
    2392
    2323
    ...
    """

    file_name_new = filename + str(suffix)
    # adding .txt for windows
    file_name_new += ".txt"
    with open(file_name_new, "w") as f:
        for i in range(len(data)):
            # reformatting
            pos = str(str(data[i]) + " " + str(errors[i]))
            # FOR COORDINATE SYSTEM
            #pos = str(new_positional[i])
            #pos = pos.strip("[]")
            #pos = pos.replace(",","")
            f.write(pos + "\n")


def radius_check(centre, radius, x, y):
    # Check if the position is within the radius of the PMT, all done in steps here.
    # Prints commented out to reduce terminal spam
    #print("")
    #print("True XY values:")
    #print(x, y)
    # Take away centre
    x = int(x) - int(centre[0])
    y = int(y) - int(centre[1])
    #print("Centre removed:")
    #print(x, y)
    # Calculate magnitude
    r = np.sqrt(x**2 + y**2)
    #print(r)

    # check if less than radius return true, otherwise return false
	# add +100 to radius to include outer edges
    if (r > radius):
        #print("Out of radius")
        return False
    else:
        # If within radius
        return True


def rogue_var_cutter(data_type, file_name, position_name, centre, radius):
    """
    Takes data 'type' predefined, and combs through data given to look for rogues, then sets them to reasonable values and writes back

    # Also take radius of PMT, and check if data point is within radius. Doing so will give different results. Take centre as [x,y] in terminal. Will format appropriately here.

    Defined data types:
    0 - P:V Ratio
    1 - Gain
    2 - Efficiency
    3 - Mu
    4 - LED Delay
    """
    centre = centre.strip("[]")
    centre = centre.split(",")
    centre[0] = int(centre[0])
    centre[1] = int(centre[1])

    print(radius)
    radius = int(radius)

    # Read position file
    positions = read_file(position_name)
    x, y = splitter(positions)
    # No switch statements in python...so we have to do this the ugly way
    # Ensure data_type is integer
    data_type = int(data_type)

    # count the number of points out of range and number of rogue counters
    counter = 0
    r_counter = 0

    # collect rogue position list
    pos_list = []
    # PV
    if (data_type == 0):
        print("Scanning P:V Ratio Values for Rogues...")
        # Read
        vals = read_file(file_name)
        values, errors = splitter(vals)
        # scan and fix rogues
        for i in range(len(values)):
            # Check that its within radius of PMT
            if (radius_check(centre, radius, x[i], y[i])):

                if (values[i] < 0) or (values[i] > 6):
                    # set rogues, add counter and save position
                    r_counter+=1
                    values[i] = 1
                    errors[i] = 0
                    pos_list.append([x[i],y[i]])
            # if it doesn't pass
            else:
                counter +=1
                values[i] = 0
                errors[i] = 0
        # Write
        write_file(file_name, values, errors, "clean")

    # Gain
    elif (data_type == 1):
        print("Scanning Gain Values for Rogues...")
        # Read
        vals = read_file(file_name)
        values, errors = splitter(vals)
        # scan and fix rogues
        for i in range(len(values)):
            # check within radius of PMT
            if (radius_check(centre, radius, x[i], y[i])):
                if (values[i] < 0) or (values[i] > 2.0e07):
                    r_counter+=1
                    values[i] = 0.5e07
                    errors[i] = 0
                    pos_list.append([x[i],y[i]])

            else:
                counter +=1
                values[i] = 0
                errors[i] = 0
            # Write
        write_file(file_name, values, errors, "clean")


    # Efficiency
    elif (data_type == 2):
        print("Scanning Efficiency Values for Rogues...")
        # Read
        vals = read_file(file_name)
        values, errors = splitter(vals)
        # scan and fix rogues
        for i in range(len(values)):
            # check within radius of pmt
            if (radius_check(centre, radius, x[i], y[i])):

                if (values[i] < 0) or (values[i] > 0.16):
                    r_counter +=1
		    # not set to zero to avoid issues with histogram plotting
                    values[i] = 0.0001
                    errors[i] = 0
                    pos_list.append([x[i],y[i]])

            else:
                counter +=1
                values[i] = 0
                errors[i] = 0
        # Write
        write_file(file_name, values, errors, "clean")


    # Mu
    elif (data_type == 3):
        print("Scanning Mu Values for Rogues...")
        # Read
        vals = read_file(file_name)
        values, errors = splitter(vals)
        # scan and fix rogues
        for i in range(len(values)):

            # check within radius of pmt
            if (radius_check(centre, radius, x[i], y[i])):

                if (values[i] < 0) or (values[i] > 0.18):
                    r_counter +=1
                    values[i] = 0.0001
                    errors[i] = 0
                    pos_list.append([x[i],y[i]])

            else:
                counter +=1
                values[i] = 0
                values[i] = 0
        # Write
        write_file(file_name, values, errors, "clean")

    # LED Delay
    elif (data_type == 4):
        print("Scanning LED Delay Values for Rogues...")
        # Read
        vals = read_file(file_name)
        values, errors = splitter(vals)
        # scan and fix rogues
        for i in range(len(values)):

            # check within radius of pmt
            if (radius_check(centre, radius, x[i], y[i])):

                if (values[i] < 60) or (values[i] > 140):
                    r_counter +=1
                    values[i] = 100
                    errors[i] = 0
                    pos_list.append([x[i],y[i]])

            else:
                counter +=1
                values[i] = 0
                errors[i] = 0
        # Write
        write_file(file_name, values, errors, "clean")

    # Delay Width
    elif (data_type == 5):
        print("Scanning LED Delay Values for Rogues...")
        # Read
        vals = read_file(file_name)
        values, errors = splitter(vals)
        # scan and fix rogues
        for i in range(len(values)):

            # check within radius of pmt
            if (radius_check(centre, radius, x[i], y[i])):

                if (values[i] > 15):
                    r_counter +=1
                    values[i] = 100
                    errors[i] = 0
                    pos_list.append([x[i],y[i]])

            else:
                counter +=1
                values[i] = 0
                errors[i] = 0
        # Write
        write_file(file_name, values, errors, "clean")


    # Final catch
    else:
        print("Please input a valid value for data_type:\n0 - P:V Ratio\n1 - Gain\n2 - Efficiency\n3 - Mu\n4 - LED Delay")
        return
    print("Number of rogues: {}\nNumber of points off PMT: {}".format(r_counter,counter))
    # plot rogues for better understanding
    plot_points(pos_list, radius, centre)

# APPLY DOWN HERE
#rogue_var_cutter(0, "P_V_Ratio")

if len(sys.argv) == 6:
    # ignoring the name of the python script
    rogue_var_cutter(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
else:
    print("collect_data takes exactly 5 arguments (" + str(len(sys.argv)-1) + ") given.\nPlease input number relative to data being cleaned:\n0 - P:V Ratio\n1 - Gain\n2 - Efficiency\n3 - Mu\n4 - LED Delay\n5 - Delay Width\n\nText file containing the relevant data\n\nPosition File that produced results\n\nCentre of PMT\n\nRadius of PMT")
