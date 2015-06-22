from WMCore.Configuration import Configuration
config = Configuration()

config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'MB_AOD_round3v01'

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_RAW2DIGI_L1Reco_MB_AOD.py'
config.JobType.outputFiles = ['step2_RAW2DIGI_L1Reco_MB_AOD.root']

config.section_('Data')
config.Data.inputDBS = 'global'
config.Data.inputDataset = '/HIMinBiasUPC/HIRun2011-v1/RAW'
config.Data.lumiMask = 'lumiInputMB.json'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 2
#config.Data.runRange = '193093-193999'
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
#config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader/'
config.Data.publication = True
config.Data.publishDataName = 'MB_AOD_DATA750pre5_round3v01'
config.Data.outLFNDirBase = '/store/user/tuos/HIAOD2015/round3/June01/MB'

config.section_('Site')
config.Site.whitelist = ['T2_US_Vanderbilt']
config.Site.storageSite = 'T2_US_Vanderbilt'
