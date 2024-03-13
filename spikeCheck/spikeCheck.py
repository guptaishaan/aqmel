import pandas as pd

def detect_spike_days(csv_path):
    # Load the CSV file
    df = pd.read_csv(csv_path)
    
    # Convert 'Start of Period' to datetime
    df['Start of Period'] = pd.to_datetime(df['Start of Period'])
    
    # Assuming PM2.5 readings are in the 56th column (55th in 0-based indexing)
    pm25_column_index = 55
    pm25_column_name = df.columns[pm25_column_index]
    df[pm25_column_name] = pd.to_numeric(df[pm25_column_name], errors='coerce')
    
    # Calculate rolling averages for previous 5 and next 5 PM2.5 readings
    df['prev_5_avg'] = df[pm25_column_name].rolling(window=5).mean().shift(1)
    df['next_5_avg'] = df[pm25_column_name].rolling(window=5).mean().shift(-5)
    
    # Identify spikes where the next 5 readings' average is more than 150% of the previous 5
    df['spike'] = df['next_5_avg'] > 1.5 * df['prev_5_avg']
    
    # Filter for dates where there is a spike
    spike_dates = df[df['spike']]['Start of Period']
    
    # Return the spike dates
    return spike_dates

# Example usage:
csv_path = '/Users/ishaangupta/Downloads/main/assderp/jorgensen-v5/pose-detection-keypoints-estimation-yolov8/aqmel/aqmel/nodeData/AYHCFXLYdata.csv'  # Replace this with the path to your CSV file
spike_dates = detect_spike_days(csv_path)
print("Spike Dates:")
print(spike_dates)
