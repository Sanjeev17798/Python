
# Algorithm: Disk Usage Monitor
# Start
# Define input parameters
# Set path (default: root /)
# Set threshold (e.g., 80%)
# Fetch disk statistics
# Get total disk space
# Get used disk space
# Get free disk space
# Calculate usage percentage
# usage % = (used / total) × 100
# Display disk details
# Print total space
# Print used space
# Print free space
# Print usage percentage
# Check threshold condition
# If usage % > threshold:
# Print warning message (Disk usage exceeded)
# Else:
# Print normal status
# (Optional enhancement)
# Log output to file
# Send alert (email/Slack)
# Run in loop for continuous monitoring
# End

import shutil

def check_disk_usage(path="/", threshold=80):
    total, used, free = shutil.disk_usage(path)
    
    used_percent = (used / total) * 100
    
    print(f"Total: {total // (2**30)} GB")
    print(f"Used: {used // (2**30)} GB")
    print(f"Free: {free // (2**30)} GB")
    print(f"Usage: {used_percent:.2f}%")
    
    if used_percent > threshold:
        print("⚠️ Disk usage exceeded threshold!")

check_disk_usage()