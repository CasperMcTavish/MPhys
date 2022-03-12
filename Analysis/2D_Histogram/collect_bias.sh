#!/bin/bash

root -b -q "histo2Ddelta.C(\"grid_positions_317.txt_mm\",\"Efficiencyclean.txtnorm.txt\",\"grid_positions_317.txt_rotated90_mm\",\"Efficiencyclean90.txtnorm.txt\")"
root -b -q "histo2Ddelta.C(\"grid_positions_317.txt_mm\",\"gainclean.txtnorm.txt\",\"grid_positions_317.txt_rotated90_mm\",gainclean90.txtnorm.txt\")"
root -b -q "histo2Ddelta.C(\"grid_positions_317.txt_mm\",\"LED_delayclean.txtnorm.txt\",\"grid_positions_317.txt_rotated90_mm\",\"LED_delayclean90.txtnorm.txt\")"
root -b -q "histo2Ddelta.C(\"grid_positions_317.txt_mm\",\"delay_widthclean.txtnorm.txt\",\"grid_positions_317.txt_rotated90_mm\",\"delay_widthclean90.txtnorm.txt\")"
root -b -q "histo2Ddelta.C(\"grid_positions_317.txt_mm\",\"muclean.txtnorm.txt\",\"grid_positions_317.txt_rotated90_mm\",\"muclean90.txtnorm.txt\")"
root -b -q "histo2Ddelta.C(\"grid_positions_317.txt_mm\",\"P_V_Ratioclean.txtnorm.txt\",\"grid_positions_317.txt_rotated90_mm\",\"P_V_Ratioclean90.txtnorm.txt\")"


