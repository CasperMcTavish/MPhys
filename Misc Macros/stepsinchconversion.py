import numpy as np

# Convert the step coordinates to mm
# taking 14.18 steps to be 1mm
# take away from centre position also

def read_positions(filename):
    with open(filename) as f:
        contents = f.readlines()

    if (len(contents) > 1):
        print("File read of length: " + str(len(contents)))
    else:
        print("File length is too short to process (please include more positions)")

    return contents


def conversion(filename, centre):
    
    # collect file data
    positional = read_positions(filename)
    new_positional = []

    # begin loop
    for i in range(len(positional)):
        # split position
        spl_pos = str.split(positional[i])
        # take away centre from each and divide by 14.18
        spl_pos[0] = (int(spl_pos[0]) - int(centre[0]))/14.18
        spl_pos[1] = (int(spl_pos[1]) - int(centre[1]))/14.18
        
        # Append
        new_positional.append([spl_pos[0],spl_pos[1]])
    
    # write
    file_name_mm = filename + "_mm"
    with open(file_name_mm, "w") as f:
        for i in range(len(new_positional)):
            # reformatting
            pos = str(new_positional[i])
            pos = pos.strip("[]")
            pos = pos.replace(",","")
            f.write(pos + "\n")

# current centre and textfile
conversion("datapoints_65.txt", [4946, 5555])


