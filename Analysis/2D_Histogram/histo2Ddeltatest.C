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
void histo2Ddeltatest(std::string file1 = "efficiencyclean.root", std::string file2 = "efficiencyclean90.root"){

  /*
	// setup streaming files

  // 1
	std::ifstream in;
	in.open(posdata.c_str());

	std::ifstream inn;
	inn.open(data.c_str());

  // 2
  std::ifstream innn;
	innn.open(posdata.c_str());

	std::ifstream innnn;
	innnn.open(data.c_str());
  */

	// Setting up canvas and margins
	string title = "2D Histogram of ";
	title += " bias; X position (mm); Y position (mm)";
	TCanvas *c1 = new TCanvas("c1", title.c_str(), 800, 800);
	c1->SetRightMargin(0.12);
  	c1->SetLeftMargin(0.12);
  	c1->SetBottomMargin(0.1);

  /*
	// Create Graph 2D
	TGraph2D* graph = new TGraph2D();
	TGraph2D* textbox = new TGraph2D();

        TH2D* h2 = new TH2D("Info",title.c_str(),21,-134,134,21,-134,134);

	graph->SetTitle(title.c_str());
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
	  //cout << "Entry " << i << endl;
	  // Checks both files for if they are at the end of file or if stream is good.
          if ((in.eof()  == true || in.good() == false) && (inn.eof()  == true || inn.good() == false)) {
	     ok =false;
	  }
	  else {
	       // Apply data to TGraph2D
	       graph->SetPoint(i, val1, val2, val3);

	       h2->Fill(val1,val2,val3);
	       // set errors
	       //cout << "Error " << val4 << endl;
	       h2->SetBinError(i, val4);
               //h2->Fill(val1,val2);
	        //cout << " val1 = " << val1 << endl;
	       //textbox->SetPoint(i, val1, val2, val3);
	       ++i;
	  }

	}
	in.close();
  */

  // Collect first histo
  TFile *f1 = new TFile(file1.c_str(), "read");
  // this is either called h2 or "Info", we'll find out quickly
  TH2D *h1 = (TH2D*)f1->Get("Info");

  // Collect second histo
  TFile *f2 = new TFile(file2.c_str(), "read");
  TH2D *h3 = (TH2D*)f2->Get("Info");

  // Get difference
  TH2D *h_out = (TH2D*)h1->Clone("hist1 - hist2");
  int nx = h_out->GetXaxis()->GetNbins();
  int ny = h_out->GetYaxis()->GetNbins();

  for (int i=1;i<=nx;i++)
    {
    for (int j=1;j<=ny;j++)
            {
            double c1 =h_out->GetBinContent(i,j);
            if (c1 > 0)
                  {
                  double c2 =h3->GetBinContent(i,j);
                  h_out->SetBinContent(i,j,c1-c2);
                  }
            cout << j << endl;
            }
  }


  h_out->Draw("COLZ");
	// Turn off errors (currently busted otherwise)
	//h2->Sumw2(kFALSE);

/*
	// plot graphs
	graph->SetMarkerStyle(20);
	graph->Draw("COLZ");
	// remove legend
	h2->SetStats(0);
        h2->Draw("colz");
	//textbox->SetMarkerColor(kRed);
	//textbox->Draw("TEXT SAME");
	// Save graph
	string file_name = posdata;
	file_name += "-";
	file_name += data;
	string file_name_pdf = file_name;
	file_name_pdf += ".pdf";
	file_name += ".root";
	c1->SaveAs(file_name_pdf.c_str());
	c1->SaveAs(file_name.c_str());

*/
}
