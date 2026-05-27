import matplotlib.pyplot as plt
import textwrap

# ── Colors for a premium, clean LIGHT theme ──────────────────────────────────
BG          = "#FFFFFF"  # Pure white background
HEADER_BG   = "#E2E8F0"  # Elegant light slate grey for headers
ROW_ALT_BG  = "#F8FAFC"  # Very soft blue-grey for alternating rows
BORDER_COLOR= "#CBD5E1"  # Clean, soft border color (no harsh black)
C_PRIMARY   = "#1E3A8A"  # Elegant deep royal blue for strategy titles
C_DARK      = "#0F172A"  # Slate black for bold titles and header text
C_TEXT      = "#334155"  # Soft dark charcoal for details (highly readable)
C_GREY      = "#64748B"  # Muted grey for subtitles

# ── Raw Data ──────────────────────────────────────────────────────────────────
headers = ["Anti-jamming Strategies", "Limitations"]
raw_data = [
    ("Frequency-Hopping Spread Spectrum (FHSS)", 
     "• Vulnerable to broadband jamming\n• Vulnerable to key establishment\n• Spectrum inefficient"),
    ("Chirp Spread Spectrum (CSS)", 
     "• Spectrum inefficient"),
    ("Direct Sequence Spread Spectrum (DSSS)", 
     "• Spectrum inefficient"),
    ("MIMO-based Techniques", 
     "• Extra hardware required"),
    ("Antenna Phase Array & Analog Beamforming", 
     "• Extra hardware required"),
    ("Rate Adaptation Algorithms", 
     "• Ineffective against high-power jamming"),
    ("Power Control Mechanisms", 
     "• Ineffective against high-power jamming"),
    ("Relay Aided Strategies", 
     "• Alternative infrastructure required"),
    ("Channel Re-selection", 
     "• Ineffective against broadband and sweeping jamming attacks"),
    ("Packet Fragmentation & Fragment Replication", 
     "• Ineffective against constant jamming"),
    ("Channel Coding Schemes", 
     "• Ineffective against high-power jamming"),
    ("Filtering & Masking Techniques", 
     "• Effective for single-tone jamming only")
]

# ── Helper Functions for Robust Text Wrapping (No Overlapping) ────────────────
def wrap_strategy(text, width=24):
    lines = []
    for part in text.split('\n'):
        wrapped = textwrap.wrap(part.strip(), width=width)
        lines.extend(wrapped)
    return "\n".join(lines)

def wrap_bullet_points(text, width=32):
    lines = []
    for part in text.split('\n'):
        clean_part = part.strip()
        if not clean_part:
            continue
        is_bullet = clean_part.startswith('•')
        if is_bullet:
            content = clean_part[1:].strip()
            wrapped_content = textwrap.wrap(content, width=width)
            if wrapped_content:
                lines.append(f"• {wrapped_content[0]}")
                for extra in wrapped_content[1:]:
                    lines.append(f"  {extra}")
            else:
                lines.append("•")
        else:
            wrapped_content = textwrap.wrap(clean_part, width=width)
            lines.extend(wrapped_content)
    return "\n".join(lines)

# Process data with auto-wrapping (Optimized width for square layout)
data = []
for strat, limit in raw_data:
    data.append((wrap_strategy(strat, width=24), wrap_bullet_points(limit, width=32)))

# ── Figure Configuration ──────────────────────────────────────────────────────
# Width: 4.7 inches (~11.9 cm)
# Height: 4.7 inches (~11.9 cm)
# Fits EXACTLY within a 12 cm x 12 cm box on slides!
fig, ax = plt.subplots(figsize=(4.7, 4.7))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

# ── Draw Table Title ─────────────────────────────────────────────────────────
ax.text(0.5, 0.96, "SUMMARY OF ANTI-JAMMING LIMITATIONS", 
        ha="center", va="center", fontsize=8.5, fontweight="bold", 
        color=C_PRIMARY, zorder=5)
ax.text(0.5, 0.925, "Survey of Wireless Defense Capabilities", 
        ha="center", va="center", fontsize=6.5, color=C_GREY, zorder=5)

# ── Coordinates Setup ────────────────────────────────────────────────────────
# Scaled for 4.7x4.7 square layout
col_x = [0.03, 0.46]  # Column X positions
row_y = 0.89          # Start Y position for header

# ── Draw Table Header ────────────────────────────────────────────────────────
header_h = 0.038
rect_header = plt.Rectangle((0.02, row_y - header_h), 0.96, header_h, 
                            facecolor=HEADER_BG, edgecolor=BORDER_COLOR, 
                            linewidth=0.8, zorder=2)
ax.add_patch(rect_header)

ax.text(col_x[0] + 0.01, row_y - header_h/2, headers[0], 
        ha="left", va="center", fontsize=6.8, fontweight="bold", 
        color=C_DARK, zorder=3)
ax.text(col_x[1] + 0.01, row_y - header_h/2, headers[1], 
        ha="left", va="center", fontsize=6.8, fontweight="bold", 
        color=C_DARK, zorder=3)

# Move pointer below header
row_y -= header_h

# ── Draw Rows Dynamically ────────────────────────────────────────────────────
for i, (strat, limit) in enumerate(data):
    # Count the lines in each wrapped text
    strat_lines = strat.count('\n') + 1
    limit_lines = limit.count('\n') + 1
    max_lines = max(strat_lines, limit_lines)
    
    # Calculate row height proportionally to avoid text overlap in square aspect
    row_h = 0.032 + max_lines * 0.013
    
    # Background striping (White vs Soft Blue-Grey)
    row_bg = ROW_ALT_BG if i % 2 == 1 else BG
    rect_row = plt.Rectangle((0.02, row_y - row_h), 0.96, row_h, 
                             facecolor=row_bg, edgecolor=BORDER_COLOR, 
                             linewidth=0.6, zorder=2)
    ax.add_patch(rect_row)
    
    # Add strategy text (vertically centered, compact font size)
    ax.text(col_x[0] + 0.01, row_y - row_h/2, strat, 
            ha="left", va="center", fontsize=5.8, color=C_PRIMARY, 
            fontweight="bold", linespacing=1.2, zorder=3)
    
    # Add limitation text (vertically centered, compact font size)
    ax.text(col_x[1] + 0.01, row_y - row_h/2, limit, 
            ha="left", va="center", fontsize=5.8, color=C_TEXT, 
            linespacing=1.25, zorder=3)
    
    # Move row pointer down
    row_y -= row_h

# ── Table Border ─────────────────────────────────────────────────────────────
rect_border = plt.Rectangle((0.02, row_y), 0.96, 0.89 - row_y, 
                            facecolor="none", edgecolor=BORDER_COLOR, 
                            linewidth=1.0, zorder=4)
ax.add_patch(rect_border)

# ── Save Image ───────────────────────────────────────────────────────────────
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
out_path = "/Users/yq/Documents/analysis/0526/anti_jamming_table.png"
plt.savefig(out_path, dpi=280, bbox_inches="tight", 
            facecolor=BG, edgecolor="none")
print(f"Saved -> {out_path}")
