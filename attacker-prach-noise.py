
import re
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
import numpy as np
import statistics

# 設定中文字體支援
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']  # 設定字體優先順序
plt.rcParams['axes.unicode_minus'] = False  # 正確顯示負號

log_data = """
[PHY]   [RAPROC] 0.19 prach_I0 = 18.9 dB
[PHY]   [RAPROC] 1.19 prach_I0 = 19.0 dB
[PHY]   [RAPROC] 2.19 prach_I0 = 18.9 dB
[PHY]   [RAPROC] 3.19 prach_I0 = 18.9 dB
[PHY]   [RAPROC] 4.19 prach_I0 = 18.9 dB
[PHY]   [RAPROC] 5.19 prach_I0 = 19.3 dB
[PHY]   [RAPROC] 6.19 prach_I0 = 19.2 dB
[PHY]   [RAPROC] 7.19 prach_I0 = 19.4 dB
[PHY]   [RAPROC] 8.19 prach_I0 = 19.2 dB
[PHY]   [RAPROC] 9.19 prach_I0 = 19.2 dB
[PHY]   [RAPROC] 10.19 prach_I0 = 19.1 dB
[PHY]   [RAPROC] 11.19 prach_I0 = 19.2 dB
[PHY]   [RAPROC] 12.19 prach_I0 = 19.7 dB
[PHY]   [RAPROC] 13.19 prach_I0 = 19.9 dB
[PHY]   [RAPROC] 14.19 prach_I0 = 19.6 dB
[PHY]   [RAPROC] 15.19 prach_I0 = 19.9 dB
[PHY]   [RAPROC] 16.19 prach_I0 = 19.8 dB
[PHY]   [RAPROC] 17.19 prach_I0 = 19.7 dB
[PHY]   [RAPROC] 18.19 prach_I0 = 19.7 dB
[PHY]   [RAPROC] 19.19 prach_I0 = 19.6 dB
[PHY]   [RAPROC] 20.19 prach_I0 = 19.6 dB
[PHY]   [RAPROC] 21.19 prach_I0 = 19.9 dB
[PHY]   [RAPROC] 22.19 prach_I0 = 19.9 dB
[PHY]   [RAPROC] 23.19 prach_I0 = 20.0 dB
[PHY]   [RAPROC] 24.19 prach_I0 = 19.8 dB
[PHY]   [RAPROC] 25.19 prach_I0 = 20.2 dB
[PHY]   [RAPROC] 26.19 prach_I0 = 20.1 dB
[NR_PHY]   [RAPROC] 27.19 Initiating RA procedure with preamble 5, energy 55.7 dB (I0 201, thres 120), delay 5 start symbol 0 freq index 0
[PHY]   [RAPROC] 27.19 prach_I0 = 24.3 dB
[NR_MAC]   27.19 UE RA-RNTI 010b TC-RNTI fa49: initiating RA procedure
[NR_MAC]   Frame 27, Slot 19: Prach Occasion id = 0 ssb per RO = 1.000000 number of active SSB 1 index = 0 fdm 8 symbol index 0 freq_index 0 total_RApreambles 64
[NR_MAC]   UE fa49: Msg3 scheduled at 28.17 (28.7 TDA 3) start 0 RBs 8
[NR_MAC]   UE fa49: 28.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 5, timing_offset = 5 (estimated distance 195.3 [m])
[NR_MAC]   28.7 Send RAR to RA-RNTI 010b
[NR_PHY]   [RAPROC] 28.19 Initiating RA procedure with preamble 62, energy 55.7 dB (I0 243, thres 120), delay 28 start symbol 0 freq index 0
[PHY]   [RAPROC] 28.19 prach_I0 = 28.0 dB
[NR_MAC]   28.19 UE RA-RNTI 010b TC-RNTI 7413: initiating RA procedure
[NR_MAC]   Frame 28, Slot 19: Prach Occasion id = 0 ssb per RO = 1.000000 number of active SSB 1 index = 0 fdm 8 symbol index 0 freq_index 0 total_RApreambles 64
[NR_MAC]   UE 7413: Msg3 scheduled at 29.17 (29.7 TDA 3) start 0 RBs 8
[NR_MAC]   UE 7413: 29.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 62, timing_offset = 28 (estimated distance 1093.8 [m])
[NR_MAC]   29.7 Send RAR to RA-RNTI 010b
[NR_MAC]     2910: RA RNTI fa49 CC_id 0 Scheduling retransmission of Msg3 in (29,17)
[NR_PHY]   [RAPROC] 29.19 Initiating RA procedure with preamble 19, energy 56.4 dB (I0 280, thres 120), delay 0 start symbol 0 freq index 0
[PHY]   [RAPROC] 29.19 prach_I0 = 31.4 dB
[NR_MAC]   29.19 UE RA-RNTI 010b TC-RNTI 5de1: initiating RA procedure
[NR_MAC]   Frame 29, Slot 19: Prach Occasion id = 0 ssb per RO = 1.000000 number of active SSB 1 index = 0 fdm 8 symbol index 0 freq_index 0 total_RApreambles 64
[NR_MAC]   UE 5de1: Msg3 scheduled at 30.17 (30.7 TDA 3) start 0 RBs 8
[NR_MAC]   UE 5de1: 30.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 19, timing_offset = 0 (estimated distance 0.0 [m])
[NR_MAC]   30.7 Send RAR to RA-RNTI 010b
[NR_MAC]     3010: RA RNTI fa49 CC_id 0 Scheduling retransmission of Msg3 in (30,17)
[NR_MAC]     3010: RA RNTI 7413 CC_id 0 Scheduling retransmission of Msg3 in (30,17)
[NR_PHY]   [RAPROC] 30.19 Initiating RA procedure with preamble 44, energy 56.4 dB (I0 314, thres 120), delay 6 start symbol 0 freq index 0
[PHY]   [RAPROC] 30.19 prach_I0 = 34.3 dB
[NR_MAC]   30.19 UE RA-RNTI 010b TC-RNTI 4f64: initiating RA procedure
[NR_MAC]   Frame 30, Slot 19: Prach Occasion id = 0 ssb per RO = 1.000000 number of active SSB 1 index = 0 fdm 8 symbol index 0 freq_index 0 total_RApreambles 64
[NR_MAC]   UE 4f64: Msg3 scheduled at 31.17 (31.7 TDA 3) start 0 RBs 8
[NR_MAC]   UE 4f64: 31.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 44, timing_offset = 6 (estimated distance 234.4 [m])
[NR_MAC]   31.7 Send RAR to RA-RNTI 010b
[NR_MAC]     3110: RA RNTI fa49 CC_id 0 Scheduling retransmission of Msg3 in (31,17)
[NR_MAC]     3110: RA RNTI 7413 CC_id 0 Scheduling retransmission of Msg3 in (31,17)
[NR_MAC]     3110: RA RNTI 5de1 CC_id 0 Scheduling retransmission of Msg3 in (31,17)
[NR_MAC]   UE 5de1 cannot find free CCE!
[NR_MAC]     3111: RA RNTI 5de1 CC_id 0 Scheduling retransmission of Msg3 in (31,18)
[NR_MAC]   UE fa49 RA failed at state WAIT_Msg3 (Reached msg3 max harq rounds)
[NR_MAC]   Remove NR rnti 0xfa49
[NR_PHY]   [RAPROC] 31.19 Initiating RA procedure with preamble 0, energy 55.7 dB (I0 343, thres 120), delay 12 start symbol 0 freq index 0
[PHY]   [RAPROC] 31.19 prach_I0 = 36.8 dB
[NR_MAC]   31.19 UE RA-RNTI 010b TC-RNTI 2c6a: initiating RA procedure
[NR_MAC]   Frame 31, Slot 19: Prach Occasion id = 0 ssb per RO = 1.000000 number of active SSB 1 index = 0 fdm 8 symbol index 0 freq_index 0 total_RApreambles 64
[NR_MAC]   UE 2c6a: Msg3 scheduled at 32.17 (32.7 TDA 3) start 0 RBs 8
[NR_MAC]   UE 2c6a: 32.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 0, timing_offset = 12 (estimated distance 468.8 [m])
[NR_MAC]   32.7 Send RAR to RA-RNTI 010b
[NR_MAC]     3210: RA RNTI 7413 CC_id 0 Scheduling retransmission of Msg3 in (32,17)
[NR_MAC]     3210: RA RNTI 5de1 CC_id 0 Scheduling retransmission of Msg3 in (32,17)
[NR_MAC]     3210: RA RNTI 4f64 CC_id 0 Scheduling retransmission of Msg3 in (32,17)
[NR_MAC]   UE 4f64 cannot find free CCE!
[NR_MAC]     3211: RA RNTI 4f64 CC_id 0 Scheduling retransmission of Msg3 in (32,18)
[NR_MAC]   UE 7413 RA failed at state WAIT_Msg3 (Reached msg3 max harq rounds)
[NR_MAC]   Remove NR rnti 0x7413
[NR_PHY]   [RAPROC] 32.19 Initiating RA procedure with preamble 4, energy 55.7 dB (I0 368, thres 120), delay 26 start symbol 0 freq index 0
[PHY]   [RAPROC] 32.19 prach_I0 = 39.0 dB
[NR_MAC]   32.19 UE RA-RNTI 010b TC-RNTI 73fe: initiating RA procedure
[NR_MAC]   Frame 32, Slot 19: Prach Occasion id = 0 ssb per RO = 1.000000 number of active SSB 1 index = 0 fdm 8 symbol index 0 freq_index 0 total_RApreambles 64
[NR_MAC]   UE 73fe: Msg3 scheduled at 33.17 (33.7 TDA 3) start 0 RBs 8
[NR_MAC]   UE 73fe: 33.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 4, timing_offset = 26 (estimated distance 1015.7 [m])
[NR_MAC]   33.7 Send RAR to RA-RNTI 010b
[NR_MAC]     3310: RA RNTI 5de1 CC_id 0 Scheduling retransmission of Msg3 in (33,17)
[NR_MAC]     3310: RA RNTI 4f64 CC_id 0 Scheduling retransmission of Msg3 in (33,17)
[NR_MAC]     3310: RA RNTI 2c6a CC_id 0 Scheduling retransmission of Msg3 in (33,17)
[NR_MAC]   UE 2c6a cannot find free CCE!
[NR_MAC]     3311: RA RNTI 2c6a CC_id 0 Scheduling retransmission of Msg3 in (33,18)
[NR_MAC]   UE 5de1 RA failed at state WAIT_Msg3 (Reached msg3 max harq rounds)
[NR_MAC]   Remove NR rnti 0x5de1
[NR_PHY]   [RAPROC] 33.19 Initiating RA procedure with preamble 39, energy 55.7 dB (I0 390, thres 120), delay 29 start symbol 0 freq index 0
[PHY]   [RAPROC] 33.19 prach_I0 = 40.9 dB
[NR_MAC]   33.19 UE RA-RNTI 010b TC-RNTI abe9: initiating RA procedure
[NR_MAC]   Frame 33, Slot 19: Prach Occasion id = 0 ssb per RO = 1.000000 number of active SSB 1 index = 0 fdm 8 symbol index 0 freq_index 0 total_RApreambles 64
[NR_MAC]   UE abe9: Msg3 scheduled at 34.17 (34.7 TDA 3) start 0 RBs 8
[NR_MAC]   UE abe9: 34.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 39, timing_offset = 29 (estimated distance 1132.9 [m])
[NR_MAC]   34.7 Send RAR to RA-RNTI 010b
[NR_MAC]     3410: RA RNTI 4f64 CC_id 0 Scheduling retransmission of Msg3 in (34,17)
[NR_MAC]     3410: RA RNTI 2c6a CC_id 0 Scheduling retransmission of Msg3 in (34,17)
[NR_MAC]     3410: RA RNTI 73fe CC_id 0 Scheduling retransmission of Msg3 in (34,17)
[NR_MAC]   UE 73fe cannot find free CCE!
[NR_MAC]     3411: RA RNTI 73fe CC_id 0 Scheduling retransmission of Msg3 in (34,18)
[NR_MAC]   UE 4f64 RA failed at state WAIT_Msg3 (Reached msg3 max harq rounds)
[NR_MAC]   Remove NR rnti 0x4f64
[NR_PHY]   [RAPROC] 34.19 Initiating RA procedure with preamble 19, energy 56.4 dB (I0 409, thres 120), delay 0 start symbol 0 freq index 0
[PHY]   [RAPROC] 34.19 prach_I0 = 42.7 dB
[NR_MAC]   34.19 UE RA-RNTI 010b TC-RNTI dd30: initiating RA procedure
[NR_MAC]   Frame 34, Slot 19: Prach Occasion id = 0 ssb per RO = 1.000000 number of active SSB 1 index = 0 fdm 8 symbol index 0 freq_index 0 total_RApreambles 64
[NR_MAC]   UE dd30: Msg3 scheduled at 35.17 (35.7 TDA 3) start 0 RBs 8
[NR_MAC]   UE dd30: 35.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 19, timing_offset = 0 (estimated distance 0.0 [m])
[NR_MAC]   35.7 Send RAR to RA-RNTI 010b
[NR_MAC]     3510: RA RNTI 2c6a CC_id 0 Scheduling retransmission of Msg3 in (35,17)
[NR_MAC]     3510: RA RNTI 73fe CC_id 0 Scheduling retransmission of Msg3 in (35,17)
[NR_MAC]     3510: RA RNTI abe9 CC_id 0 Scheduling retransmission of Msg3 in (35,17)
[NR_MAC]   UE abe9 cannot find free CCE!
[NR_MAC]     3511: RA RNTI abe9 CC_id 0 Scheduling retransmission of Msg3 in (35,18)
[NR_MAC]   UE 2c6a RA failed at state WAIT_Msg3 (Reached msg3 max harq rounds)
[NR_MAC]   Remove NR rnti 0x2c6a
[NR_PHY]   [RAPROC] 35.19 Initiating RA procedure with preamble 9, energy 55.7 dB (I0 427, thres 120), delay 19 start symbol 0 freq index 0
[PHY]   [RAPROC] 35.19 prach_I0 = 44.2 dB
[NR_MAC]   35.19 UE RA-RNTI 010b TC-RNTI 476c: initiating RA procedure
[NR_MAC]   Frame 35, Slot 19: Prach Occasion id = 0 ssb per RO = 1.000000 number of active SSB 1 index = 0 fdm 8 symbol index 0 freq_index 0 total_RApreambles 64
[NR_MAC]   UE 476c: Msg3 scheduled at 36.17 (36.7 TDA 3) start 0 RBs 8
[NR_MAC]   UE 476c: 36.7 Generating RA-Msg2 DCI, RA RNTI 0x10b, state 1, preamble_index(RAPID) 9, timing_offset = 19 (estimated distance 742.2 [m])
[NR_MAC]   36.7 Send RAR to RA-RNTI 010b
[NR_MAC]     3610: RA RNTI 73fe CC_id 0 Scheduling retransmission of Msg3 in (36,17)
[NR_MAC]     3610: RA RNTI abe9 CC_id 0 Scheduling retransmission of Msg3 in (36,17)
[NR_MAC]     3610: RA RNTI dd30 CC_id 0 Scheduling retransmission of Msg3 in (36,17)
[NR_MAC]   UE dd30 cannot find free CCE!
[NR_MAC]     3611: RA RNTI dd30 CC_id 0 Scheduling retransmission of Msg3 in (36,18)
[NR_MAC]   UE 73fe RA failed at state WAIT_Msg3 (Reached msg3 max harq rounds)
[NR_MAC]   Remove NR rnti 0x73fe
[PHY]   [RAPROC] 36.19 prach_I0 = 45.4 dB
[NR_MAC]     3710: RA RNTI abe9 CC_id 0 Scheduling retransmission of Msg3 in (37,17)
[NR_MAC]     3710: RA RNTI dd30 CC_id 0 Scheduling retransmission of Msg3 in (37,17)
[NR_MAC]     3710: RA RNTI 476c CC_id 0 Scheduling retransmission of Msg3 in (37,17)
[NR_MAC]   UE 476c cannot find free CCE!
[NR_MAC]     3711: RA RNTI 476c CC_id 0 Scheduling retransmission of Msg3 in (37,18)
[NR_MAC]   UE abe9 RA failed at state WAIT_Msg3 (Reached msg3 max harq rounds)
[NR_MAC]   Remove NR rnti 0xabe9
[PHY]   [RAPROC] 37.19 prach_I0 = 46.6 dB
[NR_MAC]     3810: RA RNTI dd30 CC_id 0 Scheduling retransmission of Msg3 in (38,17)
[NR_MAC]     3810: RA RNTI 476c CC_id 0 Scheduling retransmission of Msg3 in (38,17)
[NR_MAC]   UE dd30 RA failed at state WAIT_Msg3 (Reached msg3 max harq rounds)
[NR_MAC]   Remove NR rnti 0xdd30
[PHY]   [RAPROC] 38.19 prach_I0 = 47.6 dB
[NR_MAC]     3910: RA RNTI 476c CC_id 0 Scheduling retransmission of Msg3 in (39,17)
[NR_MAC]   UE 476c RA failed at state WAIT_Msg3 (Reached msg3 max harq rounds)
[NR_MAC]   Remove NR rnti 0x476c
[PHY]   [RAPROC] 39.19 prach_I0 = 48.6 dB
[PHY]   [RAPROC] 40.19 prach_I0 = 49.4 dB
[PHY]   [RAPROC] 41.19 prach_I0 = 50.1 dB
[PHY]   [RAPROC] 42.19 prach_I0 = 50.7 dB
[PHY]   [RAPROC] 43.19 prach_I0 = 51.3 dB
[PHY]   [RAPROC] 44.19 prach_I0 = 51.7 dB
[PHY]   [RAPROC] 45.19 prach_I0 = 52.1 dB
[PHY]   [RAPROC] 46.19 prach_I0 = 52.4 dB
[PHY]   [RAPROC] 47.19 prach_I0 = 52.7 dB
[PHY]   [RAPROC] 48.19 prach_I0 = 53.0 dB
[PHY]   [RAPROC] 49.19 prach_I0 = 53.2 dB
[PHY]   [RAPROC] 50.19 prach_I0 = 53.4 dB
[PHY]   [RAPROC] 51.19 prach_I0 = 53.7 dB
[PHY]   [RAPROC] 52.19 prach_I0 = 53.8 dB
[PHY]   [RAPROC] 53.19 prach_I0 = 53.9 dB
[PHY]   [RAPROC] 54.19 prach_I0 = 54.1 dB
[PHY]   [RAPROC] 55.19 prach_I0 = 54.2 dB
[PHY]   [RAPROC] 56.19 prach_I0 = 54.3 dB
[PHY]   [RAPROC] 57.19 prach_I0 = 54.5 dB
[PHY]   [RAPROC] 58.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 59.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 60.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 61.19 prach_I0 = 54.5 dB
[PHY]   [RAPROC] 62.19 prach_I0 = 54.5 dB
[PHY]   [RAPROC] 63.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 64.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 65.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 66.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 67.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 68.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 69.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 70.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 71.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 72.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 73.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 74.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 75.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 76.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 77.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 78.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 79.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 80.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 81.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 82.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 83.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 84.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 85.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 86.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 87.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 88.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 89.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 90.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 91.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 92.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 93.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 94.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 95.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 96.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 97.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 98.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 99.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 100.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 101.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 102.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 103.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 104.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 105.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 106.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 107.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 108.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 109.19 prach_I0 = 54.9 dB
[PHY]   [RAPROC] 110.19 prach_I0 = 54.9 dB
[PHY]   [RAPROC] 111.19 prach_I0 = 54.9 dB
[PHY]   [RAPROC] 112.19 prach_I0 = 54.9 dB
[PHY]   [RAPROC] 113.19 prach_I0 = 54.9 dB
[PHY]   [RAPROC] 114.19 prach_I0 = 54.9 dB
[PHY]   [RAPROC] 115.19 prach_I0 = 55.0 dB
[PHY]   [RAPROC] 116.19 prach_I0 = 55.0 dB
[PHY]   [RAPROC] 117.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 118.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 119.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 120.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 121.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 122.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 123.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 124.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 125.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 126.19 prach_I0 = 55.1 dB
[NR_MAC]   Frame.Slot 128.0

[PHY]   [RAPROC] 127.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 128.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 129.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 130.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 131.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 132.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 133.19 prach_I0 = 55.2 dB
[PHY]   [RAPROC] 134.19 prach_I0 = 55.2 dB
[PHY]   [RAPROC] 135.19 prach_I0 = 55.2 dB
[PHY]   [RAPROC] 136.19 prach_I0 = 55.2 dB
[PHY]   [RAPROC] 137.19 prach_I0 = 55.2 dB
[PHY]   [RAPROC] 138.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 139.19 prach_I0 = 55.4 dB
[PHY]   [RAPROC] 140.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 141.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 142.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 143.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 144.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 145.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 146.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 147.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 148.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 149.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 150.19 prach_I0 = 55.4 dB
[PHY]   [RAPROC] 151.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 152.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 153.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 154.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 155.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 156.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 157.19 prach_I0 = 51.0 dB
[PHY]   [RAPROC] 158.19 prach_I0 = 47.1 dB
[PHY]   [RAPROC] 159.19 prach_I0 = 43.6 dB
[PHY]   [RAPROC] 160.19 prach_I0 = 40.7 dB
[PHY]   [RAPROC] 161.19 prach_I0 = 37.9 dB
[PHY]   [RAPROC] 162.19 prach_I0 = 35.5 dB
[PHY]   [RAPROC] 163.19 prach_I0 = 33.6 dB
[PHY]   [RAPROC] 164.19 prach_I0 = 31.8 dB
[PHY]   [RAPROC] 165.19 prach_I0 = 30.2 dB
[PHY]   [RAPROC] 166.19 prach_I0 = 29.0 dB
[PHY]   [RAPROC] 167.19 prach_I0 = 27.9 dB
[PHY]   [RAPROC] 168.19 prach_I0 = 27.2 dB
[PHY]   [RAPROC] 169.19 prach_I0 = 26.3 dB
[PHY]   [RAPROC] 170.19 prach_I0 = 25.6 dB
[PHY]   [RAPROC] 171.19 prach_I0 = 24.8 dB
[PHY]   [RAPROC] 172.19 prach_I0 = 24.1 dB
[PHY]   [RAPROC] 173.19 prach_I0 = 23.6 dB
[PHY]   [RAPROC] 174.19 prach_I0 = 23.0 dB
[PHY]   [RAPROC] 175.19 prach_I0 = 22.5 dB
[PHY]   [RAPROC] 176.19 prach_I0 = 22.1 dB
[PHY]   [RAPROC] 177.19 prach_I0 = 21.7 dB
[PHY]   [RAPROC] 178.19 prach_I0 = 21.2 dB
[PHY]   [RAPROC] 179.19 prach_I0 = 20.8 dB
[PHY]   [RAPROC] 180.19 prach_I0 = 20.5 dB
[PHY]   [RAPROC] 181.19 prach_I0 = 20.3 dB
[PHY]   [RAPROC] 182.19 prach_I0 = 20.1 dB
[PHY]   [RAPROC] 183.19 prach_I0 = 19.8 dB
[PHY]   [RAPROC] 184.19 prach_I0 = 19.7 dB
[PHY]   [RAPROC] 185.19 prach_I0 = 19.6 dB
[PHY]   [RAPROC] 186.19 prach_I0 = 19.5 dB
[PHY]   [RAPROC] 187.19 prach_I0 = 19.4 dB
[PHY]   [RAPROC] 188.19 prach_I0 = 19.1 dB
[PHY]   [RAPROC] 189.19 prach_I0 = 18.9 dB
[PHY]   [RAPROC] 190.19 prach_I0 = 18.9 dB
[PHY]   [RAPROC] 191.19 prach_I0 = 18.8 dB
[PHY]   [RAPROC] 192.19 prach_I0 = 18.7 dB
[PHY]   [RAPROC] 193.19 prach_I0 = 18.7 dB
[PHY]   [RAPROC] 194.19 prach_I0 = 18.6 dB
[PHY]   [RAPROC] 195.19 prach_I0 = 18.5 dB
[PHY]   [RAPROC] 196.19 prach_I0 = 18.6 dB
[PHY]   [RAPROC] 197.19 prach_I0 = 18.6 dB
[PHY]   [RAPROC] 198.19 prach_I0 = 18.4 dB
[PHY]   [RAPROC] 199.19 prach_I0 = 18.4 dB
[PHY]   [RAPROC] 200.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 201.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 202.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 203.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 204.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 205.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 206.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 207.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 208.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 209.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 210.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 211.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 212.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 213.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 214.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 215.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 216.19 prach_I0 = 17.9 dB
[PHY]   [RAPROC] 217.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 218.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 219.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 220.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 221.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 222.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 223.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 224.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 225.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 226.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 227.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 228.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 229.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 230.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 231.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 232.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 233.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 234.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 235.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 236.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 237.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 238.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 239.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 240.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 241.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 242.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 243.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 244.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 245.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 246.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 247.19 prach_I0 = 18.4 dB
[PHY]   [RAPROC] 248.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 249.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 250.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 251.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 252.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 253.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 254.19 prach_I0 = 18.2 dB
[NR_MAC]   Frame.Slot 256.0
"""

