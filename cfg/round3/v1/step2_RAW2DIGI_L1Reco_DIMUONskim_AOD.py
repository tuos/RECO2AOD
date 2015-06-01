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
    output = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
'/store/results/hin/StoreResults/HIDiMuon/USER/L2DoubleMu3Skim_v10_38dff9fa051006d6e895e3c1df676d76-v1/40000/FCBF917E-13D0-E411-929D-0026B93F4112.root',
'/store/results/hin/StoreResults/HIDiMuon/USER/L2DoubleMu3Skim_v10_38dff9fa051006d6e895e3c1df676d76-v1/40000/FCC34C3D-C8CF-E411-9E9E-B083FEC76567.root'
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
    fileName = cms.untracked.string('step2_RAW2DIGI_L1Reco_DIMUONskim_AOD.root'),
#    SelectEvents = cms.untracked.PSet(
#                SelectEvents = cms.vstring("filter_step")
#                ),
    outputCommands = process.AODEventContent.outputCommands
)

process.AODoutput.outputCommands += [ 'keep recoElectronSeeds_ecalDrivenElectronSeeds_*_*' ]
process.AODoutput.outputCommands += [ 'keep recoTrackExtras_electronGsfTracks_*_*' ]

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run1_data', '')

#import HLTrigger.HLTfilters.hltHighLevel_cfi
#process.hltFilter = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
#process.hltFilter.HLTPaths = ["HLT_HIMinBiasHfOrBSC_v*"]
#process.hltFilter.throw = False
#process.hltFilter.andOr = True

# Path and EndPath definitions
#process.filter_step = cms.Path(process.hltFilter)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstructionHeavyIons + process.hiMergedConformalPixelTracking)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODoutput_step = cms.EndPath(process.AODoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.AODoutput_step)

from Configuration.Applications.ConfigBuilder import MassReplaceInputTag
MassReplaceInputTag(process)

for path in process.paths:
        getattr(process,path)._seq = getattr(process,path)._seq

