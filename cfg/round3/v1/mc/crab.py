from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'HydjetMB_RECO_round3v01'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_RAW2DIGI_L1Reco_MB_RECOSIM.py'
config.JobType.outputFiles = ['step2_RAW2DIGI_L1Reco_MB_RECOSIM.root']

config.section_('Data')
config.Data.inputDBS = 'phys03'
config.Data.inputDataset = '/Hydjet_Quenched_MinBias_5020GeV/mnguyen-HydjetMB_740pre8_MCHI2_74_V3_53XBS_DIGI-RAW-6da45e4e90741bc03dbd9aec5f36c050/USER'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.publication = True
config.Data.publishDataName = 'HydjetMB_RECO_750pre5_round3v01'
config.Data.outLFNDirBase = '/store/user/tuos/HIAOD2015/round3/June01/HydjetMBRECO'

config.section_('Site')
#config.Site.whitelist = ['T2_US_MIT']
config.Site.storageSite = 'T2_US_Vanderbilt'
