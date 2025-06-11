from collections import Counter
import re

# Log file path
log_file = "NodeJsApp.log"

# Regex to extract the User-Agent string (it's the last quoted string in the log line)
user_agent_pattern = re.compile(r'"([^"]+)"\s*$')

# Counter for user agents
user_agent_counts = Counter()

# Handle potential errors when reading the log file
try:

    # Read and process each line
    with open(log_file, "r") as f:

        # Iterate through each line in the log file
        for line in f:
            match = user_agent_pattern.search(line)
            
            # If a match is found, extract the User-Agent and update the counter
            if match:
                user_agent = match.group(1)
                user_agent_counts[user_agent] += 1

    # Display results
    print("Request Count per User-Agent:")
    for agent, count in user_agent_counts.most_common():
        print(f"Agent: {agent}: Count: {count}")

# If there are any issues with the log file, handle them gracefully
except FileNotFoundError:
    print(f"Error: The log file '{log_file}' was not found.")
except PermissionError:
    print(f"Error: Permission denied when trying to read '{log_file}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
