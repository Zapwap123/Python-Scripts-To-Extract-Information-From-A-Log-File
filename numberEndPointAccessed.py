import re
from collections import Counter

# Path to my log file
log_file = 'NodeJsApp.log'

# Regex pattern to extract the HTTP method and endpoint
pattern = re.compile(r'"[A-Z]+\s+(/[^ ]*)\s+HTTP/[\d.]+"')

# Counter to hold the endpoint access counts
endpoint_counter = Counter()

# Handle potential errors when reading the log file
try:
    
    # Read and process the log file
    with open(log_file, 'r') as f:

        # Iterate through each line in the log file
        for line in f:

            # Search for the pattern in the line
            match = pattern.search(line)

            # If a match is found, extract the endpoint and update the counter
            if match:
                endpoint = match.group(1)
                endpoint_counter[endpoint] += 1

    # Display the results
    print("Endpoint Access Counts:")
    for endpoint, count in endpoint_counter.most_common():
        print(f"{endpoint}: {count}")

# If there are any issues with the log file, handle them gracefully
except FileNotFoundError:
    print(f"Error: The log file '{log_file}' was not found.")
except PermissionError:
    print(f"Error: Permission denied when trying to read '{log_file}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
