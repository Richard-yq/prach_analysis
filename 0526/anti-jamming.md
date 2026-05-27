Ran command: `git add 0526`
Ran command: `git commit -m "add slide related work survey"`
Ran command: `git push`
Viewed Jamming_Attacks_and_Anti-Jamming_Strategies_in_Wireless_Networks_A_Comprehensive_Survey-2.pdf

這篇論文 **《Jamming Attacks and Anti-Jamming Strategies in Wireless Networks: A Comprehensive Survey》** 是一篇非常全面的綜述，系統性地整理了各種無線網路在實體層（PHY）與媒體存取控制層（MAC）所面臨的的干擾攻擊（Jamming Attacks）以及相對應的**抗干擾策略（Anti-Jamming Strategies）**。

論文在最後將文獻中所有的抗干擾方法整理為一個總體框架（如 **Table XI** 所示），並針對 9 種不同的無線網路場景進行了深入的技術分類。以下是這篇論文所整理出的主要抗干擾方法：

---

### 一、 核心通用抗干擾技術（Table XI 總結）

1. **跳頻展頻（Frequency-Hopping Spread Spectrum, FHSS）**：透過發射端與接收端同步且快速地在不同頻道間切換，以避開窄頻干擾（主要用於藍牙、認知無線電等）。
2. **直接序列展頻（Direct Sequence Spread Spectrum, DSSS）**：利用偽隨機展頻碼將信號帶寬擴展，以提高對窄頻干擾的抵抗力（主要用於 ZigBee、802.11b、GPS）。
3. **啾頻展頻（Chirp Spread Spectrum, CSS）**：利用頻率隨時間線性變化的啾頻脈衝（Chirp pulse）進行調變，天生對窄頻干擾與都卜勒頻移有極佳的魯棒性（LoRa 的核心技術）。
4. **多天線（MIMO）技術**：利用空間維度（Spatial domain），透過空間濾波、信號投影等方法將干擾信號零陷（Nulling），或投影到與干擾正交的子空間（用於行動通訊、Wi-Fi、車聯網等）。
5. **天線相位陣列與類比波束成形（Antenna Phase Array & Analog Beamforming）**：調整天線相位以形成指向性波束，增強期望信號並抑制干擾源方向的信號（主要用於 GPS 與毫米波 mmWave 通訊）。
6. **速率自適應算法（Rate Adaptation Algorithms, RAA）**：根據信道質量動態調整調變與編碼策略（MCS），在輕微干擾下降低速率以維持通訊。
7. **功率控制機制（Power Control Mechanisms）**：動態調整發射功率，提高信干噪比（SINR），但受限於設備的功率預算（Power budget）。
8. **中繼輔助策略（Relay-Aided Strategies）**：當節點受到嚴重干擾時，透過未受干擾的鄰近節點（或無人機 UAV）進行數據轉發。
9. **頻道重新選擇機制（Channel Re-selection）**：在檢測到干擾後，動態切換到其他乾淨的頻道（常用於認知無線電 CRNs）。
10. **分包與副本複製（Packet Fragmentation & Fragment Replication）**：將大數據包分割成較小的片段以降低被干擾的概率，或複製發送多個副本（用於 Wi-Fi、ZigBee 等）。
11. **信道編碼方案（Channel Coding Schemes）**：利用強大的糾錯碼（如 LDPC、Turbo 碼、里德-所羅門碼 RS）來修復被干擾破壞的位元。
12. **濾波與屏蔽技術（Filtering & Masking）**：在頻域或時域設計濾波器以濾除特定干擾成分（常用於 GPS 禦防單音干擾）。

---

### 二、 針對特定無線網路的抗干擾方法

#### 1. 無線區域網路（WLAN / Wi-Fi）
* **頻道跳躍技術**：引入「視窗駐留（Window dwelling）」與「欺騙機制」，讓接收端動態調整發送時間，並引誘干擾器去攻擊無效頻道。
* **MIMO 空間干擾消除**：
  * **正交投影（Orthogonal Subspace Projection）**：在干擾發生時，將接收信號投影到與干擾信號正交的子空間來解調數據。
  * **多頻道比例（MCR）解碼**：在發射端靜默時估算干擾器的空間信道特徵，進而將干擾消除。
  * **盲抗干擾空間濾波**：無需預先知道干擾器的信道信息，直接利用空間投影進行盲干擾抑制與同步。
