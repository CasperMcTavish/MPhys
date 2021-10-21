#!/bin/bash

# PLEASE INITIALISE THE DEVICE BEFORE CONTINUING WITH THESE FUNCTIONS
echo ""
echo "Please initialise the device before using these commands."
echo "Do so by running ./initxy.sh"
echo "For help, type: helpxy"
echo "For any questions, my email is s1739002@ed.ac.uk"
echo ""

moveabsxy() {
	# Moves XY table to specific position
        # arguments
        # $1 -> X position
        # $2 -> Y position
	xmov="X:MOV:ABS $1\n" 	
	ymov="Y:MOV:ABS $2\n"
	
	# Move to said positions
        echo -ne $xmov > /dev/ttyUSB0
        echo -ne $ymov > /dev/ttyUSB0


}

pingxy() {
	# Function that pings the absolute position of the device and
	# returns it to the cat terminal, will try and develop so cat
	#terminal isn't required

	echo -ne 'X:ABS?\n' > /dev/ttyUSB0

	echo -ne 'Y:ABS?\n' > /dev/ttyUSB0


}

fastslicexy() {
	# Input for accessing all the other slice methods, just for ease of use.
	echo "Please input the slice type"
	echo "X - Y - LLUR - ULLR"
	read slice
	case $slice in
	[Xx]* ) fastxslice;;
	[Yy]* ) fastyslice;;
	LLUR) fastLLURslice;;
	llur) fastLLURslice;;
	ullr) fastULLRslice;;
	ULLR) fastULLRslice;;
	* ) echo "Slice type not recognised.";;
	esac

}

fastxslice() {

	
	# ========================================================
	# Function for moving across the x axis quickly in one slice
	# Will move from centre of Y axis 
	# ======================================================== 

	# Move to x - 0, y - centre
	# First move entire thing to centre, then move down to x - 0
	echo -ne 'MOV:CENTRE\n' > /dev/ttyUSB0
	echo -ne 'X:MOV:ABS 0\n' > /dev/ttyUSB0


	# Move to x maximum (also currently baked in, will fix if baked in variables are fixable)
	echo -ne 'X:MOV:ABS 10257\n' > /dev/ttyUSB0
	echo "Slicing across X, please wait 30s before inputting another command."


}

fastyslice() {
	# ========================================================
	# Script for moving across the y axis quickly in one slice
	# Will move from centre of X axis
	# ========================================================

	# Move to x - centre, y - 0
	# MOV:CENTER moves x and y to centre, then Y to zero, pause between to allow for this.
	echo -ne 'MOV:CENTRE\n' > /dev/ttyUSB0
	echo -ne 'Y:MOV:ABS 0\n' > /dev/ttyUSB0

	# Move to y maximum (also currently baked in, will fix if baked in variables are fixable)
	echo -ne 'Y:MOV:ABS 10321\n' > /dev/ttyUSB0
	echo "Slicing across Y, please wait 30s before inputting another command."
	}

fastLLURslice() {

	# ========================================================
	# Script for moving from lower left (LL) to upper right (UR) in a fast slice
	# Will move from 0,0 to  10257,10321 (maximum for this table)
	# ========================================================


	# Move to x - 0, y - 0 (lower left corner)
	echo -ne 'MOV:LLC\n' > /dev/ttyUSB0

	# Move to x,y maximum (upper right corner)
	echo -ne 'MOV:URC\n' > /dev/ttyUSB0

	echo "Slicing from LL to UR, please wait 30s before inputting another command."
}

fastULLRslice() {

	# ========================================================
	# Script for moving from upper left (UL) to lower right (LR) in a fast slice
	# Will move from 10257,0 to  0,10321
	# ========================================================


	# Move to upper left corner (ULC)  
	echo -ne 'MOV:ULC\n' > /dev/ttyUSB0


	# Move to lower right corner (LRC)
	echo -ne 'MOV:LRC\n' > /dev/ttyUSB0

	echo "Slicing from UL to LR, please wait 30s before inputting another command."


}

inputxy() {
	# Function that allows you to input 2 sets of coords, and it will move between them

	echo "Please Input the start coordinates: X Y "
	read coord1
	echo "Please Input the final coordinates: X Y "
	read coord2
	moveabsxy $coord1
	moveabsxy $coord2

}


motoroff() {
	# Turn the motors off
	echo "Motors disabled."
	echo -ne 'X:DISABLE\n' > /dev/ttyUSB0
	echo -ne 'Y:DISABLE\n' > /dev/ttyUSB0
}

motoron() {
	# Turn the motors on
        echo "Motors enabled."
        echo -ne 'X:ENABLE\n' > /dev/ttyUSB0
        echo -ne 'Y:ENABLE\n' > /dev/ttyUSB0
}



helpxy() {
	# Simple helper function, will print all current functions
	echo ""
	echo "=================================="
	echo "========== HELP MENU ============="
	echo "=================================="
	echo ""
	echo "These scripts are for using an XY Table and controller developed by University of Edinburgh - School of Physics"
	echo ""
	echo "FUNCTIONS LIST:"
	echo ""
	echo "pingxy"
	echo "  Function that pings x y position to the cat terminal"
	echo ""
	echo "moveabsxy x y"
	echo "	Function that takes cartesian coordinates (x y) and moves table"
	echo "	to said position, limited by the size of your XY-table"
	echo ""
	echo "fastslicexy"
	echo "	Function that requests a type of slice you wish to complete,"
	echo "	and then executes it. Current slices are:"
	echo "		X - x slice from center of Y"
	echo "		Y - y slice from center of X"
	echo "		LLUR - slice from lower left corner to upper right"
	echo "		ULLR - slice from upper left corner to lower right"
	echo "	These individual slice functions can also be accessed if needed."
	echo ""
	echo "inputxy"
	echo "	Function that asks for two sets of coordinates and then" 	 
	echo "	will move from the starting set to the final set."
	echo ""
	echo "There are more functions available, but they're listed as alias'"
	echo "To look at them, please go input: nano ~/.bashrc "

}





