# Write a Python script to check disk usage of the system and print a warning if usage exceeds 80%.
# Start
# Define a threshold value (e.g., 80%)
# Get total, used, and free disk space of the system
# Calculate disk usage percentage:
#  (used / total) * 100
# Print the disk usage percentage
# If usage > threshold
# Print warning message
# Else
# Print “disk usage is normal”
# End

import shutil

def check_disk_usage(threshold=80):
    total, used, free = shutil.disk_usage("/")
    
    usage_percent = (used / total) * 100
    print(f"Disk Usage: {usage_percent:.2f}%")
    
    if usage_percent > threshold:
        print("WARNING: Disk usage exceeded 80%!")
    else:
        print("Disk usage is under control.")

check_disk_usage()
