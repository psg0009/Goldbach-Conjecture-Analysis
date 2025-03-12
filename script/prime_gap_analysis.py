import pandas as pd
import numpy as np

# Load the Prime Gaps data
file_path = "Prime_Gaps_Analysis.csv"  # Update with your actual file path
df = pd.read_csv(file_path)

# Compute the expected prime gap using Cramér’s conjecture
df["Log(p)^2"] = (np.log(df["Prime"]))**2

# Compute deviation ratios
df["Deviation (Prev)"] = df["Gap to Previous"] / df["Log(p)^2"]
df["Deviation (Next)"] = df["Gap to Next"] / df["Log(p)^2"]

# Identify anomalies where the gap significantly deviates
df["Anomaly (Prev)"] = df["Deviation (Prev)"] > 2  # Adjust threshold as needed
df["Anomaly (Next)"] = df["Deviation (Next)"] > 2

# Save processed data
df.to_csv("Processed_Prime_Gaps.csv", index=False)

# Display summary statistics
print(df[["Prime", "Gap to Previous", "Log(p)^2", "Deviation (Prev)", "Anomaly (Prev)"]].head())

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
from scipy.ndimage import gaussian_filter1d

# Compute a rolling average (moving average) for trendline
window_size = 20  # Adjust for smoothing effect
df["Smoothed Gap"] = df["Gap to Previous"].rolling(window=window_size, min_periods=1).mean()

# Define a colormap for density visualization
norm = mcolors.Normalize(vmin=df["Gap to Previous"].min(), vmax=df["Gap to Previous"].max())
cmap = plt.cm.viridis  # Effective colormap for visualization

# Create the figure
plt.style.use("ggplot")
fig, ax = plt.subplots(figsize=(14, 7))

# Plot actual prime gaps with color gradient
sc = ax.scatter(df["Prime"], df["Gap to Previous"], c=df["Gap to Previous"], cmap=cmap, norm=norm, alpha=0.7, s=50, label="Actual Gap to Previous")

# Add moving average trendline
smoothed_gap = gaussian_filter1d(df["Smoothed Gap"], sigma=2)
ax.plot(df["Prime"], smoothed_gap, color="black", linewidth=2.5, linestyle="-", label="Moving Average Trend")

# Plot expected gaps using Cramér’s conjecture
ax.plot(df["Prime"], df["Log(p)^2"], color="#d62728", linewidth=3, linestyle="--", label="Expected Gap (Log(p)^2)")

# Highlight anomalies dynamically based on percentile
threshold_percentile = 95
gap_threshold = np.percentile(df["Gap to Previous"], threshold_percentile)
anomalies = df[df["Gap to Previous"] > gap_threshold]

ax.scatter(anomalies["Prime"], anomalies["Gap to Previous"], color="#ff7f0e", edgecolors="black", s=100, marker="D", label="Extreme Anomalies")

# Add annotations for significant anomalies
for i, row in anomalies.iterrows():
    ax.annotate(f"{int(row['Gap to Previous'])}", (row["Prime"], row["Gap to Previous"]),
                textcoords="offset points", xytext=(0,5), ha='center', fontsize=10, color="black")

# Customize plot
ax.set_xlabel("Prime Number", fontsize=14, fontweight="bold", color="#333333")
ax.set_ylabel("Prime Gap", fontsize=14, fontweight="bold", color="#333333")
ax.set_title("Prime Gaps vs. Cramér’s Bound (with Trendline & Density)", fontsize=18, fontweight="bold", color="#222222")
ax.legend(fontsize=12, loc="upper left", frameon=True, shadow=True)
ax.set_yscale("log")
cbar = plt.colorbar(sc, ax=ax)
cbar.set_label("Gap Size (Color Intensity)", fontsize=12)

# Grid adjustments
ax.grid(True, which="both", linestyle=":", linewidth=0.7, alpha=0.8)
ax.set_facecolor("#f8f8f8")
ax.tick_params(axis="x", labelsize=12, rotation=30)
ax.tick_params(axis="y", labelsize=12)

# Show the plot
plt.show()
