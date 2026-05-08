OAI 5G NR — Multi-FDM PRACH Occasions 偽代碼
以下依照 配置 → gNB MAC 排程 → UE MAC 選擇 → PHY 接收 四個層次整理。

1. 配置階段 — config.c: nr_mac_config_scc()

// === 1. 從 RRC 參數映射 FDM 數量 ===
switch msg1_FDM:
    case 0 → num_fd_occasions = 1
    case 1 → num_fd_occasions = 2
    case 2 → num_fd_occasions = 4
    case 3 → num_fd_occasions = 8

// === 2. 為每個 FD occasion 計算起始頻率位置 k1 ===
allocate num_fd_occasions_list[num_fd_occasions]

for i = 0 to num_fd_occasions - 1:
    fd_occasion[i].prach_root_sequence_index = rach_RootSequenceIndex
    fd_occasion[i].k1 = BWP_start + msg1_FrequencyStart + (N_RA_RB * i)
    //                  └─ 每個 FD occasion 頻率起點依次偏移 N_RA_RB 個 PRB
    fd_occasion[i].prach_zero_corr_conf = zeroCorrelationZoneConfig
2. gNB MAC — 統計可用 PRACH Occasions

// === find_SSB_and_RO_available() ===
// 源碼: gNB_scheduler_RA.c:140

fdm   = num_fd_occasions          // 1/2/4/8
prach_info = get_prach_occasion_info(config_index)
// prach_info 包含:
//   N_RA_sfn   = 每 config period 內有效 SFN 數
//   N_t_slot   = 每 slot 時域 occasions 數
//   N_RA_slot  = 每 SFN 內 PRACH slots 數
//   N_dur      = 每個 occasion 佔用的符元數

// 每個 config period 內的 RO 總數
total_RO_per_period = N_RA_sfn × N_t_slot × N_RA_slot × fdm
//                    時域 SFN × 時域 occasions × PRACH slots × 頻域 FDM

// 決定 association period（讓所有 SSB 都至少能對應到一個 RO）
repeat:
    max_association_period *= 2
    total_RO = total_RO_per_period × max_association_period
until total_RO ≥ num_active_SSB / num_ssb_per_RO

total_prach_occasions = total_RO - unused_RO   // 去掉多餘的 RO
3. gNB MAC — 排程 PRACH PDU（每個 slot）

// === schedule_nr_prach(frame, slot) ===
// 源碼: gNB_scheduler_RA.c:352

if slot 不是 UL slot: return
if 當前 (frame, slot) 不符合 PRACH 排程表: return

fdm      = num_fd_occasions
N_t_slot = prach_info.N_t_slot
start_symb = prach_info.start_symbol
slot_index = (N_RA_slot > 1 && slot 為奇數) ? 1 : 0

// ─── 雙層迴圈：外層頻域、內層時域 ───
for fdm_index = 0 to fdm - 1:          // 頻域 FDM index
    for td_index = 0 to N_t_slot - 1:  // 時域 occasion index

        // 計算全域 PRACH occasion ID（3GPP TS 38.321）
        prach_occasion_id =
            (frame_in_assoc_period / config_period) × total_prach_occasions_per_period
          + (RA_sfn_index + slot_index) × N_t_slot × fdm
          + td_index × fdm
          + fdm_index
        //  └─ 排列順序: SFN → slot → 時域 occasion → 頻域 FDM

        if prach_occasion_id ≥ total_prach_occasions:
            continue   // 此 occasion 為 unused，跳過

        // 找到對應的 SSB 索引
        if num_ssb_per_RO ≤ 1:
            n_ssb = (prach_occasion_id ÷ (1/num_ssb_per_RO)) mod num_active_ssb
        else:
            first_ssb = (prach_occasion_id × num_ssb_per_RO) mod num_active_ssb
            // 該 RO 對應 num_ssb_per_RO 個 SSB

        // 分配 beam
        beam_index = get_fapi_beamforming_index(ssb_index[n_ssb])
        beam = beam_allocation_procedure(frame, slot, beam_index)

        // 僅在每個 FDM 的第一個時域 occasion (td_index==0) 建立新的 PDU
        if td_index == 0:
            prach_pdu = new PRACH PDU in UL_tti_req
            prach_pdu.phys_cell_id    = cell_id
            prach_pdu.num_prach_ocas  = N_t_slot    // 時域 occasions 數
            prach_pdu.prach_start_symbol = start_symb
            prach_pdu.num_ra          = fdm_index   // ← 頻域 FDM 索引
            prach_pdu.prach_format    = format
            prach_pdu.beam_idx        = beam_index
            // 結果: 每個頻域 FDM 位置產生一個 PDU，
            //       每個 PDU 包含 N_t_slot 個時域 occasions

