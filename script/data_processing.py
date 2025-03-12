# Core Libraries
import numpy as np
import pandas as pd
from sympy import nextprime  

# Data Visualization (Matplotlib & Plotly)
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.gridspec as gridspec
import plotly.express as px

# Data Processing & Statistical Analysis
from scipy.ndimage import gaussian_filter1d  
import plotly.express as px
import pandas as pd

extended_df = pd.read_csv("Prime_Gaps_Analysis.csv")

# Identify anomalies based on 95th percentile
gap_threshold_extended = extended_df["Gap to Previous"].quantile(0.95)
extended_anomalies = extended_df[extended_df["Gap to Previous"] > gap_threshold_extended]

# Create an interactive scatter plot with Plotly
fig = px.scatter(
    extended_df,
    x="Prime",
    y="Gap to Previous",
    color="Gap to Previous",
    color_continuous_scale="Viridis",
    title="Interactive Prime Gaps Visualization",
    labels={"Prime": "Prime Number", "Gap to Previous": "Prime Gap"},
    hover_data=["Previous Prime", "Gap to Previous", "Log(p)^2"],
)

# Highlight anomalies in red
fig.add_scatter(
    x=extended_anomalies["Prime"],
    y=extended_anomalies["Gap to Previous"],
    mode="markers",
    marker=dict(color="red", size=8, symbol="circle-open"),
    name="Anomalies",
)

# Customize layout for better visualization
fig.update_layout(
    xaxis_title="Prime Number",
    yaxis_title="Prime Gap",
    coloraxis_colorbar=dict(title="Gap Size"),
    template="plotly_dark",
    hovermode="closest",
)

# Show interactive plot
fig.show()
