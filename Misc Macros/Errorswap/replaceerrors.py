# used to swap out the errors of LED_delay with the delay_width
import numpy as np

def pos_write(positions):
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
    print("Writing...")
    # creates a file if it doesnt already exist
    with open("LED_delay_errors.txt", "w") as f:
        for i in range(len(positions)):
            # reformatting for the format our automation system uses
            pos = str(positions[i])
            pos = pos.strip("[]")
            pos = pos.replace("()","")
            pos = pos.replace(",", "")
            f.write(pos + "\n")

def read_positions(filename):
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

def main():
    delay = read_positions("LED_delayclean90.txtnorm.txt")
    width = read_positions("delay_widthclean90.txtnorm.txt")
    print(delay[:,0][5])
    LED_delay = delay[:,0]
    LED_width = width[:,0]
    print(width[:,0][5])
    LED_full = []
    LED_full = [i for i in zip(LED_delay, LED_width)]
    print(np.array(LED_full)[5])
    pos_write(np.array(LED_full))


main()
