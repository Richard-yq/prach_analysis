# 2026-06-15 碩士論文口試意見整理與行動指南

## 📋 待辦事項清單 (Todo List)

### ✍️ 論文內容與圖表修改 (Thesis & Figure Modifications)
- [ ] **流程圖替換**：第 26 頁的 Mitigation 演算法，將程式碼改為流程圖說明 (Ray)
- [ ] **圖表說明補強**：第 36 頁，補上下方圖表為什麼「間隔 4 重複」的詳細說明 (Ray)
- [ ] **文字精簡與去重**：修正論文內過多重複的敘述 (Prof. S. T. Sheu)
- [ ] **時間與參數說明**：
  - [ ] 說明第 13 頁 Msg 1 到 RAR 之間的時間差 (Prof. S. T. Sheu)
  - [ ] 說明第 34 頁的 log 是如何產生的 (Prof. R. T. Wang)
  - [ ] 補充定量的說明與計算方式 (Prof. T. Y. Hsu)
  - [ ] 說明 Phase 1 + Phase 2 總共需要花費多少時間 (Prof. R. T. Wang)
- [ ] **比較表格**：新增矛與盾的比較表格，分析自己設計的防禦機制與其他研究的優缺點、攻擊種類 (Prof. S. L. Tsao)
- [ ] **AI 比例說明**：說明論文中使用 AI 的比例與部分 (Prof. S. L. Tsao)

### 💻 簡報與 Demo 調整 (Slides & Demo Adjustments)
- [ ] **Demo UI 統一**：將自己與 Ming 的 UE Demo Web UI 版本進行統一 (Ray)
- [ ] **Demo 效果優化**：Demo 影片/展示補上語音旁白與文字說明（目前螢幕字體太小，不易看出呈現的概念）(Ray)
- [ ] **實體標籤**：硬體或設備標籤請使用印表機列印出貼上 (Ray)
- [ ] **未來工作 (Future Work)**：簡報中需補充並介紹 Future Work (Ray)

### 🔬 演算法與實驗分析 (Algorithm & Analysis)
- [ ] **參數決定機制**：說明/確定 Mitigation 演算法中的參數是如何決定的？判斷的關鍵數字為何？ (Ray, Prof. T. Y. Hsu)
- [ ] **防禦機制優化 (可變動門檻)**：
  - [ ] 針對「同時多 Preamble 攻擊（功率較低限制）」的情況，研究是否可調整 detection threshold (Prof. S. T. Sheu)
  - [ ] 定義何謂「持續一直收到」？如何界定這是一場攻擊？異常的 UE 是否會被誤判為攻擊？ (Prof. T. Y. Hsu)
  - [ ] 說明判讀 False Alarm 的具體數值是多少 (Prof. T. Y. Hsu)
- [ ] **攻擊合理性探討**：
  - [ ] 分析如果攻擊者也能讀取 SIB1 的情況與影響 (Prof. S. T. Sheu)
  - [ ] 說明與論證「不攻擊 Msg 3」的合理性（第 23, 33 頁）(Prof. S. T. Sheu)
- [ ] **HO 機制與 rAPP 策略**：
  - [ ] 針對 Contention-free HO 進行攻擊測試與分析 (Prof. S. T. Sheu)
  - [ ] 目前 rAPP 重啟需要先驅動 HO。研究「能換手的換手，不能換手的就等待，或者讓基站進入 Sleep Mode」的可行性，並思考如何偵測攻擊者已離去 (Prof. S. T. Sheu)

### 🧪 實驗與測試項目 (Testing & Experiments)
- [ ] **系統與環境測試**：
  - [ ] 測試 L2/3 OAI + Ariel cuPHY 運行在 DGX Spark + Pegatron RU 的環境 (Ray)
  - [ ] 測試與確認 OAI gNB 的實際距離與影響 (General)
  - [ ] 進行先換手再緩解的機制測試 (General)
  - [ ] 討論是否只針對 OAI 進行攻擊 (General)
