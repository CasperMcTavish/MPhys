import matplotlib.pyplot as plt
import numpy as np
import subprocess
import time
import sys
import os

## Functions that will be used for automation purposes
## TO ALLOW THIS CODE TO WORK, PLEASE INSERT IT STRAIGHT INTO THE $WM_DAQ DIRECTORY
## Currently doesnt utilise the movement code yet, will require XY-scripts to allow for this to happen.


# Initialisation function, using bash commands

# Will allow our console to run bash scripts from the XY-scripts folder
# This is essential for saving time
#def initialise():
	#command = 'source XY-scripts/scripts.sh'
	#process = subprocess.run(command.split(), stdout=subprocess.PIPE)
	#output, error = process.communicate()
	#rc = subprocess.call("XY-scripts/scripts.sh")
	#rc = subprocess.run(["source ./XY-scripts/scripts.sh"], shell=True)

# Function that reads in the XY positions into a list and returns said list
def read_positions(filename):
	
	# Open file
	with open(filename) as f:
		contents = f.readlines()

	# Check that file has been read correctly (length)
	if (len(contents) > 1):
		print("File read of length: " + str(len(contents)))
	else:
		print("File length too short to process (please include more positions!)")

	return contents
	
# Writing basic script that utilises the moveabsxy function from scripts.sh
def move_table(positionx, positiony):
	# Apply as strings
	x = positionx
	y = positiony
	print("Moving to " + x + " " + y)
	# Running shell commands
	rc = subprocess.call(["echo -ne 'X:MOV:ABS " + x + "\n' > /dev/ttyUSB0"], shell=True)
	rc = subprocess.call(["echo -ne 'Y:MOV:ABS " + y + "\n' > /dev/ttyUSB0"], shell=True)


def collect_data(collect_bash, process_bash, run_no):
	# this script will move to the data_acquisition folder within watchman, and run the data collection code
	# then it will process the data with the correct run number, which moves the data over to data_storage

	#directory = "../Watchman/Wavedump_Wrapper/Data_Acquisition/" 
	#testdir = "/home/user1/Watchman/Wavedump_Wrapper/Data_Acquisition"

	# Collect data
	rc = subprocess.call([collect_bash], shell=True)

	p = subprocess.run([process_bash], input = (run_no + "\n").encode(), stdout=subprocess.PIPE)
	
	return True
	

def main(runs):

	positional = read_positions("Positions")
	collect_data('./Run_wavedump_PCI_1_min_10_CH_NS_150.sh', './move_10_ch_nom_trig_auto.sh', runs)
	# Split position string into x,y
	#spl_pos = str.split(positional[0])
	#move_table(spl_pos[0], spl_pos[1])	
	return True



# Collect arguments to run, if you dont have enough, stop the code
# This needs to be adjusted to allow for starting run number, positions text file
if len(sys.argv) == 2:
    # ignoring the name of the python script
    main("000235")
else:
    print("collect_data takes exactly 2 arguments (" + str(len(sys.argv)-1) + ") given")