// 標記 VRB 資源占用（所有 FDM 頻段）
block PRBs: n_ra_rb × fdm 個 PRBs
4. gNB MAC — 反推接收到的 preamble 屬於哪個 SSB

// === ssb_index_from_prach(frame, slot, preamble_index, freq_index, symbol) ===
// 源碼: gNB_scheduler_RA.c:64

fdm = num_fd_occasions

// 由 symbol 反推時域 occasion index
for slot_index in {0,1}:
    for i = 0 to N_t_slot - 1:
        temp_symbol = (start_symbol + i × N_dur + 14 × slot_index) mod 14
        if temp_symbol == symbol:
            start_symbol_index = i; break

// 計算 prach_occasion_id（公式與排程端相同）
prach_occasion_id =
    (frame_in_assoc_period / config_period) × total_prach_occasions_per_period
  + (RA_sfn_index + slot_index) × N_t_slot × fdm
  + start_symbol_index × fdm
  + freq_index   // ← FAPI 上報的 freq_index 即 fdm_index

// 映射到 SSB index
if num_ssb_per_RO ≤ 1:
    ssb_index = (prach_occasion_id ÷ (1/num_ssb_per_RO)) mod num_active_ssb
else:
    ssb_index = (prach_occasion_id × num_ssb_per_RO) mod num_active_ssb
    + preamble 所屬的 SSB 內偏移

return ssb_index
5. PHY gNB — 接收並處理每個時域 Occasion

// === L1_nr_prach_procedures(frame, slot, rach_ind) ===
// 源碼: nr_prach_procedures.c:98

prach_pdu = find PRACH PDU for (frame, slot)
N_dur = get_prach_duration(prach_format)   // 每個 occasion 的符元長度

// ─── 時域 occasion 迴圈 ───
for prach_oc = 0 to num_prach_ocas - 1:   // num_prach_ocas = N_t_slot

    // 取得此 occasion 的接收信號（已做前端處理）
    rxsigF[aa] = ru.prach_rxsigF[prach_oc][ru_aa]

    // 計算此 occasion 的起始符元
    prachStartSymbol = prach_start_symbol + prach_oc × N_dur

    // 做 preamble 偵測（matched filtering + peak detection）
    rx_nr_prach(prach_pdu, prach_oc, frame, slot,
                &max_preamble, &max_preamble_energy, &max_preamble_delay)

    // 能量超過門檻 → 上報給 MAC
    if energy > I0 + threshold:
        rach_ind.pdu[n].freq_index    = prach_pdu.num_ra   // FDM 索引
        rach_ind.pdu[n].symbol_index  = prachStartSymbol
        rach_ind.pdu[n].preamble_index = max_preamble
        rach_ind.pdu[n].timing_advance = max_preamble_delay
        rach_ind.number_of_pdus++
6. UE MAC — 建立所有可用 PRACH Occasions

// === configure_prach_occasions(scs) ===
// 源碼: nr_ra_procedures.c:524

prach_info = get_prach_occasion_info(config_index)
num_fd_occasions = ra.num_fd_occasions   // 從 SIB1 解析

// ─── 遍歷所有 SFN、slot、時域 occasion、頻域 FDM ───
for n_sfn = 0 to N_RA_sfn - 1:
    for slot = 0 to slots_per_frame - 1:
        if slot 不是此 SFN 的有效 PRACH slot: continue
        for prach_slot = 0 to prach_slots_in_sf - 1:
            for t = 0 to N_t_slot - 1:
                start_symbol = start_symbol_base + t × N_dur
                if start_symbol 超出 slot 範圍: continue
                for f = 0 to num_fd_occasions - 1:
                    ra_occasions_period[count++] = {
                        slot         = slot,
                        start_symbol = start_symbol,
                        fdm          = f,     // ← 頻域索引
                        format       = prach_format,
                        frame_info   = {x, y}
                    }
// 總數 = N_RA_sfn × N_t_slot × N_RA_slot × num_fd_occasions
7. UE MAC — 選擇 PRACH Occasion（含 Multi-FDM）

