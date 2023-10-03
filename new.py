#!/usr/bin/python3
import re

raw_data = "Ingredients: 'Tomatoes, Cheese, Pepperoni, Dough', 'Eggs, Flour, Sugar'"

ingredients_pattern = r"'(.*?)'"
ingredients_matches = re.findall(ingredients_pattern, raw_data)

for ingredients in ingredients_matches:
    ingredients_list = [ingredient.strip() for ingredient in ingredients.split(',')]
    print("Ingredients:", ingredients_list)
