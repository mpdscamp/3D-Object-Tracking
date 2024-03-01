import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the results from the CSV file
results_df = pd.read_csv('results.csv')

# Visualizing TTC vs. xmin and yw in subplots
plt.figure(figsize=(18, 6))

# TTC vs. xmin
plt.subplot(1, 3, 1)
plt.scatter(results_df['xmin'], results_df['TTC_Lidar'], label='TTC Lidar', alpha=0.7)
plt.scatter(results_df['xmin'], results_df['TTC_Camera'], label='TTC Camera', alpha=0.7)
plt.title('TTC vs. Minimum X-Distance (xmin)')
plt.xlabel('Minimum X-Distance (xmin) [m]')
plt.ylabel('Time-to-Collision (Seconds)')
plt.legend()
plt.grid(True)

# TTC vs. yw
plt.subplot(1, 3, 2)
plt.scatter(results_df['yw'], results_df['TTC_Lidar'], label='TTC Lidar', alpha=0.7)
plt.scatter(results_df['yw'], results_df['TTC_Camera'], label='TTC Camera', alpha=0.7)
plt.title('TTC vs. Vehicle Width (yw)')
plt.xlabel('Vehicle Width (yw) [m]')
plt.ylabel('Time-to-Collision (Seconds)')
plt.legend()
plt.grid(True)

# NumLidarPoints vs. xmin
plt.subplot(1, 3, 3)
plt.scatter(results_df['xmin'], results_df['NumLidarPoints'], label='Number of LiDAR Points', color='green', alpha=0.7)
plt.title('Number of LiDAR Points vs. Minimum X-Distance (xmin)')
plt.xlabel('Minimum X-Distance (xmin) [m]')
plt.ylabel('Number of LiDAR Points')
plt.grid(True)

plt.tight_layout()
plt.show()

# Analyzing TTC variability and the relation to xmin and NumLidarPoints

# Calculate the absolute difference in TTC_Lidar between consecutive frames
results_df['TTC_Lidar_Diff'] = results_df['TTC_Lidar'].diff().abs()

# Define a threshold for significant TTC change, e.g., changes above the 60th percentile

# Filter for frames with significant TTC changes and below-average number of LiDAR points
threshold = 1.2
implausible_ttc_indices = results_df[
    (results_df['TTC_Lidar_Diff'] > threshold) &
    (results_df['FrameID'].diff() == 1)
].index


# Display the identified frames
print(results_df.loc[implausible_ttc_indices, ['FrameID', 'TTC_Lidar', 'TTC_Lidar_Diff', 'xmin', 'xw', 'NumLidarPoints']])

# Visualizing TTC_Lidar per Frame ID
plt.figure(figsize=(14, 8))

# Subplot for TTC_Lidar
plt.subplot(3, 1, 1)

# Plot all TTC Lidar values
frame_ids = results_df['FrameID'].values
ttc_lidar = results_df['TTC_Lidar'].values

plt.plot(frame_ids, ttc_lidar, label='TTC Lidar', marker='o', linestyle='-', color='blue')

# Highlight implausible points in red
implausible_frame_ids = results_df.loc[implausible_ttc_indices, 'FrameID'].values
implausible_ttc_values = results_df.loc[implausible_ttc_indices, 'TTC_Lidar'].values
plt.scatter(implausible_frame_ids, implausible_ttc_values, color='red', label='Implausible TTC Lidar', zorder=5)

plt.title('TTC Lidar Changes Between Consecutive Frames')
plt.xlabel('Frame ID')
plt.ylabel('TTC Lidar (seconds)')
plt.grid(True)
plt.legend()

# Subplot for Number of LiDAR Points per Frame ID, with y-axis starting at 250
plt.subplot(3, 1, 2)
plt.bar(results_df['FrameID'].values, results_df['NumLidarPoints'].values, color='orange', label='Number of LiDAR Points')
plt.ylim(250, results_df['NumLidarPoints'].max() + 10)  # Set the lower limit to 250
plt.title('Number of LiDAR Points per Frame ID')
plt.xlabel('Frame ID')
plt.ylabel('Number of LiDAR Points')
plt.grid(True)
plt.legend()

# New subplot for xw per Frame ID
plt.subplot(3, 1, 3)
xw_values = results_df['xw'].values
plt.scatter(frame_ids, xw_values, color='purple', label='xw per Frame ID', alpha=0.7)
plt.title('xw per Frame ID')
plt.xlabel('Frame ID')
plt.ylabel('xw [m]')
plt.grid(True)
plt.legend()
# Show the plot with both subplots
plt.tight_layout()
plt.show()