// === select_prach_occasion(nb_tx_ssb, ra_occasions_period, num) ===
// 源碼: nr_ra_procedures.c:443

// 根據 SSB index 和 preamble 功率計算 RO index（3GPP TS 38.321 5.1.2）
ro_index = (ssb_index × (num_ra_occasions / num_active_ssb)
           + preamble_ramping_cnt) mod num_ra_occasions

// 為所有頻域 occasions 分配清單
ra.num_sched_ro    = num_fd_occasions
ra.sched_ro_info_list = alloc[num_fd_occasions]

// ─── 擴展成 multi-FDM 清單 ───
for f = 0 to num_fd_occasions - 1:
    ra.sched_ro_info_list[f] = ra_occasions_period[ro_index]  // 相同時域 occasion
    ra.sched_ro_info_list[f].fdm = f                          // 但各自設定頻域索引
    ra.sched_ro_info_list[f].association_period_idx = ass_period_idx
// 結果: UE 同時在所有 FDM 頻段發送 preamble
8. UE MAC scheduler — 排程每個 FDM Occasion

// === nr_ue_prach_scheduler(frame, slot) ===
// 源碼: nr_ue_scheduler.c:2100

if slot 不是 UL slot: return
if 當前 frame 不在有效 PRACH frame 內: return

// ─── 遍歷所有頻域 occasions ───
for i = 0 to ra.num_sched_ro - 1:
    prach_info = ra.sched_ro_info_list[i]

    if slot ≠ prach_info.slot: continue   // slot 不匹配跳過

    // 為此 FDM occasion 分配 UL config PDU
    pdu = allocate PRACH PDU

    pdu.prach_config = {
        phys_cell_id       = cell_id,
        num_prach_ocas     = 1,                      // 每 PDU 一個 occasion
        prach_start_symbol = prach_info.start_symbol,
        num_ra             = prach_info.fdm,          // ← FDM 索引
        root_seq_id = fd_occasions_list[prach_info.fdm].prach_root_sequence_index,
        freq_msg1   = fd_occasions_list[prach_info.fdm].k1   // ← 起始頻率
    }
    // 每個 FDM 頻段用不同的 k1 和可能不同的 root sequence
整體資料流摘要

                    ┌─────────────────────────────────────────────┐
  RRC / SIB1        │  msg1_FDM = {0,1,2,3}                       │
  配置              │  → fdm = {1,2,4,8}  個 FD occasions          │
                    │  fd_occasion[i].k1 = BWP_start + FreqStart   │
                    │                    + N_RA_RB × i             │
                    └──────────────┬──────────────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────────────┐
  gNB MAC           │  schedule_nr_prach()                         │
  排程              │  for fdm_index = 0..fdm-1:                   │
                    │    for td_index = 0..N_t_slot-1:             │
                    │      occasion_id = f(frame,slot,td,fdm_idx)  │
                    │    → 建立 1 個 PDU / FDM occasion             │
                    │      PDU.num_ra = fdm_index                  │
                    │      PDU.num_prach_ocas = N_t_slot            │
                    └──────────────┬──────────────────────────────┘
                          FAPI (UL_tti_req)
                    ┌──────────────▼──────────────────────────────┐
  PHY gNB           │  L1_nr_prach_procedures()                    │
  接收              │  for prach_oc = 0..num_prach_ocas-1:         │
                    │    rxsigF = ru.prach_rxsigF[prach_oc]        │
                    │    rx_nr_prach(prach_pdu, prach_oc)          │
                    │    if energy > thresh → rach_ind.freq_index  │
                    │                        = PDU.num_ra (FDM idx)│
                    └──────────────┬──────────────────────────────┘
                          FAPI (rach_indication)
                    ┌──────────────▼──────────────────────────────┐
  gNB MAC           │  nr_mac_handle_rach_indication()             │
  處理              │  ssb_index = ssb_index_from_prach(           │
                    │               freq_index, symbol)            │
                    │  → 啟動 RA procedure (Msg2 RAR)              │
                    └─────────────────────────────────────────────┘

  ── UE 側 ──────────────────────────────────────────────────────

                    ┌─────────────────────────────────────────────┐
  UE MAC            │  configure_prach_occasions()                 │
  建立清單          │  枚舉所有 (slot, symbol, fdm) 組合           │
                    └──────────────┬──────────────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────────────┐
  UE MAC            │  select_prach_occasion()                     │
  選擇 occasion     │  ro_index = f(ssb_index, ramping_cnt)        │
                    │  for f=0..num_fd_occasions-1:                │
                    │    sched_ro_info_list[f].fdm = f             │
                    │  → UE 同時在所有 FDM 頻段發送                │
                    └──────────────┬──────────────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────────────┐
  UE Scheduler      │  nr_ue_prach_scheduler()                     │
                    │  for i=0..num_sched_ro-1:                    │
                    │    pdu.num_ra    = sched_ro_info_list[i].fdm │
                    │    pdu.freq_msg1 = fd_occasions[fdm].k1      │
                    └─────────────────────────────────────────────┘
