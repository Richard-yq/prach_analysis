# 曹教授口試與審查意見優化清單 (Professor Tsao's Review Feedback Checklist)

本清單針對「攻擊判定基準」、「演算法定量化」、「OCUDU 環境驗證」以及「雙 UE 攻擊實驗」等審查核心意見進行結構化整理，並提供後續修改之定性與定量規劃。

---

## 1. 🔍 攻擊判定基準 (Attack Detection Criterion)

評估系統如何區分「惡意協定感知攻擊」與「正常 UE 異常/Bug」的判定準則，避免誤判。

- [x] **定義「持續一直收到」之定量定義**
  - **量化指標**：本地 gNB 檢測引擎定義「持續收到」為：**連續 $N_{th}$ 個隨機接入時機 (RO) 皆偵測到 Preamble 訊號**。
  - **閾值設定**：對齊 3GPP 規範中的最大前導碼發送次數 `preambleTransMax`（本系統配置為 20）。將 $N_{th}$ 設定為該上限的兩倍：
    $$N_{th} = 2 \times \text{preambleTransMax} = 40$$
  - **判定邏輯**：連續 40 個 RO 出現 Preamble 活動在數學上不可能由單一合法 UE 產生（其最大重試限制為 20），這代表著異常且持續的隨機接入信道占用。此定量方法可精確過濾正常突發話務 (Normal Bursty Traffic) 引起的假警報。

- [x] **惡意攻擊與普通 UE Bug/異常之辨識機制**
  - **跨層關聯分析 (Cross-layer Correlation)**：結合 PHY/MAC 層與 RRC 層數據。
    - **發起接入數 ($N_{init}$)**：PHY/MAC 層偵測到的 Preamble 總數。
    - **成功接入數 ($N_{succ}$)**：完成完整 4-Step CBRA (Msg1-Msg4) 並成功建立 RRC 連線的 UE 數量。
  - **防誤判核心特徵**：
    - **特徵分歧 (Divergence)**：在攻擊洪泛下，PHY/MAC 層的 $N_{init}$ 會異常暴增，但 RRC 層的成功數 $N_{succ}$ 依然趨近於 0。此種「底層大量發起、上層零成功」的極端分歧現象在正常的高負載或單一 UE 異常 Bug 下皆不可能發生。

| 特徵維度 | 正常 UE 異常 / Bug (故障) | 惡意協定感知攻擊者 (Attacker) |
| :--- | :--- | :--- |
| **Preamble 數量** | 通常僅使用單一或極少數的 Preamble。 | 同一 RO 內發送大量、甚至覆蓋全區段 (64個) 的 Preambles。 |
| **退避行為 (Backoff)** | 遵循 MAC 層 Backoff Indicator (BI) 的隨機退避延遲限制。 | 完全忽略 BI 限制，以最高頻率或連續時槽 (Slots) 進行洪泛攻擊。 |
| **Msg3 響應率** | 若收到 RAR，UE 會嘗試發送 Msg3（即使因 Bug 導致 Payload 錯誤）。 | 完全忽略 RAR，不發送對應的 Msg3，純粹消耗 UL Grant 資源。 |
| **FDM RO 分佈** | 僅在單一頻域資源 (FDM occasion) 上發送。 | 在多個頻域 RO (如 msg1-FDM=2/4/8) 上同時發送。 |
| **跨層統計特徵** | $N_{init}$ 微幅上升，後續 RRC 連線或 Msg3 仍有嘗試與部分成功。 | $N_{init}$ 呈指數級飆升，但 $N_{succ}$ 保持為 0。 |

---

## 2. 📊 演算法定量化 (Algorithm Quantization)

說明演算法中判斷數字（如偵測閾值、分析窗口）的理論計算方法與定量依據。

- [x] **隨機接入資源消耗與統計指標定量化**
  - **分析窗口長度 ($W$)**：設定為 **10 秒 (10 s)**。平衡檢測延遲與統計穩定度，為決策規則提供充足的樣本。
  - **隨機接入成功率 ($RSR$)** 定量指標：
    $$RSR = \frac{N_{succ}}{N_{init}} \times 100\% \quad (N_{init} = 0 \implies RSR = 0\%)$$
  - **隨機接入失敗次數 ($FA$)** 指標：
    $$FA = N_{init} - N_{succ}$$
  - **活動 UE 數 (\texttt{ue\_count}) 與決策閾值 ($\tau$) 關聯**：
    - 作為防禦動作（如重啟基站）的成本感知依據。連線的 \texttt{ue\_count} 越高，代表中斷代價越大，系統將動態調高決策閾值 $\tau$，避免在有大量活躍業務時進行盲目重啟，從而落入 DoS 悖論。
- [x] **核心數據與指標對照表**
  - 填補並校對防禦演算法決策時的核心參數與基準：

| 參數符號 | 參數名稱 | 定量值 | 計算與判定依據 (論文實作) |
| :--- | :--- | :--- | :--- |
| $N_{th}$ | 本地 gNB 告警觸發閾值 | 40 個連續 ROs | $2 \times \text{preambleTransMax}$，排除單一正常 UE 的最大嘗試。 |
| $W$ | rApp 分析窗口長度 (Window) | 10 秒 (10 s) | 用於聚合 RACH 指標，在統計穩定度與回應時間之間取得平衡。此窗口長度可根據實驗場域之實際情況進行調整與設定。 |
| $\text{preambleTransMax}$ | 最大前導碼發送次數 | 20 次 | 依據 3GPP 規範的 UE MAC 配置上限。 |
| $RSR$ | 隨機接入成功率 | 依據信道健康度動態計算 | 主要健康度指標，低於正常 baseline (如 < 90%) 則判定異常。其中 baseline 是由實驗場域無攻擊環境下的 RSR 作為參考定義，可根據實驗場域的實際 RSR 進行調整。 |
| $FA$ | 隨機接入失敗數 | 依據 $N_{init} - N_{succ}$ 計算 | 累計之無效 Msg1 洪泛規模。 |
| \texttt{ue\_count} | 活動 UE 數量 | 實時監控 | 決策成本指標，與防禦反應門檻 $\tau$ 成正比。 |

---

## 3. 🧪 環境驗證與測試 (Environmental Verification)

利用實體/虛擬 O-RAN 分離式架構 (OCUDU) 進行針對性測試。

- [x] **OCUDU 架構下的測試環境架設**
- [x] **Long Preamble 攻擊成效測試**
  - **參數配置**：改用 3GPP Preamble Format 0 (序列長度 $L=839$)。
  - **測試要點**：
    - 比較 Long Preamble 與 Short Preamble ($L=139$) 在相同攻擊強度下的 Legitimate UE 接入成功率 (RSR)。

---

## 4. 👥 雙 UE 聯合攻擊實驗 (Dual-UE Cooperative Attack Experiment)

補上兩隻 UE 同時發起攻擊的實驗，評估協同/多點攻擊的衝擊。

- [ ] **雙 UE 攻擊場景設計**
- [ ] **評估指標與實驗結果紀錄**
  - 記錄雙 UE 在被攻擊時的以下核心數據，並與單 UE 攻擊對比：
    - [ ] **資源耗盡速度**：gNB 的隨機接入緩衝區 (RA Buffer) 滿載所需時間（毫秒級）。
    - [ ] **合法 UE 成功率 (RSR)**：在不同攻擊間隔 (Attack Interval) 下，合法 UE 的接入率衰減曲線。
