#include <iostream>
#include <fstream>
#include <string>
using namespace std;
void mbbarplot() {

   const Int_t nx = 206;
   const Int_t np = 26;
   char *collections[nx+1];
   collections[np-1]="All Other Modules";
   double sum = 0.;
   double sum25 = 0.;
   double collectionV[nx+1];
   collectionV[np-1]=sum-sum25; 

   char ch;
   string line[nx];
   string stringcoll[nx];
   char coll[nx+1][200];
   char collv1[nx+1][200];
   char collv2[nx+1][200]; 
   double vcollv1[nx+1];
   double vcollv2[nx+1];
   ifstream myfile ("sizemb.txt");
   if (myfile.is_open()){
     for(int i=0; i<nx; i++){
       int ich=0;
       int icoll=0;
       int icollv1=0;
       int icollv2=0;
       int iunders=0;
       int ispace=0;
       getline(myfile, line[i]);
       collections[i]=line[i].c_str();
       //cout<<collections[i]<<endl;
       while (collections[i][ich]){
         ch=collections[i][ich];
         if(ch=='_') {
           //cout<<endl;
           iunders++;
         }
         if(iunders==1||iunders==0||iunders==2){
           //coll[i][icoll]=collections[i][ich+1];
           coll[i][icoll]=collections[i][ich];
           //cout<<coll[i][icoll]<<endl;
           icoll++;
         }

         if(isspace(ch)) {
           ch='\n';
           ispace++;
         }
         if(ispace==1){
           collv1[i][icollv1]=collections[i][ich+1];
           icollv1++;
         }
         if(ispace==2){
           collv2[i][icollv2]=collections[i][ich+1];
           icollv2++;
         }

         //putchar(ch);
         ich++;
       }
       coll[i][icoll-1]='\0';
       collv1[i][icollv1-1]='\0';
       collv2[i][icollv2-1]='\0';
       //cout<<"coll= "<<coll[i]<<endl;
       //cout<<"collv1= "<<collv1[i]<<endl;
       //cout<<"collv2= "<<collv2[i]<<endl;
       //cout<<coll[i]<<" "<<atof(collv1[i])<<" "<<atof(collv2[i])<<endl;

       stringcoll[i]=string(coll[i]);
       if(i<np-1)cout<<"stringcoll="<<stringcoll[i]<<endl;
       vcollv1[i]=atof(collv1[i]);
       vcollv2[i]=atof(collv2[i]);
       if(i<np-1) sum25+=vcollv2[i];
       sum+=vcollv2[i];
     }
   }
   //cout<<"sum = "<<sum25<<", "<<sum<<endl;
   //cout<<endl;

   stringcoll[np-1]="All Other Modules"; 
   vcollv2[np-1]=sum-sum25;


double percent[np];
   TH1D *h0 = new TH1D("h0","",26,0,26);
   for (int i=0; i<np; i++) {
      percent[i]=vcollv2[i]*100.0/sum;
      h0->Fill(stringcoll[i].c_str(), percent[i]);
   }
   h0->SetStats(0);
   h0->SetFillColor(2);
   h0->SetBarWidth(0.8);
   h0->SetBarOffset(0.1);
   h0->GetYaxis()->SetTitle("Size in percent (%)");
   h0->GetYaxis()->SetTitleOffset(1.1);
   h0->GetYaxis()->CenterTitle();
   h0->SetTickLength(0.01);
   h0->SetMaximum(19);  
   h0->GetXaxis()->SetLabelSize(0.037);
   h0->GetXaxis()->SetLabelFont(62);
   //h0->GetXaxis()->SetUserRange(-0.5, 29.5);

   TCanvas *c1 = new TCanvas("c1","c1",990,550);
   gPad->SetGrid(); 
   //gPad->SetLogx(); 
   gPad->SetTicks();
   gPad->SetBottomMargin(0.09);
   gPad->SetLeftMargin(0.62);
   gPad->SetRightMargin(0.02);
   gPad->SetTopMargin(0.05);

   //gStyle->SetTitleFontSize(0.1);
gStyle->SetTitleSize(0.1,"x"); 
//h0->SetTitleSize(0.1,"x"); 

   h0->Draw("hbar0");

TLatex tex(0.5,0.5,"u");
tex.SetTextFont(42);
tex.SetTextSize(0.037);
tex.SetNDC();
tex.DrawLatex(0.755, 0.72, "Space Size in percent");
tex.DrawLatex(0.755, 0.655, "MiniBias triggered AOD");

c1->SaveAs("spaceMBAOD_1000events.png");



}