關鍵參數對照表
參數	數值範圍	意義
msg1_FDM	0–3	RRC 配置，映射到 1/2/4/8
num_fd_occasions (fdm)	1/2/4/8	同時存在的 FD PRACH occasions 數
prach_pdu.num_ra	0..fdm-1	FAPI 中的頻域 occasion 索引
fd_occasion[i].k1	PRB offset	第 i 個 FD occasion 的頻率起點
prach_occasion_id	0..total-1	全域唯一 occasion 編號
N_t_slot	1..7	每 slot 內時域 occasions 數
num_prach_ocas	= N_t_slot	每個 PDU 包含的時域 occasions 數



---


Preamble 疊加（Superposition）實作偽代碼
共有三個層次的疊加，彼此獨立：

層次 1 — RU 接收：時域重複的相干疊加
rx_nr_prach_ru() — openair1/PHY/NR_TRANSPORT/nr_prach.c:151

// 輸入: numRA (FDM 索引), prachOccasion (時域 occasion 索引)
// rxsigF = ru->prach_rxsigF[prachOccasion]  ← 取出本 occasion 的接收緩衝

// 依 PRACH format 決定重複次數 reps 與 DFT 長度 dftlen
//   format 0      → reps=1,  dftlen=24576
//   format 1      → reps=2,  dftlen=24576
//   format 2,3    → reps=4,  dftlen=24576 / 6144
//   format A1,B1  → reps=2,  dftlen=2048>>mu
//   format A2     → reps=4,  dftlen=2048>>mu
//   format A3     → reps=6,  dftlen=2048>>mu
//   format B4     → reps=12, dftlen=2048>>mu

// k = 起始子載波索引（依 msg1_frequencyStart 計算）
k = 12 × msg1_frequencyStart - 6 × N_RB_UL
k = (k < 0) ? k + ofdm_symbol_size : k
k = k × K + kbar   // 換算到 PRACH SCS 的子載波

for aa = 0 to nb_rx - 1:   // 每支接收天線獨立處理

    // ── 步驟 1: 各重複段分別做 FFT ──
    prach2 = prach[aa] + 2 × Ncp  // 跳過 CP

    for i = 0 to reps - 1:
        dft(dftsize, prach2 + 2×dftlen×i,
                     rxsigF[aa] + 2×dftlen×i)
        // 每個重複的時域信號獨立轉為頻域
        // 結果存在 rxsigF[aa] 的不同段落

    // ── 步驟 2: 跨重複的相干疊加（Coherent Combining）──
    // 假設通道在各 repetition 間不變（窄頻近似）
    k2 = k × 2   // 複數索引（實部+虛部交錯）

    for j = 0 to 2×N_ZC - 1:
        if k2 == 2×dftlen: k2 = 0  // 環繞（wrap-around DC）

        rxsigF_tmp[j] = rxsigF[aa][k2]      // 第 0 次重複

        for i = 1 to reps - 1:              // 加上第 1..reps-1 次重複
            rxsigF_tmp[j] += rxsigF[aa][k2 + i × 2×dftlen]
        //                    ↑ 頻率對齊後直接相加（相干）

        k2++

    // 用疊加結果覆蓋 rxsigF[aa] 的前 N_ZC 個複數
    rxsigF[aa][0 .. 2×N_ZC-1] = rxsigF_tmp[0 .. 2×N_ZC-1]
    // 結果: reps 份信號相干合成，SNR 理論提升 10log10(reps) dB
層次 2 — gNB PHY：多天線能量非相干疊加
rx_nr_prach() — openair1/PHY/NR_TRANSPORT/nr_prach.c:434

