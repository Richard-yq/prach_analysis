#!/bin/bash

source ./VARIABLE.sh
cd $PATH_TO_openairinterface5g/cmake_targets/ran_build/build
sudo ninja nr-softmodem nr-uesoftmodem dfts ldpc params_libconfig
# sudo ./build_oai -c --ninja --nrUE --gNB
# sudo ./build_oai -w USRP --ninja --nrUE --gNB --build-lib "nrscope" -C 
# sudo ./build_oai --ninja -c --gNB --nrUE --build-lib telnetsrv -w USRP -C

# usbreset
lsusb
sudo usbreset 
# oai gnb with debug mode
sudo ./nr-softmodem -O ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.usrpb210.conf --gNBs.[0].min_rxtxtime 6 --sa -E --continuous-tx --log_config.PRACH_debug > /home/oaignb/richard/msg1-gnb.log 2>&1

# --log_config.PRACH_debug
sudo ./nr-softmodem -O ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.usrpb210.conf --gNBs.[0].min_rxtxtime 6 --sa -E --continuous-tx --log_config.PRACH_dump

#O1 telnet enable
sudo ./nr-softmodem -O ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.usrpb210.conf --gNBs.[0].min_rxtxtime 6 -E --continuous-tx --log_config.PRACH_debug --telnetsrv --telnetsrv.shrmod o1

cd $PATH_TO_SCRIPT
bash "./all-in-one"


####
# 停止 L1
echo "o1 stop_modem" | nc -N 127.0.0.1 9090

# 設定配置（包含新的 PRACH configuration index）
echo "o1 config nrcelldu3gpp:ssbFrequency 620736 nrcelldu3gpp:arfcnDL 620020 nrcelldu3gpp:bSChannelBwDL 51 bwp3gpp:numberOfRBs 51 bwp3gpp:startRB 0 nrcelldu3gpp:prachConfigurationIndex 98" | nc -N 127.0.0.1 9090
echo "o1 prachconfig 154" | nc -N 127.0.0.1 9090
echo "o1 prachconfig 96" | nc -N 127.0.0.1 9090 #have situation
echo "o1 prachconfig 98" | nc -N 127.0.0.1 9090
echo "o1 prachconfig 148" | nc -N 127.0.0.1 9090
echo "o1 prachconfig 156" | nc -N 127.0.0.1 9090 #sfn 2 every frame Assertion (ra->association_periods * config_period <= 16) failed! Cannot find an association period for 1 SSB and 0 RO with 1.000000 SSB per RO same as originaal OAI UE
echo "o1 prachconfig 150" | nc -N 127.0.0.1 9090 
echo "o1 prachconfig 161" | nc -N 127.0.0.1 9090 # Try out come so good!!! in sfn 9 has two PRACH occasions in frame
echo "o1 prachconfig 146" | nc -N 127.0.0.1 9090 # every 8 frames
echo "o1 prachconfig 145" | nc -N 127.0.0.1 9090 # every 16 frames
echo "o1 prachconfig 159" | nc -N 127.0.0.1 9090 # every 1 frames
echo "o1 prachconfig 157" | nc -N 127.0.0.1 9090 #sfn 2 every frame Assertion (ra->association_periods * config_period <= 16) failed! Cannot find an association period for 1 SSB and 0 RO with 1.000000 SSB per RO same as originaal OAI UE



# 重啟 L1
echo "o1 start_modem" | nc -N 127.0.0.1 9090

# 驗證配置
echo "o1 stats" | nc -N 127.0.0.1 9090

# srsRAN
cd ~/wilfrid/srsRAN_Project/build/apps/gnb
sudo ./gnb -c ./gnbrichard.yaml



## OAI UE connect to OAI gNB
sudo ./nr-uesoftmodem -r 106 --numerology 1 --band 78 --ssb 516  -C 3619200000  -E --ue-fo-compensation


###
cd o1-adapter

sudo ./build-adapter.sh --adapter --no-cache

sudo ./start-adapter.sh --adapter


# 1. 清除舊的認證
git config --global --unset credential.helper

# 2. 使用 Git Credential Manager
git config --global credential.helper store

# 3. 再次 push（會提示輸入帳號密碼或 token）
git push myrepo O1-telnet-alert



# testing

cd 
sudo ./openairinterface5g/cmake_targets/ran_build/build/nr-softmodem -O /home/oaignb/richard-config/OAI_gNB_twoFDM.conf --gNBs.[0].min_rxtxtime 6 -E --continuous-tx --log_config.PRACH_debug --telnetsrv --telnetsrv.shrmod o1 > ~/OAI_gNB.log 2>&1



## srsRAN

cd ~/ocudu/build/apps/gnb$ 
sudo ./gnb -c gnb_rf_b200_tdd_n78_20mhz.yml