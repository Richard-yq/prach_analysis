# 論文與系統優化修改清單 (Thesis & System Optimization Checklist)

本清單整理自您的修改意見，包含圖表勘誤、攻擊情境探討、防禦演算法優化、以及論文新增個案分析 (Case Study) 等項目。

---

---

## ✅1. 🔍 圖表與勘誤 (Errata & Diagrams)

- [x] **Msg1 與 RAR 之間的時間間隔描述修正**
  - **細節**：修正第 13 頁 (p. 13) 內容。Msg1 到 RAR 之間存在一段時間間隔（在 RAR window 前面有一個 gap）。
  - **待辦事項**：
    - [x] 精確修正內文文字描述。
    - [x] 更新相對應的時序圖表 (Sequence Diagram / Timeline Diagram)，標示出該 Gap。

---

## 2. 🛡️ 攻擊情境與合理性探討 (Attack Scenario Feasibility)

- [ ] **探討攻擊者不接收 RAR 下的 UE 存活可能性**
  - **細節**：分析第 23、36 頁。即使攻擊者完全忽略且不接收基站發送的 RAR，是否仍有部分合法 UE 可以成功存活並入網？
  - **分析要點**：
    - 評估碰撞率、RAR 資源分配上限。
    - 撰寫理論分析或提供仿真/實驗數據支持。
- [x] **Long Preamble (長前導碼) 影響評估**
  - **細節**：分析第 21 頁。若改用 Long Preamble，在序列長度測試上是否會引發其他潛在問題？
  - **分析要點**：
    - 序列長度（如 $L=839$ vs $L=139$）對抗多路徑衰落、都卜勒頻移及防禦干擾能力的差異。
    - 評估長前導碼的計算複雜度與保護時段 (Guard Period) 對覆蓋範圍的潛在限制。
- [x] **Preamble Partitions 與 HO (Handover) 阻絕可行性**
  - **細節**：分析 Preamble 分割的影響。若攻擊者刻意「只攻擊 Contention-free preambles」以阻絕切換 (Handover, HO) 的可行性。
  - **分析要點**：
    - 分析 CF-preamble 被干擾時對 HO 成功的衝擊。
    - 評估攻擊者如何識別或精準覆蓋 CF-preamble 區段。

---

## ✅3. 💡 基站重啟與 DoS 悖論解決方案 (Defensive Logic & Algorithm Optimization)

- [x] **rAPP 緩解流程邏輯修正**
  - **細節**：修改 rAPP 的決策邏輯流程。偵測到攻擊時，**不應直接重啟基站**，而應優先進行以下動作：
    - **優先級 1**：透過 O-RAN 介面驅動切換機制 (Handover, HO)，將現有可切換的 UE 先行移轉至鄰近的正常基站。
    - 已在緩解策略中加入HO 的機制 Detect -> HO -> ->Recovery(reboot) -> Mitigation
- [x] **防禦演算法優化 (動態 Rx Power Threshold)**
  - **細節**：合法 UE 在遭受全 preamble 攻擊時，其能量會分散在不同的 preambles 上。
  - **優化設計**：rAPP 根據偵測到的攻擊功率，動態調整接收功率閾值 (Rx power threshold)。藉此拉高門檻以過濾掉低功率干擾，讓部分強訊號的 UE 可以順利上線，避免直接重啟基站。
  - 方法：已與學弟討論或許可以引入ML方式動態調整閥值，來做防禦演算法優化
- [x] **攻擊者離去判定機制設計**
  - **細節**：基站進入安全/節能模式後，系統如何精準判定攻擊者已離去（Attacker 跑掉）並安全回復正常服務。
  - **設計方向**：例如定期以低功率或短暫重啟偵測（Probe），或結合物理層能量偵測 (RSS / RSSI) 來研判。
  - 補充說明在論文 3.6 Discussion on Practical Operational Scenarios

---

## ✅4. 📝 論文補強：新增個案分析 (Case Study) :done:

需在內文中新增「**個案分析 (Case Study)**」章節，詳細分析並模擬以下三種實務情境：

- [x] **Case 1: 成功切換 (Successful Handover)**
  - **場景**：遭受攻擊時，周邊有鄰近基站支援，UE 順利 Handover 出去後原基站重啟。
  - **分析指標**：切換成功率、服務中斷時間、信令開銷。
- [x] **Case 2: 攻擊者離去判定 (Attacker Departure Detection)**
  - **場景**：基站進入安全模式後，系統精準判定攻擊者已離去並安全恢復正常服務的流程與演算法機制。
  - **分析指標**：判定準確度、恢復時間 (Recovery Delay)、誤判機率。
- [x] **Case 3: 攻擊者無法離去 (Persistent Attacker)**
  - **場景**：攻擊者持續在附近不走，基站與鄰近基站協調，共同應對持續干擾，保障服務品質與網路安全。
  - **分析指標**：多基站協同防禦機制、頻譜資源重分配、降級服務保障。
  - 補充說明在論文 3.6 Discussion on Practical Operational Scenarios

---

## ✅5. 🤖 實作與差異探討 (Implementation & OAI/SMO Questions)

- [x] **提問/釐清 OAI 實現 Attack 與 SMO rAPP 的解法差異**
  - **問題點**：如何在 OAI 實作攻擊，與在 SMO rAPP 端實現緩解方案，兩者在架構、控制介面（E2 vs O1）以及反應時間上有何具體差異？
  - 分層兩點
    1.  攻擊：直接修改 OAI gNB 的原始碼，在特定時間或特定資源上人為製造干擾：
      - 定位 RACH 資源： 在 MAC/PHY 層（例如 nfapi 介面或 L1 處理 Preamble 的函式中），攔截對應到特定 Random Access Occasion (RO) 的訊號。
      - 注入噪聲/篡改數據： 在 gNB 接收 Preamble 訊號的 Buffer 中，直接加上高斯白噪聲（AWGN）或是將其能量調零，模擬 Preamble 被強烈干擾而無法被 gNB 偵測（導致計數器破表、連線失敗）的狀況。
      - 精準射頻干擾： 依據 3GPP 規範的 RACH 配置，僅在 RO 出現的時頻資源（Time-Frequency Grid）上發射高功率信號，精準蓋掉合法 UE 的 Preamble。
    2.  防禦：SMO（Service Management and Orchestration）與其內部的 rApp 屬於 管理面（Management Plane）與非即時智慧（Non-RT RIC） 的範疇。它的核心邏輯是「收集數據 → 分析異常 → 下達策略（Policy）」。
