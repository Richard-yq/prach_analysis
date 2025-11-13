DATA = """
# MTKUE 1113-2 PrachCFID:157 B4 log
SFN/SFN/SLOT/SYMBOL,attempt time,preamble index,Tx power
241|4|1|0,1,19,-21 dBm
242|4|1|0,2,11,-19 dBm
243|4|1|0,3,14,-17 dBm
244|4|1|0,4,3,-15 dBm
245|4|1|0,5,54,-13 dBm
246|4|1|0,6,9,-11 dBm
247|4|1|0,7,0,-9 dBm
248|4|1|0,8,24,-7 dBm
249|4|1|0,9,45,-5 dBm
250|4|1|0,10,22,-3 dBm
251|4|1|0,11,18,-1 dBm
252|4|1|0,12,47,1 dBm
253|4|1|0,13,50,3 dBm
254|4|1|0,14,57,5 dBm
255|4|1|0,15,26,7 dBm
256|4|1|0,16,54,9 dBm
257|4|1|0,17,6,11 dBm
258|4|1|0,18,55,13 dBm
259|4|1|0,19,31,15 dBm
260|4|1|0,20,20,17 dBm
261|4|1|0,21,4,19 dBm
262|4|1|0,22,53,20 dBm
263|4|1|0,23,27,20 dBm
264|4|1|0,24,0,20 dBm
265|4|1|0,25,41,20 dBm
266|4|1|0,26,6,20 dBm
267|4|1|0,27,50,20 dBm
268|4|1|0,28,59,20 dBm
269|4|1|0,29,5,20 dBm
270|4|1|0,30,47,20 dBm
271|4|1|0,31,11,20 dBm
272|4|1|0,32,50,20 dBm
273|4|1|0,33,9,20 dBm
274|4|1|0,34,42,20 dBm
275|4|1|0,35,41,20 dBm
276|4|1|0,36,33,20 dBm
277|4|1|0,37,29,20 dBm

#---
# End of MTKUE 1113-2 PrachCFID:157 log
SFN/SFN/SLOT/SYMBOL,attempt time,Preamble index,Tx power
259|4|1|0,1,28,-24 dBm
260|4|1|0,2,31,-22 dBm
261|4|1|0,3,54,-19 dBm
263|4|1|0,4,9,-15 dBm
264|4|1|0,5,7,-13 dBm
265|4|1|0,6,32,-11 dBm
266|4|1|0,7,26,-9 dBm
267|4|1|0,8,58,-7 dBm
268|4|1|0,9,32,-5 dBm
269|4|1|0,10,27,-3 dBm
270|4|1|0,11,28,-1 dBm
271|4|1|0,12,31,1 dBm
272|4|1|0,13,51,3 dBm
273|4|1|0,14,33,5 dBm
274|4|1|0,15,11,7 dBm
275|4|1|0,16,29,9 dBm
276|4|1|0,17,56,11 dBm
277|4|1|0,18,4,13 dBm
278|4|1|0,19,58,15 dBm
279|4|1|0,20,56,17 dBm
280|4|1|0,21,18,19 dBm
281|4|1|0,22,48,20 dBm
282|4|1|0,23,51,20 dBm
283|4|1|0,24,58,20 dBm
284|4|1|0,25,51,20 dBm
285|4|1|0,26,21,20 dBm
286|4|1|0,27,24,20 dBm
287|4|1|0,28,16,20 dBm
288|4|1|0,29,40,20 dBm
289|4|1|0,30,21,20 dBm
290|4|1|0,31,14,20 dBm
291|4|1|0,32,16,20 dBm
292|4|1|0,33,58,20 dBm
293|4|1|0,34,13,20 dBm
294|4|1|0,35,37,20 dBm
295|4|1|0,36,37,20 dBm
296|4|1|0,37,34,20 dBm
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