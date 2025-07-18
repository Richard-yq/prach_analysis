import re
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
import numpy as np
import statistics
from scipy import stats
from scipy.signal import find_peaks

# 設定中文字體支援
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 攻擊者數據（從之前的分析中提取）
log_data = """
[PHY]   [RAPROC] 0.19 prach_I0 = 18.9 dB
[PHY]   [RAPROC] 1.19 prach_I0 = 19.0 dB
[PHY]   [RAPROC] 2.19 prach_I0 = 18.9 dB
[PHY]   [RAPROC] 3.19 prach_I0 = 18.9 dB
[PHY]   [RAPROC] 4.19 prach_I0 = 18.9 dB
[PHY]   [RAPROC] 5.19 prach_I0 = 19.3 dB
[PHY]   [RAPROC] 6.19 prach_I0 = 19.2 dB
[PHY]   [RAPROC] 7.19 prach_I0 = 19.4 dB
[PHY]   [RAPROC] 8.19 prach_I0 = 19.2 dB
[PHY]   [RAPROC] 9.19 prach_I0 = 19.2 dB
[PHY]   [RAPROC] 10.19 prach_I0 = 19.1 dB
[PHY]   [RAPROC] 11.19 prach_I0 = 19.2 dB
[PHY]   [RAPROC] 12.19 prach_I0 = 19.7 dB
[PHY]   [RAPROC] 13.19 prach_I0 = 19.9 dB
[PHY]   [RAPROC] 14.19 prach_I0 = 19.6 dB
[PHY]   [RAPROC] 15.19 prach_I0 = 19.9 dB
[PHY]   [RAPROC] 16.19 prach_I0 = 19.8 dB
[PHY]   [RAPROC] 17.19 prach_I0 = 19.7 dB
[PHY]   [RAPROC] 18.19 prach_I0 = 19.7 dB
[PHY]   [RAPROC] 19.19 prach_I0 = 19.6 dB
[PHY]   [RAPROC] 20.19 prach_I0 = 19.6 dB
[PHY]   [RAPROC] 21.19 prach_I0 = 19.9 dB
[PHY]   [RAPROC] 22.19 prach_I0 = 19.9 dB
[PHY]   [RAPROC] 23.19 prach_I0 = 20.0 dB
[PHY]   [RAPROC] 24.19 prach_I0 = 19.8 dB
[PHY]   [RAPROC] 25.19 prach_I0 = 20.2 dB
[PHY]   [RAPROC] 26.19 prach_I0 = 20.1 dB
[PHY]   [RAPROC] 27.19 prach_I0 = 24.3 dB
[PHY]   [RAPROC] 28.19 prach_I0 = 28.0 dB
[PHY]   [RAPROC] 29.19 prach_I0 = 31.4 dB
[PHY]   [RAPROC] 30.19 prach_I0 = 34.3 dB
[PHY]   [RAPROC] 31.19 prach_I0 = 36.8 dB
[PHY]   [RAPROC] 32.19 prach_I0 = 39.0 dB
[PHY]   [RAPROC] 33.19 prach_I0 = 40.9 dB
[PHY]   [RAPROC] 34.19 prach_I0 = 42.7 dB
[PHY]   [RAPROC] 35.19 prach_I0 = 44.2 dB
[PHY]   [RAPROC] 36.19 prach_I0 = 45.4 dB
[PHY]   [RAPROC] 37.19 prach_I0 = 46.6 dB
[PHY]   [RAPROC] 38.19 prach_I0 = 47.6 dB
[PHY]   [RAPROC] 39.19 prach_I0 = 48.6 dB
[PHY]   [RAPROC] 40.19 prach_I0 = 49.4 dB
[PHY]   [RAPROC] 41.19 prach_I0 = 50.1 dB
[PHY]   [RAPROC] 42.19 prach_I0 = 50.7 dB
[PHY]   [RAPROC] 43.19 prach_I0 = 51.3 dB
[PHY]   [RAPROC] 44.19 prach_I0 = 51.7 dB
[PHY]   [RAPROC] 45.19 prach_I0 = 52.1 dB
[PHY]   [RAPROC] 46.19 prach_I0 = 52.4 dB
[PHY]   [RAPROC] 47.19 prach_I0 = 52.7 dB
[PHY]   [RAPROC] 48.19 prach_I0 = 53.0 dB
[PHY]   [RAPROC] 49.19 prach_I0 = 53.2 dB
[PHY]   [RAPROC] 50.19 prach_I0 = 53.4 dB
[PHY]   [RAPROC] 51.19 prach_I0 = 53.7 dB
[PHY]   [RAPROC] 52.19 prach_I0 = 53.8 dB
[PHY]   [RAPROC] 53.19 prach_I0 = 53.9 dB
[PHY]   [RAPROC] 54.19 prach_I0 = 54.1 dB
[PHY]   [RAPROC] 55.19 prach_I0 = 54.2 dB
[PHY]   [RAPROC] 56.19 prach_I0 = 54.3 dB
[PHY]   [RAPROC] 57.19 prach_I0 = 54.5 dB
[PHY]   [RAPROC] 58.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 59.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 60.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 61.19 prach_I0 = 54.5 dB
[PHY]   [RAPROC] 62.19 prach_I0 = 54.5 dB
[PHY]   [RAPROC] 63.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 64.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 65.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 66.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 67.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 68.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 69.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 70.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 71.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 72.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 73.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 74.19 prach_I0 = 54.6 dB
[PHY]   [RAPROC] 75.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 76.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 77.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 78.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 79.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 80.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 81.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 82.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 83.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 84.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 85.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 86.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 87.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 88.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 89.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 90.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 91.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 92.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 93.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 94.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 95.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 96.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 97.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 98.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 99.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 100.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 101.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 102.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 103.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 104.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 105.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 106.19 prach_I0 = 54.7 dB
[PHY]   [RAPROC] 107.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 108.19 prach_I0 = 54.8 dB
[PHY]   [RAPROC] 109.19 prach_I0 = 54.9 dB
[PHY]   [RAPROC] 110.19 prach_I0 = 54.9 dB
[PHY]   [RAPROC] 111.19 prach_I0 = 54.9 dB
[PHY]   [RAPROC] 112.19 prach_I0 = 54.9 dB
[PHY]   [RAPROC] 113.19 prach_I0 = 54.9 dB
[PHY]   [RAPROC] 114.19 prach_I0 = 54.9 dB
[PHY]   [RAPROC] 115.19 prach_I0 = 55.0 dB
[PHY]   [RAPROC] 116.19 prach_I0 = 55.0 dB
[PHY]   [RAPROC] 117.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 118.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 119.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 120.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 121.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 122.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 123.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 124.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 125.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 126.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 127.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 128.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 129.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 130.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 131.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 132.19 prach_I0 = 55.1 dB
[PHY]   [RAPROC] 133.19 prach_I0 = 55.2 dB
[PHY]   [RAPROC] 134.19 prach_I0 = 55.2 dB
[PHY]   [RAPROC] 135.19 prach_I0 = 55.2 dB
[PHY]   [RAPROC] 136.19 prach_I0 = 55.2 dB
[PHY]   [RAPROC] 137.19 prach_I0 = 55.2 dB
[PHY]   [RAPROC] 138.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 139.19 prach_I0 = 55.4 dB
[PHY]   [RAPROC] 140.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 141.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 142.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 143.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 144.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 145.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 146.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 147.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 148.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 149.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 150.19 prach_I0 = 55.4 dB
[PHY]   [RAPROC] 151.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 152.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 153.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 154.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 155.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 156.19 prach_I0 = 55.3 dB
[PHY]   [RAPROC] 157.19 prach_I0 = 51.0 dB
[PHY]   [RAPROC] 158.19 prach_I0 = 47.1 dB
[PHY]   [RAPROC] 159.19 prach_I0 = 43.6 dB
[PHY]   [RAPROC] 160.19 prach_I0 = 40.7 dB
[PHY]   [RAPROC] 161.19 prach_I0 = 37.9 dB
[PHY]   [RAPROC] 162.19 prach_I0 = 35.5 dB
[PHY]   [RAPROC] 163.19 prach_I0 = 33.6 dB
[PHY]   [RAPROC] 164.19 prach_I0 = 31.8 dB
[PHY]   [RAPROC] 165.19 prach_I0 = 30.2 dB
[PHY]   [RAPROC] 166.19 prach_I0 = 29.0 dB
[PHY]   [RAPROC] 167.19 prach_I0 = 27.9 dB
[PHY]   [RAPROC] 168.19 prach_I0 = 27.2 dB
[PHY]   [RAPROC] 169.19 prach_I0 = 26.3 dB
[PHY]   [RAPROC] 170.19 prach_I0 = 25.6 dB
[PHY]   [RAPROC] 171.19 prach_I0 = 24.8 dB
[PHY]   [RAPROC] 172.19 prach_I0 = 24.1 dB
[PHY]   [RAPROC] 173.19 prach_I0 = 23.6 dB
[PHY]   [RAPROC] 174.19 prach_I0 = 23.0 dB
[PHY]   [RAPROC] 175.19 prach_I0 = 22.5 dB
[PHY]   [RAPROC] 176.19 prach_I0 = 22.1 dB
[PHY]   [RAPROC] 177.19 prach_I0 = 21.7 dB
[PHY]   [RAPROC] 178.19 prach_I0 = 21.2 dB
[PHY]   [RAPROC] 179.19 prach_I0 = 20.8 dB
[PHY]   [RAPROC] 180.19 prach_I0 = 20.5 dB
[PHY]   [RAPROC] 181.19 prach_I0 = 20.3 dB
[PHY]   [RAPROC] 182.19 prach_I0 = 20.1 dB
[PHY]   [RAPROC] 183.19 prach_I0 = 19.8 dB
[PHY]   [RAPROC] 184.19 prach_I0 = 19.7 dB
[PHY]   [RAPROC] 185.19 prach_I0 = 19.6 dB
[PHY]   [RAPROC] 186.19 prach_I0 = 19.5 dB
[PHY]   [RAPROC] 187.19 prach_I0 = 19.4 dB
[PHY]   [RAPROC] 188.19 prach_I0 = 19.1 dB
[PHY]   [RAPROC] 189.19 prach_I0 = 18.9 dB
[PHY]   [RAPROC] 190.19 prach_I0 = 18.9 dB
[PHY]   [RAPROC] 191.19 prach_I0 = 18.8 dB
[PHY]   [RAPROC] 192.19 prach_I0 = 18.7 dB
[PHY]   [RAPROC] 193.19 prach_I0 = 18.7 dB
[PHY]   [RAPROC] 194.19 prach_I0 = 18.6 dB
[PHY]   [RAPROC] 195.19 prach_I0 = 18.5 dB
[PHY]   [RAPROC] 196.19 prach_I0 = 18.6 dB
[PHY]   [RAPROC] 197.19 prach_I0 = 18.6 dB
[PHY]   [RAPROC] 198.19 prach_I0 = 18.4 dB
[PHY]   [RAPROC] 199.19 prach_I0 = 18.4 dB
[PHY]   [RAPROC] 200.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 201.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 202.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 203.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 204.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 205.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 206.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 207.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 208.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 209.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 210.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 211.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 212.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 213.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 214.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 215.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 216.19 prach_I0 = 17.9 dB
[PHY]   [RAPROC] 217.19 prach_I0 = 18.0 dB
[PHY]   [RAPROC] 218.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 219.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 220.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 221.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 222.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 223.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 224.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 225.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 226.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 227.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 228.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 229.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 230.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 231.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 232.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 233.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 234.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 235.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 236.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 237.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 238.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 239.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 240.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 241.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 242.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 243.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 244.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 245.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 246.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 247.19 prach_I0 = 18.4 dB
[PHY]   [RAPROC] 248.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 249.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 250.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 251.19 prach_I0 = 18.3 dB
[PHY]   [RAPROC] 252.19 prach_I0 = 18.1 dB
[PHY]   [RAPROC] 253.19 prach_I0 = 18.2 dB
[PHY]   [RAPROC] 254.19 prach_I0 = 18.2 dB
"""

