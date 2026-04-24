"""
Produce 4 publication-quality figures from detect-preambles5.log:
  Fig1  cce_single_burst.png  - CCE stacked bar for one slot (shows root cause)
  Fig2  cce_drain.png         - Queue drain across slots after a PRACH burst
  Fig3  frame_summary.png     - Per-frame Msg2 success / fail summary
  Fig4  rb_grid.png           - Time-frequency RB grid for Msg3 UL PUSCH
"""

import re, csv, collections
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as ticker
import numpy as np

LOG  = Path(__file__).parent / "detect-preambles5.log"
OUT  = Path(__file__).parent

ANSI = re.compile(r"\x1b\[[0-9;]*m")

# ── regex ─────────────────────────────────────────────────────────────────────
RE_CCE   = re.compile(
    r"\[CCE-STATUS\] N_rb=(\d+) N_symb=(\d+) total_CCE=(\d+) "
    r"occupied=(\d+) free=(\d+) \(agg=(\d+) cand=(\d+) Y=(\d+)\)")
RE_OK    = re.compile(
    r"UE ([0-9a-f]+): (\d+)\.(\d+) Generating RA-Msg2 DCI.*preamble_index\(RAPID\) (\d+)")
RE_FAIL  = re.compile(
    r"UE ([0-9a-f]+): (\d+)\.(\d+) cannot find free CCE for Msg2")
RE_MSG3  = re.compile(
    r"UE ([0-9a-f]+): Msg3 scheduled at (\d+)\.(\d+) \((\d+)\.(\d+) TDA \d+\) "
    r"start (\d+) RBs (\d+)")
RE_ALLOC = re.compile(r"Msg3 alloc for UE ([0-9a-f]+)")
RE_PRACH = re.compile(
    r"\[RAPROC\] (\d+)\.(\d+) Initiating RA procedure with preamble (\d+),")

def strip(l): return ANSI.sub("", l).strip()

lines = [strip(l) for l in LOG.open(encoding="utf-8", errors="replace")]

# ── parse ────────────────────────────────────────────────────────────────────
msg2_rows = []
msg3_rows = []
prach_cnt = collections.Counter()

i = 0
while i < len(lines):
    ln = lines[i]

    m = RE_PRACH.search(ln)
    if m:
        prach_cnt[(int(m.group(1)), int(m.group(2)))] += 1

    m = RE_MSG3.search(ln)
    if m:
        msg3_rows.append({
            "ue": m.group(1),
            "msg3_frame": int(m.group(2)), "msg3_slot": int(m.group(3)),
            "msg2_frame": int(m.group(4)), "msg2_slot":  int(m.group(5)),
            "rb_start":   int(m.group(6)), "rb_size":    int(m.group(7)),
        })

    m_cce = RE_CCE.search(ln)
    if m_cce and i + 1 < len(lines):
        nxt = lines[i + 1]
        cce = {k: int(v) for k, v in zip(
            ("n_rb","n_symb","total_cce","occupied","free","agg","cand","Y"),
            m_cce.groups())}

        m3 = RE_ALLOC.search(nxt)
        if m3:                          # success path
            rnti = m3.group(1)
            for k in range(i+2, min(i+5, len(lines))):
                m2 = RE_OK.search(lines[k])
                if m2 and m2.group(1) == rnti:
                    msg2_rows.append({**cce,
                        "frame": int(m2.group(2)), "slot": int(m2.group(3)),
                        "ue": rnti, "rapid": int(m2.group(4)),
                        "result": "success"})
                    break
        else:
            m2f = RE_FAIL.search(nxt)
            if m2f:                     # fail path
                msg2_rows.append({**cce,
                    "frame": int(m2f.group(2)), "slot": int(m2f.group(3)),
                    "ue": m2f.group(1), "rapid": None,
                    "result": "fail"})
    i += 1

# write CSVs
def write_csv(path, rows, fields):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader(); w.writerows(rows)

write_csv(OUT/"cce_msg2.csv", msg2_rows,
    ["frame","slot","ue","rapid","total_cce","occupied","free","agg","cand","result"])
write_csv(OUT/"msg3_rb.csv", msg3_rows,
    ["ue","msg2_frame","msg2_slot","msg3_frame","msg3_slot","rb_start","rb_size"])
print(f"cce_msg2.csv : {len(msg2_rows)} rows")
print(f"msg3_rb.csv  : {len(msg3_rows)} rows")

