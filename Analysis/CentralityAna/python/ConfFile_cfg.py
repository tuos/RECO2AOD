import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(300) )
#process.MessageLogger.cerr.FwkReport.reportEvery = 10

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('RecoLocalTracker.SiPixelRecHits.PixelCPEESProducers_cff')
process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
#process.load('RecoHI.HiCentralityAlgos.HiCentrality_cfi')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run1_data', '')

#import HLTrigger.HLTfilters.hltHighLevel_cfi
#process.hltFilter = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
#process.hltFilter.HLTPaths = ["HLT_HIMinBiasHfOrBSC_v*"]
#process.hltFilter.throw = False
#process.hltFilter.andOr = True

process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")
process.centralityBin.nonDefaultGlauberModel = cms.string("HydjetDrum5")
#process.centralityBin.nonDefaultGlauberModel = cms.string("")

process.GlobalTag.toGet.extend([
   cms.PSet(record = cms.string("HeavyIonRcd"),
      tag = cms.string("CentralityTable_HFtowers200_HydjetDrum5_v740x01_mc"),
      connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
      label = cms.untracked.string("HFtowersHydjetDrum5")
      #label = cms.untracked.string("HFtowers")
   ),
])

process.source = cms.Source("PoolSource",
#                            duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                            fileNames = cms.untracked.vstring(
#'file:/afs/cern.ch/user/t/tuos/work/public/reco2AOD/April10/step2_RAW2DIGI_L1Reco_MB_AOD.root'
#'file:/afs/cern.ch/user/t/tuos/work/public/reco2AOD/April10/step2_RAW2DIGI_L1Reco_MB_RECO.root'
'file:/afs/cern.ch/user/t/tuos/work/public/reco2AOD/April10/step2_RAW2DIGI_L1Reco_UCC300_AOD.root'
#'file:/afs/cern.ch/user/t/tuos/work/public/reco2AOD/April10/step2_RAW2DIGI_L1Reco_UCC300_RECO.root'
#'file:/afs/cern.ch/user/t/tuos/work/public/reco2AOD/April10/step2_RAW2DIGI_L1Reco_JET_AOD.root'
#'file:/afs/cern.ch/user/t/tuos/work/public/reco2AOD/April10/step2_RAW2DIGI_L1Reco_DIMUONskim_AOD.root'
    ))

process.TFileService = cms.Service("TFileService",
                                  fileName=cms.string("histogram_test_UCC_AOD.root"))

process.demo = cms.EDAnalyzer('CentralityAna',
   CentralitySrc    = cms.InputTag("hiCentrality"),
   centralityBinLabel = cms.InputTag("centralityBin","HFtowers")
)

#process.p = cms.Path(process.hltFilter * process.centralityBin * process.demo)
process.p = cms.Path(process.centralityBin * process.demo)
#process.p = cms.Path(process.hltFilter * process.demo)

