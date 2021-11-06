
double stream(ifstream& stream) {
        double tmpVal;
        stream >> tmpVal;
        return tmpVal;
}

void PMTShapeTwo(std::string file = "PMT.txt"){

  std::ifstream in;
  in.open(file.c_str());

  TGraph* graph = new TGraph();

  std::vector<double> r; std::vector<double> z;
  int i = 0;
  int ok = true;
  while (ok) {
    double val1 = stream(in);
    double val2 = stream(in);
    if (in.eof()  == true || in.good() == false) {
      ok =false;
   }
   else {
     // std::cout << val1 << " " << val2 << std::endl;
      graph->SetPoint(i,val1, val2);
      z.push_back(val1); r.push_back(val2);
      ++i;
    }
  }
  in.close();
  

 
    // draw 100 points 
  //  float y;
  //  int j;
  //  int k;
    // starting from higher number to avoid combination with previous
  //  int l = i+1;
  //  for (j=0; j < 6; ++j)
  //  {
  //	y = j*25.3;
  //
  //	for (k=0; k < 270; ++k)
  //	{
  //		graph->SetPoint((k+l)*(j+1),k,y);
  //	}
  //}



  graph->SetMarkerStyle(20);
  graph->Draw("AP");
  
  // Draw lines
  int o;
  float y;
  for (o=0; o < 6; ++o){
	// Finding y position for drawing the line
	y = o*25.3;
	TLine *t = new TLine(0,y,270,y);
	t->SetLineColor(3);
	t->SetLineWidth(3);
	t->Draw();
  }


  double area= 0.0;
  /*  double stepsize = 244.5/1000000;
  for (int istep =0; istep < 1000000; ++istep){
    double z = stepsize*istep;
    area+= 2*TMath::Pi()*stepsize*graph->Eval(z);
  }
  */

  for (int istep = 1; istep < r.size(); ++istep){
    double s = sqrt(std::pow(r[istep] - r[istep-1],2) + std::pow(z[istep] - z[istep-1],2.) );
    area += TMath::Pi()*s*(r[istep] + r[istep-1]);
  }
  
  std::cout <<  area <<std::endl;
}