* **隨機化速率自適應**：為應對專門攻擊 RAA 的智能干擾器，隨機且不可預測地切換傳輸速率，破壞干擾器的預測。
* **小區呼吸（Cell Breathing）**：動態調整 AP 的發射功率和覆蓋範圍，將受干擾的用戶分流負載均衡到其他 AP。
* **DeepWiFi（機器學習防禦）**：利用深度學習進行 I/Q 信號特徵提取、卷積神經網路（CNN）頻道分類（空閒/忙碌/受干擾），並使用射頻指紋（RF fingerprinting）驗證合法用戶。

#### 2. 行動通訊網路（4G LTE / 5G NR）
* **大規模天線（Massive MIMO）抗干擾**：
  * 預留部分**未使用的導頻（Unused Pilots）**，基站藉此檢測干擾的存在，並精準估算干擾信道特徵。
  * 設計最小均方誤差干擾抑制（MMSE-JS）估算器與線性強迫歸零干擾抑制（ZFJS）濾波器來消除干擾。
* **控制信道保護**：
  * 對實體廣播信道（PBCH）採用展頻調變。
  * 對實體上行控制信道（PUCCH）實施 PRB（實體資源塊）隨機化混淆（Scrambling）。
  * 對實體下行控制信道（PDCCH）導入分佈式加密方案。
* **動態資源分配**：為防止干擾器鎖定傳輸邊緣的實體上行控制信道（PUCCH），動態且偽隨機地分配資源塊（RB）。
* **機器學習檢測**：利用隨機森林、支持向量機（SVM）等演算法，分析丟包率（PER）、信號強度（RSS）與數據包遞送率（PDR）特徵來秒級檢測干擾。

#### 3. 認知無線電網路（CRNs）
* **博弈論防禦（Game-Theoretical Approaches）**：將次要用戶（SU）與干擾器之間的互動建模為隨機零和博弈（Zero-sum game）、非零和博弈或貝氏博弈。
* **強化學習**：採用 Minimax-Q 學習或多智能體強化學習（MARL），讓節點在與干擾器的對抗中，自主學習最優的頻道選擇與功率分配。
* **JENNA 演算法**：結合了隨機頻道跳躍與**網路編碼（Network Coding）**，利用鄰居節點分發控制信息，顯著降低受干擾時的鄰居發現延遲。

#### 4. ZigBee 網路 (IEEE 802.15.4)
* **隨機差分 DSSS (RD-DSSS)**：使用不可預測的擴展碼進行隨機化，降低被反應式干擾器精準攔截的概率。
* **Dodge-Jam 方案**：專門防禦 ACK 包攻擊，結合了快速頻道跳躍與**分幀發送（Frame Segmentation）**技術。
* **DEEJAM 協議**：提供四種對抗手段：
  1. **幀屏蔽（Frame Masking）**：使用加密的幀起始定界符（SFD）防止干擾器識別同步包。
  2. **頻道跳躍**。
  3. **數據包分割（Packet Fragmentation）**。
  4. **冗餘編碼（Redundant Encoding）**。
* **反應時間差防禦**：估算干擾器的檢測與啟動延遲，利用干擾器尚未反應過來的「安全時間空檔（Unjammed time slots）」完成小包傳輸。

#### 5. 藍牙網路 (Bluetooth)
* **無協調的跳頻技術（Uncoordinated FHSS）**：在沒有共享金鑰的前提下，發射端與接收端以不同的隨機跳頻規律切換，直到雙方意外「相遇」在同一頻頻道，進而安全交換金鑰。
* **協同廣播方案（Collaborative Broadcast）**：主設備在所有可能頻道上發送廣播，已經成功接收的從設備充當中繼節點，幫助轉發給其他被干擾器屏蔽的節點。

#### 6. LoRa 網路
* **啾頻共存與衝突解決（Collision Recovery）**：利用不同擴展因子（SF）的正交性，即使在同頻干擾下，仍能透過虛擬通道解調數據。
* **基於 KL 散度（Kullback-Leibler Divergence）與漢明距離（Hamming Distance）的檢測**：分析入網請求（Join request）信號的概率分佈，精準識別隱蔽的反應式干擾。

#### 7. 車聯網與無人機網路（VANETs & UAVs）
* **JammingBird 接收器**：專門針對車聯網（IEEE 802.11p），利用幀結構中未使用的空閒資源元素（RE），在每隔子載波上構建空間濾波器消除高達 25 dB 強度的干擾信號。
* **無人機空中中繼**：路側單元（RSU）受干擾時，調度無人機作為臨時空中 AP 進行數據繞路傳輸。
* **基於速度的無監督學習檢測**：利用車輛與干擾源的相對移動速度特徵，設計機器學習演算法來檢測移動干擾源，分類準確率達 98.9%。

