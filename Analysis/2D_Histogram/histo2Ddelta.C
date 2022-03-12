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


// Takes the difference between two histograms
void histo2Ddelta(std::string posdata = "grid_positions_317.txt_mm", std::string data = "Efficiencyclean.txtnorm.txt", std::string posdata2 = "grid_positions_317.txt_rotated90_mm", std::string data2 = "Efficiencyclean90.txtnorm.txt"){

	// setup streaming files

  // 1
	std::ifstream in;
	in.open(posdata.c_str());

	std::ifstream inn;
	inn.open(data.c_str());

  // 2
  std::ifstream innn;
	innn.open(posdata2.c_str());

	std::ifstream innnn;
	innnn.open(data2.c_str());


	// Setting up canvas and margins
	string title = "2D Histogram of ";
	title += data;
	title += " bias; X position (mm); Y position (mm)";
	TCanvas *c1 = new TCanvas("c1", title.c_str(), 800, 800);
	c1->SetRightMargin(0.12);
  	c1->SetLeftMargin(0.12);
  	c1->SetBottomMargin(0.1);
	//c1->Divide(3,1);

	// Create Graph 2D
	TGraph2D* graph = new TGraph2D();
	TGraph2D* textbox = new TGraph2D();

        TH2D* h2 = new TH2D("Info",title.c_str(),21,-134,134,21,-134,134);
        TH2D* h3 = new TH2D("Info2",title.c_str(),21,-134,134,21,-134,134);

	graph->SetTitle(title.c_str());
	// Apply file data to TGraph2D

  // 1
	int i = 0;
	int ok = true;
	while (ok) {
	  // Stream values in, val1 is x, val2 is y, val3 is efficiency, val4 is uncertainty
	  // This system can be functionalised

    // 1
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

	       h2->Fill(val1,val2,val3);
	       h2->SetBinError(i, val4);
	       ++i;
	  }

	}
	in.close();
  inn.close();

  // 2
  // Apply file data to TGraph2D
  i = 0;
  ok = true;
  while (ok) {
    // Stream values in, val1 is x, val2 is y, val3 is efficiency, val4 is uncertainty
    // This system can be functionalised

    // 1
    double val1 = stream(innn);
    double val2 = stream(innn);
    double val3 = stream(innnn);
    double val4 = stream(innnn);
    // Checks both files for if they are at the end of file or if stream is good.
          if ((innn.eof()  == true || innn.good() == false) && (innnn.eof()  == true || innnn.good() == false)) {
       ok =false;
    }
    else {
         // Apply data to TGraph2D
         graph->SetPoint(i, val1, val2, val3);

         h3->Fill(val1,val2,val3);
         h3->SetBinError(i, val4);
         ++i;
    }

  }
  innn.close();
  innnn.close();


	// Turn off errors (currently busted otherwise)
	h2->Sumw2(kFALSE);
  h3->Sumw2(kFALSE);

  // Subtract
  TH2D* h4 = new TH2D("Info3",title.c_str(),21,-134,134,21,-134,134);
  h4->Add(h2, h3, 1.0, -1.0);
  h4->SetEntries(1);

/*
	// plot graphs
	c1->cd(1);
	graph->SetMarkerStyle(20);
	graph->Draw("COLZ");
 	h2->SetStats(0);
	h2->Draw("colz");
	
	c1->cd(2);
	graph->SetMarkerStyle(20);
	graph->Draw("COLZ");
 	h3->SetStats(0);
	h3->Draw("colz");

	c1->cd(3);

*/
	//gStyle->SetPalette(0);
	//TColor::InvertPalette();
	graph->SetMarkerStyle(20);
	graph->Draw("COLZ");
	h4->SetStats(0);
	h4->Draw("COLZ");
	//textbox->SetMarkerColor(kRed);
	//textbox->Draw("TEXT SAME");
	// Save graph
	string file_name = posdata;
	file_name += "-";
	file_name += data;
  file_name += "_bias_";
	string file_name_pdf = file_name;
	file_name_pdf += ".pdf";
	file_name += ".root";
	c1->SaveAs(file_name_pdf.c_str());
	c1->SaveAs(file_name.c_str());


}
