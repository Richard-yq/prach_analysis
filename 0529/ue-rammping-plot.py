"""
Plot UE power ramping under attack from ue-rammping.csv.

Each row is one RACH attempt (in order).
X-axis: attempt number
Y-axis: UE Tx power (dBm)
Colour: green = success, red = fail at RAR
Annotation: preamble index (shows random selection per attempt)
"""

import os
import csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ue-rammping.csv')

SUCCESS_COLOR = '#2ca02c'
FAIL_COLOR    = '#d62728'

entries = []  # list of (attempt, preamble, power, status)

with open(CSV_PATH, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    attempt = 0
    for row in reader:
        row = [c.strip() for c in row]
        if not row or not row[0]:
            continue
        if row[0].lower().startswith('preamble'):
            continue
        try:
            preamble = int(row[0])
            power    = float(row[1])
        except (ValueError, IndexError):
            continue
        status_raw = row[2].strip().lower() if len(row) > 2 else ''
        status = 'success' if 'success' in status_raw else 'fail at RAR'
        attempt += 1
        entries.append((attempt, preamble, power, status))

if not entries:
    raise SystemExit('No data found in CSV.')

x        = [e[0] for e in entries]          # attempt number
labels   = [str(e[1]) for e in entries]     # preamble index
y        = [e[2] for e in entries]          # Tx power
statuses = [e[3] for e in entries]
colors   = [SUCCESS_COLOR if s == 'success' else FAIL_COLOR for s in statuses]

# ── Plot ──────────────────────────────────────────────────────────────────────
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(9, 5))

# connecting line to show ramping progression
ax.plot(x, y, color='#bbbbbb', linewidth=1.0, zorder=1)

# scatter points
ax.scatter(x, y, c=colors, s=90, edgecolors='k', linewidths=0.6, zorder=2)

# preamble index annotations — demonstrate random selection
for xi, yi, lab in zip(x, y, labels):
    ax.annotate(lab, (xi, yi), textcoords='offset points',
                xytext=(4, 5), fontsize=7, color='#444444')

# axes & title
ax.set_xlabel('RACH Attempt', fontsize=11)
ax.set_ylabel('UE Tx Power (dBm)', fontsize=11)
ax.set_title('UE RACH Attempt vs Tx Power (Under Attack)\n'
             'Numbers on points = preamble index (randomly selected)',
             fontsize=11, fontweight='bold', pad=8)
ax.tick_params(labelsize=9)

# y-axis: add a bit of padding so top annotation is not clipped
ax.set_ylim(min(y) - 5, max(y) + 8)

# ── Legend ────────────────────────────────────────────────────────────────────
succ_patch = mpatches.Patch(color=SUCCESS_COLOR, label='Success')
fail_patch = mpatches.Patch(color=FAIL_COLOR,    label='Failed at RAR')
ax.legend(handles=[succ_patch, fail_patch], loc='upper left',
          fontsize=9, framealpha=0.85)

# ── Stats box ─────────────────────────────────────────────────────────────────
total      = len(entries)
succ_count = sum(1 for s in statuses if s == 'success')
fail_count = total - succ_count
info = f'Total: {total}   Success: {succ_count}   Failed: {fail_count}'
ax.text(0.99, 0.02, info, transform=ax.transAxes,
        fontsize=8.5, va='bottom', ha='right',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                  alpha=0.85, edgecolor='#cccccc'))

fig.tight_layout()
outname = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ue_ramping_plot.png')
fig.savefig(outname, dpi=250, bbox_inches='tight')
print(f'Saved: {outname}')
plt.show()
