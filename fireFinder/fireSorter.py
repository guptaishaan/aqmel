import csv
import numpy as np
from collections import defaultdict

def calculate_means_and_filter(input_file, filtered_output_file, percentile=75):
    date_values = defaultdict(list)
    
    # Read the input CSV and calculate means
    with open(input_file, mode='r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            date_trimmed = row[4][:10]  # Trim the date to 'YYYY-MM-DD'
            value = row[71]  # The value from the 72nd column
            
            # Check if the value is empty or not a valid float
            if value:
                try:
                    value = float(value)
                    date_values[date_trimmed].append(value)
                except ValueError:
                    continue
    
    # Calculate mean values for each date
    date_means = [(date, sum(values) / len(values)) for date, values in date_values.items() if values]
    
    # Extract mean values and calculate the cutoff for the top percentile
    values_only = [mean for _, mean in date_means]
    cutoff = np.percentile(values_only, percentile)
    
    # Filter and write the top percentile to a new CSV file
    with open(filtered_output_file, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Date', 'Mean Value'])  # Write the header
        for date, mean in date_means:
            if mean >= cutoff:
                writer.writerow([date, mean])

# Example usage:
input_csv = '/Users/ishaangupta/Downloads/main/aqmel/extract_0.csv'
filtered_output_csv = '/Users/ishaangupta/Downloads/main/aqmel/aqmel/fireFinder/AKMKX7CN.csv'

calculate_means_and_filter(input_csv, filtered_output_csv)