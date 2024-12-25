#!/data/bin/python3

# Title: Send Notifications to Apple Watch With Android
# Author: Abishek Muthian
# Website: www.abishekmuthian.com
# Date: 12/14/24
"""
This software is released under the MIT License.
You can find a copy of the license in the LICENSE file or at https://opensource.org/licenses/MIT.
"""

import json
import subprocess
import time
import requests
import logging
import hashlib

# Set up logging

file_handler = logging.FileHandler('/data/data/com.termux/files/home/storage/termux-scripts/apple-watch-to-android/notification_script.log')
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

file = "/data/data/com.termux/files/home/storage/termux-scripts/apple-watch-to-android/sent_ids.txt"
token = ""  # replace with your actual token
user = ""  # updated user ID
url = "https://api.pushover.net/1/messages.json"
blacklist_file = "/data/data/com.termux/files/home/storage/termux-scripts/apple-watch-to-android/package_name_blacklist.txt"

# Read the package name blacklist from file
with open(blacklist_file, 'r') as f:
    package_name_blacklist = [line.strip() for line in f]

logger.info(f"Loaded {len(package_name_blacklist)} package names to be ignored")

# Check if the file exists, and create it only if it doesn't exist
with open(file, 'a+'):
    	logger.info("Checked for sent_ids.txt")

def check_notifications():
    # Use termux-notification-list to get notifications
    output = subprocess.check_output("termux-notification-list", shell=True).decode('utf-8')
    logger.debug(f"Raw notification data: {output}")

    try:
        json_data = json.loads(output)
        logger.debug(f"Parsed JSON data: {json_data}")
    except json.JSONDecodeError:
        logger.error("Failed to parse JSON data")

    for notification in json_data:
        package_name = str(notification['packageName'])
        title = str(notification['title'])
        content = str(notification['content']).encode('utf-8')  # Convert the content to bytes

        # Check if the package name is on the blacklist
        if package_name in package_name_blacklist:
            logger.info(f"Ignoring notification from package '{package_name}'")
            continue

        # Calculate the SHA256 hash of the notification content
        content_hash = hashlib.sha256(content).hexdigest()

        with open(file, 'r') as f:
            if content_hash not in f.read():
                try:
                    response = requests.post(url, data={"token": token, "user": user, "message": content, "title": title})
                    logger.info(f"Sent notification with hash {content_hash}")
                except requests.RequestException as e:
                    logger.error(f"Failed to send notification with hash {content_hash}: {e}")
                    continue

                if response.status_code == 200:
                    with open(file, 'a') as f:
                        f.write(f"{content_hash}\n")
                        logger.debug(f"Added hash {content_hash} to sent_ids.txt")

def main():
	check_notifications()

if __name__ == "__main__":
    main()