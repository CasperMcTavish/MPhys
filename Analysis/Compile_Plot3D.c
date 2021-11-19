// PLOTS YOUR X AND Y VALUES AGAINST SPECIFIC FILE VALUES
// THIS IS UNFINISHED, BUT WILL BE SETUP TO DRAW 3D HISTOGRAM

// CURRENTLY HAVE THIS SET UP TO RUN WITHIN THE RUNS24-28_PMT162 directory.
// So choose the values at val1,2,3
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

  TGraph* graph = new TGraph();
  
  int i = 0;
  int ok = true;
  while (ok) {
    double val1 = stream(in);
    double val2 = stream(in);
    double val3 = stream(inn);
    if ((in.eof()  == true || in.good() == false) && (inn.eof()  == true || inn.good() == false)) {
      ok =false;
   }
   else {
	// plotting x against efficiency here, but can be modified as needed
	// val1 -> x, val2 -> y, val3 -> parameter entered
      graph->SetPoint(i,val1, val3);
      ++i;
    }
  }
  in.close();
  inn.close();

  // plot graphs
  graph->SetMarkerStyle(20);
  graph->Draw("AP");
}