#### 8. GPS 系統
* **自適應凹口濾波器（Adaptive Notch Filter）**：在時域或頻域檢測窄頻或單音（Single-tone）干擾，並動態將該頻段挖除。
* **自相干波束成形（Self-Coherence Beamforming）**：利用 GPS C/A 碼每周期重複 20 次的自相干特性，在不需干擾源資訊的情況下直接進行波束零陷。
* **多感測器融合（Multi-Sensor Fusion）**：將 GPS 與慣性導航系統（INS）透過卡爾曼濾波（Kalman Filter）進行深耦合（Deep Coupling），在 GPS 被完全干擾時依靠慣導維持定位。

---

### 三、 綜述指出未來抗干擾的發展趨勢（Outlook）

論文在最後強調，單一領域的防禦（如單純的信號檢測）已不足以應對日漸聰明的認知/智能干擾。未來的研究正朝著以下方向發展：
* **跨域抗干擾設計（Cross-Domain Anti-Jamming）**：聯合探索時間、頻率、空間（多天線）以及編碼域（Code domain）的協同防禦。
* **跨層優化設計（Cross-Layer Design）**：將實體層（PHY）的信號特徵與 MAC 層的資源分配、傳輸控制進行聯合最佳化。
* **設計即安全（Securing Wireless System by Design）**：從系統設計之初就將抗干擾考慮進去，而非干擾發生後才啟動防禦。
* **智能反射面輔助（Intelligent Reflecting Surface, IRS）**：利用 IRS 重構無線信道，繞過干擾源的主動屏蔽路徑。



---

Viewed Jamming_Attacks_and_Anti-Jamming_Strategies_in_Wireless_Networks_A_Comprehensive_Survey-2.pdf

這篇論文《**Jamming Attacks and Anti-Jamming Strategies in Wireless Networks: A Comprehensive Survey**》（發表於 *IEEE Communications Surveys & Tutorials*, 2022）是一篇針對無線網路干擾（Jamming）與防干擾（Anti-Jamming）技術的全面性綜述。

論文中針對以下 **9 大類無線網路系統** 以及 **2 種新興無線技術** 進行了深入的干擾攻擊與防護策略分析：

### 1. 分析的無線網路系統分類

