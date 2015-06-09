// -*- C++ -*-
//
// Package:    Analysis/CentralityAna
// Class:      CentralityAna
// 
/**\class CentralityAna CentralityAna.cc Analysis/CentralityAna/plugins/CentralityAna.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Shengquan Tuo
//         Created:  Mon, 13 Apr 2015 04:17:32 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include <TH1D.h>
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/HeavyIonEvent/interface/Centrality.h"
//
// class declaration
//

class CentralityAna : public edm::EDAnalyzer {
   public:
      explicit CentralityAna(const edm::ParameterSet&);
      ~CentralityAna();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------
   edm::Service<TFileService> fs;
  edm::Handle<int> cbin_;
  edm::EDGetTokenT<int> CentralityBinTag_;
   TH1D* centHist;
   TH1D* trkHist;
   TH1D* hfHist;
  edm::InputTag CentralityTag_;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
CentralityAna::CentralityAna(const edm::ParameterSet& iConfig)

//CentralityBinTag_(consumes<int>(iConfig.getParameter<edm::InputTag>("centralityBinLabel")))
{
   //now do what ever initialization is needed
CentralityBinTag_ = consumes<int>(iConfig.getParameter<edm::InputTag>("centralityBinLabel"));
edm::Service<TFileService> fs;
trkHist = fs->make<TH1D>("ntrkhist","Ntrk Distribution", 100, 0., 3000.);
hfHist = fs->make<TH1D>("hfhist","Sum HFET Distribution", 100, 0., 5000.);
centHist = fs->make<TH1D>("centhist","Centrality Distribution", 200, 0., 200.);
CentralityTag_ = iConfig.getParameter<edm::InputTag> ("CentralitySrc");

}


CentralityAna::~CentralityAna()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
CentralityAna::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace std;
   using namespace reco;

   iEvent.getByToken(CentralityBinTag_,cbin_);
   int bin = *cbin_;
   centHist->Fill(bin);

    edm::Handle<reco::Centrality> centrality;
    iEvent.getByLabel(CentralityTag_, centrality);
    trkHist->Fill(centrality->Ntracks());
    hfHist->Fill(centrality->EtHFtowerSum());
    cout<<"Centraliyt bin = "<<bin<<",  Ntracks= "<<centrality->Ntracks()<<", EtHFtowerSum= "<<centrality->EtHFtowerSum()<<endl;


#ifdef THIS_IS_AN_EVENT_EXAMPLE
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);
#endif
   
#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
#endif
}


// ------------ method called once each job just before starting event loop  ------------
void 
CentralityAna::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
CentralityAna::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
/*
void 
CentralityAna::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
CentralityAna::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
CentralityAna::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
CentralityAna::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
CentralityAna::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(CentralityAna);