frames = []
prach_i0_values = []

# Regex to find lines with "prach_I0 = X.Y dB"
# It captures the number before ".19" as the frame and X.Y as prach_I0 value
# This regex also handles the specific line "PHY] prach_I0 = 17.3 dB" which lacks a frame number
pattern = re.compile(r'(?:\[PHY\]\s+\[RAPROC\]\s+)?(\d+\.\d+)\s+prach_I0\s*=\s*(\d+\.\d+)\s*dB')
fallback_pattern = re.compile(r'\[PHY\]\s+prach_I0\s*=\s*(\d+\.\d+)\s*dB')

for line in log_data.strip().split('\n'):
    match = pattern.search(line)
    if match:
        frame_full = match.group(1)
        # Extract just the integer part as the frame number
        frame = int(float(frame_full))
        prach_i0 = float(match.group(2))
        frames.append(frame)
        prach_i0_values.append(prach_i0)
    else:
        # Handle the specific case where the frame number is missing
        fallback_match = fallback_pattern.search(line)
        if fallback_match:
            # For these cases, we might need to infer the frame or handle it differently.
            # For now, let's skip it or assign a placeholder/previous frame if logical.
            # Given the request is for "each frame", skipping is safer if no explicit frame.
            # If you want to associate these with the previous frame, you'd need to modify this logic.
            # For this example, we'll skip lines that don't have the frame.xx format before prach_I0
            pass

