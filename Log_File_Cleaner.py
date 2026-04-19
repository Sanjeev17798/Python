# Write a Python script that scans a directory and deletes .log files older than 7 days.

# Start
# Take directory path as input (or define it in code)
# Get current time
# Loop through all files in the directory
# For each file:
# Check if file ends with .log
# Get file’s last modified time
# Calculate file age in days
# If file age > 7 days:
# Delete the file
# Print file name (optional)
# End

import os
import time

def delete_old_logs(directory, days=7):
    current_time = time.time()
    
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        
        # Check if it's a file and ends with .log
        if os.path.isfile(file_path) and file.endswith(".log"):
            
            file_mtime = os.path.getmtime(file_path)
            file_age_days = (current_time - file_mtime) / (24 * 3600)
            
            if file_age_days > days:
                os.remove(file_path)
                print(f"Deleted: {file_path}")

if __name__ == "__main__":
    directory_path = input("Enter directory path: ")
    delete_old_logs(directory_path)
