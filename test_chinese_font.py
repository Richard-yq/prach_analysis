import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager

# 設定中文字體支援
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 測試中文字體顯示
fig, ax = plt.subplots(figsize=(8, 5))
ax.text(0.5, 0.7, 'prach_I0 隨 Frame 的變化', fontsize=16, ha='center', transform=ax.transAxes)
ax.text(0.5, 0.5, '中文字體測試：正確顯示', fontsize=14, ha='center', transform=ax.transAxes)
ax.text(0.5, 0.3, 'Frame 數據分析圖表', fontsize=12, ha='center', transform=ax.transAxes)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title('中文字體顯示測試')
ax.set_xlabel('測試軸標籤')
ax.set_ylabel('數值 (dB)')

plt.tight_layout()
plt.show()

# 查看當前使用的字體
current_font = plt.rcParams['font.sans-serif'][0]
print(f"當前使用的字體：{current_font}")

# 列出系統可用的中文字體
chinese_fonts = []
for font in font_manager.fontManager.ttflist:
    if 'Chinese' in font.name or 'Arial Unicode' in font.name or 'SimHei' in font.name:
        chinese_fonts.append(font.name)

if chinese_fonts:
    print("\n系統中可用的中文字體：")
    for font in set(chinese_fonts):
        print(f"- {font}")
else:
    print("\n未找到專門的中文字體，但 Arial Unicode MS 應該支援中文字符")
