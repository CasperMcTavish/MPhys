#!/bin/bash

root -b -q "Compile_Plot2D.c(\"Bend_radii\",\"mu\")"
root -b -q "Compile_Plot2D.c(\"Bend_radii\",\"gain\")"
root -b -q "Compile_Plot2D.c(\"Bend_radii\",\"LED_delay\")"
root -b -q "Compile_Plot2D.c(\"Bend_radii\",\"delay_width\")"
root -b -q "Compile_Plot2D.c(\"Bend_radii\",\"Efficiency\")"
root -b -q "Compile_Plot2D.c(\"Bend_radii\",\"P:V_Ratio\")"