// 輸入: prach_pdu (含 num_ra = FDM 索引), prachOccasion
// rxsigF = gNB->prach_vars.rxsigF  ← 已由 L1_prach_procedures 設好

// 依 FDM 索引讀取對應的根序列與頻率參數
rootSequenceIndex = fd_occasions_list[num_ra].prach_root_sequence_index
k1                = fd_occasions_list[num_ra].k1
NCS2 = (N_ZC==839) ? (NCS×1024/839) : (NCS×256/139)  // IFFT 後的 NCS

// ── 外層迴圈: 64 個 preamble index ──
for preamble_index = 0 to 63:

    // 計算對應的根序列 offset 與循環位移 preamble_shift
    // （unrestricted set: offset = preamble_index / (N_ZC/NCS)
    //   restricted  set: 按 TS 38.211 附表迭代計算）

    if 根序列改變 (new_dft == 1):
        Xu = X_u[preamble_offset - first_nonzero_root_idx]  // 取 ZC 序列

        prach_ifft[0..IFFT_SIZE-1] = 0   // 清空能量累積緩衝
        prachF[0..2×1024-1]        = 0

        // ── 內層迴圈: 跨天線能量非相干疊加 ──
        for aa = 0 to nb_rx - 1:

            // 步驟 A: 頻域相關（Matched Filter）
            // 計算 rxsigF[aa] × Xu* （元素乘法）
            for offset = 0 to 2×N_ZC - 1 step 2:
                prachF[offset]   = (Xu[offset]   × rxsigF[aa][offset]
                                  + Xu[offset+1] × rxsigF[aa][offset+1]) >> 15
                prachF[offset+1] = (Xu[offset]   × rxsigF[aa][offset+1]
                                  - Xu[offset+1] × rxsigF[aa][offset])   >> 15
                // 結果 = 頻域相關，等效時域延遲剖面（PDP）

            // 步驟 B: IFFT → 時延域
            if N_ZC == 839:
                idft_1024(prachF, prach_ifft_tmp)   // 1024 點 IFFT
                IFFT_SIZE = 1024
            else:
                idft_256(prachF, prach_ifft_tmp)    // 256 點 IFFT
                IFFT_SIZE = 256

            // 步驟 C: 能量疊加（非相干，incoherent combining）
            for i = 0 to IFFT_SIZE - 1:
                prach_ifft[i] += prach_ifft_tmp[2i]²
                               + prach_ifft_tmp[2i+1]²
                // 各天線的瞬時功率直接累加（不需相位對齊）

        // 步驟 D: 正規化
        for i = 0 to IFFT_SIZE - 1:
            prach_ifft[i] = (prach_ifft[i] >> log2_IFFT_SIZE) / nb_rx
            // 除以 IFFT 增益與天線數

    // ── preamble 偵測: 在 NCS2 視窗內找峰值 ──
    preamble_shift2 = (preamble_shift × IFFT_SIZE) / N_ZC

    for i = 0 to NCS2 - 1:
        lev_dB = dB(prach_ifft[preamble_shift2 + i])
        if lev_dB > max_energy:
            max_energy = lev_dB
            max_delay  = i          // Timing Advance 估計
            max_preamble = preamble_index

// 輸出: (max_preamble, max_energy, max_delay)
層次 3 — UE 發送：多 Preamble 頻域相干疊加
generate_nr_prach() — openair1/PHY/NR_UE_TRANSPORT/nr_prach.c:57

// prachF[0..dftlen-1] = {0}  ← 共用的頻域疊加緩衝（跨所有 FDM occasions）

