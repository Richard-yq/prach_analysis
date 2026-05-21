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



---


romf

```
│ 2026-05-21 08:57:28 - 🚀 Starting RAN OAM Mediation Function (ROMF) Agent  │
│  * Serving Flask app 'romf_agent'                                          │
│  * Debug mode: off                                                         │
│ WARNING: This is a development server. Do not use it in a production deplo │
│  * Running on all addresses (0.0.0.0)                                      │
│  * Running on http://127.0.0.1:5000                                        │
│  * Running on http://10.244.204.20:5000                                    │
│ Press CTRL+C to quit                                                       │
│ 2026-05-21 09:00:34 - INFO - SSH connection established to 192.168.8.59    │
│ 2026-05-21 09:00:34 - ✅ SSH connection reconnected for active gNB         │
│ 127.0.0.1 - - [21/May/2026 09:00:35] "GET /health HTTP/1.1" 200 -          │
│ 2026-05-21 09:00:41 - 📡 Received request: GET /api/v1/gnb/ra-stats        │
│ 2026-05-21 09:00:41 - INFO - [gNB] Analyzing RA procedure from log file... │
│ 2026-05-21 09:00:42 - INFO - [gNB] RA Procedure Analysis Results:          │
│ 2026-05-21 09:00:42 - INFO - RA Procedure Initiated: 587 times             │
│ 2026-05-21 09:00:42 - INFO - RA Procedure Succeeded: 25 times              │
│ 2026-05-21 09:00:42 - INFO - Success Rate: 4.26%                           │
│ 2026-05-21 09:00:42 - OUTCOME - [gNB] Poor RA procedure success rate - req │
│ 127.0.0.1 - - [21/May/2026 09:00:42] "GET /api/v1/gnb/ra-stats?gnb_id=rich │
│ 2026-05-21 09:01:02 - 📡 Received request: GET /api/v1/gnb/connection-info │
│ 127.0.0.1 - - [21/May/2026 09:01:02] "GET /api/v1/gnb/connection-info?gnb_ │
│ 2026-05-21 09:01:09 - 📡 Received request: GET /api/v1/gnb/raw-log         │
│ 127.0.0.1 - - [21/May/2026 09:01:09] "GET /api/v1/gnb/raw-log?gnb_id=richa │
│ 2026-05-21 09:01:49 - 📡 Received request: GET /api/v1/gnb/raw-log         │
│ 127.0.0.1 - - [21/May/2026 09:01:50] "GET /api/v1/gnb/raw-log?gnb_id=richa │
│      
```

