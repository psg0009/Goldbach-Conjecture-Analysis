# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import pandas as pd
import matplotlib.gridspec as gridspec
from scipy.ndimage import gaussian_filter1d

# Load the processed dataset
df = pd.read_csv("Processed_Prime_Gaps.csv")  # Update with the actual file path if needed

# Define a colormap for density visualization
cmap = plt.cm.viridis

# Compute a rolling average (moving average) for trendline
window_size = 20  # Adjust for smoothing effect
df["Smoothed Gap"] = df["Gap to Previous"].rolling(window=window_size, min_periods=1).mean()

# Compute threshold for anomaly detection (95th percentile)
threshold_percentile = 95
gap_threshold = np.percentile(df["Gap to Previous"], threshold_percentile)
anomalies = df[df["Gap to Previous"] > gap_threshold]

# ---- Create a figure with subplots (Main Scatter Plot + Histograms) ----
fig = plt.figure(figsize=(16, 8))
gs = gridspec.GridSpec(2, 2, height_ratios=[3, 1], width_ratios=[3, 1])  
ax_main = plt.subplot(gs[0, 0])  # Main scatter plot
ax_hist_x = plt.subplot(gs[1, 0])  # Histogram for prime gaps
ax_hist_y = plt.subplot(gs[0, 1])  # Histogram for gap distribution (vertical)

# ---- Main Scatter Plot ----
sc = ax_main.scatter(df["Prime"], df["Gap to Previous"], c=df["Gap to Previous"], cmap=cmap, alpha=0.7, s=50, label="Actual Gap to Previous")
ax_main.plot(df["Prime"], df["Smoothed Gap"], color="black", linewidth=2.5, linestyle="-", label="Moving Average Trend")
ax_main.plot(df["Prime"], df["Log(p)^2"], color="#d62728", linewidth=3, linestyle="--", label="Expected Gap (Log(p)^2)")
ax_main.scatter(anomalies["Prime"], anomalies["Gap to Previous"], color="#ff7f0e", edgecolors="black", s=100, marker="D", label="Extreme Anomalies")

# Labels and formatting
ax_main.set_xlabel("Prime Number", fontsize=14, fontweight="bold", color="#333333")
ax_main.set_ylabel("Prime Gap", fontsize=14, fontweight="bold", color="#333333")
ax_main.set_title("Prime Gaps vs. Cramér’s Bound (with Histogram & Density)", fontsize=18, fontweight="bold", color="#222222")
ax_main.legend(fontsize=12, loc="upper left", frameon=True, shadow=True)
ax_main.set_yscale("log")
ax_main.grid(True, linestyle="--", alpha=0.5)
ax_main.set_facecolor("#f8f8f8")

# ---- Histogram of Prime Gaps (X-Axis) ----
ax_hist_x.hist(df["Gap to Previous"], bins=30, color="#1f77b4", alpha=0.7, edgecolor="black")
ax_hist_x.set_xlabel("Prime Gap Size", fontsize=12, fontweight="bold")
ax_hist_x.set_ylabel("Frequency", fontsize=12, fontweight="bold")
ax_hist_x.set_title("Distribution of Prime Gaps", fontsize=14, fontweight="bold")
ax_hist_x.grid(True, linestyle="--", alpha=0.5)

# ---- Histogram of Extreme Gaps (Vertical) ----
ax_hist_y.hist(df["Gap to Previous"], bins=30, orientation="horizontal", color="#2ca02c", alpha=0.7, edgecolor="black")
ax_hist_y.set_xlabel("Frequency", fontsize=12, fontweight="bold")
ax_hist_y.set_ylabel("Prime Gap Size", fontsize=12, fontweight="bold")
ax_hist_y.set_title("Gap Frequency", fontsize=14, fontweight="bold")
ax_hist_y.grid(True, linestyle="--", alpha=0.5)

# Adjust layout for clarity
plt.tight_layout()
plt.show()