# 數據解析
frames = []
prach_i0_values = []

pattern = re.compile(r'(?:\[PHY\]\s+\[RAPROC\]\s+)?(\d+\.\d+)\s+prach_I0\s*=\s*(\d+\.\d+)\s*dB')

for line in log_data.strip().split('\n'):
    match = pattern.search(line)
    if match:
        frame_full = match.group(1)
        frame = int(float(frame_full))
        prach_i0 = float(match.group(2))
        frames.append(frame)
        prach_i0_values.append(prach_i0)

# 攻擊階段定義
def define_attack_phases(frames, values):
    """基於數據特徵自動識別攻擊階段"""
    phases = {}
    
    # 階段1：正常基線 (Frame 0-26)
    normal_end = 26
    phases['正常基線'] = {
        'frames': [f for f in frames if f <= normal_end],
        'values': [v for f, v in zip(frames, values) if f <= normal_end],
        'start_frame': 0,
        'end_frame': normal_end
    }
    
    # 階段2：攻擊上升 (Frame 27-39) - 急劇上升階段
    ramp_up_end = 39
    phases['攻擊上升'] = {
        'frames': [f for f in frames if normal_end < f <= ramp_up_end],
        'values': [v for f, v in zip(frames, values) if normal_end < f <= ramp_up_end],
        'start_frame': normal_end + 1,
        'end_frame': ramp_up_end
    }
    
    # 階段3：攻擊維持高峰 (Frame 40-156) - 維持高噪聲水平
    sustain_end = 156
    phases['攻擊維持'] = {
        'frames': [f for f in frames if ramp_up_end < f <= sustain_end],
        'values': [v for f, v in zip(frames, values) if ramp_up_end < f <= sustain_end],
        'start_frame': ramp_up_end + 1,
        'end_frame': sustain_end
    }
    
    # 階段4：攻擊下降 (Frame 157-189) - 快速下降階段
    ramp_down_end = 189
    phases['攻擊下降'] = {
        'frames': [f for f in frames if sustain_end < f <= ramp_down_end],
        'values': [v for f, v in zip(frames, values) if sustain_end < f <= ramp_down_end],
        'start_frame': sustain_end + 1,
        'end_frame': ramp_down_end
    }
    
    # 階段5：恢復正常 (Frame 190-254)
    phases['恢復正常'] = {
        'frames': [f for f in frames if f > ramp_down_end],
        'values': [v for f, v in zip(frames, values) if f > ramp_down_end],
        'start_frame': ramp_down_end + 1,
        'end_frame': max(frames)
    }
    
    return phases

