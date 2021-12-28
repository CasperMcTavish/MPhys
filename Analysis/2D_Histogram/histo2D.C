// PLOT YOUR EFFICIENCY VALUES IN A 2D HISTOGRAM METHOD USING COLZ
// SELECT POSITIONS FILE THAT IS X,Y POSITIONS, WITH OTHER FILE THAT GIVES EFFICIENCY, PV, ETC
//
// WILL IMPLEMENT WITH COLZ, NEED TO STUDY THIS NOW.
//

// Stream file data
double stream(ifstream& stream) {
        double tmpVal;
        stream >> tmpVal;
        return tmpVal;
}

void histo2D(std::string posdata = "Positions2D", std::string data = "Efficiency2D"){
	
	// setup streaming files
	std::ifstream in;
	in.open(posdata.c_str());

	std::ifstream inn;
	inn.open(data.c_str());

	// Setting up canvas and margins
	string title = "2D Histogram of ";
	title += data;
	TCanvas *c1 = new TCanvas("c1", title.c_str());
	c1->SetRightMargin(0.09);
  	c1->SetLeftMargin(0.15);
  	c1->SetBottomMargin(0.15);
 	
	TGraph2D* graph = new TGraph2D();

	// Apply file data to TGraph2D
	int i = 0;
	int ok = true;
	while (ok) {
	  // Stream values in, val1 is x, val2 is y, val3 is efficiency, val4 is uncertainty
	  // This system can be functionalised
	  double val1 = stream(in);
          double val2 = stream(in);
          double val3 = stream(inn);
          double val4 = stream(inn);
	  // Checks both files for if they are at the end of file or if stream is good.
          if ((in.eof()  == true || in.good() == false) && (inn.eof()  == true || inn.good() == false)) {
	     ok =false;
	  }
	  else {
	       // Apply data to TGraph2D
	       graph->SetPoint(i, val1, val2, val3);
	       ++i;
	  }

	}
	in.close();
	inn.close();

	// plot graphs
	graph->SetMarkerStyle(20);
	graph->Draw("COLZ");

}		
