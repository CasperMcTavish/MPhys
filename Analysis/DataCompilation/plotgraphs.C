// PLOTS MULTIPLE GRAPHS ALONG ONE AXIS (EFFICIENCY, PV, ETC AGAINST POSITION)
// Will take the file inputs as arguments, add more arguments of the same form if needed.
//
// Input required like so, or will default to the below files:
// 		root "plotgraphs.C(\"Efficiency260.root\",\"Efficiency206.root\")"

void plotgraphs(std::string data1 = "Positions-Efficiency206.root", std::string data2 = "Positions-Efficiency260.root"){
	
	// Read files into TFiles
	TFile * inputfile1 = new TFile(data1.c_str());
	TFile * inputfile2 = new TFile(data2.c_str());

	// Create canvas and plot files
	TCanvas* comp = new TCanvas("c1", "c1", 800, 600);
	comp->SetRightMargin(0.09);
  	comp->SetLeftMargin(0.15);
  	comp->SetBottomMargin(0.15);
  	
	
	// Plot first graph
	TGraphErrors* plot1 = (TGraphErrors*)inputfile1->Get(";1");
	TGraphErrors* plot2 = (TGraphErrors*)inputfile2->Get(";1");
	
	// Setting Y axis (needs to be altered based on the graph itself
	plot1->GetYaxis()->SetTitle("Efficiency");
	
	// Set colour (if you have more than 2 plots, will colours change?)
	plot1->SetMarkerColor(2); // red = 2
	plot1->Draw("AP");
	plot2->Draw("P");
	// Create Legend
	auto legend = new TLegend(0.15, 0.15, 0.5, 0.25);
	legend->AddEntry(plot1, data1.c_str(), "p");
	legend->AddEntry(plot2, data2.c_str(), "p");
	legend->Draw();

	// Change file naming system to be unique to each value assessed (PV, efficiency, etc)
	// Will have to change how data is inputted to allow for this to happen.
	string file_name = "CompiledData.root";
	comp->SaveAs(file_name.c_str());


}
