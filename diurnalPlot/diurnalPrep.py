import pandas as pd

def analyze_hourly_pm25(file_path):
    # Load the data
    df = pd.read_csv(file_path)
    
    # Ensure the date column is in datetime format and extract both date and hour
    df['DateTime'] = pd.to_datetime(df.iloc[:, 5])
    df['Date'] = df['DateTime'].dt.date
    df['Hour'] = df['DateTime'].dt.hour
    
    # Extract PM2.5 readings (assuming they are in column 56, as per 0-based indexing)
    df['PM2.5'] = pd.to_numeric(df.iloc[:, 55], errors='coerce')

    # Define the date ranges for non-wildfire and wildfire periods
    non_wildfire_start = pd.to_datetime('2023-11-30').date()
    non_wildfire_end = pd.to_datetime('2023-12-13').date()
    wildfire_start = pd.to_datetime('2023-12-14').date()
    wildfire_end = pd.to_datetime('2023-12-27').date()

    # Filter data for non-wildfire and wildfire periods
    non_wildfire_df = df[(df['Date'] >= non_wildfire_start) & (df['Date'] <= non_wildfire_end)]
    wildfire_df = df[(df['Date'] >= wildfire_start) & (df['Date'] <= wildfire_end)]

    # Group by hour and calculate mean and standard deviation for PM2.5
    non_wildfire_stats = non_wildfire_df.groupby('Hour')['PM2.5'].agg(['mean', 'std']).reset_index().rename(columns={'mean': 'Mean PM2.5', 'std': 'Std PM2.5'})
    wildfire_stats = wildfire_df.groupby('Hour')['PM2.5'].agg(['mean', 'std']).reset_index().rename(columns={'mean': 'Mean PM2.5', 'std': 'Std PM2.5'})

    # Optionally, save these stats to CSV or return them
    non_wildfire_stats.to_csv('/Users/ishaangupta/Downloads/main/assderp/jorgensen-v5/pose-detection-keypoints-estimation-yolov8/aqmel/non_wildfire_stats.csv', index=False)
    wildfire_stats.to_csv('/Users/ishaangupta/Downloads/main/assderp/jorgensen-v5/pose-detection-keypoints-estimation-yolov8/aqmel/wildfire_stats.csv', index=False)

    return non_wildfire_stats, wildfire_stats

# Example usage
file_path = '/Users/ishaangupta/Downloads/main/assderp/jorgensen-v5/pose-detection-keypoints-estimation-yolov8/aqmel/aqmel/nodeData/AQQCNWJ6data.csv'
non_wildfire_stats, wildfire_stats = analyze_hourly_pm25(file_path)

# Display the first few rows of the results for verification
non_wildfire_stats.head(), wildfire_stats.head()
