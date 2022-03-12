{
   // Draw ellipse
   TEllipse el1(0.,0.,110.,110.);
   el1.SetFillStyle(0);
   el1.SetLineColor(2);
   el1.SetLineWidth(5);
   el1.SetLineStyle(9);
   el1.Draw();

   string file_name_pdf = "test.pdf";
   c1->SaveAs(file_name_pdf.c_str());
}
