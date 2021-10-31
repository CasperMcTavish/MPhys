#include <iomanip>
#include <iostream>

#include "TFile.h"
#include "TH1F.h"
#include "TF1.h"
#include "TLine.h"

#include "Poisson.C"
#include "GetPeakToValley.C"

#include <TLatex.h>

#include "wmStyle.C"

// Will alter this to take file name as argument for automation.
float testprog(string rootFileName = "hQ_Fixed_Run_13_PMT_162_Loc_9_Test_N.root",string pathToData = "./"){

	string hName = rootFileName;

	// strip away the .root extension
	if (!hName.empty()) {
	hName.resize(hName.size() - 5);
	}

	Result * result = GetPeakToValley(hName,
				    pathToData);

	float valley_Q = result->valley.value;
	float peak_Q   = result->peak.value;
	float diff     = peak_Q - valley_Q;

	return diff;

	

 }