# 階段統計分析
def analyze_phase(phase_data, phase_name):
    """分析單個攻擊階段的詳細統計"""
    frames = phase_data['frames']
    values = phase_data['values']
    
    if not values:
        return None
    
    analysis = {
        'name': phase_name,
        'duration': len(frames),
        'frame_range': f"{min(frames)} - {max(frames)}",
        'mean': np.mean(values),
        'std': np.std(values),
        'min': min(values),
        'max': max(values),
        'range': max(values) - min(values),
        'cv': (np.std(values) / np.mean(values)) * 100 if np.mean(values) != 0 else 0
    }
    
    # 計算變化率
    if len(values) > 1:
        changes = np.diff(values)
        analysis['max_change'] = max(abs(change) for change in changes)
        analysis['avg_change'] = np.mean(np.abs(changes))
        analysis['change_std'] = np.std(changes)
        
        # 線性趨勢
        x = np.arange(len(values))
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, values)
        analysis['slope'] = slope
        analysis['r_squared'] = r_value**2
        analysis['trend_significance'] = p_value
    
    return analysis

# 攻擊效果評估
def assess_attack_effectiveness(phases):
    """評估攻擊效果和影響"""
    normal_baseline = phases['正常基線']['values']
    attack_sustain = phases['攻擊維持']['values']
    recovery = phases['恢復正常']['values']
    
    baseline_mean = np.mean(normal_baseline)
    attack_mean = np.mean(attack_sustain)
    recovery_mean = np.mean(recovery)
    
    effectiveness = {
        'baseline_level': baseline_mean,
        'attack_peak': attack_mean,
        'recovery_level': recovery_mean,
        'attack_amplification': attack_mean - baseline_mean,
        'amplification_ratio': attack_mean / baseline_mean if baseline_mean != 0 else float('inf'),
        'recovery_effectiveness': abs(recovery_mean - baseline_mean) / baseline_mean * 100 if baseline_mean != 0 else 0,
        'attack_duration': len(phases['攻擊上升']['frames']) + len(phases['攻擊維持']['frames']) + len(phases['攻擊下降']['frames'])
    }
    
    return effectiveness

