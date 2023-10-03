#!/usr/bin/env python3
import re

def extract_usernames(text):
    pattern = r'@([a-zA-Z0-9_]+)'
    matches = re.findall(pattern, text)
    return matches

if __name__ == "__main__":
    text = "Check out this cool post by @user123 and follow @example_user!"
    usernames = extract_usernames(text)
    print("Usernames:", usernames)

