{
   // Draw ellipse
   TEllipse el1(0.,0.,110.,110.);
   el1.SetFillStyle(0);
   el1.SetLineColor(2);
   el1.SetLineWidth(5);
   el1.SetLineStyle(9);
   el1.Draw();

   // Draw Dynode box
   TBox *box1 = new TBox(-12.5, -12.5, 12.5, 12.5);
   box1->Class_Name("Dynode");
   box1->SetFillStyle(0);
   box1->SetLineColor(4);
   box1->SetLineWidth(4);
   box1->SetLineStyle(9);
   box1->Draw();


   //TLegend *legend = new TLegend(100, 50);
   //legend->AddEntry("box1", "Dynode", "l");
   //legend->AddEntry("el1", "Photocathode", "l");
   //legend->Draw();
   c1->BuildLegend();
   string file_name_pdf = "dynodering.pdf";
   string file_name_root = "dynodering.root";
   c1->SaveAs(file_name_pdf.c_str());
   c1->SaveAs(file_name_root.c_str());
}