# ── colour palette ────────────────────────────────────────────────────────────
C_OCC  = "#E07B54"   # occupied CCE
C_FREE = "#5B9BD5"   # free CCE
C_SUC  = "#2CA02C"   # success
C_FAIL = "#D62728"   # fail
C_WAIT = "#FF7F0E"   # waiting / pending

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.labelsize": 11,
    "axes.titlesize": 12,
    "legend.fontsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
})

# ═══════════════════════════════════════════════════════════════════════════════
# Fig 1 – CCE stacked bar for ONE slot  (Frame 688, Slot 10)
#          Shows: 10 UEs compete → 2 succeed (CCE 0-3, 4-7), 8 fail
# ═══════════════════════════════════════════════════════════════════════════════
target = [(r["frame"], r["slot"]) for r in msg2_rows
          if r["frame"] == 688 and r["slot"] == 10]
burst  = [r for r in msg2_rows if r["frame"] == 688 and r["slot"] == 10]

fig, ax = plt.subplots(figsize=(8, 4))
n     = len(burst)
x     = np.arange(n)
occ   = [r["occupied"] for r in burst]
free  = [r["free"]     for r in burst]
total = burst[0]["total_cce"]

ax.bar(x, occ,  color=C_OCC,  width=0.6, label="Occupied CCEs", zorder=2)
ax.bar(x, free, color=C_FREE, width=0.6, bottom=occ, label="Free CCEs", zorder=2)

for xi, row in enumerate(burst):
    ok = row["result"] == "success"
    ax.text(xi, total + 0.25,
            "✓" if ok else "✗",
            ha="center", va="bottom", fontsize=13,
            color=C_SUC if ok else C_FAIL, fontweight="bold")
    # CCE index annotation inside the free (blue) portion of success bars
    if ok:
        cce_start = row["occupied"]
        cce_mid   = cce_start + row["agg"] / 2          # mid-point of allocated block
        ax.text(xi, cce_mid,
                f"CCE {cce_start}–{cce_start+row['agg']-1}",
                ha="center", va="center", fontsize=8, color="white", fontweight="bold")

ax.set_xticks(x)
ax.set_xticklabels([f"UE {i+1}\n({r['ue']})" for i, r in enumerate(burst)], fontsize=8)
ax.set_yticks(range(0, total + 2))
ax.set_ylim(0, total + 1.5)
ax.set_ylabel("Number of CCEs")
ax.set_xlabel("UE Scheduling Attempt Order")
ax.set_title(
    f"PDCCH CCE Occupancy — Frame 688, Slot 10\n"
    f"(CORESET: {total} CCEs total, Aggregation Level = {burst[0]['agg']})",
    pad=10)
ax.yaxis.grid(True, linestyle="--", alpha=0.45, zorder=0)
ax.legend(
    handles=[
        mpatches.Patch(color=C_OCC,  label="Occupied CCEs"),
        mpatches.Patch(color=C_FREE, label="Free CCEs"),
        mpatches.Patch(color=C_SUC,  label="Msg2 Scheduled (✓)"),
        mpatches.Patch(color=C_FAIL, label="No Free CCE – Deferred (✗)"),
    ],
    loc="upper left", framealpha=0.9)
fig.tight_layout()
fig.savefig(OUT/"cce_single_burst.png", dpi=180, bbox_inches="tight")
plt.close(fig)
print("Saved → cce_single_burst.png")

# ═══════════════════════════════════════════════════════════════════════════════
# Fig 2 – Queue drain  (first PRACH burst: 192 preambles → drain over slots)
#          Shows cumulative served vs still-waiting after each DL slot
# ═══════════════════════════════════════════════════════════════════════════════
# The first PRACH burst (frame 687) produces UEs that appear in Msg2 at 688, 690, 692
# We can track the drain by looking at cce_msg2 sorted by frame/slot

# Collect all UEs from the "first wave" — they are all in frames 688 and beyond
# until the fail count reaches 0 (queue empty)
# Group by (frame, slot) in order; track cumulative served and remaining_fail
wave_slots = []
cum_served = 0
prev_fails = None

