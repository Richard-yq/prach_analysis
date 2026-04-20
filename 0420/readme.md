分析multipreamble attack 實作 vs 正常preamble detect


這樣對基地台的detecetion有影響嗎
很好的問題！不影響，原因在於 gNB 的偵測機制根本不看包絡，讓我解釋：

gNB 為什麼不受非恆定包絡影響
1. gNB 用的是線性相關器（Matched Filter）
$$R[n] = \text{IDFT}\bigl{\text{FFT}(r) \cdot \overline{\text{FFT}(x_u)}\bigr}$$

這是線性運算。對攻擊訊號：

$$s_{\text{atk}} = x_{u,CS_1} + x_{u,CS_2} + x_{u,CS_3}$$

代入後線性展開：

$$R_{\text{atk}}[n] = \underbrace{R_1[n]}{\text{peak @ }n_1} + \underbrace{R_2[n]}{\text{peak @ } n_2} + \underbrace{R_3[n]}_{\text{peak @ }n_3}$$

三個峰完全獨立，互不干擾。gNB 看到的是 M 個尖峰，跟攻擊訊號的 I/Q 長什麼樣無關。

2. CAZAC 的正交性保證峰值分離
ZC 序列的不同 CS 版本之間循環相關為零（Zero Autocorrelation）：

$$\sum_k x_{u,CS_m}[k] \cdot \overline{x_{u,CS_n}[k]} = 0 \quad \text{for } m \neq n$$

所以 Preamble 1 的峰 完全不會污染 Preamble 2 的峰的位置，包絡怎麼變都不影響這個性質。

3. 那非恆定包絡有什麼實際影響？
面向	影響	說明
gNB 相關峰偵測	✅ 無影響	線性操作，CAZAC 正交性保護
RF 功率放大器 (PA)	⚠️ 有影響	高 PAPR（振幅變化大）→ PA 可能飽和/非線性失真
總傳輸功率	⚠️ 有影響	M 個疊加 → 平均功率是單一 preamble 的 M 倍（無縮放時）
每個偵測峰的高度	⚠️ 看有無功率縮放	不縮放：每峰跟正常一樣高；縮放至單 preamble 總功率：每峰降低 $10\log_{10}(1/M)$ dB


I/Q 非恆定包絡只是攻擊訊號的「外觀」特徵，對 gNB 的 DFT 相關器完全透明。真正讓攻擊成功的是 CAZAC 的線性疊加性質，而不是包絡本身。這也是為什麼這個攻擊在理論上幾乎無法靠改進相關器來防禦——只能在更高層（RA 回應分配策略、O-RAN xApp 偵測異常）做防護。

![alt text](image.png)

為什麼一定要縮放？(Hardware Constraints)
在我們的模擬中，單一 ZC Preamble 的振幅（Amplitude）是 1。 如果你把 5 個 Preamble 直接疊加起來，某些取樣點的振幅會疊加到 5（如圖 ② 的 Y 軸所示）。

如果不縮放：當你把這個訊號送進 SDR（例如 USRP）的 DAC（數位類比轉換器）和 PA（功率放大器）時，硬體能夠接受的輸入範圍通常是 [-1.0, 1.0]。振幅超過 1 的部分會被硬體強制「削頂（Clipping）」。
Clipping 的災難：削頂是一種嚴重的「非線性失真」。這會破壞 ZC 序列的完美正交性，產生大量的雜訊（Intermodulation distortion），結果就是 gNB 端的 noise floor 會整個暴增，最後 5 個 Peak 都會被自己的雜訊淹沒而偵測不到。


實務上該怎麼縮放？
為了避免 Clipping，通常有兩種常見的縮放方式：

Peak Normalization (除以 $M$)：把疊加後的訊號除以 $M$ (這裡是 5)。這樣可以「保證」最大振幅絕對不會超過 1。這是最安全的做法。
RMS Normalization (除以 $\sqrt{M}$)：因為 5 個 preamble 的相位是亂數疊加的，它看起來像高斯雜訊（OFDM 的 PAPR 特性），所以除以 $\sqrt{5}$ 就可以讓「總平均發射功率」保持不變（與單一 preamble 時相同）。
3. 對 gNB Detection 的影響是什麼？(Power Penalty)
這就是攻擊者的代價（Trade-off）。gNB 的相關接收器（Correlator）是一個高度**線性（Linear）**的系統：

