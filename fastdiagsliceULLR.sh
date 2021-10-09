#!/bin/bash

# ========================================================
# Script for moving from upper left (UL) to lower right (LR) in a fast slice
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

# Move to upper left corner (ULC)  
echo -ne 'MOV:ULC\n' > /dev/ttyUSB0


# Move to lower right corner (LRC)
echo -ne 'MOV:LRC\n' > /dev/ttyUSB0

echo "Moving to X-MAX, Y-MAX now..."