# Create the plot with analysis
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

# 主要時間序列圖
ax1.plot(frames, prach_i0_values, marker='o', linestyle='-', color='b', markersize=3)
ax1.set_title('prach_I0 隨 Frame 的變化 (時間序列)', fontsize=14)
ax1.set_xlabel('Frame')
ax1.set_ylabel('prach_I0 (dB)')
ax1.grid(True, alpha=0.3)

# 添加統計線
mean_val = np.mean(prach_i0_values)
std_val = np.std(prach_i0_values)
ax1.axhline(y=mean_val, color='r', linestyle='--', alpha=0.8, label=f'平均值: {mean_val:.2f} dB')
ax1.axhline(y=mean_val + std_val, color='orange', linestyle=':', alpha=0.8, label=f'+1σ: {mean_val + std_val:.2f} dB')
ax1.axhline(y=mean_val - std_val, color='orange', linestyle=':', alpha=0.8, label=f'-1σ: {mean_val - std_val:.2f} dB')
ax1.legend()

# 直方圖分析
ax2.hist(prach_i0_values, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
ax2.axvline(mean_val, color='r', linestyle='--', linewidth=2, label=f'平均值: {mean_val:.2f} dB')
ax2.axvline(np.median(prach_i0_values), color='g', linestyle='--', linewidth=2, label=f'中位數: {np.median(prach_i0_values):.2f} dB')
ax2.set_title('prach_I0 數值分布直方圖', fontsize=14)
ax2.set_xlabel('prach_I0 (dB)')
ax2.set_ylabel('頻次')
ax2.legend()
ax2.grid(True, alpha=0.3)

# 移動平均分析
window_size = 20
if len(prach_i0_values) >= window_size:
    moving_avg = np.convolve(prach_i0_values, np.ones(window_size)/window_size, mode='valid')
    moving_frames = frames[window_size-1:]
    ax3.plot(frames, prach_i0_values, alpha=0.3, color='lightblue', label='原始數據')
    ax3.plot(moving_frames, moving_avg, color='red', linewidth=2, label=f'{window_size}點移動平均')
    ax3.set_title(f'prach_I0 移動平均分析 (窗口大小: {window_size})', fontsize=14)
    ax3.set_xlabel('Frame')
    ax3.set_ylabel('prach_I0 (dB)')
    ax3.legend()
    ax3.grid(True, alpha=0.3)

# 數據變化率分析
changes = np.diff(prach_i0_values)
change_frames = frames[1:]
ax4.plot(change_frames, changes, marker='o', linestyle='-', color='purple', markersize=2)
ax4.axhline(y=0, color='black', linestyle='-', alpha=0.5)
ax4.set_title('prach_I0 變化率分析 (相鄰Frame差值)', fontsize=14)
ax4.set_xlabel('Frame')
ax4.set_ylabel('prach_I0 變化量 (dB)')
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 詳細統計分析
print("="*60)
print("prach_I0 數據統計分析報告")
print("="*60)

print(f"\n【基本統計資訊】")
print(f"數據點總數: {len(prach_i0_values)}")
print(f"Frame 範圍: {min(frames)} ~ {max(frames)}")
print(f"prach_I0 範圍: {min(prach_i0_values):.1f} ~ {max(prach_i0_values):.1f} dB")
print(f"平均值: {mean_val:.2f} dB")
print(f"中位數: {np.median(prach_i0_values):.2f} dB")
print(f"標準差: {std_val:.2f} dB")
print(f"變異係數: {(std_val/mean_val)*100:.1f}%")

print(f"\n【分位數分析】")
percentiles = [5, 10, 25, 50, 75, 90, 95]
for p in percentiles:
    val = np.percentile(prach_i0_values, p)
    print(f"{p}% 分位數: {val:.2f} dB")

print(f"\n【異常值檢測】(使用 IQR 方法)")
Q1 = np.percentile(prach_i0_values, 25)
Q3 = np.percentile(prach_i0_values, 75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = [val for val in prach_i0_values if val < lower_bound or val > upper_bound]
print(f"IQR: {IQR:.2f} dB")
print(f"異常值範圍: < {lower_bound:.2f} dB 或 > {upper_bound:.2f} dB")
print(f"異常值數量: {len(outliers)} 個")
if outliers:
    print(f"異常值: {sorted(set(outliers))}")

print(f"\n【數據穩定性分析】")
print(f"最大變化量: {max(abs(change) for change in changes):.2f} dB")
print(f"平均變化量: {np.mean(np.abs(changes)):.2f} dB")
print(f"變化量標準差: {np.std(changes):.2f} dB")

print(f"\n【關鍵事件識別】")
# 尋找大幅變化的點
large_changes = [(i+1, change) for i, change in enumerate(changes) if abs(change) > 2*np.std(changes)]
if large_changes:
    print("大幅變化事件 (變化量 > 2σ):")
    for frame_idx, change in large_changes[:10]:  # 顯示前10個
        frame_num = frames[frame_idx]
        val_before = prach_i0_values[frame_idx-1]
        val_after = prach_i0_values[frame_idx]
        print(f"  Frame {frame_num}: {val_before:.1f} → {val_after:.1f} dB (變化: {change:+.1f} dB)")

# 尋找最高和最低值
max_idx = prach_i0_values.index(max(prach_i0_values))
min_idx = prach_i0_values.index(min(prach_i0_values))
print(f"\n最高值: {max(prach_i0_values):.1f} dB (Frame {frames[max_idx]})")
print(f"最低值: {min(prach_i0_values):.1f} dB (Frame {frames[min_idx]})")

print(f"\n【趨勢分析】")
# 簡單線性回歸
x = np.array(range(len(prach_i0_values)))
y = np.array(prach_i0_values)
slope, intercept = np.polyfit(x, y, 1)
print(f"整體趨勢斜率: {slope:.4f} dB/點")
if abs(slope) < 0.001:
    trend = "基本穩定"
elif slope > 0:
    trend = "略微上升"
else:
    trend = "略微下降"
print(f"趨勢判定: {trend}")

print("="*60)

print("已提取的 Frame 和 prach_I0 數據：")
for i in range(len(frames)):
    print(f"Frame: {frames[i]}, prach_I0: {prach_i0_values[i]} dB")