#!/bin/bash

# ========================================================
# Script for moving across the y axis quickly in one slice
# Will move from centre of X axis
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

# Move to x - centre, y - 0
# MOV:CENTER moves x and y to centre, then Y to zero, pause between to allow for this.
echo -ne 'MOV:CENTRE\n' > /dev/ttyUSB0
# It takes 15s for our board to move between opposite corners (BL->UR)
# sleep 15s

echo -ne 'Y:MOV:ABS 0\n' > /dev/ttyUSB0

# Move to y maximum (also currently baked in, will fix if baked in variables are fixable)
echo -ne 'Y:MOV:ABS 10321\n' > /dev/ttyUSB0
echo "Moving to Y-MAX now..."
