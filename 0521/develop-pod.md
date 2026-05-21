這是一個在 Kubernetes 實際開發中非常經典且重要的需求！

為了讓您能順利測試新開發的 rApp，同時不丟失且隨時可以切換回舊的 rApp，最優雅、最推薦的方法是 Kubernetes 的「縮容至 0 (Scale to 0)」 機制。

這就如同「暫停鍵」一樣，舊的配置、服務、設定檔通通保留在叢集裡，只是暫時把運作的 Pod 關閉，完全不佔用任何 CPU 與記憶體，隨時可以一鍵復活。

以下是為您整理的極速切換測試指南：

🛑 步驟一：暫時「暫停」舊的 rApp (Scale to 0)
請在您的終端機執行以下命令，將舊 rApp 的副本數量縮減為 0：

先查詢舊 rApp 的 Deployment 確切名稱：

bash
kubectl get deployments -n nonrtric
(假設查詢出來的名稱是 richard-mitigation-rapp)

將它暫停（縮容至 0）：

bash
kubectl scale deployment richard-mitigation-rapp --replicas=0 -n nonrtric
💡 此時，原本那個 richard-mitigation-rapp-xxxx-xxxx 的 Pod 就會優雅地關閉並消失，但它的所有設定都還完好地存在 K8s 裡。

🚀 步驟二：部署並測試您新開發的 rApp
現在，舊的 Pod 已經騰出空間。您可以前往新開發的目錄，建置並部署您的新 rApp：

bash
cd /Users/yq/Documents/develop/develop-richard-nonrtric-rapp-mitigation
# 執行您新開發的部署腳本
./redeploy.sh
這會把您的最新代碼（完全使用 ROMF REST API 的版本）打包部署到 nonrtric 空間中。您可以開始對它進行各種閉環防禦聯調測試！

🔄 步驟三：測試完畢，如何一鍵還原？
當您新版測試完成，想要回到原本那個舊的 rApp 時，只需簡單兩步：

把新開發的 rApp 暫停（或者直接刪除）：

bash
# 暫停新版 (假設新版 deployment 名稱為 richard-mitigation-rapp-new)
kubectl scale deployment richard-mitigation-rapp-new --replicas=0 -n nonrtric
# 或者如果您不想留著新版，可以直接用新目錄下的 deployment.yaml 卸載它：
# kubectl delete -f deployment.yaml
一鍵「復活」原本的舊版 rApp：

bash
kubectl scale deployment richard-mitigation-rapp --replicas=1 -n nonrtric
💡 舊的 Pod 就會立刻在 3 秒鐘內重新啟動（Running），且帶著它原本所有的環境變數與 ConfigMap 完美復活！

這套 Scale to 0 的方案是目前 K8s 灰度發布與 A/B 測試中最安全、最推薦的做法，您可以放心大膽地進行新版 rApp 的測試了！

下午5:08
