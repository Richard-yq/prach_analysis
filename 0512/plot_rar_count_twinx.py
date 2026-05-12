#!/usr/bin/env python3
import re
from pathlib import Path
from collections import defaultdict
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

LOG_FILE = Path(__file__).parent / "oai-fdm24.log"
OUT_DIR = Path(__file__).parent

RAPROC_PAT = re.compile(r"\[RAPROC\] Frame (\d+), slot (\d+), fdm (\d+)")
NO_FREE_PAT = re.compile(r"FAILURE:\s+(\d+)\.(\d+) initiating RA procedure for preamble index \d+: no free RA process")
RA_INIT_PAT = re.compile(r"(\d+)\.(\d+) UE RA-RNTI [0-9a-f]+ TC-RNTI ([0-9a-f]+): initiating RA procedure")

def parse_log():
    ra_init_events = defaultdict(int)
    ra_drop_events = defaultdict(int)
    raproc_events = defaultdict(int)
    with open(LOG_FILE, "r", errors="replace") as f:
        for line in f:
            line = re.sub(r"\x1b\[[0-9;]*m", "", line)
            m = RAPROC_PAT.search(line)
            if m:
                raproc_events[(int(m[1]), int(m[2]))] += 1
                continue
            m = NO_FREE_PAT.search(line)
            if m:
                ra_drop_events[(int(m[1]), int(m[2]))] += 1
                continue
            m = RA_INIT_PAT.search(line)
            if m:
                ra_init_events[(int(m[1]), int(m[2]))] += 1
                continue
    return raproc_events, ra_init_events, ra_drop_events

def main():
    raproc, ra_init, ra_drop = parse_log()
    all_occasions = sorted(set(raproc.keys()) | set(ra_init.keys()) | set(ra_drop.keys()))
    filtered_occasions = [(f, s) for f, s in all_occasions if 960 <= f <= 976]
    
    x = np.arange(len(filtered_occasions))
    labels = [f"{f}.{s}" for f, s in filtered_occasions]
    
    detected = [raproc[occ] for occ in filtered_occasions]
    accepted = [ra_init[occ] for occ in filtered_occasions]
    dropped = [ra_drop[occ] for occ in filtered_occasions]
    
    fig_w = max(10, 1 + len(filtered_occasions) * 0.2)
    fig, ax1 = plt.subplots(figsize=(fig_w, 6))
    
    # Ax1: left y-axis (low values: accepted)
    ax1.plot(x, accepted, marker='s', linestyle='-', color='#2ecc71', label='Allocated RARs (Accepted)', linewidth=2, markersize=6)
    ax1.axhline(y=4, color='#c0392b', linestyle='--', linewidth=2, label='OAI gNB RAR Capacity Limit (Max 4)')
    ax1.set_ylim(-0.5, 6)
    ax1.set_ylabel('Accepted / Capacity Count', color='#2ecc71', fontsize=12, fontweight='bold')
    ax1.tick_params(axis='y', labelcolor='#2ecc71')
    
    # Ax2: right y-axis (high values: detected / dropped)
    ax2 = ax1.twinx()
    ax2.plot(x, detected, marker='o', linestyle='-', color='#34495e', label='Detected Preambles (Requests)', linewidth=2, markersize=6)
    ax2.plot(x, dropped, marker='x', linestyle='-.', color='#e74c3c', label='Dropped Preambles (No free RA process)', linewidth=2, markersize=6)
    ax2.set_ylim(120, 135)
    ax2.set_ylabel('Detected / Dropped Count', color='#34495e', fontsize=12, fontweight='bold')
    ax2.tick_params(axis='y', labelcolor='#34495e')
    
    # Texts
    for i in range(len(x)):
        ax1.text(x[i], accepted[i] + 0.2, f"{accepted[i]}", color='#27ae60', ha='center', va='bottom', fontsize=9, fontweight='bold')
        if detected[i] != accepted[i]:
            ax2.text(x[i], detected[i] + 0.3, f"{detected[i]}", color='#34495e', ha='center', va='bottom', fontsize=9, fontweight='bold')
        if dropped[i] > 0:
            ax2.text(x[i], dropped[i] - 1.0, f"{dropped[i]}", color='#e74c3c', ha='center', va='top', fontsize=9, fontweight='bold')

    if len(x) > 40:
        tick_step = max(1, len(x) // 20)
        ax1.set_xticks(x[::tick_step])
        ax1.set_xticklabels(labels[::tick_step], rotation=45, ha='right')
    else:
        ax1.set_xticks(x)
        ax1.set_xticklabels(labels, rotation=45, ha='right')
        
    ax1.set_xlabel('Random Access Occasion (Frame.Slot)', fontsize=12)
    ax1.set_title('Resource Exhaustion Concept (Frames 960-976)', fontsize=14, fontweight='bold')
    
    ax1.grid(True, linestyle=':', alpha=0.7)
    
    # Legend
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='center right', bbox_to_anchor=(0.98, 0.5), fontsize=11)
    
    plt.tight_layout()
    out = OUT_DIR / "resource_exhaustion_concept_fdm24_twinx.png"
    plt.savefig(out, dpi=150)
    plt.close(fig)

if __name__ == '__main__':
    main()