| 網路類型 | 主要分析的標準與技術細節 | 主要干擾與防干擾分析重點 |
| :--- | :--- | :--- |
| **WLANs / Wi-Fi**<br>(無線區域網路) | IEEE 802.11a/g/n/ac/ax (Wi-Fi 6) | <ul><li>**干擾對象**：針對時間同步、頻率同步、通道估測（Channel Estimation）、循環前綴（CP）、下行 MU-MIMO 波束成形、速率自適應演算法（RAA）與 MAC 控制封包（如 CTS/ACK）的精準干擾。</li><li>**防禦策略**：通道跳頻、直接序列擴頻（DSSS，如 802.11b）、MIMO 空間濾波、動態功率控制與機器學習接收器（DeepWiFi）。</li></ul> |
| **Cellular Networks**<br>(行動通訊網路) | 4G LTE / LTE-Advanced、5G New Radio (NR)，以及傳統 3G WCDMA / GSM | <ul><li>**干擾對象**：針對控制通道（PDCCH/PUCCH/PCFICH）、資料通道（PDSCH/PUSCH）、同步訊號（PSS/SSS）、廣播通道（PBCH）、隨機接入（PRACH）、參考訊號（Reference Signals）等實體層結構的干擾。</li><li>**防禦策略**：大規模多輸入多輸出（Massive MIMO）空間干擾抑制、擴頻技術、動態資源分配、切換至備用基地台（eNodeB）等。</li></ul> |
| **CRNs**<br>(認知無線電網路) | 集中式與分散式認知無線電網路、CRAHN (Ad-hoc) | <ul><li>**干擾對象**：針對協同頻譜感測（CSS）過程、次要網路（Secondary Network）與公共控制通道（Common Control Channel）的干擾。</li><li>**防禦策略**：主要使用**賽局理論（Game Theory）**進行防干擾建模（如零和賽局、馬可夫決策過程、Minimax-Q 學習），並結合主動跳頻與網路編碼。</li></ul> |
| **ZigBee Networks**<br>(低功耗無線網路) | IEEE 802.15.4 標準 | <ul><li>**干擾對象**：利用 Wi-Fi 網卡進行跨技術干擾（Cross-technology jamming）、反應式干擾（Reactive Jamming）。</li><li>**防禦策略**：隨機差分擴頻（RD-DSSS）、通道跳頻與封包分段（Dodge-Jam 演算法、DEEJAM 協定）。</li></ul> |
| **Bluetooth Networks**<br>(藍牙網路) | 傳統藍牙（79個通道）與低功耗藍牙 BLE（40個非重疊通道） | <ul><li>**干擾對象**：精準追蹤藍牙跳頻序列（FHSS）與時鐘的智能干擾。</li><li>**防禦策略**：無協調跳頻（Uncoordinated FHSS）金鑰協商、協同廣播方案。</li></ul> |
| **LoRa / LoRaWAN Networks**<br>(低功耗廣域網路) | LPWAN 應用與 CSS（ Chirp Spread Spectrum，線性調頻擴頻）調變 | <ul><li>**干擾對象**：發送同步 Chirp 訊號進行碰撞干擾、觸發式干擾（Triggered）與選擇性干擾（Selective Jamming，解鎖 MAC 標頭後干擾特定節點）。</li><li>**防禦策略**：利用 CSS 調變天然的抗噪與抗干擾能力、基於 Kullback-Leibler 散度與漢明距離的干擾檢測演算法。</li></ul> |
| **Vehicular Networks**<br>(車聯網) | <ul><li>**陸地車聯網 (VANETs)**：基於 DSRC / IEEE 802.11p</li><li>**空中無人機網路 (UAVs)**</li></ul> | <ul><li>**干擾對象**：<br>1. **VANETs**：針對車對車（V2V）與車對基礎設施（V2I）安全通道的干擾，可能引發交通事故。<br>2. **UAVs**：針對無人機控制指令的干擾（Control command attack）及 GPS 導航訊號干擾。</li><li>**防禦策略**：利用無人機作為中繼站傳輸、多天線空間濾波（JammingBird 接收器結構）、車輛相對速度檢測干擾源，以及無人機軌跡與功率自適應優化。</li></ul> |
| **RFID Systems**<br>(無線射頻辨識) | GEN2 UHF RFID 讀寫器與標籤通訊 | <ul><li>**干擾對象**：利用讀寫器連續波（CW）能量特性進行訊號干擾，或使用高功率電磁感應進行破壞實體前端電路的「毀滅性攻擊」（Zapping Attack）。</li><li>**防禦策略**：基於封包遞送率（PDR）與接收訊號強度（RSS）的低功耗干擾檢測機制。</li></ul> |
| **GPS System**<br>(全球定位系統) | 民用 C/A Code (L1 頻段)、軍用 P-Code (L1/L2 頻段) | <ul><li>**干擾對象**：針對車載 GPS 接收器、海上航行系統以及電網中同步相量測量單元（PMUs）的時間同步進行干擾。</li><li>**防禦策略**：時頻遮罩濾波（如自適應凹口濾波器 Notch Filter）、天線陣列（Antenna Array）與空間濾波（如 CLEAN 演算法）、結合慣性導航系統（INS）的多感測器卡爾曼濾波融合。</li></ul> |

---

### 2. 針對新興無線技術的防干擾分析

除了上述網路架構，論文在後半部分也特別挑選了兩種新興技術進行專題分析：

*   **學習輔助無線系統 (Learning-Assisted Wireless Systems)**
    *   分析實體層的**對抗性機器學習攻擊（Adversarial ML Attacks）**。例如：攻擊者產生微小的對抗性擾動（Adversarial perturbation），使接收端的調變分類器、頻譜感測模型或 5G 毫米波波束預測模型出錯。
    *   探討如何利用強化學習（DRL）設計動態通道接入與主動路由防禦。
*   **毫米波通訊 (mmWave Communications)**
    *   分析毫米波獨特的傳播特性（如高定向性波束）。
    *   探討在高定向性波束與大規模 MIMO（Massive MIMO）環境下的防干擾，主要聚焦於**混合波束成形（Hybrid Beamforming）**設計，利用模擬波束向量消除干擾源，數位波束向量消除用戶間干擾。

---

### 💡 總結
這篇論文的分析維度非常完整，它不僅涵蓋了我們熟知的 **Wi-Fi**、**行動網路（4G/5G）** 與 **車聯網**，也深入討論了物聯網場景（**ZigBee, BLE, LoRa, RFID**）以及基礎設施層面（**GPS**）的干擾威脅。如果您正在撰寫相關的筆記或學術分析，這篇論文的 Table III (Wi-Fi)、Table V (Cellular) 以及 Table XI (總體防禦策略對照) 是非常有參考價值的整理指標。