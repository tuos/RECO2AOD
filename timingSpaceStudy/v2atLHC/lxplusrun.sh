#!/bin/bash
cd /afs/cern.ch/user/t/tuos/work/public/reco2AOD/round3/CMSSW_7_5_0_pre5/src
#cmsenv
eval `scramv1 runtime -sh`

cd /afs/cern.ch/user/t/tuos/work/public/reco2AOD/round3/CMSSW_7_5_0_pre5/src/timingSpace/v1

bsub -R "pool>5000" -M 3000000 -q 1nd -J job01AOD < /afs/cern.ch/user/t/tuos/work/public/reco2AOD/round3/CMSSW_7_5_0_pre5/src/timingSpace/v1/cmsrun.sh

