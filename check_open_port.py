#  Algorithm: Check Open Ports

# Start
# Import required library
# Import psutil module
# Fetch network connections
# Call function to get all active network connections
# Iterate through connections
# Loop over each connection in the list
# Filter listening ports
# Check if connection status is "LISTEN"
# Display port number
# Print the local port number of matching connections
# End

import psutil

def check_open_ports():
    connections = psutil.net_connections()
    
    for conn in connections:
        if conn.status == 'LISTEN':
            print(f"Port: {conn.laddr.port}")

check_open_ports()