# 主要分析
phases = define_attack_phases(frames, prach_i0_values)

# 創建綜合視覺化
fig = plt.figure(figsize=(20, 16))

# 1. 完整時間序列與階段標記
ax1 = plt.subplot(3, 3, (1, 3))
colors = ['green', 'orange', 'red', 'blue', 'purple']
phase_names = ['正常基線', '攻擊上升', '攻擊維持', '攻擊下降', '恢復正常']

# 繪製完整數據
ax1.plot(frames, prach_i0_values, 'k-', alpha=0.3, linewidth=1, label='完整數據')

# 為每個階段著色
for i, (phase_name, phase_data) in enumerate(phases.items()):
    if phase_data['frames']:
        ax1.plot(phase_data['frames'], phase_data['values'], 
                color=colors[i], linewidth=2, label=phase_name, marker='o', markersize=3)

ax1.set_title('攻擊階段完整分析 - 時間序列', fontsize=16, fontweight='bold')
ax1.set_xlabel('Frame')
ax1.set_ylabel('prach_I0 (dB)')
ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
ax1.grid(True, alpha=0.3)

# 2. 各階段箱形圖比較
ax2 = plt.subplot(3, 3, 4)
phase_values = [phases[name]['values'] for name in phase_names if phases[name]['values']]
phase_labels = [name for name in phase_names if phases[name]['values']]
bp = ax2.boxplot(phase_values, labels=phase_labels, patch_artist=True)
for patch, color in zip(bp['boxes'], colors[:len(phase_values)]):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
ax2.set_title('各階段數值分布比較', fontsize=14)
ax2.set_ylabel('prach_I0 (dB)')
ax2.tick_params(axis='x', rotation=45)

