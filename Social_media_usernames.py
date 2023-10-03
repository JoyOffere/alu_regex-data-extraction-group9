#!/usr/bin/env python3
import re

def extract_usernames(API_responses):
    pattern = r'@([a-zA-Z0-9_]+)'
    matches = re.findall(pattern, API_responses)
    return matches

if __name__ == "__main__":
    API_responses = "Check out this cool post by @user123 and follow @example_user!"
    usernames = extract_usernames(API_responses)
    print("Usernames:", usernames)

