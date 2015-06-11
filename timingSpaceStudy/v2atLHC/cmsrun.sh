cd /afs/cern.ch/user/t/tuos/work/public/reco2AOD/round3/CMSSW_7_5_0_pre5/src
#cmsenv
eval `scramv1 runtime -sh`

cd /afs/cern.ch/user/t/tuos/work/public/reco2AOD/round3/CMSSW_7_5_0_pre5/src/timingSpace/v1

cmsRun step2_RAW2DIGI_L1Reco_MB_AODSIM2760GeV.py &> job01A1out.log
cmsRun step2_RAW2DIGI_L1Reco_MB_AODSIM5020GeV.py &> job01A2out.log
cmsRun step2_RAW2DIGI_L1Reco_DIJET_AODSIM2760GeV.py &> job01A3out.log
cmsRun step2_RAW2DIGI_L1Reco_DIJET_AODSIM5020GeV.py &> job01A4out.log

cmsRun step2_RAW2DIGI_L1Reco_MB_AOD.py &> job01A5out.log
cmsRun step2_RAW2DIGI_L1Reco_JET_AOD.py &> job01A6out.log
cmsRun step2_RAW2DIGI_L1Reco_DIMUONskim_AOD.py &> job01A7out.log
cmsRun step2_RAW2DIGI_L1Reco_UCC_AOD.py &> job01A8out.log


