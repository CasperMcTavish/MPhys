import matplotlib.pyplot as plt
import numpy as np
import os
import sys


## SUPERSEDED BY THE NEW DATACOMPILE.PY PROGRAM THAT INCLUDES ERRORS
## Left here in case anything goes disastrously wrong.

# Code that will go into each RUN and select the files, read them to into a list.
# Then from the list, it will take the text before the first '=', and use this to add it to a list
# For that specific value

# start with this function when sitting at ../XYTesting/ within data storage.
# For the test rig at home, will be starting at ../RUNFILES/

def collect_data(first_run = 24, last_run = 28, pmt = 162):
    """
    Collects the data from the xy_results.txt files across multiple runs in a format that allows for easy entry into ROOT for graphical purposes.

    The code currently works across the runs sequentially, (24, 25, 26, ...) so be aware of this when running the program.

    Example usage:
    collect_data(24, 28, 162)

    :param first_run:   The first run to be analysed
    :param last_run:    The last run to be analysed
    :param pmt:         The PMT that you wish to collect data over
    """

    # Create directory to hold all these textfiles in if it doesnt yet exist
    run_length = "RUNS" + str(first_run) + "-" + str(last_run) + "_PMT" + str(pmt)
    if not os.path.exists(run_length):
        os.makedirs(run_length)

    # Convert first and last runs to integers for the loop (apparently converted by sys)
    first_run = int(first_run)
    last_run = int(last_run)

    # create loop across all runs
    for i in range(first_run,last_run+1):

        # Create RUN0000NN section of path
        path = str(i)
        path = str(path).zfill(6)
        path = "/RUN" + path
        
        # RUN0000NN/0162 or whatever your PMT of choice is
        path += "/PMT"
        path += str(pmt).zfill(4)
        
        # Hardcoded, change if this changes, or if you're doing this for a different run-type
        path += "/Nominal"
        
        path += "/TextFiles/"

        # Collect current working directory and append it onto the full list. This ensures that it runs.
        startpath = os.getcwd()
        path = startpath + "/" + path

        # Here you are in the directory, so will list all files and run the process for each
        files = os.listdir(path)

        for j in range(len(files)):
            file = path + files[j]
            
            #Variable for storing each runs data
            mylines = []
            
            # Collect variables
            with open (file, 'rt') as myfile:
                for myline in myfile:
                    mylines.append(myline.rstrip('\n'))
            
            # Now separate them out based on label and add them onto files (if they haven't been already)
            for k in range(len(mylines)-1):
                # Ignoring first component as it is file title, hence k+1

                # Split up around '=', so that data and label can be collected separately
                comp = mylines[k+1].partition('=')

                # collect label
                label = comp[0]
                
                # remove ending whitespace, then replace all other spaces with _
                label = label.strip()
                label = label.replace(" ","_")
                
                # collect data
                data = comp[2]
                
                text_dir = run_length + "/" + label
                
                # create text file if one doesnt exist to write to.
                if not os.path.exists(text_dir):
                    print(text_dir + " does not exist! Creating file...")
                    open(text_dir, 'w').close()
                # Same as above but for errors
                if not os.path.exists(text_dir + "_errors"):
                    print(text_dir + "_errors" + " does not exist! Creating file...")
                    open(text_dir + "_errors", 'w').close()




                # Append data to the file

                # remove starting space, then split into error and data
                data = data.strip()

                # Pull out the data, separate from error [value, error]
                data = data.partition(" ")

                # remove brackets from the errors
                error = data[2].strip("()")

                # Write data and errors to respective files
                with open(text_dir, "a") as myfile:
                    myfile.write(data[0] + "\n")
                with open(text_dir + "_errors", "a") as myfile:
                    myfile.write(error + "\n")



    print("Data written to " + run_length)
            





            

        
# Collect arguments to run, if you dont have enough, stop the code

if len(sys.argv) == 4:
    # ignoring the name of the python script
    collect_data(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    print("collect_data takes exactly 3 arguments (" + str(len(sys.argv)-1) + ") given")





