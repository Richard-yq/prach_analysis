[UTIL]   running in SA mode (no --phy-test, --do-ra, --nsa option present)
[0m[OPT]   OPT disabled
[0m[HW]   Version: Branch: msg1_fdm_enable Abrev. Hash: 624ef372a1 Date: Mon Jul 21 15:09:42 2025 +0800
[0m[GNB_APP]   Initialized RAN Context: RC.nb_nr_inst = 1, RC.nb_nr_macrlc_inst = 1, RC.nb_nr_L1_inst = 1, RC.nb_RU = 1, RC.nb_nr_CC[0] = 1
[0m[NR_PHY]   Initializing gNB RAN context: RC.nb_nr_L1_inst = 1 
[0m[NR_PHY]   Registered with MAC interface module (0x5bae7bfae270)
[0m[NR_PHY]   Initializing NR L1: RC.nb_nr_L1_inst = 1
[0m[NR_PHY]   L1_RX_THREAD_CORE -1 (15)
[0m[NR_PHY]   TX_AMP = 519 (-36 dBFS)
[0m[PHY]   No prs_config configuration found..!!
[0m[GNB_APP]   pdsch_AntennaPorts N1 1 N2 1 XP 1 pusch_AntennaPorts 1
[0m[GNB_APP]   minTXRXTIME 6
[0m[GNB_APP]   SIB1 TDA 1
[0m[GNB_APP]   CSI-RS 1, SRS 1, SINR:0, 256 QAM may be on, delta_MCS off, maxMIMO_Layers -1, HARQ feedback enabled, num DLHARQ:16, num ULHARQ:16
[0m[NR_MAC]   No RedCap configuration found
[0m[GNB_APP]   sr_ProhibitTimer 0, sr_TransMax 64, sr_ProhibitTimer_v1700 0, t300 400, t301 400, t310 2000, n310 10, t311 3000, n311 1, t319 400
[0m[NR_MAC]   Candidates per PDCCH aggregation level on UESS: L1: 0, L2: 2, L4: 0, L8: 0, L16: 0
[0m[RRC]   Read in ServingCellConfigCommon (PhysCellId 0, ABSFREQSSB 641280, DLBand 78, ABSFREQPOINTA 640008, DLBW 106,RACH_TargetReceivedPower -96
[0m[RRC]   absoluteFrequencySSB 641280 corresponds to 3619200000 Hz
[0m[NR_MAC]   TDD period index = 6, based on the sum of dl_UL_TransmissionPeriodicity from Pattern1 (5.000000 ms) and Pattern2 (0.000000 ms): Total = 5.000000 ms
[0m[UTIL]   threadCreate() for MAC_STATS: creating thread with affinity ffffffff, priority 2
[0m[NR_MAC]   PUSCH Target 150, PUCCH Target 200, PUCCH Failure 10, PUSCH Failure 10
[0m[NR_PHY]   Copying 0 blacklisted PRB to L1 context
[0m[NR_MAC]   Set TX antenna number to 1, Set RX antenna number to 1 (num ssb 1: 40000000,0)
[0m[NR_MAC]   TDD period index = 6, based on the sum of dl_UL_TransmissionPeriodicity from Pattern1 (5.000000 ms) and Pattern2 (0.000000 ms): Total = 5.000000 ms
[0m[NR_MAC]   Set TDD configuration period to: 8 DL slots, 3 UL slots, 10 slots per period (NR_TDD_UL_DL_Pattern is 7 DL slots, 2 UL slots, 6 DL symbols, 4 UL symbols)
[0m[NR_MAC]   Configured 1 TDD patterns (total slots: pattern1 = 10, pattern2 = 0)
[0m[NR_PHY]   Set TDD Period Configuration: 2 periods per frame, 20 slots to be configured (8 DL, 3 UL)
[0m[NR_PHY]   TDD period configuration: slot 0 is DOWNLINK
[0m[NR_PHY]   TDD period configuration: slot 1 is DOWNLINK
[0m[NR_PHY]   TDD period configuration: slot 2 is DOWNLINK
[0m[NR_PHY]   TDD period configuration: slot 3 is DOWNLINK
[0m[NR_PHY]   TDD period configuration: slot 4 is DOWNLINK
[0m[NR_PHY]   TDD period configuration: slot 5 is DOWNLINK
[0m[NR_PHY]   TDD period configuration: slot 6 is DOWNLINK
[0m[NR_PHY]   TDD period configuration: slot 7 is FLEXIBLE: DDDDDDFFFFUUUU
[0m[NR_PHY]   TDD period configuration: slot 8 is UPLINK
[0m[NR_PHY]   TDD period configuration: slot 9 is UPLINK
[0m[NR_MAC]   Configuring analog beamforming in config_request message
[0m[PHY]   DL frequency 3619200000 Hz, UL frequency 3619200000 Hz: band 48, uldl offset 0 Hz
[0m[PHY]   Initializing frame parms for mu 1, N_RB 106, Ncp 0
[0m[PHY]   Init: N_RB_DL 106, first_carrier_offset 900, nb_prefix_samples 108,nb_prefix_samples0 132, ofdm_symbol_size 1536
[0m[NR_MAC]   Total available RO 8, num of active SSB 1: unused RO = 0 association_period 1 N_RA_sfn 1 total_prach_occasions_per_config_period 8
[0m[NR_RRC]   SIB1 freq: offsetToPointA 86
[0m[GNB_APP]   F1AP: gNB idx 0 gNB_DU_id 3584, gNB_DU_name gNB-OAI, TAC 1 MCC/MNC/length 1/1/2 cellID 12345678
[0m[GNB_APP]   ngran_DU: Configuring Cell 0 for TDD
[0m[GNB_APP]   SDAP layer is disabled
[0m[GNB_APP]   Data Radio Bearer count 1
[0m[GNB_APP]   Parsed IPv4 address for NG AMF: 192.168.70.129
[0m[UTIL]   threadCreate() for TASK_SCTP: creating thread with affinity ffffffff, priority 50
[0m[X2AP]   X2AP is disabled.
[0m[UTIL]   threadCreate() for TASK_NGAP: creating thread with affinity ffffffff, priority 50
[0m[34m[NGAP]   Starting NGAP layer
[0m[UTIL]   threadCreate() for TASK_RRC_GNB: creating thread with affinity ffffffff, priority 50
[0m[NGAP]   Registered new gNB[0] and macro gNB id 3584
[0m[NGAP]   [gNB 0] check the amf registration state
[0m[NR_RRC]   Entering main loop of NR_RRC message task
[0m[GTPU]   Configuring GTPu
[0m[GTPU]   SA mode 
[0m[GTPU]   Configuring GTPu address : 192.168.70.129, port : 2152
[0m[GTPU]   Initializing UDP for local address 192.168.70.129 with port 2152
[0m[GTPU]   Created gtpu instance id: 95
[0m[UTIL]   threadCreate() for TASK_GNB_APP: creating thread with affinity ffffffff, priority 50
[0m[NR_RRC]   Accepting new CU-UP ID 3584 name gNB-OAI (assoc_id -1)
[0m[32m[NGAP]   Send NGSetupRequest to AMF
[0m[NGAP]   3584 -> 0000e000
[0m[UTIL]   threadCreate() for TASK_GTPV1_U: creating thread with affinity ffffffff, priority 50
[0m[NR_RRC]   Received F1 Setup Request from gNB_DU 3584 (gNB-OAI) on assoc_id -1
[0m[NR_RRC]   Accepting DU 3584 (gNB-OAI), sending F1 Setup Response
[0m[NR_RRC]   DU uses RRC version 17.3.0
[0m[MAC]   received F1 Setup Response from CU (null)
[0m[MAC]   CU uses RRC version 17.3.0
[0m[MAC]   Clearing the DU's UE states before, if any.
[0m[NR_RRC]   cell PLMN 001.01 Cell ID 12345678 is in service
[0m[MAC]   received gNB-DU configuration update acknowledge
[0m[34m[NGAP]   Served GUAMIs for AMF (no name) (assoc_id=8):
[0m[34m[NGAP]    GUAMI:
[0m[34m[NGAP]      PLMN: MCC=001, MNC=01
[0m[34m[NGAP]      AMF Region ID: 202
[0m[34m[NGAP]      AMF Set ID: 1016
[0m[34m[NGAP]      AMF Pointer: 0
[0m[NGAP]   Supported PLMN 0: MCC=001 MNC=01
[0m[NGAP]   Supported slice (PLMN 0): SST=0x01 SD=123
[0m[NGAP]   Supported slice (PLMN 0): SST=0x01 SD=173451
[0m[32m[NGAP]   Received NGSetupResponse from AMF
[0m[GNB_APP]   [gNB 0] Received NGAP_REGISTER_GNB_CNF: associated AMF 1
[0m[UTIL]   threadCreate() for time source realtime: creating thread with affinity ffffffff, priority 2
[0m[UTIL]   time manager configuration: [time source: reatime] [mode: standalone] [server IP: 127.0.0.1} [server port: 7374] (server IP/port not used)
[0m[PHY]   RU clock source set as internal
[0m[PHY]   number of L1 instances 1, number of RU 1, number of CPU cores 4
[0m[PHY]   Initialized RU proc 0 (,synch_to_ext_device),
[0m[PHY]   RU thread-pool core string -1,-1 (size 2)
[0m[UTIL]   threadCreate() for Tpool0_-1: creating thread with affinity ffffffff, priority 97
[0m[UTIL]   threadCreate() for Tpool1_-1: creating thread with affinity ffffffff, priority 97
[0m[UTIL]   threadCreate() for ru_thread: creating thread with affinity ffffffff, priority 97
[0m[PHY]   Starting RU 0 (,synch_to_ext_device) on cpu 1
[0m[PHY]   Initializing frame parms for mu 1, N_RB 106, Ncp 0
[0m[PHY]   Init: N_RB_DL 106, first_carrier_offset 900, nb_prefix_samples 108,nb_prefix_samples0 132, ofdm_symbol_size 1536
[0m[PHY]   fp->scs=30000
[0m[PHY]   fp->ofdm_symbol_size=1536
[0m[PHY]   fp->nb_prefix_samples0=132
[0m[PHY]   fp->nb_prefix_samples=108
[0m[PHY]   fp->slots_per_subframe=2
[0m[PHY]   fp->samples_per_subframe_wCP=43008
[0m[PHY]   fp->samples_per_frame_wCP=430080
[0m[PHY]   fp->samples_per_subframe=46080
[0m[PHY]   fp->samples_per_frame=460800
[0m[PHY]   fp->dl_CarrierFreq=3619200000
[0m[PHY]   fp->ul_CarrierFreq=3619200000
[0m[PHY]   fp->Nid_cell=0
[0m[PHY]   fp->first_carrier_offset=900
[0m[PHY]   fp->ssb_start_subcarrier=0
[0m[PHY]   fp->Ncp=0
[0m[PHY]   fp->N_RB_DL=106
[0m[PHY]   fp->numerology_index=1
[0m[PHY]   fp->nr_band=48
[0m[PHY]   fp->ofdm_offset_divisor=8
[0m[PHY]   fp->threequarter_fs=1
[0m[PHY]   fp->sl_CarrierFreq=0
[0m[PHY]   fp->N_RB_SL=0
[0m[NR_PHY]   nb_tx_streams 1, nb_rx_streams 1, num_Beams_period 1
[0m[PHY]   Setting RF config for N_RB 106, NB_RX 1, NB_TX 1
[0m[PHY]   tune_offset 0 Hz, sample_rate 46080000 Hz
[0m[PHY]   Channel 0: setting tx_gain offset 12, tx_freq 3619200000 Hz
[0m[PHY]   Channel 0: setting rx_gain offset 102, rx_freq 3619200000 Hz
[0m[HW]   openair0_cfg[0].sdr_addrs == '(null)'
[0m[HW]   openair0_cfg[0].clock_source == '0' (internal = 0, external = 1)
[0m[HW]   UHD version 4.6.0.HEAD-0-g50fa3baa (4.6.0)
[0m[HW]   Found USRP b200
[0m[HW]   Setting clock source to internal
[0m[HW]   Setting time source to internal
[0mCMDLINE: "./nr-softmodem" "-O" "../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.usrpb210.conf" "--gNBs.[0].min_rxtxtime" "6" "-E" "--continuous-tx" "--log_config.PRACH_debug" 
[CONFIG] function config_libconfig_init returned 0
DL frequency 3619200000: band 48, UL frequency 3619200000
[HW]   cal 0: freq 3500000000.000000, offset 44.000000, diff 119200000.000000
[0m[HW]   cal 1: freq 2660000000.000000, offset 49.800000, diff 959200000.000000
[0m[HW]   cal 2: freq 2300000000.000000, offset 51.000000, diff 1319200000.000000
[0m[HW]   cal 3: freq 1880000000.000000, offset 53.000000, diff 1739200000.000000
[0m[HW]   cal 4: freq 816000000.000000, offset 57.000000, diff 2803200000.000000
[0m[HW]   RX Gain 0 102.000000 (44.000000) => 58.000000 (max 76.000000)
[0m[HW]   USRP TX_GAIN:77.75 gain_range:89.75 tx_gain:12.00
[0m[HW]   Actual master clock: 46.080000MHz...
[0m[HW]   Actual clock source internal...
[0m[HW]   Actual time source internal...
[0m[HW]   setting rx channel 0
[0m[HW]   RF board max packet size 1916, size for 100µs jitter 4608 
[0m[HW]   rx_max_num_samps 1916
[0m[HW]   RX Channel 0
[0m[HW]     Actual RX sample rate: 46.080000MSps...
[0m[HW]     Actual RX frequency: 3.619200GHz...
[0m[HW]     Actual RX gain: 58.000000...
[0m[HW]     Actual RX bandwidth: 40.000000M...
[0m[HW]     Actual RX antenna: RX2...
[0m[HW]   TX Channel 0
[0m[HW]     Actual TX sample rate: 46.080000MSps...
[0m[HW]     Actual TX frequency: 3.619200GHz...
[0m[HW]     Actual TX gain: 77.750000...
[0m[HW]     Actual TX bandwidth: 40.000000M...
[0m[HW]     Actual TX antenna: TX/RX...
[0m[HW]     Actual TX packet size: 1916
[0mUsing Device: Single USRP:
  Device: B-Series Device
  Mboard 0: B210
  RX Channel: 0
    RX DSP: 0
    RX Dboard: A
    RX Subdev: FE-RX2
  RX Channel: 1
    RX DSP: 1
    RX Dboard: A
    RX Subdev: FE-RX1
  TX Channel: 0
    TX DSP: 0
    TX Dboard: A
    TX Subdev: FE-TX2
  TX Channel: 1
    TX DSP: 1
    TX Dboard: A
    TX Subdev: FE-TX1

[HW]   Device timestamp: 1.198087...
[0m[HW]   [RAU] has loaded USRP B200 device.
[0m[PHY]   RU 0 Setting N_TA_offset to 600 samples (UL Freq 3600120, N_RB 106, mu 1)
[0m[PHY]   Signaling main thread that RU 0 is ready, sl_ahead 6
[0m[PHY]   L1 configured with analog beamforming
[0m[PHY]   Max number of concurrent beams: 1
[0m[PHY]   Attaching RU 0 antenna 0 to gNB antenna 0
[0m[UTIL]   threadCreate() for Tpool0_-1: creating thread with affinity ffffffff, priority 97
[0m[UTIL]   threadCreate() for Tpool1_-1: creating thread with affinity ffffffff, priority 97
[0m[UTIL]   threadCreate() for Tpool2_-1: creating thread with affinity ffffffff, priority 97
[0m[UTIL]   threadCreate() for Tpool3_-1: creating thread with affinity ffffffff, priority 97
[0m[UTIL]   threadCreate() for Tpool4_-1: creating thread with affinity ffffffff, priority 97
[0m[UTIL]   threadCreate() for Tpool5_-1: creating thread with affinity ffffffff, priority 97
[0m[UTIL]   threadCreate() for Tpool6_-1: creating thread with affinity ffffffff, priority 97
[0m[UTIL]   threadCreate() for Tpool7_-1: creating thread with affinity ffffffff, priority 97
[0m[UTIL]   threadCreate() for L1_rx_thread: creating thread with affinity ffffffff, priority 97
[0m[UTIL]   threadCreate() for L1_tx_thread: creating thread with affinity ffffffff, priority 97
[0m[UTIL]   threadCreate() for L1_stats: creating thread with affinity ffffffff, priority 1
[0m[PHY]   got sync (ru_thread)
[0m[PHY]   got sync (L1_stats_thread)
[0mTYPE <CTRL-C> TO TERMINATE
[HW]   current pps at 2.000000, starting streaming at 3.000000
[0m[PHY]   RU 0 rf device ready
[0m[PHY]   RU 0 RF started cpu_meas_enabled 0
[0msleep...
sleep...
sleep...
sleep...
sleep...
sleep...
sleep...
sleep...
sleep...
[NR_PHY]   [301.19] NR gNB I0 measurements: avg_I0=27 dB, prach_I0=0.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m27)
[1;31m[HW]   [recv] received 19967 samples out of 23040
[0m[1;31m[HW]   Time: 3.03043 s
ERROR_CODE_OVERFLOW (Overflow)

[0m[1;31m[PHY]   rx_rf: Asked for 23040 samples, got 19967 from USRP
[0m[1;31m[PHY]   problem receiving samples
[0m[NR_PHY]   Per-antenna avg I0: ([0m[32m[NR_PHY]   [RAPROC] 269.19 Initiating RA procedure with preamble 35, energy 55.7 dB (I0 183, thres 120), delay 30 start symbol 0 freq index 0
[0m[NR_PHY]   [269.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=22.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[32m[NR_MAC]   269.19 UE RA-RNTI 010b TC-RNTI 268c: initiating RA procedure
[0m[NR_MAC]   Frame 269, Slot 19: Prach Occasion id = 0 ssb per RO = 1.000000 number of active SSB 1 index = 0 fdm 8 symbol index 0 freq_index 0 total_RApreambles 64
[0m[NR_MAC]   UE 268c: Msg3 scheduled at 270.17 (270.7 TDA 3) start 0 RBs 8
[0m[32m[NR_MAC]   UE 268c: 270.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 35, timing_offset = 30 (estimated distance 1171.9 [m])
[0m[32m[NR_MAC]   270.7 Send RAR to RA-RNTI 010b
[0m[PHY]   [RNTI 268c] RSSI -137 dBm/RE, RSSI (digital) 13 dB (N_RB_UL 8), WBand CQI tot -18 dB, N0 Power tot 1115, RX Power tot 19
[0m[32m[NR_PHY]   [RAPROC] 270.19 Initiating RA procedure with preamble 24, energy 55.7 dB (I0 227, thres 120), delay 24 start symbol 0 freq index 0
[0m[NR_PHY]   [270.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=26.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[32m[NR_MAC]   270.19 UE RA-RNTI 010b TC-RNTI 6a97: initiating RA procedure
[0m[NR_MAC]   Frame 270, Slot 19: Prach Occasion id = 0 ssb per RO = 1.000000 number of active SSB 1 index = 0 fdm 8 symbol index 0 freq_index 0 total_RApreambles 64
[0m[NR_MAC]   UE 6a97: Msg3 scheduled at 271.17 (271.7 TDA 3) start 0 RBs 8
[0m[32m[NR_MAC]   UE 6a97: 271.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 24, timing_offset = 24 (estimated distance 937.5 [m])
[0m[32m[NR_MAC]   271.7 Send RAR to RA-RNTI 010b
[0m[NR_MAC]    27110: RA RNTI 268c CC_id 0 Scheduling retransmission of Msg3 in (271,17)
[0m[PHY]   [RNTI 268c] RSSI -136 dBm/RE, RSSI (digital) 14 dB (N_RB_UL 8), WBand CQI tot -16 dB, N0 Power tot 1013, RX Power tot 28
[0m[PHY]   [RNTI 6a97] RSSI -136 dBm/RE, RSSI (digital) 14 dB (N_RB_UL 8), WBand CQI tot -16 dB, N0 Power tot 1013, RX Power tot 28
[0m[32m[NR_PHY]   [RAPROC] 271.19 Initiating RA procedure with preamble 0, energy 54.9 dB (I0 266, thres 120), delay 17 start symbol 0 freq index 0
[0m[NR_PHY]   [271.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=29.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[32m[NR_MAC]   271.19 UE RA-RNTI 010b TC-RNTI 1cac: initiating RA procedure
[0m[NR_MAC]   Frame 271, Slot 19: Prach Occasion id = 0 ssb per RO = 1.000000 number of active SSB 1 index = 0 fdm 8 symbol index 0 freq_index 0 total_RApreambles 64
[0m[NR_MAC]   UE 1cac: Msg3 scheduled at 272.17 (272.7 TDA 3) start 0 RBs 8
[0m[32m[NR_MAC]   UE 1cac: 272.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 0, timing_offset = 17 (estimated distance 664.1 [m])
[0m[32m[NR_MAC]   272.7 Send RAR to RA-RNTI 010b
[0m[NR_MAC]    27210: RA RNTI 268c CC_id 0 Scheduling retransmission of Msg3 in (272,17)
[0m[NR_MAC]    27210: RA RNTI 6a97 CC_id 0 Scheduling retransmission of Msg3 in (272,17)
[0m[PHY]   [RNTI 268c] RSSI -136 dBm/RE, RSSI (digital) 14 dB (N_RB_UL 8), WBand CQI tot -15 dB, N0 Power tot 918, RX Power tot 28
[0m[PHY]   [RNTI 6a97] RSSI -136 dBm/RE, RSSI (digital) 14 dB (N_RB_UL 8), WBand CQI tot -15 dB, N0 Power tot 918, RX Power tot 28
[0m[PHY]   [RNTI 1cac] RSSI -136 dBm/RE, RSSI (digital) 14 dB (N_RB_UL 8), WBand CQI tot -15 dB, N0 Power tot 918, RX Power tot 28
[0m[32m[NR_PHY]   [RAPROC] 272.19 Initiating RA procedure with preamble 3, energy 54.9 dB (I0 299, thres 120), delay 6 start symbol 0 freq index 0
[0m[NR_PHY]   [272.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=32.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[32m[NR_MAC]   272.19 UE RA-RNTI 010b TC-RNTI 24d6: initiating RA procedure
[0m[NR_MAC]   Frame 272, Slot 19: Prach Occasion id = 0 ssb per RO = 1.000000 number of active SSB 1 index = 0 fdm 8 symbol index 0 freq_index 0 total_RApreambles 64
[0m[NR_MAC]   UE 24d6: Msg3 scheduled at 273.17 (273.7 TDA 3) start 0 RBs 8
[0m[32m[NR_MAC]   UE 24d6: 273.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 3, timing_offset = 6 (estimated distance 234.4 [m])
[0m[32m[NR_MAC]   273.7 Send RAR to RA-RNTI 010b
[0m[NR_MAC]    27310: RA RNTI 268c CC_id 0 Scheduling retransmission of Msg3 in (273,17)
[0m[NR_MAC]    27310: RA RNTI 6a97 CC_id 0 Scheduling retransmission of Msg3 in (273,17)
[0m[NR_MAC]    27310: RA RNTI 1cac CC_id 0 Scheduling retransmission of Msg3 in (273,17)
[0m[1;31m[NR_MAC]   UE 1cac cannot find free CCE!
[0m[NR_MAC]    27311: RA RNTI 1cac CC_id 0 Scheduling retransmission of Msg3 in (273,18)
[0m[PHY]   [RNTI 268c] RSSI -132 dBm/RE, RSSI (digital) 18 dB (N_RB_UL 8), WBand CQI tot -12 dB, N0 Power tot 988, RX Power tot 58
[0m[PHY]   [RNTI 6a97] RSSI -132 dBm/RE, RSSI (digital) 18 dB (N_RB_UL 8), WBand CQI tot -12 dB, N0 Power tot 988, RX Power tot 58
[0m[PHY]   [RNTI 24d6] RSSI -132 dBm/RE, RSSI (digital) 18 dB (N_RB_UL 8), WBand CQI tot -12 dB, N0 Power tot 988, RX Power tot 58
[0m[93m[NR_MAC]   UE 268c RA failed at state WAIT_Msg3 (Reached msg3 max harq rounds)
[0m[NR_MAC]   Remove NR rnti 0x268c
[0m[PHY]   [RNTI 1cac] RSSI -135 dBm/RE, RSSI (digital) 15 dB (N_RB_UL 8), WBand CQI tot -15 dB, N0 Power tot 988, RX Power tot 29
[0m[32m[NR_PHY]   [RAPROC] 273.19 Initiating RA procedure with preamble 6, energy 56.4 dB (I0 328, thres 120), delay 0 start symbol 0 freq index 0
[0m[NR_PHY]   [273.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=35.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[32m[NR_MAC]   273.19 UE RA-RNTI 010b TC-RNTI 8269: initiating RA procedure
[0m[NR_MAC]   Frame 273, Slot 19: Prach Occasion id = 0 ssb per RO = 1.000000 number of active SSB 1 index = 0 fdm 8 symbol index 0 freq_index 0 total_RApreambles 64
[0m[NR_MAC]   UE 8269: Msg3 scheduled at 274.17 (274.7 TDA 3) start 0 RBs 8
[0m[32m[NR_MAC]   UE 8269: 274.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 6, timing_offset = 0 (estimated distance 0.0 [m])
[0m[32m[NR_MAC]   274.7 Send RAR to RA-RNTI 010b
[0m[NR_MAC]    27410: RA RNTI 6a97 CC_id 0 Scheduling retransmission of Msg3 in (274,17)
[0m[NR_MAC]    27410: RA RNTI 1cac CC_id 0 Scheduling retransmission of Msg3 in (274,17)
[0m[NR_MAC]    27410: RA RNTI 24d6 CC_id 0 Scheduling retransmission of Msg3 in (274,17)
[0m[1;31m[NR_MAC]   UE 24d6 cannot find free CCE!
[0m[NR_MAC]    27411: RA RNTI 24d6 CC_id 0 Scheduling retransmission of Msg3 in (274,18)
[0m[PHY]   [RNTI 6a97] RSSI -136 dBm/RE, RSSI (digital) 14 dB (N_RB_UL 8), WBand CQI tot -16 dB, N0 Power tot 987, RX Power tot 24
[0m[PHY]   [RNTI 1cac] RSSI -136 dBm/RE, RSSI (digital) 14 dB (N_RB_UL 8), WBand CQI tot -16 dB, N0 Power tot 987, RX Power tot 24
[0m[PHY]   [RNTI 8269] RSSI -136 dBm/RE, RSSI (digital) 14 dB (N_RB_UL 8), WBand CQI tot -16 dB, N0 Power tot 987, RX Power tot 24
[0m[93m[NR_MAC]   UE 6a97 RA failed at state WAIT_Msg3 (Reached msg3 max harq rounds)
[0m[NR_MAC]   Remove NR rnti 0x6a97
[0m[PHY]   [RNTI 24d6] RSSI -134 dBm/RE, RSSI (digital) 16 dB (N_RB_UL 8), WBand CQI tot -14 dB, N0 Power tot 987, RX Power tot 39
[0m[32m[NR_PHY]   [RAPROC] 274.19 Initiating RA procedure with preamble 27, energy 55.7 dB (I0 356, thres 120), delay 17 start symbol 0 freq index 0
[0m[NR_PHY]   [274.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=37.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[32m[NR_MAC]   274.19 UE RA-RNTI 010b TC-RNTI 76d2: initiating RA procedure
[0m[NR_MAC]   Frame 274, Slot 19: Prach Occasion id = 0 ssb per RO = 1.000000 number of active SSB 1 index = 0 fdm 8 symbol index 0 freq_index 0 total_RApreambles 64
[0m[NR_MAC]   UE 76d2: Msg3 scheduled at 275.17 (275.7 TDA 3) start 0 RBs 8
[0m[32m[NR_MAC]   UE 76d2: 275.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 27, timing_offset = 17 (estimated distance 664.1 [m])
[0m[32m[NR_MAC]   275.7 Send RAR to RA-RNTI 010b
[0m[NR_MAC]    27510: RA RNTI 1cac CC_id 0 Scheduling retransmission of Msg3 in (275,17)
[0m[NR_MAC]    27510: RA RNTI 24d6 CC_id 0 Scheduling retransmission of Msg3 in (275,17)
[0m[NR_MAC]    27510: RA RNTI 8269 CC_id 0 Scheduling retransmission of Msg3 in (275,17)
[0m[1;31m[NR_MAC]   UE 8269 cannot find free CCE!
[0m[NR_MAC]    27511: RA RNTI 8269 CC_id 0 Scheduling retransmission of Msg3 in (275,18)
[0m[PHY]   [RNTI 1cac] RSSI -133 dBm/RE, RSSI (digital) 17 dB (N_RB_UL 8), WBand CQI tot -13 dB, N0 Power tot 952, RX Power tot 51
[0m[PHY]   [RNTI 24d6] RSSI -133 dBm/RE, RSSI (digital) 17 dB (N_RB_UL 8), WBand CQI tot -13 dB, N0 Power tot 952, RX Power tot 51
[0m[PHY]   [RNTI 76d2] RSSI -133 dBm/RE, RSSI (digital) 17 dB (N_RB_UL 8), WBand CQI tot -13 dB, N0 Power tot 952, RX Power tot 51
[0m[93m[NR_MAC]   UE 1cac RA failed at state WAIT_Msg3 (Reached msg3 max harq rounds)
[0m[NR_MAC]   Remove NR rnti 0x1cac
[0m[PHY]   [RNTI 8269] RSSI -135 dBm/RE, RSSI (digital) 15 dB (N_RB_UL 8), WBand CQI tot -15 dB, N0 Power tot 952, RX Power tot 32
[0m[32m[NR_PHY]   [RAPROC] 275.19 Initiating RA procedure with preamble 28, energy 55.7 dB (I0 379, thres 120), delay 12 start symbol 0 freq index 0
[0m[NR_PHY]   [275.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=40.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[32m[NR_MAC]   275.19 UE RA-RNTI 010b TC-RNTI 4582: initiating RA procedure
[0m[NR_MAC]   Frame 275, Slot 19: Prach Occasion id = 0 ssb per RO = 1.000000 number of active SSB 1 index = 0 fdm 8 symbol index 0 freq_index 0 total_RApreambles 64
[0m[NR_MAC]   UE 4582: Msg3 scheduled at 276.17 (276.7 TDA 3) start 0 RBs 8
[0m[32m[NR_MAC]   UE 4582: 276.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 28, timing_offset = 12 (estimated distance 468.8 [m])
[0m[32m[NR_MAC]   276.7 Send RAR to RA-RNTI 010b
[0m[NR_MAC]    27610: RA RNTI 24d6 CC_id 0 Scheduling retransmission of Msg3 in (276,17)
[0m[NR_MAC]    27610: RA RNTI 8269 CC_id 0 Scheduling retransmission of Msg3 in (276,17)
[0m[NR_MAC]    27610: RA RNTI 76d2 CC_id 0 Scheduling retransmission of Msg3 in (276,17)
[0m[1;31m[NR_MAC]   UE 76d2 cannot find free CCE!
[0m[NR_MAC]    27611: RA RNTI 76d2 CC_id 0 Scheduling retransmission of Msg3 in (276,18)
[0m[PHY]   [RNTI 24d6] RSSI -135 dBm/RE, RSSI (digital) 15 dB (N_RB_UL 8), WBand CQI tot -15 dB, N0 Power tot 1058, RX Power tot 34
[0m[PHY]   [RNTI 8269] RSSI -135 dBm/RE, RSSI (digital) 15 dB (N_RB_UL 8), WBand CQI tot -15 dB, N0 Power tot 1058, RX Power tot 34
[0m[PHY]   [RNTI 4582] RSSI -135 dBm/RE, RSSI (digital) 15 dB (N_RB_UL 8), WBand CQI tot -15 dB, N0 Power tot 1058, RX Power tot 34
[0m[93m[NR_MAC]   UE 24d6 RA failed at state WAIT_Msg3 (Reached msg3 max harq rounds)
[0m[NR_MAC]   Remove NR rnti 0x24d6
[0m[PHY]   [RNTI 76d2] RSSI -136 dBm/RE, RSSI (digital) 14 dB (N_RB_UL 8), WBand CQI tot -16 dB, N0 Power tot 1058, RX Power tot 26
[0m[32m[NR_PHY]   [RAPROC] 276.19 Initiating RA procedure with preamble 13, energy 55.7 dB (I0 400, thres 120), delay 19 start symbol 0 freq index 0
[0m[NR_PHY]   [276.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=41.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[32m[NR_MAC]   276.19 UE RA-RNTI 010b TC-RNTI feb7: initiating RA procedure
[0m[NR_MAC]   Frame 276, Slot 19: Prach Occasion id = 0 ssb per RO = 1.000000 number of active SSB 1 index = 0 fdm 8 symbol index 0 freq_index 0 total_RApreambles 64
[0m[NR_MAC]   UE feb7: Msg3 scheduled at 277.17 (277.7 TDA 3) start 0 RBs 8
[0m[32m[NR_MAC]   UE feb7: 277.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 13, timing_offset = 19 (estimated distance 742.2 [m])
[0m[32m[NR_MAC]   277.7 Send RAR to RA-RNTI 010b
[0m[NR_MAC]    27710: RA RNTI 8269 CC_id 0 Scheduling retransmission of Msg3 in (277,17)
[0m[NR_MAC]    27710: RA RNTI 76d2 CC_id 0 Scheduling retransmission of Msg3 in (277,17)
[0m[NR_MAC]    27710: RA RNTI 4582 CC_id 0 Scheduling retransmission of Msg3 in (277,17)
[0m[1;31m[NR_MAC]   UE 4582 cannot find free CCE!
[0m[NR_MAC]    27711: RA RNTI 4582 CC_id 0 Scheduling retransmission of Msg3 in (277,18)
[0m[PHY]   [RNTI 8269] RSSI -136 dBm/RE, RSSI (digital) 14 dB (N_RB_UL 8), WBand CQI tot -15 dB, N0 Power tot 932, RX Power tot 27
[0m[PHY]   [RNTI 76d2] RSSI -136 dBm/RE, RSSI (digital) 14 dB (N_RB_UL 8), WBand CQI tot -15 dB, N0 Power tot 932, RX Power tot 27
[0m[PHY]   [RNTI feb7] RSSI -136 dBm/RE, RSSI (digital) 14 dB (N_RB_UL 8), WBand CQI tot -15 dB, N0 Power tot 932, RX Power tot 27
[0m[93m[NR_MAC]   UE 8269 RA failed at state WAIT_Msg3 (Reached msg3 max harq rounds)
[0m[NR_MAC]   Remove NR rnti 0x8269
[0m[PHY]   [RNTI 4582] RSSI -134 dBm/RE, RSSI (digital) 16 dB (N_RB_UL 8), WBand CQI tot -14 dB, N0 Power tot 932, RX Power tot 38
[0m[32m[NR_PHY]   [RAPROC] 277.19 Initiating RA procedure with preamble 23, energy 55.7 dB (I0 418, thres 120), delay 5 start symbol 0 freq index 0
[0m[NR_PHY]   [277.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=43.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[32m[NR_MAC]   277.19 UE RA-RNTI 010b TC-RNTI 52f6: initiating RA procedure
[0m[NR_MAC]   Frame 277, Slot 19: Prach Occasion id = 0 ssb per RO = 1.000000 number of active SSB 1 index = 0 fdm 8 symbol index 0 freq_index 0 total_RApreambles 64
[0m[NR_MAC]   UE 52f6: Msg3 scheduled at 278.17 (278.7 TDA 3) start 0 RBs 8
[0m[32m[NR_MAC]   UE 52f6: 278.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 23, timing_offset = 5 (estimated distance 195.3 [m])
[0m[32m[NR_MAC]   278.7 Send RAR to RA-RNTI 010b
[0m[NR_MAC]    27810: RA RNTI 76d2 CC_id 0 Scheduling retransmission of Msg3 in (278,17)
[0m[NR_MAC]    27810: RA RNTI 4582 CC_id 0 Scheduling retransmission of Msg3 in (278,17)
[0m[NR_MAC]    27810: RA RNTI feb7 CC_id 0 Scheduling retransmission of Msg3 in (278,17)
[0m[1;31m[NR_MAC]   UE feb7 cannot find free CCE!
[0m[NR_MAC]    27811: RA RNTI feb7 CC_id 0 Scheduling retransmission of Msg3 in (278,18)
[0m[PHY]   [RNTI 76d2] RSSI -137 dBm/RE, RSSI (digital) 13 dB (N_RB_UL 8), WBand CQI tot -18 dB, N0 Power tot 1035, RX Power tot 18
[0m[PHY]   [RNTI 4582] RSSI -137 dBm/RE, RSSI (digital) 13 dB (N_RB_UL 8), WBand CQI tot -18 dB, N0 Power tot 1035, RX Power tot 18
[0m[PHY]   [RNTI 52f6] RSSI -137 dBm/RE, RSSI (digital) 13 dB (N_RB_UL 8), WBand CQI tot -18 dB, N0 Power tot 1035, RX Power tot 18
[0m[93m[NR_MAC]   UE 76d2 RA failed at state WAIT_Msg3 (Reached msg3 max harq rounds)
[0m[NR_MAC]   Remove NR rnti 0x76d2
[0m[PHY]   [RNTI feb7] RSSI -133 dBm/RE, RSSI (digital) 17 dB (N_RB_UL 8), WBand CQI tot -13 dB, N0 Power tot 1035, RX Power tot 54
[0m[32m[NR_PHY]   [RAPROC] 278.19 Initiating RA procedure with preamble 2, energy 55.7 dB (I0 434, thres 120), delay 3 start symbol 0 freq index 0
[0m[NR_PHY]   [278.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=44.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[32m[NR_MAC]   278.19 UE RA-RNTI 010b TC-RNTI 5f7c: initiating RA procedure
[0m[NR_MAC]   Frame 278, Slot 19: Prach Occasion id = 0 ssb per RO = 1.000000 number of active SSB 1 index = 0 fdm 8 symbol index 0 freq_index 0 total_RApreambles 64
[0m[NR_MAC]   UE 5f7c: Msg3 scheduled at 279.17 (279.7 TDA 3) start 0 RBs 8
[0m[32m[NR_MAC]   UE 5f7c: 279.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 2, timing_offset = 3 (estimated distance 117.2 [m])
[0m[32m[NR_MAC]   279.7 Send RAR to RA-RNTI 010b
[0m[NR_MAC]    27910: RA RNTI 4582 CC_id 0 Scheduling retransmission of Msg3 in (279,17)
[0m[NR_MAC]    27910: RA RNTI feb7 CC_id 0 Scheduling retransmission of Msg3 in (279,17)
[0m[NR_MAC]    27910: RA RNTI 52f6 CC_id 0 Scheduling retransmission of Msg3 in (279,17)
[0m[1;31m[NR_MAC]   UE 52f6 cannot find free CCE!
[0m[NR_MAC]    27911: RA RNTI 52f6 CC_id 0 Scheduling retransmission of Msg3 in (279,18)
[0m[PHY]   [RNTI 4582] RSSI -135 dBm/RE, RSSI (digital) 15 dB (N_RB_UL 8), WBand CQI tot -16 dB, N0 Power tot 1171, RX Power tot 32
[0m[PHY]   [RNTI feb7] RSSI -135 dBm/RE, RSSI (digital) 15 dB (N_RB_UL 8), WBand CQI tot -16 dB, N0 Power tot 1171, RX Power tot 32
[0m[PHY]   [RNTI 5f7c] RSSI -135 dBm/RE, RSSI (digital) 15 dB (N_RB_UL 8), WBand CQI tot -16 dB, N0 Power tot 1171, RX Power tot 32
[0m[93m[NR_MAC]   UE 4582 RA failed at state WAIT_Msg3 (Reached msg3 max harq rounds)
[0m[NR_MAC]   Remove NR rnti 0x4582
[0m[PHY]   [RNTI 52f6] RSSI -133 dBm/RE, RSSI (digital) 17 dB (N_RB_UL 8), WBand CQI tot -14 dB, N0 Power tot 1171, RX Power tot 47
[0m[NR_PHY]   [279.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=46.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_MAC]    28010: RA RNTI feb7 CC_id 0 Scheduling retransmission of Msg3 in (280,17)
[0m[NR_MAC]    28010: RA RNTI 52f6 CC_id 0 Scheduling retransmission of Msg3 in (280,17)
[0m[NR_MAC]    28010: RA RNTI 5f7c CC_id 0 Scheduling retransmission of Msg3 in (280,17)
[0m[1;31m[NR_MAC]   UE 5f7c cannot find free CCE!
[0m[NR_MAC]    28011: RA RNTI 5f7c CC_id 0 Scheduling retransmission of Msg3 in (280,18)
[0m[PHY]   [RNTI feb7] RSSI -134 dBm/RE, RSSI (digital) 16 dB (N_RB_UL 8), WBand CQI tot -14 dB, N0 Power tot 1034, RX Power tot 36
[0m[PHY]   [RNTI 52f6] RSSI -134 dBm/RE, RSSI (digital) 16 dB (N_RB_UL 8), WBand CQI tot -14 dB, N0 Power tot 1034, RX Power tot 36
[0m[93m[NR_MAC]   UE feb7 RA failed at state WAIT_Msg3 (Reached msg3 max harq rounds)
[0m[NR_MAC]   Remove NR rnti 0xfeb7
[0m[PHY]   [RNTI 5f7c] RSSI -133 dBm/RE, RSSI (digital) 17 dB (N_RB_UL 8), WBand CQI tot -13 dB, N0 Power tot 1034, RX Power tot 54
[0m[NR_PHY]   [280.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=47.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_MAC]    28110: RA RNTI 52f6 CC_id 0 Scheduling retransmission of Msg3 in (281,17)
[0m[NR_MAC]    28110: RA RNTI 5f7c CC_id 0 Scheduling retransmission of Msg3 in (281,17)
[0m[PHY]   [RNTI 52f6] RSSI -137 dBm/RE, RSSI (digital) 13 dB (N_RB_UL 8), WBand CQI tot -17 dB, N0 Power tot 1016, RX Power tot 21
[0m[PHY]   [RNTI 5f7c] RSSI -137 dBm/RE, RSSI (digital) 13 dB (N_RB_UL 8), WBand CQI tot -17 dB, N0 Power tot 1016, RX Power tot 21
[0m[93m[NR_MAC]   UE 52f6 RA failed at state WAIT_Msg3 (Reached msg3 max harq rounds)
[0m[NR_MAC]   Remove NR rnti 0x52f6
[0m[NR_PHY]   [281.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=48.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_MAC]    28210: RA RNTI 5f7c CC_id 0 Scheduling retransmission of Msg3 in (282,17)
[0m[PHY]   [RNTI 5f7c] RSSI -134 dBm/RE, RSSI (digital) 16 dB (N_RB_UL 8), WBand CQI tot -15 dB, N0 Power tot 1125, RX Power tot 37
[0m[93m[NR_MAC]   UE 5f7c RA failed at state WAIT_Msg3 (Reached msg3 max harq rounds)
[0m[NR_MAC]   Remove NR rnti 0x5f7c
[0m[NR_PHY]   [282.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=48.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [283.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=49.5 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [284.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=50.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [285.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=50.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [286.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=51.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [287.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=51.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [288.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=52.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [289.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=52.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [290.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=52.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [291.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=53.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [292.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=53.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [293.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=53.5 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [294.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=53.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [295.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=53.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [296.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [297.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [298.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [299.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [300.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [301.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.5 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [302.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [303.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [304.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [305.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [306.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [307.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [308.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [309.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [310.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [311.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [312.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [313.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [314.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [315.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [316.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [317.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [318.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [319.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [320.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [321.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [322.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [323.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [324.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [325.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [326.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [327.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.5 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [328.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [329.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [330.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [331.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [332.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [333.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [334.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [335.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [336.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [337.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [338.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [339.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [340.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [341.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [342.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [343.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [344.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [345.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [346.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [347.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [348.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [349.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [350.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [351.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [352.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [353.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [354.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [355.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [356.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [357.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [358.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [359.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [360.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [361.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [362.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [363.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [364.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [365.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.5 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [366.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [367.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [368.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [369.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [370.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [371.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [372.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [373.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [374.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [375.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [376.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [377.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [378.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [379.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [380.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [381.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [382.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_MAC]   Frame.Slot 384.0

[0m[NR_PHY]   [383.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [384.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [385.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [386.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [387.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [388.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [389.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [390.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [391.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [392.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [393.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [394.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [395.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [396.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [397.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [398.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [399.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [400.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [401.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [402.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [403.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [404.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [405.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [406.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [407.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [408.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [409.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [410.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [411.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [412.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [413.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [414.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [415.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [416.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [417.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [418.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [419.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [420.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [421.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [422.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [423.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [424.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [425.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [426.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [427.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [428.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [429.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [430.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [431.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [432.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [433.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [434.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [435.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [436.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [437.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [438.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [439.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [440.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [441.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [442.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [443.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [444.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [445.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [446.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [447.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [448.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [449.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [450.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [451.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [452.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [453.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [454.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [455.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [456.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [457.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [458.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [459.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [460.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [461.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [462.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [463.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [464.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [465.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [466.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [467.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [468.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [469.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [470.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [471.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [472.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [473.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [474.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [475.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [476.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [477.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [478.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [479.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [480.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [481.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [482.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [483.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [484.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [485.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [486.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [487.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [488.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [489.19] NR gNB I0 measurements: avg_I0=60 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [490.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [491.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [492.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [493.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [494.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [495.19] NR gNB I0 measurements: avg_I0=60 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [496.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [497.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [498.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [499.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [500.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [501.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [502.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [503.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [504.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [505.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [506.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [507.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [508.19] NR gNB I0 measurements: avg_I0=60 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [509.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [510.19] NR gNB I0 measurements: avg_I0=60 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_MAC]   Frame.Slot 512.0

[0m[NR_PHY]   [511.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [512.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [513.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [514.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [515.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [516.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [517.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [518.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [519.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [520.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [521.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [522.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [523.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [524.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [525.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [526.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [527.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [528.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [529.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [530.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [531.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [532.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [533.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [534.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [535.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [536.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [537.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [538.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [539.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [540.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [541.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [542.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [543.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [544.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [545.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [546.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [547.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [548.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [549.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [550.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [551.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [552.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [553.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [554.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [555.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [556.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [557.19] NR gNB I0 measurements: avg_I0=27 dB, prach_I0=50.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [558.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=51.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [559.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=51.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [560.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=52.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [561.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=52.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [562.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=52.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [563.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=53.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [564.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=53.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [565.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=53.5 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [566.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=53.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [567.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=53.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [568.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=53.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [569.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [570.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [571.19] NR gNB I0 measurements: avg_I0=27 dB, prach_I0=49.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [572.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=50.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [573.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=50.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [574.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=51.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [575.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=51.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [576.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=52.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [577.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=52.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [578.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=52.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [579.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=52.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [580.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=53.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [581.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=53.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [582.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=53.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [583.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=53.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [584.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=53.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [585.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [586.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [587.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [588.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [589.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.5 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [590.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.6 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [591.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [592.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [593.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [594.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [595.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [596.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [597.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [598.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [599.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [600.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [601.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [602.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [603.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [604.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [605.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [606.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [607.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [608.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [609.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [610.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [611.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [612.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [613.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [614.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [615.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [616.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [617.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [618.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [619.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [620.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [621.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [622.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [623.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [624.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [625.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [626.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [627.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [628.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [629.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [630.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [631.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [632.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [633.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [634.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [635.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [636.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [637.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [638.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_MAC]   Frame.Slot 640.0

[0m[NR_PHY]   [639.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [640.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [641.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [642.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [643.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [644.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [645.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [646.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [647.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [648.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [649.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [650.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [651.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [652.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [653.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [654.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [655.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [656.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [657.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [658.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [659.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [660.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [661.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [662.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [663.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m30)
27)
27)
27)
27)
27)
29)
29)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
29)
29)
27)
27)
27)
27)
27)
29)
29)
29)
29)
30)
29)
29)
29)
29)
30)
30)
29)
30)
30)
27)
27)
27)
27)
29)
29)
30)
27)
27)
29)
27)
30)
29)
29)
30)
29)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
24)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
27)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
60)
61)
61)
61)
61)
61)
60)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
60)
61)
60)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
27)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
27)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
[NR_PHY]   [664.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [665.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [666.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [667.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [668.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [669.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [670.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [671.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [672.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [673.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [674.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [675.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [676.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [677.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [678.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [679.19] NR gNB I0 measurements: avg_I0=60 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [680.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [681.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [682.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [683.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [684.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [685.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [686.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [687.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [688.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [689.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [690.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [691.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [692.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [693.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [694.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [695.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [696.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [697.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [698.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [699.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [700.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [701.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [702.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [703.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [704.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [705.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [706.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [707.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [708.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [709.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [710.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [711.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [712.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [713.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [714.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [715.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [716.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [717.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [718.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [719.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [720.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [721.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [722.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [723.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [724.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [725.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [726.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [727.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [728.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [729.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [730.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [731.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [732.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [733.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [734.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [735.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [736.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [737.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [738.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [739.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [740.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [741.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [742.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [743.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [744.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [745.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [746.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [747.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [748.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [749.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [750.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [751.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [752.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [753.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [754.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [755.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [756.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [757.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [758.19] NR gNB I0 measurements: avg_I0=60 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [759.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [760.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [761.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [762.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [763.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [764.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [765.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [766.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_MAC]   Frame.Slot 768.0

[0m[NR_PHY]   [767.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [768.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [769.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [770.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [771.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [772.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [773.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [774.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [775.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [776.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [777.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [778.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [779.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [780.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [781.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [782.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [783.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [784.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [785.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [786.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [787.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [788.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [789.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [790.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [791.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [792.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [793.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [794.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [795.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [796.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [797.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [798.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [799.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [800.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [801.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [802.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [803.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [804.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [805.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [806.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [807.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [808.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [809.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [810.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [811.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [812.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [813.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [814.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [815.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [816.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [817.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [818.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [819.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [820.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [821.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [822.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [823.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [824.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [825.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [826.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [827.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [828.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [829.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [830.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [831.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [832.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [833.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [834.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [835.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [836.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [837.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [838.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [839.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [840.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [841.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [842.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [843.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [844.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [845.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [846.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [847.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [848.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [849.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [850.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [851.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [852.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [853.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [854.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [855.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [856.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [857.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [858.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [859.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [860.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [861.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [862.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [863.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [864.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [865.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [866.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [867.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [868.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [869.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [870.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.7 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [871.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.8 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [872.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [873.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [874.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [875.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [876.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [877.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [878.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [879.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [880.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [881.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [882.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [883.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [884.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [885.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [886.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [887.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [888.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [889.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [890.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [891.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [892.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [893.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [894.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_MAC]   Frame.Slot 896.0

[0m[NR_PHY]   [895.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [896.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [897.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [898.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [899.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [900.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [901.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [902.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [903.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [904.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [905.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [906.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [907.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [908.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [909.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [910.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [911.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [912.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [913.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [914.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [915.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [916.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [917.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
60)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
60)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
[NR_PHY]   [918.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m61)
[NR_PHY]   [919.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m61)
[NR_PHY]   [920.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m61)
[NR_PHY]   [921.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m61)
[NR_PHY]   [922.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [923.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [924.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [925.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [926.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [927.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [928.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [929.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [930.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [931.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [932.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [933.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [934.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [935.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [936.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [937.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [938.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [939.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [940.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [941.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [942.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [943.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [944.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [945.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [946.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [947.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [948.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [949.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [950.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [951.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=54.9 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [952.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [953.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [954.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [955.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [956.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [957.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [958.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [959.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [960.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [961.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [962.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [963.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [964.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [965.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [966.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [967.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [968.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [969.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [970.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [971.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [972.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [973.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [974.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [975.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [976.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [977.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [978.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [979.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [980.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [981.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [982.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [983.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [984.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [985.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [986.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [987.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [988.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [989.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [990.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [991.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [992.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [993.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [994.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [995.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [996.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [997.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [998.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [999.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1000.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1001.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1002.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1003.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1004.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1005.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1006.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1007.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1008.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1009.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1010.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1011.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1012.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1013.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1014.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1015.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1016.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1017.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1018.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1019.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1020.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1021.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1022.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_MAC]   Frame.Slot 0.0

[0m[NR_PHY]   [1023.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[PHY]   prach_I0 = 55.3 dB
[0m[NR_PHY]   [0.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [1.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [2.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [3.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [4.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [5.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [6.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [7.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [8.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [9.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [10.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [11.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [12.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [13.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [14.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [15.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [16.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [17.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [18.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [19.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [20.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [21.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [22.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [23.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [24.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [25.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [26.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [27.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [28.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [29.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [30.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [31.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [32.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [33.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [34.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [35.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [36.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [37.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [38.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [39.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [40.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [41.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [42.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [43.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [44.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [45.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [46.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [47.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [48.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [49.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [50.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [51.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [52.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [53.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [54.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [55.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [56.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [57.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [58.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [59.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [60.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [61.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [62.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [63.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [64.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [65.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [66.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [67.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [68.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [69.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [70.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [71.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [72.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [73.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [74.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [75.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [76.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [77.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [78.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [79.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [80.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [81.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [82.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [83.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [84.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [85.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [86.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [87.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [88.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [89.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [90.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [91.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [92.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [93.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [94.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [95.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [96.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [97.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [98.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [99.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [100.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [101.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [102.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [103.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [104.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [105.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [106.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [107.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [108.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [109.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [110.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [111.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [112.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [113.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [114.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [115.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [116.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [117.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [118.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [119.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [120.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [121.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [122.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [123.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [124.19] NR gNB I0 measurements: avg_I0=60 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [125.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [126.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_MAC]   Frame.Slot 128.0

[0m[NR_PHY]   [127.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [128.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [129.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [130.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [131.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [132.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [133.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [134.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [135.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [136.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [137.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [138.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [139.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [140.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [141.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [142.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [143.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [144.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [145.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [146.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [147.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [148.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [149.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [150.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [151.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [152.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [153.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [154.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [155.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [156.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [157.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [158.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [159.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [160.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [161.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [162.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [163.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [164.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [165.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [166.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [167.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [168.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [169.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [170.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [171.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [172.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [173.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [174.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [175.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [176.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [177.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [178.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [179.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [180.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [181.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [182.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [183.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [184.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [185.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [186.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [187.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [188.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [189.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [190.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [191.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [192.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [193.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [194.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [195.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [196.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [197.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [198.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [199.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [200.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [201.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [202.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [203.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [204.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [205.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [206.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [207.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [208.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [209.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [210.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [211.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [212.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [213.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [214.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [215.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [216.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [217.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [218.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [219.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [220.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [221.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [222.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [223.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [224.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [225.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [226.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [227.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [228.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [229.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [230.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [231.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [232.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [233.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [234.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [235.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [236.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [237.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [238.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [239.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [240.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [241.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [242.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [243.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [244.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [245.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [246.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [247.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [248.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [249.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [250.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [251.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [252.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [253.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [254.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_MAC]   Frame.Slot 256.0

[0m[NR_PHY]   [255.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [256.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [257.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [258.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [259.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [260.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [261.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [262.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [263.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [264.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [265.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [266.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [267.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [268.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [269.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [270.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [271.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [272.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [273.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [274.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [275.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [276.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [277.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [278.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [279.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [280.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [281.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [282.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [283.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [284.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [285.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [286.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [287.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [288.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [289.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [290.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [291.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [292.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [293.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [294.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [295.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [296.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [297.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [298.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [299.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [300.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [301.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [302.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [303.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [304.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [305.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [306.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [307.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [308.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [309.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [310.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [311.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [312.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [313.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [314.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [315.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [316.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [317.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [318.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [319.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [320.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [321.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [322.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [323.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [324.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [325.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [326.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [327.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [328.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [329.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [330.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [331.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [332.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [333.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [334.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [335.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [336.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [337.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [338.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [339.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [340.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [341.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [342.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [343.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [344.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [345.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [346.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [347.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [348.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [349.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [350.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [351.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [352.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [353.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [354.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [355.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [356.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [357.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [358.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [359.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [360.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [361.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [362.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [363.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [364.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [365.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [366.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [367.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [368.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [369.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [370.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [371.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [372.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [373.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [374.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [375.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [376.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [377.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [378.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [379.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [380.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [381.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [382.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_MAC]   Frame.Slot 384.0

[0m[NR_PHY]   [383.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [384.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [385.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [386.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [387.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [388.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [389.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [390.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [391.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [392.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [393.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [394.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [395.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [396.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [397.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [398.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [399.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [400.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [401.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [402.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [403.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [404.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [405.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [406.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [407.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [408.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [409.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [410.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [411.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [412.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [413.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [414.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [415.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [416.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [417.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [418.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [419.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [420.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [421.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [422.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [423.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [424.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [425.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [426.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [427.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [428.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [429.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [430.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [431.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [432.19] NR gNB I0 measurements: avg_I0=60 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [433.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [434.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [435.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [436.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [437.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [438.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [439.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [440.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [441.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [442.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [443.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [444.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [445.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [446.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [447.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [448.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [449.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [450.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [451.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [452.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [453.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [454.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [455.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [456.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [457.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [458.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [459.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [460.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [461.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [462.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [463.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [464.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [465.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [466.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [467.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [468.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [469.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [470.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [471.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [472.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [473.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [474.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [475.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [476.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [477.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [478.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [479.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [480.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [481.19] NR gNB I0 measurements: avg_I0=60 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [482.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [483.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [484.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [485.19] NR gNB I0 measurements: avg_I0=60 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [486.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [487.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [488.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [489.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [490.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [491.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [492.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [493.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [494.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [495.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [496.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [497.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [498.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [499.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [500.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [501.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [502.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [503.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [504.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [505.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [506.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [507.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [508.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [509.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [510.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_MAC]   Frame.Slot 512.0

[0m[NR_PHY]   [511.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [512.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [513.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [514.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [515.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [516.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [517.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [518.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [519.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [520.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [521.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.3 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [522.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.4 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [523.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.2 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [524.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [525.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [526.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [527.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [528.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [529.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [530.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [531.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [532.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.1 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [533.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [534.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [535.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m[NR_PHY]   [536.19] NR gNB I0 measurements: avg_I0=61 dB, prach_I0=55.0 dB, measured_PRBs=105
[0m[NR_PHY]   Per-antenna avg I0: ([0m
** Caught SIGTERM, shutting down
[GNB_APP]   stopping nr-softmodem
[0m[PHY]   Killing gNB 0 processing threads
[0m61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
60)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
60)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
60)
61)
61)
61)
60)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
61)
Returned from ITTI signal handler

** Caught SIGTERM, shutting down

** Caught SIGTERM, shutting down
[PHY]   Stopping RU 0 processing threads
[0m[HW]   releasing USRP
[0m
** Caught SIGTERM, shutting down
[PHY]   RU 0 RF device stopped
[0mBye.
