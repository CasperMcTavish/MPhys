import numpy as np
import sys

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



def rogue_var_cutter(data_type, file_name):
    """
    Takes data 'type' predefined, and combs through data given to look for rogues, then sets them to reasonable values and writes back

    Defined data types:
    0 - P:V Ratio
    1 - Gain
    2 - Efficiency
    3 - Mu
    4 - LED Delay
    """

    # No switch statements in python...so we have to do this the ugly way
    # Ensure data_type is integer
    data_type = int(data_type)

    # PV
    if (data_type == 0):
        print("Scanning P:V Ratio Values for Rogues...")
        # Read
        vals = read_file(file_name)
        values, errors = splitter(vals)
        # scan and fix rogues
        for i in range(len(values)):
            if (values[i] < 0) or (values[i] > 7):
                values[i] = 1
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
            if (values[i] < 0) or (values[i] > 2.0e07):
                values[i] = 0.5e07
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
            if (values[i] < 0) or (values[i] > 0.2):
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
            if (values[i] < 0) or (values[i] > 0.2):
                values[i] = 0
                errors[i] = 0
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
            if (values[i] < 80) or (values[i] > 120):
                values[i] = 100
                errors[i] = 0
        # Write
        write_file(file_name, values, errors, "clean")
    # Final catch
    else:
        print("Please input a valid value for data_type:\n0 - P:V Ratio\n1 - Gain\n2 - Efficiency\n3 - Mu\n4 - LED Delay")
        return

# APPLY DOWN HERE
#rogue_var_cutter(0, "P_V_Ratio")

if len(sys.argv) == 3:
    # ignoring the name of the python script
    rogue_var_cutter(sys.argv[1], sys.argv[2])
else:
    print("collect_data takes exactly 2 arguments (" + str(len(sys.argv)-1) + ") given.\nPlease input number relative to data being cleaned:\n0 - P:V Ratio\n1 - Gain\n2 - Efficiency\n3 - Mu\n4 - LED Delay\n\nAnd text file containing the relevant data...")
