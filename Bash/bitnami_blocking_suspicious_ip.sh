#!/bin/bash

# This is a small script to check suspicious IP from the bitnami access log and then block it in the iptables.
# Small script to identify malicious traffic from IPs that overload bitnami WordPress website.
# This has been developed based on the following resources:
# https://docs.bitnami.com/general/faq/configuration/block-suspicious-ip/
# https://jilaxzone.com/2021/05/27/aws-lightsail-bitnami-wordpress-fix-for-cpu-utilization-always-high-while-cpu-bursting-always-remain-zero/

# Creating the file to save the result of checks
date=`date +"%Y%m%dT%H%M%S"`
file=/root/suspicious_ips/logs/check_of_${date}.txt
touch $file

# Get top-10 list of IP Address accessing  WordPress website
# Checking the logs and saving the output to a file
tail -n 500 /opt/bitnami/apache2/logs/access_log | awk '{print $1}'| sort| uniq -c| sort -nr| head -n 10 > $file

# Analyzing the file contents
#file="/root/suspicious_ips/logs/check_of-20231006T121307.txt"

while read -r line; do
        #echo -e "Line: $line"
        count=$(awk '{print $1}' <<< "$line") # 1st column
        ip=$(awk '{print $2}' <<< "$line") # 2nd column

        # Checking the count and adding the ip to iptables
        if [ $count -ge 100 ]; then
                echo -e "Suspicious bot: $line"
                cp /opt/bitnami/iptables-rules /root/suspicious_ips/backups/iptables-rules_${date} # take a bcakup of the iptables files
                /usr/sbin/iptables -A INPUT -s $ip -j DROP # adding the rule to drop the traffic
                /usr/sbin/iptables-save > /opt/bitnami/iptables-rules # iptables rules active even after rebooting the server
                #echo "$(cat /opt/bitnami/iptables-rules)"
        else
                #    echo "No new IP with high traffic."                
        fi
done < $file