rApp
```
============================================
2026-05-21 09:28:39 - INFO - Success rate threshold: 70.0%
2026-05-21 09:28:39 - INFO - Analysis time window: 10s
2026-05-21 09:28:39 - INFO - Failed attempts threshold: 10
2026-05-21 09:28:39 - 
📡 Initializing VES Alarm Monitor...
2026-05-21 09:28:39 - INFO - Connecting to Kafka at onap-strimzi-kafka-bootstrap.onap:9092...
2026-05-21 09:28:39 - 🔐 Using SASL/SCRAM authentication (internal connection)
2026-05-21 09:28:39 -    Username: strimzi-kafka-admin
2026-05-21 09:28:39 - ✅ Successfully connected to Kafka with SASL/SCRAM
2026-05-21 09:28:39 - 📡 Subscribed to topics: unauthenticated.SEC_3GPP_FAULTSUPERVISION_OUTPUT
2026-05-21 09:28:39 - ✅ Connected to Kafka successfully
2026-05-21 09:28:39 - INFO - Using reconfiguration parameters from config file:
2026-05-21 09:28:39 -        prach_ConfigurationIndex = 98
2026-05-21 09:28:39 -        absoluteFrequencySSB = 621312
2026-05-21 09:28:39 -        dl_absoluteFrequencyPointA = 620040
2026-05-21 09:28:39 - 
📡 Sending baseline configuration to TEIV...
2026-05-21 09:28:39 - WARNING - Failed to communicate with ROMF: HTTPConnectionPool(host='romf.nonrtric', port=5000): Max retries exceeded with url: /api/v1/gnb/current-params?config_path=%2Fhome%2Foaignb%2Frichard-config%2FOAI_gNB.conf&gnb_id=richard-gNB (Caused by NameResolutionError("HTTPConnection(host='romf.nonrtric', port=5000): Failed to resolve 'romf.nonrtric' ([Errno -2] Name or service not known)"))
2026-05-21 09:28:39 - WARNING - Could not read current config parameters
2026-05-21 09:28:39 - 
🔍 ===== STARTING CONTINUOUS MONITORING =====
2026-05-21 09:28:39 - INFO - Monitoring for PRACH attack alarms...
2026-05-21 09:28:39 - INFO - Press Ctrl+C to stop monitoring
2026-05-21 09:28:39 - INFO - Analysis window: 10 seconds
2026-05-21 09:28:39 - INFO - Success rate threshold: 70.0%
2026-05-21 09:28:39 - INFO - Remote config: /home/oaignb/richard-config/OAI_gNB.conf
2026-05-21 09:28:39 - --------------------------------------------------------------------------------
2026-05-21 09:28:39 - 
⏳ Waiting for next alarm event...
2026-05-21 09:28:39 - 🔍 Waiting for OAI_Alarm_Alarms event (timeout: 30s)...

============================================
✅ Redeploy completed!
============================================

To follow logs in real-time, run:
  kubectl logs -f -n nonrtric -l app=richard-mitigation-rapp-dev

To check pod status, run:
  kubectl get pods -n nonrtric | grep richard-mitigation

╭─ubuntu@zhongkui ~/richard/develop-O1-rApp ‹O1-REST-v3.1●› 
╰─$   kubectl logs -f -n nonrtric -l app=richard-mitigation-rapp-dev
^[🔍 ===== STARTING CONTINUOUS MONITORING =====
2026-05-21 09:28:39 - INFO - Monitoring for PRACH attack alarms...
2026-05-21 09:28:39 - INFO - Press Ctrl+C to stop monitoring
2026-05-21 09:28:39 - INFO - Analysis window: 10 seconds
2026-05-21 09:28:39 - INFO - Success rate threshold: 70.0%
2026-05-21 09:28:39 - INFO - Remote config: /home/oaignb/richard-config/OAI_gNB.conf
2026-05-21 09:28:39 - --------------------------------------------------------------------------------
2026-05-21 09:28:39 - 
⏳ Waiting for next alarm event...
2026-05-21 09:28:39 - 🔍 Waiting for OAI_Alarm_Alarms event (timeout: 30s)...
2026-05-21 09:29:00 - ⏳ Still waiting... (20/30s)
2026-05-21 09:29:10 - ⏱️ Timeout: No alarm detected within 30 seconds
2026-05-21 09:29:10 - 
⏳ Waiting for next alarm event...
2026-05-21 09:29:10 - 🔍 Waiting for OAI_Alarm_Alarms event (timeout: 30s)...
2026-05-21 09:29:15 - 🚨 ===== OAI ALARM DETECTED =====
2026-05-21 09:29:15 - 📡 Source: gNB-Eurecom-5GNRBox-00001
2026-05-21 09:29:15 - 🎯 Event: stndDefined_OAI_Alarm_Alarms_prachAttackDetected
2026-05-21 09:29:15 - ⚠️ Alarm Type: SECURITY_SERVICE_OR_MECHANISM_VIOLATION
2026-05-21 09:29:15 - 🔍 Probable Cause: prachAttackDetected
2026-05-21 09:29:15 - 📊 Severity: CRITICAL
2026-05-21 09:29:15 - 💬 Details: Open Air Interface
2026-05-21 09:29:15 - ================================
2026-05-21 09:29:15 - 
🚨 ===== PRACH ATTACK DETECTED (Detection #1) =====
2026-05-21 09:29:15 - 📊 Alarm Details:
2026-05-21 09:29:15 -    - Event: stndDefined_OAI_Alarm_Alarms_prachAttackDetected
2026-05-21 09:29:15 -    - Probable Cause: prachAttackDetected
2026-05-21 09:29:15 -    - Severity: CRITICAL
2026-05-21 09:29:15 -    - Source: gNB-Eurecom-5GNRBox-00001
2026-05-21 09:29:15 -    - Time: 2026-05-21 09:29:15
2026-05-21 09:29:15 - 
📊 ===== ANALYZING RA PROCEDURE (Detection #1) =====
2026-05-21 09:29:15 - INFO - Analysis time window: 10 seconds
2026-05-21 09:29:15 - INFO - Collecting RA procedure data...
2026-05-21 09:29:25 - ❌ Failed to parse RA procedure via ROMF: HTTPConnectionPool(host='romf.nonrtric', port=5000): Max retries exceeded with url: /api/v1/gnb/ra-stats?gnb_id=richard-gNB (Caused by NameResolutionError("HTTPConnection(host='romf.nonrtric', port=5000): Failed to resolve 'romf.nonrtric' ([Errno -2] Name or service not known)"))
2026-05-21 09:29:25 - 
✅ Detection #1 processing completed
2026-05-21 09:29:25 - --------------------------------------------------------------------------------
2026-05-21 09:29:25 - 
⏳ Waiting for next alarm event...
2026-05-21 09:29:25 - 🔍 Waiting for OAI_Alarm_Alarms event (timeout: 30s)...
2026-05-21 09:29:46 - ⏳ Still waiting... (20/30s)
2026-05-21 09:29:56 - ⏱️ Timeout: No alarm detected within 30 seconds
2026-05-21 09:29:56 - 
⏳ Waiting for next alarm event...
2026-05-21 09:29:56 - 🔍 Waiting for OAI_Alarm_Alarms event (timeout: 30s)...
2026-05-21 09:30:17 - ⏳ Still waiting... (20/30s)
2026-05-21 09:30:27 - ⏱️ Timeout: No alarm detected within 30 seconds
2026-05-21 09:30:27 - 
⏳ Waiting for next alarm event...
2026-05-21 09:30:27 - 🔍 Waiting for OAI_Alarm_Alarms event (timeout: 30s)...
```