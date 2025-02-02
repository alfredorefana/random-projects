#!/bin/bash

# This is a small script to check suspicious IP from the bitnami access log and then block it in the iptables.
# Small script to identify malicious traffic from IPs which overload bitnami wordpress website.
# This has been developed based on the following resources:
# https://docs.bitnami.com/general/faq/configuration/block-suspicious-ip/
# https://jilaxzone.com/2021/05/27/aws-lightsail-bitnami-wordpress-fix-for-cpu-utilization-always-high-while-cpu-bursting-always-remain-zero/

# Creating the file to save the result of checks
date=`date +"%Y%m%dT%H%M%S"`
WORK_DIR="/root/suspicious_ips"
file="$WORK_DIR/logs/check_of_${date}.txt"
touch $file

# Get top-10 list of IP Address accessing  WordPress website
# Checking the logs and saving the output to a file
tail -n 10000 /opt/bitnami/apache2/logs/access_log | awk '{print $1}'| sort| uniq -c| sort -nr| head -n 10 > $file

# Analyzing the file contents
#file="/root/suspicious_ips/logs/check_of-20231006T121307.txt"

rules="/opt/bitnami/iptables-rules"

while read -r line; do
        #echo -e "Line: $line"
        count=$(awk '{print $1}' <<< "$line") # 1st column
        ip=$(awk '{print $2}' <<< "$line") # 2nd column
        # Checking the count and adding the ip to iptables
        if [ $count -ge 500 ]; then
                echo -e "Suspicious bot: $line"
                if ! grep -q $ip $rules; then
                        echo "IP not blocked yet, adding to the rules."
                        cp /opt/bitnami/iptables-rules $WORK_DIR/backups/iptables-rules_${date} # take a bcakup of the iptables files
                        /usr/sbin/iptables -A INPUT -s $ip -j DROP # adding the rule to drop the traffic
                        /usr/sbin/iptables-save > /opt/bitnami/iptables-rules # making iptables-rules to be persistent even after rebooting the server
                        echo "$(cat /opt/bitnami/iptables-rules)"
                else
                        echo "IP already blocked."
                fi
        else
                echo "This IP $ip seems to be a legit visitor with $count requests."
        fi
done < $file

# Deleting old files.
# Find and delete files older than 5 days
find "$WORK_DIR/logs" -type f -mtime +3 -exec rm -f {} \;
echo "Files older than 5 days have been deleted from $WORK_DIR/logs."
