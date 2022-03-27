## Misc Macros
Contains all the unique little scripts that don't fit into any particular category.

### Bias distribution
Produces 1D histograms of the bias distribution within your data files.

### Errorswap
Simple script to swap errors out of our text file

### Normalisation
Takes two files, finds the largest value between the two files and normalises all values with respect to that value.

### Rotation
Rotate our 90 degree data to be aligned with the 0 degree data.

### datapoints
Script that allows for the production of grid or ring scans on the PMT surface as defined by the user, and then will print a file that contains the related XY coordinates.

### Plotting macros
Simple macros for plotting things on .ROOT files, here we just have a simple macro to plot the dynode box and PMT photocathode ring onto our 2D histograms.

### data_plotting2D.py
Testing other methods of plotting our data, as ROOT was being finicky.

### datacompile.py
SUPERSEDED BY THE NEW DATACOMPILE.PY PROGRAM THAT INCLUDES ERRORS WITHIN /../Analysis

### eventview.py
Simple python script that lets you go through individual PMT events from a .root file

### roguecatcher.py
Removes values above or below what is physical for our PMT properties, and sets them to neutral values.

### stepinchconversion.py
Change steps into mm for better plots