如果你發送訊號時，把整個訊號乘上一個係數 $c$ （例如 $c = 1/\sqrt{5}$）。
到了 gNB 端，算出來的每個 Peak 功率，就會下降 $c^2$ 的倍數。


對 gNB Detection 的影響是什麼？(Power Penalty)
這就是攻擊者的代價（Trade-off）。gNB 的相關接收器（Correlator）是一個高度**線性（Linear）**的系統：

如果你發送訊號時，把整個訊號乘上一個係數 $c$ （例如 $c = 1/\sqrt{5}$）。
到了 gNB 端，算出來的每個 Peak 功率，就會下降 $c^2$ 的倍數。
具體影響：

假設你本來打 1 個 Preamble，gNB 收到的 Peak Power 是 $0$ dB。
現在你疊加了 5 個，為了硬體不爆掉，你把總訊號除以 $\sqrt{5}$。
那麼到了 gNB，這 5 個 Peak 雖然都能被完美分開，但每一個 Peak 的 Power 都會下降約 7 dB ($10 \log_{10}(1/5) \approx -7$ dB)。
如果除以 5 (Peak normalization)，每個 Peak 甚至會下降 14 dB。


### 📡 RMS Scaling: Preamble 疊加數量與接收衰減速查表

| 疊加數量 ($M$) | 縮放係數 ($1/\sqrt{M}$) | 每個 Peak 掉餘的 dB 數 ($\Delta P$) | 實務攻擊含意 (假設 gNB Threshold = -13 dB) |
| :---: | :---: | :---: | :--- |
| **1** | $1.00$ | **$0.0$ dB** | 正常連線，全功率發射 |
| **2** | $0.71$ | **$-3.0$ dB** | 損失了一半的能量（-3 dB），依然極易被偵測 |
| **3** | $0.58$ | **$-4.8$ dB** | 攻擊 3 個 slot，訊號仍非常健康 |
| **4** | $0.50$ | **$-6.0$ dB** | 四分之一功率。如果 SNR 佳，仍遠高於閾值 |
| **5** | $0.45$ | **$-7.0$ dB** | 五連波攻擊，Peak 高度來到約 -7 dB |
| **6** | $0.41$ | **$-7.8$ dB** | |
| **8** | $0.35$ | **$-9.0$ dB** | |
| **10** | $0.32$ | **$-10.0$ dB** | 十連波！功率衰減 10 dB，開始逼近 Threshold |
| **16** | $0.25$ | **$-12.0$ dB** | 接近極限！若距離稍遠，可能會掉下 -13 dB 的閾值 |
| **34** | $0.17$ | **$-15.3$ dB** | **塞滿整個 PRACH！** 但預計完全低於 -13 dB Threshold，攻擊會**全部失效** (gNB 把一切當作雜訊) |

The proposed attacker modifies the signal generation process to aggregate $M$ distinct preambles. The combined frequency-domain signal $Y_{attack}[k]$ constructed by the attacker is given by:
\begin{equation}
    Y_{attack}[k] = \sum_{m=0}^{M-1} \frac{\alpha}{M} \cdot X_{u_m}[k] \cdot e^{-j \frac{2\pi k C_{v_m}}{N_{ZC}}}
\end{equation}
where:
\begin{itemize}
    \item $M$ is the number of simultaneous attack sequences.
    \item $u_m$ and $C_{v_m}$ are the root sequence index and cyclic shift for the $m$-th preamble, respectively.
    \item $\alpha$ represents the total transmit amplitude. To prevent Digital-to-Analog Converter (DAC) overflow and maintain signal integrity, the amplitude of each component sequence is scaled by $1/M$.
\end{itemize}

This superposition allows the attacker to mimic multiple distinct UEs simultaneously. The resulting time-domain signal $y_{attack}(t)$ is obtained via IDFT:
\begin{equation}
    y_{attack}(t) = \text{IDFT}\{Y_{attack}[k]\}