# 3. 攻擊上升階段詳細分析
ax3 = plt.subplot(3, 3, 5)
ramp_up = phases['攻擊上升']
if ramp_up['frames']:
    ax3.plot(ramp_up['frames'], ramp_up['values'], 'o-', color='orange', linewidth=2, markersize=6)
    # 添加趨勢線
    z = np.polyfit(range(len(ramp_up['values'])), ramp_up['values'], 1)
    p = np.poly1d(z)
    ax3.plot(ramp_up['frames'], p(range(len(ramp_up['values']))), "--", color='red', alpha=0.8, linewidth=2)
    ax3.set_title(f'攻擊上升階段詳細分析\n(Frame {ramp_up["start_frame"]}-{ramp_up["end_frame"]})', fontsize=14)
    ax3.set_xlabel('Frame')
    ax3.set_ylabel('prach_I0 (dB)')
    ax3.grid(True, alpha=0.3)

# 4. 攻擊維持階段穩定性分析
ax4 = plt.subplot(3, 3, 6)
sustain = phases['攻擊維持']
if sustain['frames']:
    ax4.plot(sustain['frames'], sustain['values'], 'o-', color='red', linewidth=1, markersize=2, alpha=0.7)
    mean_sustain = np.mean(sustain['values'])
    std_sustain = np.std(sustain['values'])
    ax4.axhline(y=mean_sustain, color='darkred', linestyle='--', linewidth=2, label=f'平均值: {mean_sustain:.1f} dB')
    ax4.axhline(y=mean_sustain + std_sustain, color='orange', linestyle=':', alpha=0.8, label=f'+1σ: {mean_sustain + std_sustain:.1f} dB')
    ax4.axhline(y=mean_sustain - std_sustain, color='orange', linestyle=':', alpha=0.8, label=f'-1σ: {mean_sustain - std_sustain:.1f} dB')
    ax4.set_title(f'攻擊維持階段穩定性\n(Frame {sustain["start_frame"]}-{sustain["end_frame"]})', fontsize=14)
    ax4.set_xlabel('Frame')
    ax4.set_ylabel('prach_I0 (dB)')
    ax4.legend()
    ax4.grid(True, alpha=0.3)

