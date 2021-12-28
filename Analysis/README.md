## Analysis
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
