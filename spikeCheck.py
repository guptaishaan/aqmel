import pandas as pd

# Step 2: Define Parameters
csv_file_path = '/Users/ishaangupta/Downloads/main/assderp/jorgensen-v5/pose-detection-keypoints-estimation-yolov8/aqmel/aqmel/nodeData/extract_0.csv'
recursive_window_size = 3  # Example: considering the past 5 values
threshold_ratio = 2  # Example threshold

# Step 3: Read the CSV File
df = pd.read_csv(csv_file_path)
dates_column = 'Start of Period'  # Adjust the column name as per your CSV
particulate_level_column = 'PM 10 mass concentration, 1-hour mean, WaDwerAqi raw'  # Adjust the column name as per your CSV

# Ensure the Particulate Level data is numeric for calculations
df[particulate_level_column] = pd.to_numeric(df[particulate_level_column], errors='coerce')

# Step 4: Initialize the List for Spike Dates
spike_dates = []

# Step 5: Iterate Through Each Row in the CSV File
for index, row in df.iterrows():
    if index >= recursive_window_size:
        # Calculate the mean of the past 'recursive window size' values
        previous_values_mean = df[particulate_level_column][index-recursive_window_size:index].mean()
        
        current_particulate_level = row[particulate_level_column]
        
        # Calculate the ratio of the current level to the previous average
        if previous_values_mean != 0:  # Avoid division by zero
            ratio = current_particulate_level / previous_values_mean
            if ratio > threshold_ratio:
                spike_date = row[dates_column]
                spike_dates.append(spike_date)
                print(spike_date)


"""import pandas as pd

def detect_spikes(csv_file, window_size, threshold):
    # Load the data
    data = pd.read_csv('/Users/ishaangupta/Downloads/main/assderp/jorgensen-v5/pose-detection-keypoints-estimation-yolov8/aqmel/aqmel/nodeData/extract_0.csv')
    
    # Assuming the columns are named 'Date' and 'ParticulateMatter'
    # If your CSV has different column names, adjust them accordingly
    dates = data['Start of Period']
    levels = data['PM 10 mass concentration, 1-hour mean, WaDwerAqi raw']
    
    # Calculate the moving average
    moving_average = levels.rolling(window=window_size).mean()
    
    # Calculate the ratio of the current measurement to the moving average
    ratio = levels / moving_average
    
    # Identify spikes
    spikes = ratio > threshold
    spike_dates = dates[spikes]
    
    # Print the dates with spikes
    print("Dates with spikes in particulate matter levels:")
    print(spike_dates)

# Example usage
csv_file = '/Users/ishaangupta/Downloads/main/assderp/jorgensen-v5/pose-detection-keypoints-estimation-yolov8/aqmel/aqmel/nodeData/extract_0.csv'  # Update this to the path of your CSV file
window_size = 3  # Number of past measurements to include in the moving average
threshold = 1.5  # The ratio threshold to determine a spike, adjust based on your criteria

detect_spikes(csv_file, window_size, threshold)
"""