# 5. 攻擊下降階段分析
ax5 = plt.subplot(3, 3, 7)
ramp_down = phases['攻擊下降']
if ramp_down['frames']:
    ax5.plot(ramp_down['frames'], ramp_down['values'], 'o-', color='blue', linewidth=2, markersize=6)
    # 添加指數衰減擬合
    try:
        from scipy.optimize import curve_fit
        def exp_decay(x, a, b, c):
            return a * np.exp(-b * x) + c
        
        x_data = np.array(range(len(ramp_down['values'])))
        y_data = np.array(ramp_down['values'])
        popt, _ = curve_fit(exp_decay, x_data, y_data, maxfev=2000)
        ax5.plot(ramp_down['frames'], exp_decay(x_data, *popt), '--', color='darkblue', alpha=0.8, linewidth=2, label='指數衰減擬合')
        ax5.legend()
    except:
        pass
    
    ax5.set_title(f'攻擊下降階段分析\n(Frame {ramp_down["start_frame"]}-{ramp_down["end_frame"]})', fontsize=14)
    ax5.set_xlabel('Frame')
    ax5.set_ylabel('prach_I0 (dB)')
    ax5.grid(True, alpha=0.3)

# 6. 變化率分析
ax6 = plt.subplot(3, 3, 8)
changes = np.diff(prach_i0_values)
change_frames = frames[1:]
colors_change = []
for i, frame in enumerate(change_frames):
    if frame <= 26:
        colors_change.append('green')
    elif frame <= 39:
        colors_change.append('orange')
    elif frame <= 156:
        colors_change.append('red')
    elif frame <= 189:
        colors_change.append('blue')
    else:
        colors_change.append('purple')

ax6.bar(change_frames, changes, color=colors_change, alpha=0.7, width=0.8)
ax6.axhline(y=0, color='black', linestyle='-', alpha=0.5)
ax6.set_title('各階段變化率分析', fontsize=14)
ax6.set_xlabel('Frame')
ax6.set_ylabel('prach_I0 變化量 (dB)')
ax6.grid(True, alpha=0.3)

# 7. 攻擊效果統計
ax7 = plt.subplot(3, 3, 9)
effectiveness = assess_attack_effectiveness(phases)
metrics = ['基線水平', '攻擊峰值', '恢復水平']
values_eff = [effectiveness['baseline_level'], effectiveness['attack_peak'], effectiveness['recovery_level']]
bars = ax7.bar(metrics, values_eff, color=['green', 'red', 'purple'], alpha=0.7)
ax7.set_title('攻擊效果對比', fontsize=14)
ax7.set_ylabel('prach_I0 (dB)')
for bar, value in zip(bars, values_eff):
    ax7.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             f'{value:.1f} dB', ha='center', va='bottom', fontweight='bold')
ax7.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 詳細統計報告
print("="*80)
print("🚨 攻擊階段深度分析報告 🚨")
print("="*80)

