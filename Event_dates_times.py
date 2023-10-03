#!/usr/bin/python3
import re

API_sample = "Event on: Dec 25, 2023 - 02:30 PM, Dec 31, 2023 - 00:00 AM, Oct 01, 2024 - 04:00 PM, Oct 03, 2025 - 00:00 AM, ..."

pattern = r"(\w{3}\s\d{2},\s\d{4}\s-\s\d{2}:\d{2}\s[APap][Mm])"
matches = re.findall(pattern, API_sample)
if matches:
    for event in matches:
        print(f"Event on: {event}")
else:
        print("No matching event dates and times found.")
