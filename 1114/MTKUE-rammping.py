DATA = """
# MTKUE 1114 PrachCFID:148 B4 log
SFN/SFN/SLOT/SYMBOL,attempt time,preamble index,Tx power
887|9|1|0,1,1,-27 dbm
889|9|1|0,2,3,-25 dbm
891|9|1|0,3,13,-23 dbm
893|9|1|0,4,47,-21 dbm
895|9|1|0,5,17,-19 dbm
897|9|1|0,6,27,-17 dbm
899|9|1|0,7,25,-15 dbm
901|9|1|0,8,59,-13 dbm
903|9|1|0,9,1,-11 dbm
905|9|1|0,10,43,-9 dbm
907|9|1|0,11,37,-7 dbm
909|9|1|0,12,35,-5 dbm
911|9|1|0,13,29,-3 dbm
913|9|1|0,14,3,-1 dbm
915|9|1|0,15,1,1 dbm
917|9|1|0,16,3,3 dbm
919|9|1|0,17,5,5 dbm
921|9|1|0,18,7,7 dbm


SFN/SFN/SLOT/SYMBOL,attempt time,preamble index,Tx power
905|9|1|0,1,12,-27 dbm
907|9|1|0,2,24,-25 dbm
909|9|1|0,3,56,-23 dbm
911|9|1|0,4,48,-21 dbm
913|9|1|0,5,39,-19 dbm
915|9|1|0,6,36,-17 dbm
917|9|1|0,7,33,-15 dbm
919|9|1|0,8,56,-13 dbm
921|9|1|0,9,56,-11 dbm
923|9|1|0,10,18,-9 dbm
925|9|1|0,11,22,-7 dbm
927|9|1|0,12,58,-5 dbm
929|9|1|0,13,58,-3 dbm
931|9|1|0,14,58,-1 dbm
933|9|1|0,15,46,1 dbm
935|9|1|0,16,54,3 dbm
937|9|1|0,17,14,5 dbm
939|9|1|0,18,26,7 dbm
941|9|1|0,19,21,9 dbm


# MTKUE 1114 PrachCFID:146 B4 log

SFN/SFN/SLOT/SYMBOL,attempt time,preamble index,Tx power
329|9|0|0,1,7,-27 dbm
337|9|0|0,2,53,-25 dbm
345|9|0|0,3,50,-23 dbm
353|9|0|0,4,0,-21 dbm
361|9|0|0,5,8,-19 dbm

# MTKUE 1114 PrachCFID:146 B4 log

SFN/SFN/SLOT/SYMBOL,attempt time,preamble index,Tx power
353|9|0|0,1,11,-27 dbm
361|9|0|0,2,15,-25 dbm
369|9|0|0,3,34,-23 dbm
377|9|0|0,4,5,-21 dbm


# MTKUE 1114 PrachCFID:145 B4 log

SFN/SFN/SLOT/SYMBOL,attempt time,preamble index,Tx power
193|9|0|0,1,54,-27 dbm
209|9|0|0,2,7,-25 dbm
225|9|0|0,3,24,-23 dbm


# MTKUE 1114 PrachCFID:145 B4 log

SFN/SFN/SLOT/SYMBOL,attempt time,preamble index,Tx power
225|9|0|0,1,19,-27 dbm
241|9|0|0,2,14,-25 dbm


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
        if len(parts) < 4:
            continue
        # parse SFN from first part (before first '|')
        first = parts[0]
        try:
            sfn = int(first.split('|')[0])
        except Exception:
            # not a valid data line
            continue
        attempt = parts[1]
        try:
            preamble = int(parts[2])
        except Exception:
            # could be non-integer, skip
            continue
        power_field = parts[3]
        m = re.search(r'[-+]?\d+\.?\d*', power_field)
        if not m:
            continue
        power = float(m.group())

        # status: 資料中沒有 success 標示，預設為 failed at RAR
        status = 'failed at RAR'

        entries.append({'sfn': sfn, 'attempt': attempt, 'preamble': preamble, 'power': power, 'status': status})

    if not entries:
        print('找不到符合格式的資料，請確認檔案內容。')
    else:
        # sort by sfn
        entries.sort(key=lambda e: e['sfn'])
        x = [e['sfn'] for e in entries]
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

        plt.xlabel('SFN')
        plt.ylabel('Tx power (dBm)')
        plt.title('SFN vs Tx power (annotated with preamble index)')
        plt.grid(alpha=0.3)

        # legend: 手動建立
        import matplotlib.patches as mpatches
        succ_patch = mpatches.Patch(color='green', label='success')
        fail_patch = mpatches.Patch(color='red', label='failed at RAR')
        plt.legend(handles=[succ_patch, fail_patch], loc='upper left')

        # 小格子顯示總嘗試數
        total = len(entries)
        succ_count = sum(1 for s in statuses if s == 'success')
        fail_count = sum(1 for s in statuses if s == 'failed at RAR')
        info = f'Total: {total}\nSuccess: {succ_count}\nFailed at RAR: {fail_count}'
        plt.gca().text(0.98, 0.02, info, transform=plt.gca().transAxes,
                       fontsize=9, va='bottom', ha='right', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        plt.tight_layout()
        outname = 'MTKUE_ramping_plot.png'
        plt.savefig(outname, dpi=200)
        print(f'圖已儲存為 {outname}')
        plt.show()