print("\n📊 【各攻擊階段統計摘要】")
print("-" * 60)
for phase_name in phase_names:
    if phases[phase_name]['values']:
        analysis = analyze_phase(phases[phase_name], phase_name)
        print(f"\n🔹 {analysis['name']}階段:")
        print(f"   ⏱️  持續時間: {analysis['duration']} 個Frame ({analysis['frame_range']})")
        print(f"   📈 平均值: {analysis['mean']:.2f} dB")
        print(f"   📊 標準差: {analysis['std']:.2f} dB")
        print(f"   📏 數值範圍: {analysis['min']:.1f} - {analysis['max']:.1f} dB (範圍: {analysis['range']:.1f} dB)")
        print(f"   🎯 變異係數: {analysis['cv']:.1f}%")
        
        if 'slope' in analysis:
            trend_desc = "上升" if analysis['slope'] > 0.1 else "下降" if analysis['slope'] < -0.1 else "穩定"
            print(f"   📈 趨勢斜率: {analysis['slope']:.4f} dB/Frame ({trend_desc})")
            print(f"   🎯 趨勢擬合度: R² = {analysis['r_squared']:.3f}")
            print(f"   ⚡ 最大變化: {analysis['max_change']:.2f} dB")
            print(f"   📊 平均變化: {analysis['avg_change']:.2f} dB")

print("\n" + "="*60)
print("🎯 【攻擊效果評估】")
print("="*60)
effectiveness = assess_attack_effectiveness(phases)
print(f"🔸 基線噪聲水平: {effectiveness['baseline_level']:.2f} dB")
print(f"🔸 攻擊峰值水平: {effectiveness['attack_peak']:.2f} dB")
print(f"🔸 恢復後水平: {effectiveness['recovery_level']:.2f} dB")
print(f"🚨 噪聲放大幅度: +{effectiveness['attack_amplification']:.2f} dB")
print(f"🚨 放大倍數: {effectiveness['amplification_ratio']:.1f}x")
print(f"⏱️  攻擊總持續時間: {effectiveness['attack_duration']} 個Frame")
print(f"🔄 恢復效果: {effectiveness['recovery_effectiveness']:.1f}% 偏差於基線")

print("\n" + "="*60)
print("⚠️  【關鍵攻擊特徵】")
print("="*60)

# 攻擊上升階段分析
ramp_up = phases['攻擊上升']
if ramp_up['values']:
    ramp_analysis = analyze_phase(ramp_up, '攻擊上升')
    print(f"🔥 攻擊啟動速度: {ramp_analysis['slope']:.2f} dB/Frame")
    print(f"🚀 上升階段最大跳躍: {ramp_analysis['max_change']:.2f} dB")

# 攻擊維持階段分析
sustain = phases['攻擊維持']
if sustain['values']:
    sustain_analysis = analyze_phase(sustain, '攻擊維持')
    print(f"🎯 攻擊維持穩定性: CV = {sustain_analysis['cv']:.1f}% (越低越穩定)")
    print(f"⏱️  高噪聲維持時間: {sustain_analysis['duration']} 個Frame")

# 攻擊下降階段分析  
ramp_down = phases['攻擊下降']
if ramp_down['values']:
    ramp_down_analysis = analyze_phase(ramp_down, '攻擊下降')
    print(f"📉 攻擊結束速度: {abs(ramp_down_analysis['slope']):.2f} dB/Frame")
    print(f"⚡ 下降階段最大跳躍: {ramp_down_analysis['max_change']:.2f} dB")

print("\n" + "="*60)
print("🛡️  【防禦建議】")
print("="*60)
print("基於攻擊模式分析，建議以下防禦措施：")
print(f"1. 🚨 設定動態閾值檢測: > {effectiveness['baseline_level'] + 3:.1f} dB 觸發警報")
print(f"2. ⏱️  快速響應時間: 檢測到連續 3 個Frame 異常變化 (> 2 dB) 即啟動防護")
print(f"3. 📊 變化率監控: 監控相鄰Frame變化率，超過 ±2 dB 即為可疑")
print(f"4. 🔄 恢復驗證: 確保攻擊結束後數值回到 {effectiveness['baseline_level']:.1f} ± 1 dB 範圍")
print(f"5. 📈 趨勢預警: 監控短期移動平均，異常趨勢變化可提前預警")

print("\n" + "="*80)
