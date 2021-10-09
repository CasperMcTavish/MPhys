import uproot
import matplotlib.pyplot as plt
import numpy as np
#import functions as fnc

# Viewing particular event of particular file.
# Open the data, apply to variable
file = "E:\Github\SHProjectSignalDetection\Code\PMTsignals\Run_2_PMT_162_Loc_9_Test_N.root"
# File directory specific, just to remove the E:\PMTsignals\ rubbish
filename = file[14:]

# Taking specific cooked run, you can check them in python easily, swap 36 with 35
tree = uproot.open(file)["Cooked_Run_2_PMT_162_Loc_9_Test_N;36"]
branches = tree.arrays()
#print(branches['ADC'])

# how long between data taken
timegate = 2
# length of event
eventno = len(branches['ADC'][0])
time = []
# Creating list for sample times that are 2ns intervals, 150 samples
for i in range(eventno):
    time.append(i*timegate)

# Input event
eventmore = int(input("How many events?"))


for i in range(eventmore):
    plt.plot(time,branches['ADC'][i], linewidth = 5)
    plt.xlabel("Sample Time (ns)", fontsize = 17)
    plt.ylabel("ADC Value", fontsize = 17)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.title(str(filename) + " event " + str(i), fontsize = 22)
    plt.show()
