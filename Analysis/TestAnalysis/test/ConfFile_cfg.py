import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1500) )
#process.MessageLogger.cerr.FwkReport.reportEvery = 10

#process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run1_data', '')

process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")
process.centralityBin.nonDefaultGlauberModel = cms.string("HydjetDrum5")

process.GlobalTag.toGet.extend([
   cms.PSet(record = cms.string("HeavyIonRcd"),
      tag = cms.string("CentralityTable_HFtowers200_HydjetDrum5_v740x01_mc"),
      #connect = cms.untracked.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
      connect = cms.string("frontier://FrontierProd/CMS_COND_31X_PHYSICSTOOLS"),
      label = cms.untracked.string("HFtowersHydjetDrum5")
   ),
])

process.source = cms.Source("PoolSource",
#                            duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                            fileNames = cms.untracked.vstring(
'/store/user/tuos/HIAOD2015/round3/June01/MB/HIMinBiasUPC/MB_AOD_DATA750pre5_round3v01/150601_201116/0000/step2_RAW2DIGI_L1Reco_MB_AOD_1.root'
))

process.TFileService = cms.Service("TFileService",
                                  fileName=cms.string("histogram_test_MB_AOD_10events.root")
)

process.demo = cms.EDAnalyzer('TestAnalysis',
   CentralitySrc    = cms.InputTag("hiCentrality"),
   centralityBinLabel = cms.InputTag("centralityBin","HFtowers"),
   srcTracks = cms.InputTag("hiGeneralTracks"),
   srcVertex= cms.InputTag("hiSelectedVertex"),
   UseQuality = cms.bool(True),
   TrackQuality = cms.string('highPurity'),
   trackEtaCut = cms.double(2.4),
   trackPtCut = cms.double(0.3)
)


process.p = cms.Path(process.centralityBin * process.demo)


