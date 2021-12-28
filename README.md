# General README

This repository contains all the code I am using/working on during my MPhys at UoE
There are currently 4 folders:

* XYScripts - Set up for controlling the XY table (and soon its integration with data collection and analysis)
* Fitting - Deprecated folder that contains all the required .C files for XYanalysis.C to function. Not necessarily required here and in the future may be removed/cut down.
* Analysis - Contains the up to date analysis files that are used for collecting and analysing our .root PMT data. These files will need to be placed in certain respective directories to function as intented (eg, XYwrite, XYanalysis and efficiency all need to be placed in $WM_ANALYSE/Fitting/ in the watchman repository).
* Automation Code - The basic python script that is (currently) used to collect and cook wavedump data while moving the XY table automatically, without human intervention.
* Misc Macros - Just scripts and short pieces of code that I have written or modified that have their own uses and such will not be removed.

### Automation Code

#### auto_fnc_DAQ.py

Contains all the functions required to automate data, as well as the current automation function that implements these functions to automate the data collection.

#### Positions

The input data required by auto_fnc_DAQ.py to run across different XY table positions.

### Analysis
Self explanatory from above, will add to this when needed

#### efficiency.C

Using Fitting functions from the Watchman [Wavedump_Wrapper](https://github.com/Watchman-PMT/Wavedump_Wrapper/tree/master/Data_Analysis/Fitting) to collect important data for analysis.

*Insert into /Data_Analysis/Fitting/*

#### XYanalysis.C

Collect important data into a structure using efficiency.C, ready for output to XYwrite.C

*Insert into /Data_Analysis/Fitting/*

#### XYwrite.C

Input .root file as argument and collect analysis data from XYanalysis.C. This data is then written into a file

*Insert into /Data_Analysis/Fitting/*

#### XY_move_analyse.sh

Script to write analysis data from hQ.root files to data storage folder.Start in the /Data_Storage/RUN0000NN folder that you wish to analyse. This code will automatically generate a text file with the results P:V, mu, efficiency, and gain within them in the RUN0000NN/PMT0YYY/Nominal/Text_Files/ folder.

A separate file is produced via [mu_From_Hist.C](https://github.com/Watchman-PMT/Wavedump_Wrapper/blob/master/Data_Analysis/Fitting/mu_From_Hist.C#L109) on the local computer at the lab, but hasn't been pushed to main repo.

(Currently leaves the hQ file in the fitting folder, will adjust to delete this after it is finished with it.)

*Insert into /Wavedump_Wrapper/ and call using source XY_move_analyse.sh*

#### datacompile.py

Collects the data and errors from the xy_results.txt files across multiple runs in a format that allows for easy entry into ROOT for graphical/plotting purposes.

Input starting run and finishing run, and also input PMT sampled. Outputs individual property files within a new directory within current directory (Labelled RUN24-28_PMT162).

**NOTE: The data files in RUNS24-28_PMT162 are out of date and have separate error and value files. This is not reproduced by the updated script.**

*Insert into /Data_Storage/John/XYTesting/, or whatever directory houses the RUN0000NN folders*

#### Compile_Plot2D.c

Plots your X/Y values against specific property values with errors (efficiency, mu, etc)
Currently have this set up to run when within and 'RUNS00-99_PMTXYZ directory

To plot specific property against X/Y, write the root command like so:
	
	root "Compile_Plot2D.c(\"XY\",\"mu\")"

  
To plot from a different directory, write like so:

	root "Compile_Plot2D.c(\"DIR1/DIR2/XY\",\"DIR1/DIR2/mu\")"

*Insert into /Data_Storage/John/XYTesting/RUNS00-99_PMT162/, but can technically be run outside of this directary as explained above*

#### xy_results.txt
File that contains the readable values for different properties of the system
- P:V Ratio
- mu
- efficiency
- gain

xy_fit_results.txt is another file that is produced as explained in **XY_move_analyse.sh** section, but should function with datacompile.py regardless.

**Currently out of date within this repo. Includes above values with errors with current code.**

### 2D_Histogram
Folder that contains the macro (histo2D.C) for creating a 2D histogram plot with position plots (Positions2D) and a value (efficiency, PV, etc). Acts a bit strange if you only plot along the x and y axis (will fill in the gaps). So need a valid amount of data for worthwhile information.

### DataCompilation
Folder that contains a basic malleable script (plotgraphs.C) that allows for the overlay of multiple sets of PMT data.
Saved here for ease of use with two input files (.root). Can be changed to have more inputs.
WIP -> Allow unlimited number of file to be added to the graph if need be.

To run with unique files, input like:

	root "plotgraphs.C(\"Efficiency260.root\",\"Efficiency206.root\")"
Or change default files within plotgraphs.C

### XYScripts - XY Table Control
Only .sh files required for XY table control are:

  - initxy.sh
  - scripts.sh

initxy.sh calibrates and sets up the XY table, ensure that the carriage is initially moved away from the centre!
scripts.sh contains multiple functions that can be run.

The separate .sh slice files can also initialise the table, but can be called from within scripts.sh without initialisation.

The bash_rc file contains alias' that are useful for basic tasks, such as pinging and clearing errors, or initialising without scripts.

To apply scripts.sh and use its functions within a terminal, please use the standard: source ./scripts.sh


#### HELP MENU FOR SCRIPTS.SH 

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

motoron/motoroff

	Function that disables the physical motors of the table.
	WHEN DISABLED DO NOT SEND MOVEMENT COMMANDS!
	The table will believe it has moved and update its position, but will not
	have actually moved.
	
There are more functions available, but they're listed as alias'
To look at them, please go input: nano ~/.bashrc 

```
