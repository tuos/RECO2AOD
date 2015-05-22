#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void mbbarplot() {

   const Int_t nx = 207;
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
   char collv1[nx+1][200];
   char collv2[nx+1][200];
   char collv3[nx+1][200]; 
   char collv4[nx+1][200]; 
   double vcollv2[nx+1];
   double vcollv3[nx+1];
   ifstream myfile ("stimingmb.txt");
   if (myfile.is_open()){
     for(int i=0; i<nx; i++){
       int ich=0;
       int icoll=0;
       int icollv1=0;
       int icollv2=0;
       int icollv3=0;
       int icollv4=0;
       int ispace=0;
       getline(myfile, line[i]);
       collections[i]=line[i].c_str();
       //cout<<collections[i]<<endl;
       while (collections[i][ich]){
         ch=collections[i][ich];

         if(isspace(ch)) {
           ch='\n';
           ispace++;
         }
         if(ispace==0){
           collv1[i][icollv1]=collections[i][ich];
           icollv1++;
         }
         if(ispace==1){
           collv2[i][icollv2]=collections[i][ich+1];
           icollv2++;
         }
         if(ispace==2){
           collv3[i][icollv3]=collections[i][ich+1];
           icollv3++;
         }
         if(ispace==3){
           collv4[i][icollv4]=collections[i][ich+1];
           icollv4++;
         }
         //putchar(ch);
         ich++;
       }
       //coll[i][icoll-1]='\0';
       //collv1[i][icollv1-1]='\0';
       //collv2[i][icollv2-1]='\0';

       //cout<<collv1[i]<<", "<<atof(collv2[i])<<", "<<atof(collv3[i])<<",  "<<collv4[i]<<endl;


       stringcoll[i]=string(collv4[i]);
       if(i<np-1)cout<<"stringcoll="<<stringcoll[i]<<endl;
       vcollv2[i]=atof(collv2[i]);
       vcollv3[i]=atof(collv3[i]);
       if(i<np-1) sum25+=vcollv2[i];
       sum+=vcollv2[i];

     }
   }
   //cout<<"sum = "<<sum25<<", "<<sum<<endl;
   //cout<<endl;

   stringcoll[np-1]="All Other Modules"; 
   vcollv2[np-1]=sum-sum25;


double percent[nx];
   TH1D *h0 = new TH1D("h0","",26,0,26);
   for (int i=0; i<np; i++) {
      percent[i]=vcollv2[i]*100.0/sum;
      h0->Fill(stringcoll[i].c_str(), percent[i]);
   }
   h0->SetStats(0);
   h0->SetFillColor(2);
   h0->SetBarWidth(0.8);
   h0->SetBarOffset(0.1);
   h0->GetYaxis()->SetTitle("Time in percent (%)");
   h0->GetYaxis()->SetTitleOffset(1.1);
   h0->GetYaxis()->CenterTitle();
   h0->SetTickLength(0.01);
   h0->SetMaximum(23);  
   //h0->GetXaxis()->SetUserRange(-0.5, 29.5);

   TCanvas *c1 = new TCanvas("c1","c1",880,660);
   gPad->SetGrid(); 
   //gPad->SetLogx(); 
   gPad->SetTicks();
   gPad->SetBottomMargin(0.09);
   gPad->SetLeftMargin(0.30);
   gPad->SetRightMargin(0.02);
   gPad->SetTopMargin(0.05);

   h0->Draw("hbar0");

TLatex tex(0.5,0.5,"u");
tex.SetTextFont(42);
tex.SetTextSize(0.04);
tex.SetNDC();
tex.DrawLatex(0.555, 0.72, "Timing in the reconstruction step");
tex.DrawLatex(0.555, 0.655, "MiniBias triggered AOD");

c1->SaveAs("timingMBAOD_1000events.png");


}