\end{equation}



# 實作code


## 4. PHY Layer - PRACH Generation (nr_prach.c)

### Macro Definition

```pseudo
#define num_attack_sequences 3  // Number of simultaneous preambles
```

---

### Function: generate_nr_prach()

**Purpose**: Generate PRACH signals with multi-preamble and multi-FD-occasion support

```pseudo
function generate_nr_prach(ue, gNB_id, frame, slot) {
    
    // ... existing initialization ...
    
    fd_occasion = prach_pdu->num_ra  // FD occasion index from MAC
    
    // Use controlled amplitude from preconfigured value
    amp = ue->prach_vars[gNB_id]->amp
    
    prachF = prachF_tmp
    
    // MAIN LOOP: Process all FD occasions
    for (current_fd_occasion = 0; current_fd_occasion <= fd_occasion; current_fd_occasion++) {
        
        LOG_D(PHY, "Processing FD occasion %d/%d\n", current_fd_occasion, fd_occasion)
        
        // Compute root sequences for this FD occasion (if needed)
        if (!root_seq_computed) {
            compute_nr_prach_seq(
                nrUE_config->prach_config.prach_sequence_length,
                nrUE_config->prach_config.num_prach_fd_occasions_list[current_fd_occasion].num_root_sequences,
                nrUE_config->prach_config.num_prach_fd_occasions_list[current_fd_occasion].prach_root_sequence_index,
                ue->X_u
            )
        }
        
        // Get frequency parameters for this FD occasion
        n_ra_prb = nrUE_config->prach_config.num_prach_fd_occasions_list[current_fd_occasion].k1
        k = 12 * n_ra_prb - 6 * fp->N_RB_UL
        
        // Normalize k to valid range
        if (k < 0) {
            k += fp->ofdm_symbol_size
        }
        
        k *= K
        k += kbar
        
        LOG_I(PHY, "FD occasion %d: placing PRACH at position %d, freq start %d\n",
              current_fd_occasion, k * 2, n_ra_prb)
        
        // Sanity check for attack sequences
        Assert(num_attack_sequences < num_root_sequences,
               "num_attack_sequences must be less than available root sequences")
        
        // Reduce amplitude to prevent overflow when combining sequences
        original_amp = amp
        amp = original_amp / num_attack_sequences
        initial_k = k
        
        // ATTACK: Combine multiple root sequences
        for (seq_idx = 0; seq_idx < num_attack_sequences; seq_idx++) {
            
            // Select different root sequence for each iteration
            root_seq_index = (preamble_offset - first_nonzero_root_idx + seq_idx) 
                           % num_root_sequences
            
            Xu = ue->X_u[root_seq_index]
            current_k = initial_k
            
            // Generate signal for this sequence
            for (offset = 0; offset < N_ZC; offset++) {
                
                offset2 = offset * preamble_shift
                if (offset2 >= N_ZC) {
                    offset2 -= N_ZC
                }
                
                // Multiply with amplitude
                Xu_t = Xu[offset] * amp
                
                // Apply cyclic shift
                w = 2 * PI * offset2 / N_ZC
                ru = exp(j * w)
                
                // Combine signal (ADD to existing prachF)
                p = Xu_t * ru
                prachF[current_k].real += p.real
                prachF[current_k].imag += p.imag
                
                current_k++
                if (current_k * 2 == dftlen) {
                    current_k = 0
                }
            }
        }
    }
    
    // Mark root sequences as computed
    root_seq_computed = 1
    
    // ATTACK: Force PRACH format to 8
    prach_fmt_id = 8
    
    // Continue with standard PRACH processing...
    // (DFT, OFDM modulation, etc.)
}
```

**Key Attack Features**:
1. **Loop over all FD occasions**: Each FD occasion uses different frequency resources
2. **Multiple root sequences per FD occasion**: Combine 3 different sequences (num_attack_sequences = 3)
3. **Amplitude reduction**: Divide by num_attack_sequences to prevent overflow
4. **Signal accumulation**: Add all sequences to the same time-frequency resources
5. **Force PRACH format 8**: Ensures consistent format across all occasions
