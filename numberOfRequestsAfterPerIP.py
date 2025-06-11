import re
from datetime import datetime, timedelta
from collections import defaultdict

# Log file name
log_file = 'NodeJsApp.log'

# Regex pattern to extract timestamp and IP address
log_pattern = re.compile(r'(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z) (?P<ip>\d+\.\d+\.\d+\.\d+)')

# Dictionary to hold list of timestamps per IP
ip_requests = defaultdict(list)

# Handle potential errors when reading the log file
try:
    
    # Read and parse the log file
    with open(log_file, 'r') as f:

        # Iterate through each line in the log file
        for line in f:

            # Search for the pattern in the line
            match = log_pattern.search(line)

            # If a match is found, extract the timestamp and IP address
            if match:
                timestamp_str = match.group("timestamp")
                ip = match.group("ip")

                # Parse the timestamp and store it in the dictionary
                try:
                    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%fZ")
                    ip_requests[ip].append(timestamp)
                except ValueError:
                    # Skip malformed timestamp
                    continue

    # Analyze and print results
    for ip, times in ip_requests.items():
        times.sort()
        if not times:
            continue
        first_request = times[0]
        window_end = first_request + timedelta(seconds=10)
        count_after_first = sum(1 for t in times[1:] if t <= window_end)
        print(f"{ip}: {count_after_first} requests within 10 seconds after the first")

# If there are any issues with the log file, handle them gracefully
except FileNotFoundError:
    print(f"Error: The log file '{log_file}' was not found.")
except PermissionError:
    print(f"Error: Permission denied when trying to read '{log_file}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
