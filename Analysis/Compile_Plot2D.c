// PLOTS YOUR X/Y VALUES AGAINST SPECIFIC FILE VALUES WITH ERRORS
// CURRENTLY HAVE THIS SET UP TO RUN WITHIN THE RUNS24-28_PMT162 directory.
// This can be edited by changing the inputs to be the full file directories I imagine
//
// So choose the values at val1,2,3
//
//
//  TO PLOT FOR SPECIFIC XY FILE AND DATA POINT WRITE IN BASH:
//		root "Compile_Plot2D.c(\"XY\",\"mu\")"
//  TO PLOT FROM A DIFFERENT DIRECTORY WRITE LIKE SO:
//  	        root "Compile_Plot2D.c(\"DIR1/DIR2/XY\",\"DIR1/DIR2/mu\")"



double stream(ifstream& stream) {
        double tmpVal;
        stream >> tmpVal;
        return tmpVal;
}

void Compile_Plot2D(std::string file = "XY", std::string data = "Efficiency"){

  std::ifstream in;
  in.open(file.c_str());
  
  std::ifstream inn;
  inn.open(data.c_str());

  
  TGraphErrors* graph = new TGraphErrors();
  graph->GetXaxis()->SetTitle("X position (mm)");
  graph->GetYaxis()->SetTitle(data.c_str());
	
  
  int i = 0;
  int ok = true;
  while (ok) {
    double val1 = stream(in);
    double val2 = stream(in);
    double val3 = stream(inn);
    double val4 = stream(inn);
    if ((in.eof()  == true || in.good() == false) && (inn.eof()  == true || inn.good() == false)) {
      ok =false;
   }
   else {
	// plotting x against efficiency here, but can be modified as needed
	// val1 -> x, val2 -> y, val3 -> parameter entered
      graph->SetPoint(i,val1, val3);
        // first value (0) for XY axis, val4 -> parameter uncertainty
      graph->SetPointError(i, 0, val4);
      ++i;
    }
  }
  in.close();
  inn.close();

  // plot graphs
  graph->SetMarkerStyle(20);
  graph->Draw("AP");
}
