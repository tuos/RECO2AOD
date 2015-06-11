# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --conditions auto:run1_data -s RAW2DIGI,L1Reco,RECO --process AOD -n 10 --data --eventcontent AOD --scenario HeavyIons --datatier AOD --repacked --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('AOD')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    output = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
'/store/hidata/HIRun2011/HIHighPt/RAW/v1/000/181/969/E843155B-A611-E111-9B78-002481E0D83E.root',
'/store/hidata/HIRun2011/HIHighPt/RAW/v1/000/181/969/E890E44F-9F11-E111-A874-E0CB4E5536AE.root',
'/store/hidata/HIRun2011/HIHighPt/RAW/v1/000/181/969/E892668A-8B11-E111-914F-001D09F276CF.root',
'/store/hidata/HIRun2011/HIHighPt/RAW/v1/000/181/969/E8B87ACF-A211-E111-9C47-002481E0CC00.root',
'/store/hidata/HIRun2011/HIHighPt/RAW/v1/000/181/969/EA432269-8911-E111-A00C-001D09F28E80.root',
'/store/hidata/HIRun2011/HIHighPt/RAW/v1/000/181/969/EAA5053B-A411-E111-BABF-BCAEC518FF44.root',
'/store/hidata/HIRun2011/HIHighPt/RAW/v1/000/181/969/EACB24AD-8811-E111-B33D-003048D3C980.root',
'/store/hidata/HIRun2011/HIHighPt/RAW/v1/000/181/969/EAD4FBAF-A011-E111-9C70-BCAEC532972E.root',
'/store/hidata/HIRun2011/HIHighPt/RAW/v1/000/181/969/EC6337E4-A911-E111-B859-002481E0D7D8.root',
'/store/hidata/HIRun2011/HIHighPt/RAW/v1/000/181/969/EC6A2A91-9E11-E111-A161-BCAEC5364C93.root'
),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
wantSummary = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.AODoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('AOD'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fileName = cms.untracked.string('step2_RAW2DIGI_L1Reco_JET_AOD100events.root'),
    SelectEvents = cms.untracked.PSet(
                SelectEvents = cms.vstring("filter_step")
                ),
    outputCommands = process.AODEventContent.outputCommands
)

process.AODoutput.outputCommands += [ 'keep recoElectronSeeds_ecalDrivenElectronSeeds_*_*' ]
process.AODoutput.outputCommands += [ 'keep recoTrackExtras_electronGsfTracks_*_*' ]

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run1_data', '')

import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltFilter = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltFilter.HLTPaths = ["HLT_HIJet80_v*"]
process.hltFilter.throw = False
process.hltFilter.andOr = True

# Path and EndPath definitions
process.filter_step = cms.Path(process.hltFilter)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstructionHeavyIons + process.hiMergedConformalPixelTracking)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODoutput_step = cms.EndPath(process.AODoutput)

# Schedule definition
process.schedule = cms.Schedule(process.filter_step,process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.AODoutput_step)

from Configuration.Applications.ConfigBuilder import MassReplaceInputTag
MassReplaceInputTag(process)

for path in process.paths:
        getattr(process,path)._seq = process.hltFilter * getattr(process,path)._seq

