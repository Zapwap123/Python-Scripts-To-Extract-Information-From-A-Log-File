import re
from collections import Counter

# Path to my log file
log_file = 'NodeJsApp.log'

# Regex pattern to extract the HTTP method and endpoint
pattern = re.compile(r'"[A-Z]+\s+(/[^ ]*)\s+HTTP/[\d.]+"')

# Counter to hold the endpoint access counts
endpoint_counter = Counter()

# Read and process the log file
with open(log_file, 'r') as f:
    for line in f:
        match = pattern.search(line)
        if match:
            endpoint = match.group(1)
            endpoint_counter[endpoint] += 1

# Display the results
print("Endpoint Access Counts:")
for endpoint, count in endpoint_counter.most_common():
    print(f"{endpoint}: {count}")