// ── 外層迴圈: 所有 FDM occasions（0 到 fd_occasion）──
for current_fd = 0 to fd_occasion:

    // 計算此 FD occasion 的根序列（若尚未計算）
    compute_nr_prach_seq(prach_sequence_length,
                         num_root_sequences[current_fd],
                         root_sequence_index[current_fd],
                         X_u)

    // 此 FD occasion 的起始子載波
    k = 12 × k1[current_fd] - 6 × N_RB_UL
    k = k × K + kbar   // 換算到 PRACH SCS

    // ── 計算所有要疊加的 preamble 總數 ──
    total_sequences = 0
    for m = 0 to num_attack_sequences - 1:
        if unrestricted_set:
            m_num_shifts[m] = (NCS==0) ? 1 : N_ZC/NCS
        else:
            m_num_shifts[m] = 按 TS 38.211 高速集計算
        total_sequences += m_num_shifts[m]

    // 振幅縮放：防止疊加溢出（等功率分配）
    amp = original_amp / sqrt(total_sequences)
    //    ↑ 總功率保持不變，各 preamble 振幅等比縮小

    // ── 中層迴圈: 多根序列 ──
    for m = 0 to num_attack_sequences - 1:
        seq_idx = (preamble_offset - first_nonzero_root_idx + m)
                  mod num_root_sequences[current_fd]
        Xu = X_u[seq_idx]   // 第 m 個根 ZC 序列

        // ── 內層迴圈: 每個根序列的所有循環位移 ──
        for v = 0 to m_num_shifts[m] - 1:
            if unrestricted_set:
                shift_v = v × NCS
            else:
                shift_v = d_start × (v/n_shift_ra) + (v mod n_shift_ra) × NCS

            current_k = k   // 從此 FD occasion 的起始子載波開始

            // ── 最內層: 將移位後的 ZC 序列疊加進 prachF ──
            offset2 = 0
            for n = 0 to N_ZC - 1:
                if offset2 >= N_ZC: offset2 -= N_ZC

                // 生成相位旋轉子（cyclic shift）
                w  = 2π × offset2 / N_ZC
                ru = exp(jw) = (cos(w), sin(w))  × 32767

                // ZC 序列乘以振幅縮放
                Xu_scaled = Xu[n] × amp / 2^15

                // 計算此子載波的貢獻
                p = Xu_scaled × ru / 2^15

                // ★ 疊加：直接累加到共用頻域緩衝 ★
                prachF[current_k].real += p.real
                prachF[current_k].imag += p.imag
                // 多個根序列、多個循環位移、多個 FDM occasion
                // 的信號全部疊加在同一個 prachF 上

                current_k = (current_k + 1) mod (dftlen/2)
                offset2  += shift_v

// ── 疊加完成後做單次 IDFT → 時域信號 ──
idft(dftsize, prachF, prach_time)
// 所有疊加的 preamble 一次性轉為時域

// ── 加入 CP 並依 format 複製重複段 ──
prach_out = [CP] + [prach_time] × reps
三層疊加的整體對照

┌─────────────────────────────────────────────────────────────────┐
│               UE TX  (generate_nr_prach)                        │
│                                                                 │
│  prachF = Σ  Σ  Σ  (Xu[m,seq_idx][n] × e^{j2π·shift·n/N_ZC}) │
│          fd  m  v                                               │
│  其中:                                                          │
│    fd  = FDM occasion index (0..fd_occasion)                    │
│    m   = root sequence index (0..num_attack_sequences-1)        │
│    v   = cyclic shift index (0..m_num_shifts[m]-1)             │
│    amp = original_amp / sqrt(total_sequences)  (功率等分)       │
│                                                                 │
│  → 單次 IDFT → 時域 PRACH 信號                                  │
└────────────────────────────┬────────────────────────────────────┘
                             │ 無線通道
┌────────────────────────────▼────────────────────────────────────┐
│               RU RX  (rx_nr_prach_ru)                           │
│                                                                 │
│  per antenna aa:                                                │
│    FFT 各重複段: rxsigF[aa][i·dftlen..(i+1)·dftlen-1]          │
│                                                                 │
│  相干疊加 (coherent combining over repetitions):                │
│    rxsigF_combined[aa][k..k+N_ZC-1]                            │
│      = Σ rxsigF[aa][k + i·dftlen]    i=0..reps-1              │
│                                                                 │
│  結果: rxsigF[aa] 只保留 ZC 頻段，SNR ↑ reps 倍                 │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│               gNB PHY  (rx_nr_prach)                            │
│                                                                 │
│  for each preamble candidate p:                                 │
│    Xu = ZC sequence for root[p]                                 │
│                                                                 │
│    非相干疊加 (incoherent combining over antennas):              │
│    prach_ifft[τ] = Σ |IFFT(rxsigF[aa] · Xu*)|²[τ]             │
│                   aa                                            │
│                 = Σ |h_aa * ZC_p|²[τ]   (延遲剖面 PDP)         │
│                                                                 │
│    正規化: prach_ifft /= (IFFT_SIZE × nb_rx)                    │
│    偵測: argmax_τ prach_ifft[τ] in [shift_p, shift_p+NCS2)     │
│                                                                 │
│    → (max_preamble_index, max_energy, max_delay/TA)             │
└─────────────────────────────────────────────────────────────────┘
關鍵變數總覽
變數	所在函數	疊加類型	說明
prachF[k].r += p.r	generate_nr_prach	頻域相干	多 preamble / 多 FDM 疊加
rxsigF_tmp[j] += rxsigF2[k2 + i×2×dftlen]	rx_nr_prach_ru	頻域相干	跨重複段疊加
prach_ifft[i] += re² + im²	rx_nr_prach	能量非相干	跨天線功率累積
amp = orig / sqrt(total)	generate_nr_prach	功率控制	防止 clip，總功率恆定
prach_ifft[i] /= IFFT_SIZE × nb_rx	rx_nr_prach	正規化	消除 IFFT 增益與天線數



