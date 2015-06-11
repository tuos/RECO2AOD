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
'/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/181/913/F0E10658-EA10-E111-BF76-0030486780B8.root',
'/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/181/913/F20296BD-EB10-E111-9531-003048F1110E.root',
'/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/181/913/F21F58B1-F010-E111-9F1E-001D09F29619.root',
'/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/181/913/F24E9E46-D710-E111-AD18-003048D2BE06.root',
'/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/181/913/F2643149-F410-E111-AB6D-0025901D624E.root',
'/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/181/913/F2842D80-EC10-E111-A0C5-BCAEC518FF62.root',
'/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/181/913/F28FA79E-EE10-E111-AE01-0025B32036D2.root',
'/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/181/913/F2A76444-C410-E111-A4ED-0019B9F72F97.root',
'/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/181/913/F2AF0E5B-C910-E111-9775-0025901D5DB2.root',
'/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/181/913/F2F32F23-CE10-E111-B9A3-001D09F28F25.root'
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
    fileName = cms.untracked.string('step2_RAW2DIGI_L1Reco_UCC_AOD100events.root'),
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
process.hltFilter.HLTPaths = ["HLT_HIUCC015_v*"]
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

