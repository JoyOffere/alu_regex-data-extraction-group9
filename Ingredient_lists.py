#!/usr/bin/python3
import re

API_sample = "Ingredients: tomato, fish, onion, garlic, salt, pepper, olive oil, basil leaves, pasta, parmesan cheese, lemon juice, capers, mushrooms, bell pepper, oregano, thyme, red wine vinegar, chicken breast, cumin, coriander, paprika, soy sauce, ginger, sugar, broccoli, carrots, cilantro, coconut milk, turmeric, chickpeas, tahini, honey, almonds, quinoa, cheddar cheese, spinach, nutmeg, rosemary, parsley, walnuts, apples, cinnamon, honey mustard"

pattern = r"(\b\w+\b)(?:,|$)"
ingredient_matches = re.findall(pattern, API_sample)
ingredient_list = [ingredient.strip() for ingredient in ingredient_matches]
print("Ingredients:", ingredient_list)