---

```latex
Algorithm~\ref{alg:signal-gen} summarizes the complete signal-generation procedure, translating the mathematical model above into an executable sequence of operations.

\begin{algorithm}[htbp]
\caption{Composite PRACH Attack Signal Generation}
\label{alg:signal-gen}
\begin{algorithmic}[1]
\Require $M$ root sequences $\{u_0,\ldots,u_{M-1}\}$, RACH config $(N_{ZC}, N_{CS})$, $N_{FD}$ FD occasions
\Ensure Composite time-domain PRACH signal $y_{attack}(t)$
\State Compute $V_m$ for each root $m$; accumulate $T \leftarrow \sum_{m=0}^{M-1} V_m$
\State Set amplitude scale: $c_{rms} \leftarrow A_{max}/\sqrt{T}$ \Comment{Eq.~\eqref{eq:crms}: total power held constant}
\State Initialize shared frequency buffer: $Y[k] \leftarrow 0$ for all $k$
\For{FD occasion $f = 0$ \textbf{to} $N_{FD}-1$}
    \For{root index $m = 0$ \textbf{to} $M-1$}
        \State Retrieve ZC root sequence $X_{u_m}[\cdot]$
        \For{cyclic shift $v = 0$ \textbf{to} $V_m-1$}
            \State Compute shift offset $C_{v,m}$ (unrestricted or restricted set)
            \State $Y[k_f : k_f{+}N_{ZC}] \mathrel{+}= c_{rms} \cdot X_{u_m} \cdot e^{\,j2\pi C_{v,m}(\cdot)/N_{ZC}}$ \Comment{Eq.~\eqref{eq:attack_signal}}
        \EndFor
    \EndFor
\EndFor
\State $y_{attack}(t) \leftarrow \mathrm{IDFT}\{Y[k]\}$; prepend cyclic prefix; repeat for \textit{reps} segments
\State \Return $y_{attack}(t)$
\end{algorithmic}
\end{algorithm}
```

---

```latex

Algorithm~\ref{alg:flooding-loop} captures the complete attack execution flow, integrating the PHY-layer modifications and MAC-layer overrides described above into a single persistent loop.

\begin{algorithm}[htbp]
\caption{MSG1 Flooding Attack Main Loop}
\label{alg:flooding-loop}
\begin{algorithmic}[1]
\Require RACH configuration decoded from SIB1
\State Derive root sequence set $\{u_0,\ldots,u_{M-1}\}$, FD occasion table, $N_{FD}$ from SIB1
\State Fix transmit power: $P_{tx} \leftarrow P_{max}$
\While{\textbf{True}} \Comment{Infinite flooding loop; no exit condition}
    \State Wait for next available PRACH slot
    \For{each occasion RO across all $N_{FD} \times N_{t,slot}$ time--frequency resources}
        \State $y \leftarrow$ \Call{GenerateCompositeSignal}{} \Comment{Algorithm~\ref{alg:signal-gen}: all $T$ preambles superimposed}
        \State Transmit $y$ at power $P_{tx}$
    \EndFor
    \State Discard all received downlink PDUs \Comment{Suppress RAR / MSG2 decoding}
    \State Reset RA state $\leftarrow$ \textsc{Msg1-Ready} \Comment{Bypass attempt counter \& RAR window timer}
\EndWhile
\end{algorithmic}
\end{algorithm}
```

---

