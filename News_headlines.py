#!/usr/bin/python3
import re

#raw API response containing news headlines
raw_data = """Here are some news headlines:
    Headline: Breaking News - Important Announcement
    Headline: Latest Updates - Weather Forecast
    Headline: Sports News - Exciting Match Results
    """
pattern = r'Headline: (.*?) - (.*?)'
matches = re.finditer(pattern, raw_data)
structured_headlines = []

for match in matches:
    headline = match.group(1)
    subheader = match.group(2)
    structured_headlines.append({"Headline": headline, "Subheader": subheader})
    for item in structured_headlines:
        print(item)
