#!/usr/bin/env python3
import re
from pathlib import Path
from collections import defaultdict
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Use oai-fdm24.log for reference
LOG_FILE = Path(__file__).parent / "oai-fdm24.log"
OUT_DIR = Path(__file__).parent

RAPROC_PAT = re.compile(r"\[RAPROC\] Frame (\d+), slot (\d+), fdm (\d+)")
NO_FREE_PAT = re.compile(r"FAILURE:\s+(\d+)\.(\d+) initiating RA procedure for preamble index \d+: no free RA process")
RA_INIT_PAT = re.compile(r"(\d+)\.(\d+) UE RA-RNTI [0-9a-f]+ TC-RNTI ([0-9a-f]+): initiating RA procedure")
MSG3_PAT = re.compile(r"UE ([0-9a-f]+): Msg3 scheduled at (\d+)\.(\d+) ")
RETX_PAT = re.compile(r"RA RNTI ([0-9a-f]+) CC_id 0 Scheduling retransmission of Msg3 in \((\d+),(\d+)\)")
FAIL_MSG3_PAT = re.compile(r"UE ([0-9a-f]+) RA failed at state WAIT_Msg3")

def parse_log():
    ra_init_events = defaultdict(int) # (frame, slot) -> number of RARs initiated
    ra_drop_events = defaultdict(int) # (frame, slot) -> number of drops
    raproc_events = defaultdict(int)  # (frame, slot) -> detected preambles
    
    with open(LOG_FILE, "r", errors="replace") as f:
        for line in f:
            # Clean ANSI
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
    
    # Get all occasions and filter by frame 960 to 976
    all_occasions = sorted(set(raproc.keys()) | set(ra_init.keys()) | set(ra_drop.keys()))
    filtered_occasions = [(f, s) for f, s in all_occasions if 960 <= f <= 976]
    
    x = np.arange(len(filtered_occasions))
    labels = [f"{f}.{s}" for f, s in filtered_occasions]
    
    detected = [raproc[occ] for occ in filtered_occasions]
    accepted = [ra_init[occ] for occ in filtered_occasions]
    dropped = [ra_drop[occ] for occ in filtered_occasions]
    
    # Adjust figure width dynamically but keep it in one image
    fig_w = max(10, 1 + len(filtered_occasions) * 0.2)
    fig, ax = plt.subplots(figsize=(fig_w, 6))
    
    # Plotting lines with markers
    ax.plot(x, detected, marker='o', linestyle='-', color='#34495e', label='Detected Preambles (Requests)', linewidth=2, markersize=6)
    ax.plot(x, accepted, marker='s', linestyle='-', color='#2ecc71', label='Allocated RARs (Accepted)', linewidth=2, markersize=6)
    ax.plot(x, dropped, marker='x', linestyle='-.', color='#e74c3c', label='Dropped Preambles (No free RA process)', linewidth=2, markersize=6)
    
    # Capacity limit line
    ax.axhline(y=4, color='#c0392b', linestyle='--', linewidth=2, label='OAI gNB RAR Capacity Limit (Max 4)')
    
    # Add text for RARs
    for i in range(len(x)):
        ax.text(x[i], accepted[i] + 0.3, f"{accepted[i]}", color='#27ae60', ha='center', va='bottom', fontsize=9, fontweight='bold')
        if detected[i] != accepted[i]:
            ax.text(x[i], detected[i] + 0.3, f"{detected[i]}", color='#34495e', ha='center', va='bottom', fontsize=9, fontweight='bold')
        if dropped[i] > 0:
            ax.text(x[i], dropped[i] + 0.3, f"{dropped[i]}", color='#e74c3c', ha='center', va='bottom', fontsize=9, fontweight='bold')

    # Sparse x-ticks if there are too many, otherwise show all
    if len(x) > 40:
        tick_step = max(1, len(x) // 20)
        ax.set_xticks(x[::tick_step])
        ax.set_xticklabels(labels[::tick_step], rotation=45, ha='right')
    else:
        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation=45, ha='right')
        
    ax.set_xlabel('Random Access Occasion (Frame.Slot)', fontsize=12)
    ax.set_ylabel('Count', fontsize=12)
    
    # Add dynamic y-limit to ensure annotations are not cut off
    max_val = max([max(detected) if detected else 0, max(dropped) if dropped else 0, 4])
    ax.set_ylim(0, max_val * 1.2)
    
    ax.set_title('Resource Exhaustion Concept (Frames 960-976)', fontsize=14, fontweight='bold')
    
    # Custom grid
    ax.grid(True, linestyle=':', alpha=0.7)
    
    # Legend
    ax.legend(loc='upper right', bbox_to_anchor=(1.0, 0.65), fontsize=11)
    
    plt.tight_layout()
    out = OUT_DIR / "resource_exhaustion_concept_fdm24.png"
    plt.savefig(out, dpi=150)
    plt.close(fig)
    print(f"Saved to {out}")

if __name__ == '__main__':
    main()
