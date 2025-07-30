# Enhanced 5G NR gNB PRACH Measurements

## 概述

本模組提供增強的 5G NR gNB PRACH 測量功能，參考 LTE eNB 測量機制並針對 5G NR 系統進行優化。主要目標是改善 PRACH 檢測的準確性和可靠性。

## 主要功能

### 1. 增強的 I0 (雜訊底層) 測量
- **函數**: `nr_gNB_prach_I0_measurements()`
- **功能**: 提供更精確的雜訊底層估測
- **特色**:
  - 多天線支援
  - PRB 級別的雜訊測量
  - IIR 濾波器平滑處理
  - 可配置的測量清除機制

### 2. 增強的 PRACH 檢測
- **函數**: `nr_gNB_enhanced_prach_detection()`
- **功能**: 改進的 PRACH 前導碼檢測算法
- **特色**:
  - 自適應門檻值管理
  - 改進的雜訊底層濾波
  - 詳細的檢測邊界計算
  - 增強的日誌記錄

### 3. 統計資料輸出
- **函數**: `dump_nr_prach_I0_stats()`
- **功能**: 詳細的測量統計資料輸出
- **特色**:
  - PRB 級別的 I0 分布
  - 多天線統計
  - 黑名單 PRB 處理
  - 格式化的調試輸出

### 4. 初始化支援
- **函數**: `nr_gNB_prach_measurements_init()`
- **功能**: 系統初始化和預設值設定

## 文件結構

```
openair1/PHY/NR_ESTIMATION/
├── nr_gNB_prach_measurements.c    # 主要實作文件
└── nr_ul_estimation.h             # 函數聲明 (已更新)

openair1/SCHED_NR/
└── nr_prach_procedures.c          # 整合範例 (已更新)

examples/
└── nr_gNB_enhanced_measurements_example.c  # 使用範例和整合指南
```

## 使用方法

### 基本整合步驟

1. **包含標頭檔**:
```c
#include "PHY/NR_ESTIMATION/nr_ul_estimation.h"
```

2. **系統初始化** (在 gNB 啟動時執行一次):
```c
nr_gNB_prach_measurements_init(gNB);
```

3. **定期執行 I0 測量** (建議每個時隙執行):
```c
// 每 100 個訊框清除一次測量以獲得新的雜訊底層估測
unsigned char clear = (frame % 100 == 0) ? 1 : 0;
nr_gNB_prach_I0_measurements(gNB, slot, frame, clear);
```

4. **使用增強檢測** (在 PRACH 處理中):
```c
int detected = nr_gNB_enhanced_prach_detection(gNB, frame, slot, 
                                              max_preamble_energy, 
                                              detection_threshold);
```

5. **統計資料輸出** (用於調試):
```c
dump_nr_prach_I0_stats(stdout, gNB);
```

### 整合到現有程式碼

在 `nr_prach_procedures.c` 中的修改範例:

```c
void L1_nr_prach_procedures(PHY_VARS_gNB *gNB, int frame, int slot, nfapi_nr_rach_indication_t *rach_ind)
{
    // ... 現有程式碼 ...
    
    // 添加增強的 I0 測量
    nr_gNB_prach_I0_measurements(gNB, slot, frame, (frame % 100 == 0) ? 1 : 0);
    
    // ... PRACH 處理程式碼 ...
    
    // 使用增強檢測替代原有邏輯
    int enhanced_detection = nr_gNB_enhanced_prach_detection(gNB, frame, slot, 
                                                            &max_preamble_energy[0], 
                                                            gNB->prach_thres);
    
    if ((gNB->prach_energy_counter == NUM_PRACH_RX_FOR_NOISE_ESTIMATE) 
        && enhanced_detection 
        && (rach_ind->number_of_pdus < MAX_NUM_NR_RX_RACH_PDUS)) {
        // ... PRACH 檢測處理 ...
    }
}
```

## 主要改進

### 相對於原始 LTE 實作

1. **5G NR 適應性**:
   - 支援 5G NR 的時隙結構
   - 適應不同的 numerology
   - 處理可變的 PRB 配置

2. **增強的濾波**:
   - 更保守的 IIR 濾波器設定
   - 改進的雜訊底層穩定性
   - 更好的瞬態響應

3. **更好的日誌記錄**:
   - 詳細的檢測邊界資訊
   - 多層級日誌支援
   - 格式化的統計輸出

4. **效能優化**:
   - 減少不必要的計算
   - 更有效的記憶體使用
   - 平行處理友善的設計

## 配置選項

### 主要參數

- **Detection Threshold**: PRACH 檢測門檻值 (建議 3-10 dB)
- **Measurement Clear Period**: 測量清除週期 (建議 100-1000 frames)
- **IIR Filter Coefficients**: k1=1024, k2=0 (與 LTE 相容)

### 調優建議

1. **城市密集環境**: 
   - 較高的檢測門檻值 (8-10 dB)
   - 更頻繁的測量清除 (每 50 frames)

2. **郊區環境**:
   - 較低的檢測門檻值 (3-5 dB)
   - 較少的測量清除 (每 200 frames)

3. **多天線系統**:
   - 啟用每天線統計
   - 考慮天線間的相關性

## 編譯和測試

### 編譯選項

```bash
# 標準編譯 (包含在 OAI 建置系統中)
cd openairinterface5g
source oaienv
cd cmake_targets
./build_oai -w USRP --gNB

# 獨立測試範例
gcc -DSTANDALONE_TEST -I../openair1 examples/nr_gNB_enhanced_measurements_example.c -o test_measurements
```

### 測試建議

1. **單元測試**: 測試個別函數的正確性
2. **整合測試**: 在真實 gNB 環境中測試
3. **效能測試**: 測量 CPU 使用率和延遲
4. **現場測試**: 在不同環境條件下測試

## 除錯和監控

### 日誌級別

- **LOG_I**: 重要事件和初始化
- **LOG_D**: 詳細的檢測資訊
- **LOG_T**: 詳細的測量資料

### 監控指標

- `prach_I0`: PRACH 雜訊底層 (dB)
- `n0_subband_power_avg_dB`: 平均雜訊功率
- `detection_margin`: 檢測邊界
- 成功檢測率統計

### 常見問題

1. **檢測靈敏度過低**: 降低檢測門檻值
2. **誤檢測過多**: 提高檢測門檻值或改善雜訊估測
3. **效能問題**: 減少測量頻率或優化計算

## 相容性

- **向後相容**: 與現有 OAI 程式碼完全相容
- **API 穩定性**: 函數介面設計為穩定的 API
- **配置相容**: 支援現有的 gNB 配置參數

## 未來改進

1. **機器學習增強**: 整合 ML 算法改善檢測
2. **多小區協調**: 支援多小區雜訊測量協調
3. **即時調優**: 動態門檻值調整
4. **更多統計**: 增加更詳細的效能指標

## 作者和貢獻

基於 OpenAirInterface LTE eNB measurements，針對 5G NR 進行改進和優化。

## 授權

遵循 OpenAirInterface 公共許可證 1.1 版本。

---

如需更多資訊或技術支援，請參考 OpenAirInterface 官方文件或聯繫開發團隊。
