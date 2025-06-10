
import re, ipaddress
# Path to the log file
logFilePath = "./NodeJsApp.log"
counterDict = {}

# ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

ipv4_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
ipv6_pattern = r'\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b|\b(?:[0-9a-fA-F]{1,4}:)*::[0-9a-fA-F]{0,4}(?::[0-9a-fA-F]{1,4})*\b'
ip_pattern = f'({ipv4_pattern}|{ipv6_pattern})'

with open(logFilePath) as f:
    for line in f:
        try:
            userIP = line.split(" ")[1]
            if re.search(ip_pattern, userIP):
                # ipaddress.ip_address(userIP)
                counterDict[userIP] = counterDict.get(userIP, 0) + 1
            else:
                continue
        except IndexError:
            pass

# Print the number of unique IP addresses and the addresses themselves
print("Unique IP Count:", len(counterDict))

for ip, count in counterDict.items():
    print(f"IP: {ip}: Count: {count}")

# 1.For each ip address, check to see how many request came in, 
#   after the very first request, within a 10 sec window
# 2. Write a script to determine the number of request coming 
#    from each user agent type
# 3. Write a script to count the number of times each end point was accessed