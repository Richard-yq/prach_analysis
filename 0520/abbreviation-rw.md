# 國立台灣科技大學碩士學位論文——縮寫使用審視報告 (Thesis Abbreviation Review Report)

本報告針對碩士學位論文 **`my_ntust_thesis.pdf`** 及其對應的 LaTeX 原始碼（位於 `sections/` 目錄下）進行了全自動化與人工雙重校對的深度審視。主要針對以下三類學術論文寫作中常見的縮寫（Abbreviation）規範問題進行清查：
1. **未定義即使用 (Undefined Abbreviations)**：使用了縮寫，但全文（摘要或正文 1-5 章）未曾定義其完整名稱。
2. **重複定義 (Duplicate Definitions)**：在正文中多次出現「完整名稱 (縮寫)」的定義格式，造成冗餘。
3. **先使用後定義 (Used Before Defined)**：在正文前面的頁面使用了縮寫，卻在後面的頁面才定義它。
4. **不一致性與拼寫錯誤 (Inconsistencies & Typos)**。

---

## 📊 審視結果摘要 (Executive Summary)

整體而言，本篇論文的架構完整、學術用語專業。然而，在縮寫的規範性上有幾處典型的學術寫作瑕疵。我們在正文（第 1 章至第 5 章，排除最後的 References）中發現了：
* **8 個** 實質上**完全未定義**的學術縮寫（如 `MCS`, `PDCCH`, `PDU` 等）。
* **10 個** 在正文中被**重複定義 2 次至 6 次**的縮寫（如 `RO` 被定義了 6 次，`SMO` 和 `RAR` 被定義了 5 次）。
* **5 個** **先使用後定義**的縮寫（例如 `SIB` 和 `FDM` 在第 1 章就已使用，卻分別遲至第 5 章和第 3 章才被定義）。
* **1 處** 明顯的術語使用不一致（在同一句子中混用 `RAOs` 與 `ROs`）。

以下為您詳細列出每一個有問題的字、所在的 PDF 頁碼、對應的 LaTeX 檔案與精確行號，以及具體的修改建議。

---

## 一、 未定義即使用的縮寫 (Undefined Abbreviations)

這類縮寫在論文中直接以簡稱出現，讀者無法在正文中找到其完整名稱的定義。
> [!WARNING]
> 學術論文規範要求：所有非通用常識之縮寫，在正文第一次出現時必須給出完整名稱。以下縮寫在正文中**從未被定義**：

