🩺Medical Data Visualizer
This project explores the relationship between cardiovascular disease and various health indicators using a dataset of patient information. The goal is to analyze patterns using categorical plots and correlation heatmaps.

📁 Dataset

File: medical_examination.csv

Each row represents a patient.

Columns include age, weight, height, blood pressure, lifestyle habits, and health outcomes.

📊 Visualizations

1. Categorical Plot (draw_cat_plot)

What it shows:

Comparison of counts for features (cholesterol, gluc, smoke, alco, active, overweight) between patients with and without cardiovascular disease (cardio = 0 and 1).

Steps:

Added a new overweight column based on BMI > 25.

Normalized cholesterol and gluc:

1 → 0 (good),

2 or 3 → 1 (bad)

Melted the DataFrame using pd.melt().

Grouped and counted values by variable, value, and cardio.

Plotted using sns.catplot() with kind='count'.

2. Heatmap (draw_heat_map)

What it shows:

A correlation matrix between all numerical features to identify strong relationships.

Cleaning criteria:

Diastolic pressure cannot exceed systolic pressure (ap_lo <= ap_hi)
Height and weight within 2.5th to 97.5th percentiles.
Steps:
Computed the correlation matrix with df.corr().
Created a mask for the upper triangle of the heatmap.
Plotted using sns.heatmap() with annotations
