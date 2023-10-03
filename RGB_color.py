#!/usr/bin/python3
import re

API_sample = "This is a color: rgb(255, 0, 128), rgb(0, 255, 0), rgb(255, 255, 255), rgb(210, 210), rgb(0, 0, 0)..."
pattern = r"rgb\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)"

matches = re.findall(pattern, API_sample)

for match in matches:
    color_0, color_1, color_2 = map(int, match)
    print(f"RGB Color: rgb({color_0}, {color_1}, {color_2})")
