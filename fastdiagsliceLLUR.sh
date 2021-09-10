#!/bin/bash

# ========================================================
# Script for moving from lower left (LL) to upper right (UR) in a fast slice
# Will move from 0,0 to  10257,10321 (maximum for this table)
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

# Move to x - 0, y - 0 (lower left corner)
echo -ne 'MOV:LLC\n' > /dev/ttyUSB0

# Move to x,y maximum (upper right corner)
echo -ne 'MOV:URC\n' > /dev/ttyUSB0

echo "Moving to X-MAX, Y-MAX now..."
