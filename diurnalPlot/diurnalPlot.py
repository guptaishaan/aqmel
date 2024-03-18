import matplotlib.pyplot as plt
import pandas as pd

# Load the hourly stats from the CSV files
non_wildfire_stats = pd.read_csv('/Users/ishaangupta/Downloads/main/assderp/jorgensen-v5/pose-detection-keypoints-estimation-yolov8/aqmel/non_wildfire_stats.csv')
wildfire_stats = pd.read_csv('/Users/ishaangupta/Downloads/main/assderp/jorgensen-v5/pose-detection-keypoints-estimation-yolov8/aqmel/wildfire_stats.csv')

# Adjust the hour to match a 1-24 format instead of 0-23
non_wildfire_stats['Hour'] += 1
wildfire_stats['Hour'] += 1

# Plotting
plt.figure(figsize=(12, 6))

# Non-Wildfire Data
plt.plot(non_wildfire_stats['Hour'], non_wildfire_stats['Mean PM2.5'], label='Non-Wildfire Dates (11|30|23 - 12|13|23)', color='blue', marker='o')
plt.fill_between(non_wildfire_stats['Hour'], non_wildfire_stats['Mean PM2.5'] - non_wildfire_stats['Std PM2.5'],
                 non_wildfire_stats['Mean PM2.5'] + non_wildfire_stats['Std PM2.5'], color='blue', alpha=0.2)

# Wildfire Data
plt.plot(wildfire_stats['Hour'], wildfire_stats['Mean PM2.5'], label='Wildfire Dates ((12|14|23 - 12|27|23))', color='red', marker='o')
plt.fill_between(wildfire_stats['Hour'], wildfire_stats['Mean PM2.5'] - wildfire_stats['Std PM2.5'],
                 wildfire_stats['Mean PM2.5'] + wildfire_stats['Std PM2.5'], color='red', alpha=0.2)

# Formatting the Plot
plt.title('Hourly PM2.5 Concentrations: Non-Wildfire vs. Wildfire')
plt.xlabel('Hour of the Day')
plt.ylabel('PM2.5 (μg/m³)')
plt.xticks(range(1, 25))  # Ensure x-axis labels show every hour
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
