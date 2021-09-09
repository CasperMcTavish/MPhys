#!/bin/bash

# ========================================================
# Script for moving from bottom left (BL) to top right (TR) in a fast slice
# Will move from 10257,0 to  0,10321
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

# Move to x - max, y - 0
echo -ne 'X:MOV:ABS 10257\n' > /dev/ttyUSB0
echo -ne 'Y:MOV:ABS 0\n' > /dev/ttyUSB0

# Move to x - 0, y - max (also currently baked in, will fix if baked in variables are fixable)
echo -ne 'X:MOV:ABS 0\n' > /dev/ttyUSB0
echo -ne 'X:MOV:ABS 10321\n' > /dev/ttyUSB0
echo "Moving to X-MAX, Y-MAX now..."