- [ ] **OCUDU 平台測試**：
  - [ ] 使用 OCUDU 進行測試 (Prof. T. Y. Hsu)
  - [ ] 使用 OCUDU 測試 Long Preamble (Prof. T. Y. Hsu)
- [ ] **Long Preamble 評估**：分析如果使用 Long Preamble 是否會有其他潛在問題（第 21 頁） (Prof. S. T. Sheu)
- [ ] **多 UE 與入網分析**：
  - [ ] 補上兩隻 UE 同時攻擊的實驗結果 (Prof. T. Y. Hsu)
  - [ ] 分析並評估攻擊對於「入網成功率」與「Access Delay」的影響 (Prof. S. L. Tsao, Prof. T. Y. Hsu)
- [ ] **跨基站攻擊測試**：嘗試對 VIAVI 與 TY 基站進行攻擊測試 (Prof. T. Y. Hsu)

---

## 👨‍🏫 委員意見詳細紀錄 (Detailed Comments)

### 👤 Ray
- 測試 OAI L2/3 + Ariel cuPHY 於 DGX Spark + Pegatron RU。
- 第 26 頁：是否可用流程圖，而不是程式碼來說明演算法。
- Mitigation 演算法的參數要如何決定？
- 第 36 頁：補上下方的圖為什麼間隔 4 重複的說明。
- 第 39 頁：目前可以同時送幾個 Msg3？
- 與 Ming 的 UE Demo 的 Web UI 版本需要統一。
- 實體設備標籤請用印表機印出。
- Demo 要補上語音旁白與文字，目前螢幕字體太小，看不出來要呈現的概念。
- Future Work 需要在簡報中介紹。

### 👤 Prof. S. L. Tsao (曹孝櫟 教授)
- 既然做了防禦（盾），需要與其他人的研究進行比較。例如：你做了很多攻擊，那跟其他人比較起來，你的矛與盾的優缺點各自為何？建議用一個表格做出比較。
- 論文中使用 AI 的比例是多少？
- 評估攻擊對於入網成功機率、Access Delay 的影響。

### 👤 Prof. S. T. Sheu (許紹婷 教授)
- 論文內有太多重複的敘述，需要精簡。
- 第 13 頁：Msg 1 到 RAR 之間有一段時間差，需要說明。
- 第 28 頁：如果攻擊者也能讀取 SIB1，會對防禦造成什麼影響？
- 盾的設計稍嫌簡單。建議可調整 detection threshold，來解決同時多 preamble 攻擊（且功率較低）的限制。
- 第 21 頁：如果改用 Long Preamble 會不會有什麼問題？
- 第 23、33 頁：不攻擊 Msg 3，這樣做合理嗎？需要給出合理解釋。
- 嘗試攻擊 Contention-free HO。
- 關於 rAPP 重啟與 HO 策略：rAPP 目前要重啟，需要先驅動 HO。原則是能換手的就換手，不能換手的就等待，或者讓基站進入 Sleep Mode。另外，該如何知道 Attacker 已經跑掉了？

### 👤 Prof. T. Y. Hsu (許騰尹 教授)
- 第 26 頁：如何判定是攻擊？何謂「持續一直收到」？UE 的異常是否會被誤當作是攻擊？
- 第 27 頁：判讀 False Alarm 的數值是多少？
- 用 OCUDU 測試 Long Preamble。
- 補上兩隻 UE 同時進行攻擊的結果。
- 補充定量的說明，並給出數字是如何計算出來的。
- 說明演算法的判斷數字/門檻值。
- 進行 OCUDU 平台的測試。
- 分析入網成功率。
- 嘗試對 VIAVI 與 TY 基站進行攻擊看看。

### 👤 Prof. R. T. Wang (王瑞堂 教授)
- Phase 1 + Phase 2 的流程需要耗時多久？
- 第 34 頁：如何產生你的 log？

---

### 📌 補充/初步討論紀錄 (Preliminary Notes)
- 先換手再緩解
- 討論是否只對 OAI 進行攻擊
- 測試 OCUDU
- Attacker距離