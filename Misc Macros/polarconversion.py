import numpy as np

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
        # theta
        theta = np.arctan(spl_pos[1]/spl_pos[0])
        # R
        R = np.sqrt(spl_pos[0]**2 + spl_pos[1]**2)
        # Append
        new_positional.append([theta,R])

    # write
    file_name_mm = filename + "_polar"
    with open(file_name_mm, "w") as f:
        for i in range(len(new_positional)):
            # reformatting
            pos = str(new_positional[i])
            pos = pos.strip("[]")
            pos = pos.replace(",","")
            f.write(pos + "\n")

# current centre and textfile
conversion("datapoints_65.txt", [4946, 5555])