```latex

Algorithm~\ref{alg:rapp} consolidates the event-driven detection logic and the mitigation decision into a single closed-loop procedure, showing how the four anomaly conditions gate the three-step response.

\begin{algorithm}[htbp]
\caption{rApp Event-Driven PRACH Anomaly Detection and Mitigation}
\label{alg:rapp}
\begin{algorithmic}[1]
\State Retrieve current gNB configuration via O1 interface; push baseline snapshot to TEIV
\While{\textbf{True}} \Comment{Asynchronous Kafka polling loop}
    \State $\mathit{event} \leftarrow$ poll Kafka topic \texttt{prachAttackDetected}
    \If{no event} \textbf{continue} \EndIf
    \State Aggregate RA metrics over analysis window $W$:
           $\{\texttt{ra\_initiated},\ \texttt{ra\_succeeded},\ \texttt{success\_rate},\ \texttt{failed\_attempts}\}$
    \State $\mathit{attack} \leftarrow \mathbf{False}$
    \If{$\texttt{ra\_succeeded} = 0$ \textbf{and} $\texttt{ra\_initiated} > 0$}
        \State $\mathit{attack} \leftarrow \mathbf{True}$ \Comment{Zero-success: unambiguous attack indicator}
    \EndIf
    \If{$\texttt{failed\_attempts} \geq \texttt{preambleTransMax}$}
        \State $\mathit{attack} \leftarrow \mathbf{True}$ \Comment{Saturation: retry limit reached}
    \EndIf
    \If{$\texttt{ra\_initiated} > N_{vol}$ \textbf{and} $\texttt{success\_rate} < \alpha_{flood}$}
        \State $\mathit{attack} \leftarrow \mathbf{True}$ \Comment{High-volume low-success flooding pattern}
    \EndIf
    \If{$\texttt{success\_rate} < \alpha_{op}$}
        \State $\mathit{attack} \leftarrow \mathbf{True}$ \Comment{Success-rate below operational threshold}
    \EndIf
    \If{$\mathit{attack}$}
        \State Reconfigure via O1: \texttt{prach-ConfigurationIndex}, \texttt{absoluteFrequencySSB}, \texttt{dl\_absoluteFrequencyPointA}
        \State Synchronize updated configuration to TEIV
        \State Trigger gNB restart to apply new parameters and purge transient RA state
    \EndIf
\EndWhile \Comment{Loop continues; renewed flooding triggers another mitigation cycle}
\end{algorithmic}
\end{algorithm}
```

---

```latex

Algorithm~\ref{alg:rapp} consolidates the event-driven detection logic and the mitigation decision into a single closed-loop procedure, showing how the four anomaly conditions gate the three-step response.

\begin{algorithm}[htbp]
\caption{rApp Event-Driven PRACH Anomaly Detection and Mitigation}
\label{alg:rapp}
\begin{algorithmic}[1]
\State Retrieve gNB config via O1; push baseline snapshot to TEIV
\While{\textbf{True}} \Comment{Asynchronous Kafka polling loop}
    \State $\mathit{event} \leftarrow$ poll Kafka topic \texttt{prachAttackDetected}
    \lIf{no event}{\textbf{continue}}
    \State Aggregate RA metrics over window $W$:
    \Statex \hspace{2.9em}$\{\texttt{ra\_initiated},\ \texttt{ra\_succeeded},\ \texttt{success\_rate},\ \texttt{failed\_attempts}\}$
    \State $\mathit{attack} \leftarrow \mathbf{False}$
    \lIf{$\texttt{ra\_succeeded}=0$ \textbf{and} $\texttt{ra\_initiated}>0$}{$\mathit{attack}\leftarrow\mathbf{True}$} \Comment{Zero-success}
    \lIf{$\texttt{failed\_attempts}\geq\texttt{preambleTransMax}$}{$\mathit{attack}\leftarrow\mathbf{True}$} \Comment{Saturation}
    \lIf{$\texttt{ra\_initiated}>N_{vol}$ \textbf{and} $\texttt{success\_rate}<\alpha_{flood}$}{$\mathit{attack}\leftarrow\mathbf{True}$} \Comment{Flooding}
    \lIf{$\texttt{success\_rate}<\alpha_{op}$}{$\mathit{attack}\leftarrow\mathbf{True}$} \Comment{Low SR}
    \If{$\mathit{attack}$}
        \State Reconfigure via O1: \texttt{prach-ConfigurationIndex},
               \texttt{absoluteFrequencySSB}, \texttt{dl\_absoluteFrequencyPointA}
        \State Synchronize updated configuration to TEIV
        \State Trigger gNB restart
    \EndIf
\EndWhile
\end{algorithmic}
\end{algorithm}
```
