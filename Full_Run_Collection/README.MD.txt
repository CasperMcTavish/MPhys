This folder will hopefully contain all relevant files for the processing and automatic analysis of data.

- XY-position production

Contains scripts used to produce the XY-position text files that are used for automated scanning across the PMT surface. Also includes example outputs of said scripts
Eg: datapointscartesian.py allows for the production of a grid of XY-positions above the PMT surface, dependent on user input.

- Data Collection

Includes the scripts required for automated data collection across the PMT surface.
Currently relies on the inclusion of two WATCHMAN-specific scripts: 
* "Run_wavedump_PCI_1_min_10_CH_NS_150.sh"
* "move_10_ch_nom_trig_auto.sh"

The first script allows for the collection of data for 1 minute across the 10th channel, with each individual event being 150 samples (300ns) in length. The second script automatically moves the 10th channel data to a RUN directory within the WATCHMAN's wavedump repository's "storage" section. These are specific scripts produced for the MPhys project, and instead can be replaced with any appropriate wavedump scripts.

- Data Analysis

Consists of a python script that collects a range of RUN directories from within the repository's storage section, and applies fitting provided by the WATCHMANs 'Analysis/Fitting' directory to determine specific characteristics of each run (such as efficiency, P:V, etc) via the use of a shell script. This will require some tinkering on your machine to ensure that the directories are all correctly positioned and described within the script, but speeds up the analysis process significantly.

Also includes the relevant C files for applying this automated analysis, but you should preferably look at the WATCHMAN's analysis/fitting directory as shown here: https://github.com/Watchman-PMT/Wavedump_Wrapper/tree/master/Analysis

- Analysis Collation

Script that collects the relevant characteristics across multiple RUN directories and produces text files that contain all of these characteristics corresponding the position file produced within XY-position production.

- Analysis Visualisation

Folder containing all the small scripts that then use these aforementioned text file to produce 2D histograms, bias histograms, etc. Everything in this folder is only used to try and develop the visual component of this project, with the most significant part being the "2D_Histogram" directory, which contains the scripts that produce our 2D histograms (histo2D.C)


Thank you for reading, if you have any questions, feel free to email me at s1739002@ed.ac.uk or johnwaiton@hotmail.co.uk