for (fr, sl) in sorted(set((r["frame"], r["slot"]) for r in msg2_rows)):
    slot_rows = [r for r in msg2_rows if r["frame"] == fr and r["slot"] == sl]
    s = sum(1 for r in slot_rows if r["result"] == "success")
    f = sum(1 for r in slot_rows if r["result"] == "fail")
    cum_served += s
    wave_slots.append({"label": f"{fr}.{sl:02d}", "success": s, "fail": f,
                       "cum_served": cum_served})

labels  = [d["label"]      for d in wave_slots]
succ    = [d["success"]    for d in wave_slots]
fail    = [d["fail"]       for d in wave_slots]
pending = [d["fail"]       for d in wave_slots]  # UEs still blocked this slot

# show only first 16 slots (enough to see the drain pattern)
show = 16
labels  = labels[:show];  succ = succ[:show];  fail = fail[:show]

fig2, ax2 = plt.subplots(figsize=(10, 4))
x2 = np.arange(show)
w  = 0.5
ax2.bar(x2, succ, width=w, color=C_SUC,  label="Msg2 Success (CCE found)",  zorder=2)
ax2.bar(x2, fail, width=w, color=C_FAIL, label="Deferred (no free CCE)",
        bottom=succ, zorder=2)

# annotate the success count on top of each success bar
for xi, (s, f) in enumerate(zip(succ, fail)):
    ax2.text(xi, s / 2, str(s), ha="center", va="center",
             color="white", fontsize=8, fontweight="bold")
    if f > 0:
        ax2.text(xi, s + f / 2, str(f), ha="center", va="center",
                 color="white", fontsize=8, fontweight="bold")

ax2.set_xticks(x2)
ax2.set_xticklabels(labels, rotation=45, ha="right")
ax2.set_ylabel("Msg2 Attempts per Slot")
ax2.set_xlabel("Frame.Slot (DL scheduling window)")
ax2.set_title(
    "Msg2 CCE Scheduling — Queue Drain after Mass PRACH Event\n"
    "(Max 2 Msg2 per slot due to CCE bottleneck, Aggregation Level = 4)")
ax2.yaxis.grid(True, linestyle="--", alpha=0.45, zorder=0)
ax2.legend(loc="upper right")
fig2.tight_layout()
fig2.savefig(OUT/"cce_drain.png", dpi=180, bbox_inches="tight")
plt.close(fig2)
print("Saved → cce_drain.png")

# ═══════════════════════════════════════════════════════════════════════════════
# Fig 3 – Per-frame summary (aggregated to 109 frames → readable bar chart)
# ═══════════════════════════════════════════════════════════════════════════════
per_frame = collections.defaultdict(lambda: {"s": 0, "f": 0})
for r in msg2_rows:
    per_frame[r["frame"]]["s" if r["result"]=="success" else "f"] += 1

frames_sorted = sorted(per_frame)
fs = [per_frame[f]["s"] for f in frames_sorted]
ff = [per_frame[f]["f"] for f in frames_sorted]

fig3, ax3 = plt.subplots(figsize=(14, 4))
x3 = np.arange(len(frames_sorted))
ax3.bar(x3, fs, color=C_SUC,  label="Msg2 Success", zorder=2)
ax3.bar(x3, ff, color=C_FAIL, label="Deferred (no free CCE)",
        bottom=fs, zorder=2)

