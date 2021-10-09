#!/bin/bash

# ========================================================
# Script for moving across the x axis quickly in one slice
# Will move from centre of Y axis 
# ======================================================== 

# Checking if you have run the initialisation script yet
while true; do
    read -p "Have you initialised the controller already? [Y/N]" yn
    case $yn in
	[Yy]* ) break;;
	[Nn]* ) echo "Running xyinit.sh, please ensure these scripts are in the same folder"; ./xyinit.sh ; break;;
	* ) echo "Please choose Y or N"
    esac
done

# Move to x - 0, y - centre
# First move entire thing to centre, then move down to x - 0
echo -ne 'MOV:CENTRE\n' > /dev/ttyUSB0
echo -ne 'X:MOV:ABS 0\n' > /dev/ttyUSB0


# Move to x maximum (also currently baked in, will fix if baked in variables are fixable)
echo -ne 'X:MOV:ABS 10257\n' > /dev/ttyUSB0
echo "Moving to X-MAX now..."

# add while loop that sleeps here, which will check every X seconds whether or not the device has reached its required position. then will say "DONE!" This most likely wont work, as the only wayto know if its reached its required position is to have cat within this script...look into this


