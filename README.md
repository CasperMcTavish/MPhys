# General README


Set up for controlling the XY table (and soon its integration with data collection)
Only .sh files required are:

  - initxy.sh
  - scripts.sh

initxy.sh calibrates and sets up the XY table, ensure that the carriage is initially moved away from the centre!
scripts.sh contains multiple functions that can be run.

The separate .sh slice files can also initialise the table, but can be called from within scripts.sh without initialisation.

The bash_rc file contains alias' that are useful for basic tasks, such as pinging and clearing errors, or initialising without scripts.

To apply scripts.sh and use its functions within a terminal, please use the standard: source ./scripts.sh


HELP MENU FOR SCRIPTS.SH 
=============================================

These scripts are for the explicit use in the XY Table and controller developed by University of Edinburgh - School of Physics
```
FUNCTIONS LIST:

pingxy
  Function that pings x y position to the cat terminal

moveabsxy x y
	Function that takes cartesian coordinates (x y) and moves table
	to said position, limited by the size of your XY-table

fastslicexy
	Function that requests a type of slice you wish to complete,
	and then executes it. Current slices are:
		X - x slice from center of Y
		Y - y slice from center of X
		LLUR - slice from lower left corner to upper right
		ULLR - slice from upper left corner to lower right
	These individual slice functions can also be accessed if needed.

inputxy
	Function that asks for two sets of coordinates and then
	will move from the starting set to the final set.
```
