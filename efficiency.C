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

using namespace std;

// Testing if this works


float efficiency(TString rootFileName = "hQ_Fixed_Run_13_PMT_162_Loc_9_Test_N.root", 
 			  int low  = 100,
			  int high = 5000){
 
  // This is the method from GetPeakToValley.C
  TString hName = rootFileName;	
  TString rootFilePath = "./";
  rootFilePath += rootFileName;
  
  TFile *rootFile = new TFile(rootFilePath);

  rootFile.ls();

  TH1F * hQ = (TH1F*)rootFile.Get("hQ");
  hQ->Draw();
  int binLow  = hQ->GetXaxis()->FindBin(low);
  int binHigh = hQ->GetXaxis()->FindBin(high);
  
  float prob = hQ->Integral(binLow,binHigh)/hQ->Integral();
  
  return prob;
}
