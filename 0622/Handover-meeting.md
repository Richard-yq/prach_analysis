小諭 —— 論文攻擊程式驗證與防禦延伸
短、中期任務（實地驗證）：
負責驗證 Richard 的 5G gNB RACH (Msg1/Msg3) Jamming 攻擊專案。
後續需配合教授指示，將攻擊設備與天線帶至外部（如 G Reign 那邊）進行跨基站、跨硬體測試。
需主動向群組內的 Tobby 學長詢問並學習 HTC 相關設備/伺服器 的開啟、運行與配置方法。
長期研究方向（防禦機制）：
若想延續此題目，Richard 建議往防禦與環節（Mitigation）方向發展：利用 Machine Learning 偵測異常值（如訊號能量分佈、連線成功機率），並設計防禦 Action（如讓基站暫時休眠、引導 UE 進行 Handover）。
待辦事項：
先在自己的虛擬機中，利用 RF Simulator (OAI) 搭配 Richard 修改過的程式碼（Master branch）進行 Build 與編譯測試。


亭寬 & JT Finn —— DGX-Spark 與 O-RAN Layer 1 加速整合
核心研究：
利用 NVIDIA 的 DGX 伺服器進行底層 CUDA 加速（Layer 1），並與 OAI 的 Layer 2 / Layer 3 gNB 進行串接（由 FH 介面連接實體 RU）。
待辦事項：
對照 NVIDIA 官方文件與 Richard 留下的安裝筆記，研究如何將 OAI 原本的 L1 替換成 NVIDIA 的加速方案。
後續需確認與填寫 RU 的 MAC Address 配置。


三位學弟目前皆已成功連線至伺服器。
在 Finn 的公共資料夾下已建立一個 progress.md 筆記檔案。
要求： 三人後續的開發與測試進度，請以「Markdown 標題（如 #小玉、#亭寬）」分區，即時記錄指令、進度與 Bug 解法。