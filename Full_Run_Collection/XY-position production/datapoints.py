import math
import matplotlib.pyplot as plt
import numpy as np
# Code to determine PMT measuring positions by taking equally spaced points on a circle at certain radii, then makes a file with the data
# Working in STEPS here, but can be used for any form of measurement
# Alter the rounding for what is needed

'''
Created on Jan 11 2022
@author John Waiton
'''

def circle_points(centre, radius, no_of_scans):
    '''
    Plots a circle of points with a radius R around a centre position

    :param centre:          List or tuple of centre coordinates. Eg [2000, 3000]
    :param radius:          The radius of the ring
    :param no_of_scans:     The number of points along the ring
    :return positions:      List of [x,y] coordinates on ring.

    '''
    # Take the radius of the circle and number of points
    # Calculate the arc length, do mod of the arc length by 2? figure it out
    # Find the positions along the circle related to the angle.
    # Append to positions list and output

    # define change in degrees per scan
    angle = np.linspace(0, 2 * math.pi, no_of_scans, endpoint = False)
    #print(no_of_scans)
    #print(angle)

    # calculate positions and write them
    positions = []
    for i in range(no_of_scans):
        # round positions to , we're working in steps/mm here, so anything beyond that is too small.
        x = round(radius * math.cos(angle[i]))
        y = round(radius * math.sin(angle[i]))
        # Scale with the centre positions
        x = x + centre[0]
        y = y + centre[1]
        #print(angle*i)
        positions.append([x,y])

    return(positions)

def collate_datapoints(centre, radii, scans_per_radii):
    '''
    Collects the datapoints from circle_points for multiple Radii

    :param centre:              List or tuple of centre coordinates. Eg [2000, 3000]
    :param radii:               List of radii values for different rings
    :param scans_per_radii:     List of the number of points on each ring
    :return position:           List of the [x,y] positions for all rings
    '''
    # format that allows a list of multiple radii and a respective no. of scans per radii to be inputted, creating a comprehensive list of data points that covers the entire PMT

    # Start with the centre
    position = [centre]

    for i in range(len(radii)):
        position.extend(circle_points(centre, radii[i], scans_per_radii[i]))

    #print(position)
    return position



def pos_write(positions, file_name):
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

    plt.title("Data points taken across PMT")
    file_name = "datapoints_"
    file_name += str(len(positions))
    file_name += ".pdf"
    plt.savefig(file_name)
    plt.show()




def radi_calculation(radius, no_of_steps):
    '''
    gives the list of radii specific radii apart

    :param radius:          Radius step Size
    :param no_of_steps:     Number of radius steps
    :return radi_calc:      The list of radius values
    '''
    # Calculate the radii we want
    radi_calc = []
    for j in range(no_of_steps):
        radi_calc.append((j+1)*radius)

    print("Radii values: " + str(radi_calc))
    return radi_calc



##########################################
# REMOVE FIRST # FROM THESE ROWS
## example use
## Centre point 4462, 5535, move out in rings of 355, 5 times (equivalent to 25mm steps)
## no of scans per ring increases as you go on. (4 cardinal directions + 2*scan_no) until the edge, as I dont feel the need to scan very accurately out there
#
#radi_calc = radi_calculation(355, 5)
#
#position_values = collate_datapoints([4462, 5535], (radi_calc), [8, 12, 20, 36, 36])
#pos_write(position_values, "ring_positions_113.txt")
#
## plotting a circle of the PMT, the PMT radius in steps is
#plot_points(position_values, 1796, [4462, 5535])
#
###############################################

# example used
# Centre point, 4462, 5535, move out in rings of 590, 3 times (equivalent to 41.5mm steps)
# no of scans per ring increases as you go on (4 cardinal directions + scan_no) until the edge

radi_calc = radi_calculation(400, 4)
position_values = collate_datapoints([4462, 5535], (radi_calc), [8, 16, 20, 20])
pos_write(position_values, "ring_positions_60.txt")

plot_points(position_values, 1796, [4462, 5535])
