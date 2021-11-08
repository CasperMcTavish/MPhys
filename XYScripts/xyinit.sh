#!/bin/bash

# ====================================================
# Script for initialising and calibrating the xy table
# ====================================================

# NOTE System will often read a line, run the line and then spit out an error, which is peculiar, as the error is the standard "undefined header" error.

# Permitting the device to read and write, this can be seen as correct
# by the results of ls (three rw's is what you're looking for, not two)

ls -l /dev/ttyUSB0;
sudo chmod o+rw /dev/ttyUSB0;
ls -l /dev/ttyUSB0;


# Open new terminal and start reading from xy table

gnome-terminal -e "cat -v < /dev/ttyUSB0"
# this shouldnt close automatically, but if it does, use
# --window-with-profile=JohnMPhys

# Initialise XY controller
echo -ne 'INIT\n' > /dev/ttyUSB0
echo -ne '*CLS\n' > /dev/ttyUSB0


echo "Posting ID to terminal 2..."
echo -ne '*IDN?\n' > /dev/ttyUSB0
 

# Calibration

echo -ne 'SYST:ERR?\n' > /dev/ttyUSB0
echo -ne '*CLS\n' > /dev/ttyUSB0

echo "Calibrating..."
echo -ne 'REF\n' > /dev/ttyUSB0
# giving a pause before removing standard error
sleep 1s
echo -ne '*CLS\n' > /dev/ttyUSB0