| 縮寫 | 完整名稱 (建議補充) | 首次出現 PDF 頁碼 | 首次出現之 LaTeX 檔案與行號 | 首次出現上下文 (Context) |
| :--- | :--- | :--- | :--- | :--- |
| **MCS** | Modulation and Coding Scheme | Page 33 (Ch. 2) | [sections/system.tex:L19](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/system.tex#L19) | `... maintains link quality through adaptive MCS selection and HARQ-based ...` |
| **PDCCH** | Physical Downlink Control Channel | Page 33 (Ch. 2) | [sections/system.tex:L19](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/system.tex#L19) | `... ically schedules uplink and downlink resources via the PDCCH [21], and ...` |
| **PDU** | Protocol Data Unit | Page 47 (Ch. 3) | [sections/method.tex:L132](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/method.tex#L132) | `... preventing residual samples from prior PRACH PDU processing ...` |
| **OAM** | Operations, Administration, and Maintenance | Page 32 (Ch. 2) | [sections/system.tex:L11](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/system.tex#L11) | `... Within the SMO, the RAN NF OAM handles RAN data management ...` |
| **NF** | Network Function | Page 32 (Ch. 2) | [sections/system.tex:L11](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/system.tex#L11) | `... Within the SMO, the RAN NF OAM handles RAN data management ...` |
| **RMS** | Root Mean Square (常用於 $c_{rms}$) | Page 43 (Ch. 3) | [sections/method.tex:L63](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/method.tex#L63) | `... and c_rms is the RMS normalization scaling factor defined as ...` |
| **VNF** | Virtualized Network Function | Page 54 (Ch. 3) | [sections/method.tex:L226](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/method.tex#L226) | `... VES (VNF Event Streaming) alert ...` |
| **3GPP** | 3rd Generation Partnership Project | Page 19 (Ch. 1) | [sections/introduction.tex:L76](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L76) | `... as specified in 3GPP TS 38.211 [4].` (註：此詞在被註解掉的 % 程式碼中定義過，但在編譯出的正文中**完全未定義**) |

💡 **修改指引**：
1. **`MCS` & `PDCCH`**：請在 [sections/system.tex:L19](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/system.tex#L19) 第一次出現時，將其改為 `Physical Downlink Control Channel (PDCCH)` 及 `Modulation and Coding Scheme (MCS)`。
2. **`OAM` & `NF`**：請在 [sections/system.tex:L11](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/system.tex#L11) 第一次出現時，將其改為 `RAN Network Function (NF) Operations, Administration, and Maintenance (OAM)`。
3. **`3GPP`**：請在 [sections/introduction.tex:L76](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L76) 改為 `3rd Generation Partnership Project (3GPP)`。

---

## 二、 重複定義的縮寫 (Duplicate Definitions)

重複定義指的是同一個縮寫在正文不同的地方被多次寫出「完整名稱 (縮寫)」，這在學術寫作中被視為冗餘，應僅在第一次出現時定義，後續直接使用縮寫。
> [!IMPORTANT]
> 以下縮寫在正文（第 1-5 章）中被重複定義了多次，其中 `RO` 竟然被重複定義了 **6 次**！

```mermaid
barChart
    title "縮寫在正文中的重複定義次數"
    x-axis ["RO", "SMO", "RAR", "SSB", "DoS", "RA", "MAC", "ML", "RB", "TAC"]
    y-axis "定義次數"
    "RO" : 6
    "SMO" : 5
    "RAR" : 5
    "SSB" : 4
    "DoS" : 3
    "RA" : 3
    "MAC" : 2
    "ML" : 2
    "RB" : 2
    "TAC" : 2
```

### 1. `RO` (Random Access Occasion) —— 重複定義 6 次 ⚠️
* **第 1 次**：Page 33 (Ch. 2) — [sections/system.tex:L19](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/system.tex#L19) (`... allocated as Random Access Occasions (ROs) ...`) —— **此處應保留為唯一正式定義**。
* **第 2 次**：Page 39 (Ch. 3) — [sections/method.tex:L126](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/method.tex#L126) (`... single Random Access Occasion (RO). ...`)
* **第 3 次**：Page 41 (Ch. 3) — [sections/method.tex:L21](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/method.tex#L21) (`... single Random Access Occasion (RO) ...`)
* **第 4 次**：Page 46 (Ch. 3) — [sections/method.tex:L126](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/method.tex#L126) (`... single Random Access Occasion (RO) ...`)
* **第 5 次**：Page 48 (Ch. 3) — [sections/method.tex:L147](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/method.tex#L147) (`... single Random Access Occasion (RO) ...`)
* **第 6 次**：Page 80 (Ch. 4) — [sections/experiment.tex:L159](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/experiment.tex#L159) (`... Random Access Occasions (ROs) ...`)

### 2. `SMO` (Service Management and Orchestration) —— 重複定義 5 次 ⚠️
* **第 1 次**：Page 17 (Ch. 1) — [sections/introduction.tex:L7](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L7) (`... Service Management and Orchestration (SMO) ...`) —— **此處應保留**。
* **第 2 次**：Page 26 (Ch. 1) — [sections/introduction.tex:L174](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L174) (`... Service Management and Orchestration (SMO) ...`)
* **第 3 次**：Page 32 (Ch. 2) — [sections/system.tex:L11](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/system.tex#L11) (`... Service Management and Orchestration (SMO) ...`)
* **第 4 次**：Page 33 (Ch. 2) — [sections/system.tex:L21](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/system.tex#L21) (`... Service Management and Orchestration (SMO) ...`)
* **第 5 次**：Page 66 (Ch. 4) — [sections/experiment.tex:L5](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/experiment.tex#L5) (`... Service Management and Orchestration (SMO) ...`)

### 3. `RAR` (Random Access Response) —— 重複定義 5 次 ⚠️
* **第 1 次**：Page 16 (Ch. 1) — [sections/introduction.tex:L6](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L6) (`... Random Access Response (RAR) ...`) —— **此處應保留**。
* **第 2 次**：Page 21 (Ch. 1) — [sections/introduction.tex:L79](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L79) (`... Random Access Response (RAR) ...`)
* **第 3 次**：Page 43 (Ch. 3) — [sections/method.tex:L68](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/method.tex#L68) (`... Random Access Responses (RAR) ...`)
* **第 4 次**：Page 69 (Ch. 4) — [sections/experiment.tex:L57](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/experiment.tex#L57) (`... ra-ResponseWindow Random Access Response window ...` - 表格中)
* **第 5 次**：Page 76 (Ch. 4) — [sections/experiment.tex:L112](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/experiment.tex#L112) (`... Random Access Responses (RAR) ...`)

### 4. `SSB` (Synchronization Signal Block) —— 重複定義 4 次 ⚠️
* **第 1 次**：Page 17 (Ch. 1) — [sections/introduction.tex:L20](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L20) (`... Synchronization Signal/PBCH Block (SSB). ...`) —— **此處應保留**。
* **第 2 次**：Page 33 (Ch. 2) — [sections/system.tex:L19](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/system.tex#L19) (`... Synchronization Signal Blocks (SSBs) ...`)
* **第 3 次**：Page 61 (Ch. 3) — [sections/method.tex:L309](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/method.tex#L309) (`... Synchronization Signal Block ...`)
* **第 4 次**：Page 92 (Ch. 5) — [sections/conclusion.tex:L12](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/conclusion.tex#L12) (`... Synchronization Signal Blocks (SSBs) ...`)

### 5. `DoS` (Denial of Service) —— 重複定義 3 次
* **第 1 次**：Page 72 (Ch. 4) — [sections/experiment.tex:L157](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/experiment.tex#L157) (`... Denial of Service (DoS) ...`) —— **此處應保留**（因為這是它在正文中的第 1 次定義）。
* **第 2 次**：Page 73 (Ch. 4) — [sections/experiment.tex:L159](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/experiment.tex#L159) (`... Denial of Service (DoS) ...`)
* **第 3 次**：Page 90 (Ch. 5) — [sections/conclusion.tex:L5](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/conclusion.tex#L5) (`... Denial of Service (DoS) ...`)

### 6. `RA` (Random Access) —— 重複定義 3 次
* **第 1 次**：Page 16 (Ch. 1) — [sections/introduction.tex:L6](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L6) (`... Random Access (RA) procedure ...`) —— **此處應保留**。
* **第 2 次**：Page 21 (Ch. 1) — [sections/introduction.tex:L79](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L79) (`... Random Access (RA) ...`)
* **第 3 次**：Page 40 (Ch. 3) — [sections/method.tex:L29](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/method.tex#L29) (`... Random Access (RA-RNTI) ...` - 註：這裡似乎把 `RA-RNTI` 當成了 `Random Access (RA-RNTI)` 或者是手誤)

### 7. 其他重複定義 2 次的縮寫
* **`MAC` (Medium Access Control)**：
  1. Page 27 (Ch. 1) — [sections/introduction.tex:L188](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L188) (`Medium Access Control (MAC)`) —— **應保留**。
  2. Page 39 (Ch. 3) — [sections/method.tex:L3](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/method.tex#L3) (`Medium Access Control (MAC)`)
* **`ML` (Machine Learning)**：
  1. Page 29 (Ch. 1) — [sections/introduction.tex:L257](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L257) (`Machine Learning (ML)`) —— **應保留**。
  2. Page 91 (Ch. 5) — [sections/conclusion.tex:L12](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/conclusion.tex#L12) (`Machine Learning (ML)`)
* **`RB` (Resource Block)**：
  1. Page 74 (Ch. 4) — [sections/experiment.tex:L112](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/experiment.tex#L112) (`resource block (RB)`) —— **應保留**。
  2. Page 77 (Ch. 4) — [sections/experiment.tex:L118](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/experiment.tex#L118) (`resource block (RB)`)
* **`TAC` (Timing Advance Command)**：
  1. Page 21 (Ch. 1) — [sections/introduction.tex:L79](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L79) (`Timing Advance Command (TAC)`) —— **應保留**。
  2. Page 25 (Ch. 1) — [sections/introduction.tex:L123](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L123) (`Timing Advance Command (TAC)`)

💡 **修改指引**：
除了標註為「**應保留**」的第一處定義外，後續的所有重複定義都應直接改用**純縮寫**（例如：將 `Service Management and Orchestration (SMO)` 直接改為 `SMO`）。

---

## 三、 先使用後定義的縮寫 (Used Before Defined)

這類縮寫出現在較前的章節，卻在較後的章節才第一次給出定義。
> [!CAUTION]
> 讀者在前半部分讀到該縮寫時會產生困惑。這在學術審查中是一個嚴重的寫作錯誤。

### 1. `FDM` (Frequency Domain Multiplexing) 
* **首次使用**：Page 18 (Ch. 1) — [sections/introduction.tex:L22](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L22) (`... msg1-FDM (the number of PRACH occasions multiplexed in the frequency domain) ...`) —— 此處以註解式說明，非正式定義。
* **首次正式定義**：Page 48 (Ch. 3) — [sections/method.tex:L147](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/method.tex#L147) (`... frequency-domain multiplexed (FDM) ROs ...`)
* 💡 **修改建議**：應在第 1 章 [sections/introduction.tex:L22](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L22) 首次出現時，直接定義為 `Frequency-Domain Multiplexing (FDM)`，後續在第 3 章則直接使用 `FDM`。

### 2. `SIB` (System Information Block)
* **首次使用**：Page 18 (Ch. 1) — [sections/introduction.tex:L22](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L22) (`... and scheduling rules for other SIBs. ...`)
* **首次正式定義**：Page 91 (Ch. 5) — [sections/conclusion.tex:L12](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/conclusion.tex#L12) (`... System Information Block (SIB) manipulation ...`) —— **這非常不妥，讀者直到結論才看到 SIB 的定義！**
* 💡 **修改建議**：應在第 1 章 [sections/introduction.tex:L22](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L22) 正式定義為 `System Information Block (SIB)`。同時注意：論文中第一章寫了 `System Information Block 1 (SIB1)`，但對於通用詞 `SIB` 卻沒有獨立定義，建議在 `other SIBs` 出現處將其定義為 `System Information Blocks (SIBs)`。

### 3. `C-RNTI` (Cell Radio Network Temporary Identifier)
* **首次使用**：Page 21 (Ch. 1) — [sections/introduction.tex:L79](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L79) (`... and (iv) a Temporary C-RNTI (TC-RNTI) for temporary identification ...`)
* **首次正式定義**：Page 22 (Ch. 1) — [sections/introduction.tex:L81](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L81) (`... Cell Radio Network Temporary Identifier (C-RNTI) ...`)
* 💡 **修改建議**：在 Page 21 [sections/introduction.tex:L79](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L79) 的 `Temporary C-RNTI (TC-RNTI)` 之前，讀者尚未見過 `C-RNTI`。應在此行將 `C-RNTI` 的全稱寫出來，或調整前後句的定義順序。

### 4. `ML` (Machine Learning)
* **首次使用**：Page 27 (Ch. 1) — [sections/introduction.tex:L199](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L199) (`... while ML-based detection ...`)
* **首次正式定義**：Page 29 (Ch. 1) — [sections/introduction.tex:L257](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L257) (`... Machine Learning (ML) solutions. ...`)
* 💡 **修改建議**：請將定義移到 Page 27 [sections/introduction.tex:L199](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/introduction.tex#L199) 的首次出現處（改為 `Machine Learning (ML)-based`），而 Page 29 則改用純縮寫 `ML`。

### 5. `RB` (Resource Block)
* **首次使用**：Page 49 (Ch. 3) — [sections/method.tex:L144](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/method.tex#L144) (`... starting Physical Resource Block (PRB) index ...` 註：此處雖有 `PRB`，但直接使用 `RB` 也是在這一章的後半部分)
* **首次正式定義**：Page 74 (Ch. 4) — [sections/experiment.tex:L112](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/experiment.tex#L112) (`... Msg3 resource block (RB) allocation ...`)
* 💡 **修改建議**：由於 `PRB` 在第三章已經被定義為 `Physical Resource Block (PRB)`，可以在首次出現 `RB` 時直接說明其為 `Resource Block (RB)`，通常兩者應統一或在第三章即給予 `RB` 的正式定義。

---

## 四、 術語不一致性與細微錯誤 (Inconsistencies & Typos)

### 1. `RAOs` 與 `ROs` 混用錯誤 (Inconsistent Abbreviation)
* **位置**：Page 61 (Ch. 3) — [sections/method.tex:L307](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/method.tex#L307)
* **原文**：
  > `... affecting the periodicity and resource allocation of RAOs. Adjusting this parameter changes the distribution characteristics of ROs and ...`
* **問題**：在同一個句子中，前半句使用了 **`RAOs`**，後半句卻使用了 **`ROs`**。
* **修改建議**：在整篇論文中，`RO` 被定義為 `Random Access Occasion`，且已被廣泛使用。這裡的 **`RAOs`** 是一個手誤，**強烈建議將 `RAOs` 修改為 `ROs`**，以保持全文術語的嚴謹與一致性。

### 2. `MU-MIMO` 定義不完整
* **位置**：Page 92 (Ch. 5) — [sections/conclusion.tex:L12](file:///Users/yq/Documents/Richard_Thesis__For_NTUST_/sections/conclusion.tex#L12)
* **原文**：
  > `... Multiple-Input Multiple-Output (MU-MIMO) systems ...`
* **問題**：括號中為 `MU-MIMO`，但前面只寫了 `Multiple-Input Multiple-Output`，漏掉了 **`Multi-User` (MU)** 的定義。
* **修改建議**：改為 `Multi-User Multiple-Input Multiple-Output (MU-MIMO) systems`。

---

## 🛠️ 下一步修改建議 (Action Plan)

既然您在 LaTeX 編輯器中已經打開了相關文件（如 `sections/introduction.tex` 等），您可以直接根據本報告中提供的 **[檔案與行號連結]** 跳轉到對應位置進行修改。

1. **修正未定義縮寫**：在表格中列出的 LaTeX 首次出現行，補上 `Full Name (Abbrev)` 的格式。
2. **清除重複定義**：使用搜尋功能，將正文中第二次及之後出現的 `Full Name (Abbrev)` 替換成單純的 `Abbrev`。特別是 `RO`、`SMO`、`RAR` 和 `SSB` 這四個重災區。
3. **調整先後順序**：將 `FDM`、`SIB`、`C-RNTI`、`ML` 等縮寫的定義移動到它們各自首次出現的位置。
4. **修正 L307 的 `RAOs`**：直接跳轉到 `sections/method.tex` 第 307 行，將 `RAOs` 改為 `ROs`。
