#!/usr/bin/env python3
import re

def extract_usernames(API_sample):
    pattern = r'@([a-zA-Z0-9_]+)'
    matches = re.findall(pattern, API_sample)
    return matches

if __name__ == "__main__":
    API_sample = "Dec 25, 2023 - 02:30 PM, Dec 31, 2023 - 00:00 AM, Oct 01, 2024 - 04:00 PM, Oct 03, 2025 - 00:00 AM, rgb(255, 0, 128), rgb(0, 255, 0), rgb(255, 255, 255), rgb(210, 210), rgb(0, 0, 0), Headline: Breaking News - Important Announcement, Headline: Latest Updates - Weather Forecast, Headline: Sports News - Exciting Match Results, ABC123, JOY010, FAITH112, ACE247,  EYE001, big101, @user123, @user789..."
    usernames = extract_usernames(API_sample)
    print("Usernames:", usernames)

