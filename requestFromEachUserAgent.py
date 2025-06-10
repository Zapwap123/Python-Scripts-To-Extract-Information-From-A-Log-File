from collections import Counter
import re

# Log file path
log_file = "NodeJsApp.log"

# Regex to extract the User-Agent string (it's the last quoted string in the log line)
user_agent_pattern = re.compile(r'"([^"]+)"\s*$')

# Counter for user agents
user_agent_counts = Counter()

# Read and process each line
with open(log_file, "r") as f:
    for line in f:
        match = user_agent_pattern.search(line)
        if match:
            user_agent = match.group(1)
            user_agent_counts[user_agent] += 1

# Display results
print("Request Count per User-Agent:")
for agent, count in user_agent_counts.most_common():
    print(f"Agent: {agent}: Count: {count}")
