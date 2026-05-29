import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cbra_ota_timing.csv")
df["seq"] = range(1, len(df) + 1)
delta = df["delta_sec"]
mean_val = delta.mean()

fig, ax = plt.subplots(figsize=(10, 4))

outlier_mask = delta > 15

ax.plot(df["seq"], delta, color="#4477AA", linewidth=0.9, alpha=0.8)
ax.axhline(mean_val, color="tomato", linewidth=1.5, linestyle="--",
           label=f"Mean = {mean_val:.2f} s")

for idx, row in df[outlier_mask].iterrows():
    ax.scatter(row["seq"], row["delta_sec"], color="red", zorder=5, s=60,
               label="Outlier")
    ax.annotate(f"{row['delta_sec']:.1f} s",
                xy=(row["seq"], row["delta_sec"]),
                xytext=(row["seq"] + 6, row["delta_sec"] - 1.5),
                fontsize=10, color="red",
                arrowprops=dict(arrowstyle="->", color="red", lw=1.2))

ax.set_xlabel("Trial Index", fontsize=12)
ax.set_ylabel("Latency (s)", fontsize=12)
ax.set_title("RACH Re-establishment Latency after gNB Restart (N=250)", fontsize=13)
ax.set_xlim(1, len(df))
ax.set_ylim(0, 25)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("cbra_ota_timing.png", dpi=150, bbox_inches="tight")
print("Saved → cbra_ota_timing.png")