# x-ticks: show every 10th frame label to avoid clutter
step = max(1, len(frames_sorted) // 20)
ax3.set_xticks(x3[::step])
ax3.set_xticklabels([str(frames_sorted[i]) for i in range(0, len(frames_sorted), step)],
                     rotation=45, ha="right")
ax3.set_ylabel("Msg2 Attempts")
ax3.set_xlabel("Frame Number")
ax3.set_title(
    f"Per-Frame Msg2 Scheduling Result  ({len(frames_sorted)} frames, "
    f"Total: {sum(fs)} success / {sum(ff)} deferred)")
ax3.yaxis.grid(True, linestyle="--", alpha=0.45, zorder=0)
ax3.legend(loc="upper right")

# annotate first frame manually (worst congestion)
ax3.annotate(f"Frame {frames_sorted[0]}\n(first burst)",
             xy=(0, fs[0]+ff[0]), xytext=(6, ff[0]+2),
             arrowprops=dict(arrowstyle="->", color="gray"),
             fontsize=8, color="gray")

fig3.tight_layout()
fig3.savefig(OUT/"frame_summary.png", dpi=180, bbox_inches="tight")
plt.close(fig3)
print("Saved → frame_summary.png")

# ═══════════════════════════════════════════════════════════════════════════════
# Fig 4 – RB grid  (time × frequency heatmap for Msg3 UL PUSCH)
#          X = Msg3 UL slot  (e.g., 688.19, 689.7, 690.19, …)
#          Y = RB index (0 – 107)
#          Color = allocated
# ═══════════════════════════════════════════════════════════════════════════════
# Build unique slot labels and allocate a column per slot
msg3_slots = sorted(set((r["msg3_frame"], r["msg3_slot"]) for r in msg3_rows))
slot_idx   = {s: i for i, s in enumerate(msg3_slots)}
bwp_size   = 106  # N_RB from log

# grid: rows = RB, cols = slots
grid = np.zeros((bwp_size, len(msg3_slots)), dtype=np.int8)
for r in msg3_rows:
    col = slot_idx[(r["msg3_frame"], r["msg3_slot"])]
    for rb in range(r["rb_start"], r["rb_start"] + r["rb_size"]):
        if rb < bwp_size:
            grid[rb, col] = 1

# show only first 30 slots; zoom Y to 0-25 to show free space above allocations
show_cols = min(30, len(msg3_slots))
rb_show   = 26                           # display RBs 0-25
grid_show = grid[:rb_show, :show_cols]
labels_show = [f"{fr}.{sl:02d}" for fr, sl in msg3_slots[:show_cols]]

# use a 3-level colourmap: white=free, orange=UE1 (RB 0-7), blue=UE2 (RB 8-15)
colored = np.zeros((*grid_show.shape, 3))   # RGB
ue1_mask = np.zeros_like(grid_show, dtype=bool)
ue2_mask = np.zeros_like(grid_show, dtype=bool)
for r in msg3_rows:
    col = slot_idx[(r["msg3_frame"], r["msg3_slot"])]
    if col >= show_cols: continue
    for rb in range(r["rb_start"], min(r["rb_start"] + r["rb_size"], rb_show)):
        if r["rb_start"] == 0:
            ue1_mask[rb, col] = True
        else:
            ue2_mask[rb, col] = True

colored[:] = [0.97, 0.97, 0.97]           # default: light grey = free
colored[ue1_mask] = matplotlib.colors.to_rgb(C_OCC)    # orange = UE1
colored[ue2_mask] = matplotlib.colors.to_rgb(C_FREE)   # blue   = UE2

fig4, ax4 = plt.subplots(figsize=(13, 5))
ax4.imshow(colored, aspect="auto", origin="lower", interpolation="nearest")

ax4.set_xticks(range(show_cols))
ax4.set_xticklabels(labels_show, rotation=60, ha="right", fontsize=7)
ax4.set_yticks(range(0, rb_show, 2))
ax4.set_ylabel("Resource Block (RB) Index")
ax4.set_xlabel("Frame.Slot (Msg3 UL Transmission Slot)")
ax4.set_title(
    "Msg3 PUSCH Time-Frequency Resource Allocation\n"
    f"(BWP = {bwp_size} RBs, each Msg3 = 8 RBs, first {show_cols} UL slots shown)")

# separator line and band labels
ax4.axhline(7.5,  color="white", linewidth=1.5, linestyle="-")
ax4.axhline(15.5, color="gray",  linewidth=0.8, linestyle="--")
ax4.text(-0.8, 3.5,  "UE₁\nRB 0–7",  ha="right", va="center",
         fontsize=8.5, color=C_OCC,  fontweight="bold")
ax4.text(-0.8, 11.5, "UE₂\nRB 8–15", ha="right", va="center",
         fontsize=8.5, color=C_FREE, fontweight="bold")
ax4.text(-0.8, 20,   "Free",          ha="right", va="center",
         fontsize=8, color="gray")

legend_patches = [
    mpatches.Patch(color=C_OCC,    label="UE₁ Allocated (RB 0–7)"),
    mpatches.Patch(color=C_FREE,   label="UE₂ Allocated (RB 8–15)"),
    mpatches.Patch(color="#F7F7F7", label="Free RBs", ec="gray"),
]
ax4.legend(handles=legend_patches, loc="upper right", framealpha=0.9)
fig4.tight_layout()
fig4.savefig(OUT/"rb_grid.png", dpi=180, bbox_inches="tight")
plt.close(fig4)
print("Saved → rb_grid.png")

print("\nAll done.")
