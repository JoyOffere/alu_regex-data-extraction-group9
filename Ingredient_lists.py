#!/usr/bin/python3
import re

API_sample = "Dec 25, 2023 - 02:30 PM, Dec 31, 2023 - 00:00 AM, Oct 01, 2024 - 04:00 PM, Oct 03, 2025 - 00:00 AM, rgb(255, 0, 128), rgb(0, 255, 0), rgb(255, 255, 255), rgb(210, 210), rgb(0, 0, 0), Headline: Breaking News - Important Announcement, Headline: Latest Updates - Weather Forecast, Headline: Sports News - Exciting Match Results, ABC123, JOY010, FAITH112, ACE247,  EYE001, big101, @user123, @user789..."

ingredients_pattern = r"'(.*?)'"
ingredients_matches = re.findall(ingredients_pattern, raw_data)

for ingredients in ingredients_matches:
    ingredients_list = [ingredient.strip() for ingredient in ingredients.split(',')]
    print("Ingredients:", ingredients_list)
