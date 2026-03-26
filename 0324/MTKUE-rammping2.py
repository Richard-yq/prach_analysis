DATA = """
# MTKUE 1205 PrachCFID:148 B4 log power rammping 2 db
attempt time,preamble index,Tx power
1,38,-24 dbm
2,24,-24 dbm
3,22,-24 dbm
4,44,-24 dbm
5,18,-24 dbm
6,28,-24 dbm
7,29,-24 dbm
8,19,-24 dbm
9,22,-24 dbm
10,32,-24 dbm

11,8,-24 dbm,failed at RAR
12,27,-24 dbm,failed at RAR
13,35,-24 dbm,failed at RAR
14,43,-22 dbm,failed at RAR
15,51,-20 dbm,failed at RAR
16,59,-18 dbm,failed at RAR
17,23,-16 dbm,failed at RAR
18,31,-14 dbm,failed at RAR
19,39,-12 dbm,failed at RAR
20,47,-10 dbm,failed at RAR
21,55,-8 dbm
22,11,-24 dbm
23,19,-24 dbm
24,27,-24 dbm
25,35,-24 dbm
26,43,-24 dbm
27,51,-24 dbm


"""

if __name__ == "__main__":
    """繪圖工具：解析本檔案中的 log lines 並繪製 SFN vs Tx power。

    規則：
    - 每一筆資料格式範例：241|4|1|0,1,19,-21 dBm
      -> 第一欄取 '|' 分隔的第一個數，視為 SFN
      -> 逗號分隔後的第3欄為 preamble index
      -> 第4欄包含 Tx power (帶 'dBm')
    - 預設所有記錄為 'failed at RAR'（紅色）。可以修改 status 判斷邏輯以顯示成功點。
    """
    import re
    import matplotlib.pyplot as plt

    # 解決 Mac 環境下 matplotlib 顯示中文會出現方塊/警告的問題
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'PingFang TC', 'Heiti TC', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False

    #filepath = __file__

    entries = []  # list of dict: {'sfn':int, 'attempt':str, 'preamble':int, 'power':float, 'status':str}

    # 直接從 DATA 逐行讀取，避免把整個檔案當作程式碼執行時發生 SyntaxError
    import sys, os

    def load_lines_from_source(path=None):
        """若指定 path 且存在，從該檔案讀取；否則回傳內建 DATA 的行清單。"""
        if path:
            if os.path.isfile(path):
                with open(path, 'r', encoding='utf-8') as fh:
                    return fh.read().splitlines()
            else:
                print(f"找不到檔案: {path}，改用內建 DATA")
        return DATA.splitlines()

    # 如果有提供命令列參數，第一個參數視為資料檔案路徑
    source = None
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg in ('-h', '--help'):
            print('Usage: python3 MTKUE-rammping.py [data_file.txt]\n如果未指定 data_file，程式會使用內建的 DATA。')
            sys.exit(0)
        source = arg

    lines = load_lines_from_source(source)
    
    # 從註解中提取 PrachCFID
    prach_cfid = None
    for raw in lines:
        if 'PrachCFID' in raw:
            m = re.search(r'PrachCFID[:\s]*(\d+)', raw)
            if m:
                prach_cfid = m.group(1)
                break
    
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        if line.startswith('#'):
            continue
        # skip header lines
        if 'SFN/SFN/SLOT/SYMBOL' in line or 'attempt time' in line or 'Preamble index' in line:
            continue
        # expected data lines contain commas
        if ',' not in line:
            continue
        parts = [p.strip() for p in line.split(',')]
        if len(parts) < 3:
            continue
            
        # 兼容有 SFN 與沒有 SFN 的格式
        if '|' in parts[0] and len(parts) >= 4:
            attempt = parts[1]
            preamble_str = parts[2]
            power_field = parts[3]
        else:
            attempt = parts[0]
            preamble_str = parts[1]
            power_field = parts[2]

        try:
            int(attempt) # 檢查 attempt 是否為數字，避免讀到標題
            preamble = int(preamble_str)
        except Exception:
            # could be non-integer, skip
            continue
            
        m = re.search(r'[-+]?\d+\.?\d*', power_field)
        if not m:
            continue
        power = float(m.group())

        # status: 你提到這幾筆都是 success，所以預設為 success (綠色點)
        status = 'success'
        
        # 若未來想在資料加上自訂的狀態欄位 (例如加上第 4 個逗號並填入 failed at RAR)
        if not ('|' in parts[0]) and len(parts) >= 4:
            status = parts[3].strip()
        elif ('|' in parts[0]) and len(parts) >= 5:
            status = parts[4].strip()

        entries.append({'attempt': attempt, 'preamble': preamble, 'power': power, 'status': status})

    if not entries:
        print('找不到符合格式的資料，請確認檔案內容。')
    else:
        # sort by attempt
        entries.sort(key=lambda e: int(e['attempt']))
        x = [int(e['attempt']) for e in entries]
        y = [e['power'] for e in entries]
        labels = [str(e['preamble']) for e in entries]
        statuses = [e['status'] for e in entries]

        color_map = {'success': 'green', 'failed at RAR': 'red'}
        colors = [color_map.get(s, 'red') for s in statuses]

        plt.figure(figsize=(12, 6))
        sc = plt.scatter(x, y, c=colors, s=80, edgecolors='k')

        # 標示 preamble index
        for xi, yi, lab in zip(x, y, labels):
            plt.annotate(lab, (xi, yi), textcoords='offset points', xytext=(4, 4), fontsize=8)

        plt.xlabel('Attempt')
        plt.ylabel('Tx power (dBm)')
        title = 'COTS UE RA Attempt vs Tx power'
        if prach_cfid:
            title += f' - PRACH Configuration Index: {prach_cfid}'
        plt.title(title)
        plt.grid(alpha=0.3)

        # legend: 手動建立
        import matplotlib.patches as mpatches
        import matplotlib.lines as mlines
        succ_patch = mpatches.Patch(color='green', label='Success')
        fail_patch = mpatches.Patch(color='red', label='Failed at RAR')
        # 用空心圓表示 preamble index
        circle_marker = mlines.Line2D([], [], marker='o', color='w', markerfacecolor='none', 
                                       markeredgecolor='k', markersize=6, label='Numbers = preamble index')
        plt.legend(handles=[succ_patch, fail_patch, circle_marker], loc='upper left')
        

        # 小格子顯示總嘗試數
        total = len(entries)
        succ_count = sum(1 for s in statuses if s == 'success')
        fail_count = sum(1 for s in statuses if s == 'failed at RAR')
        info = f'Total: {total}\nSuccess: {succ_count}\nFailed at RAR: {fail_count}'
        plt.gca().text(0.98, 0.98, info, transform=plt.gca().transAxes,
                       fontsize=9, va='top', ha='right', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        plt.tight_layout()
        script_dir = os.path.dirname(os.path.abspath(__file__))
        outname = os.path.join(script_dir, 'MTKUE_ramping_plot.png')
        plt.savefig(outname, dpi=200)
        print(f'圖已儲存為 {outname}')
        plt.show()