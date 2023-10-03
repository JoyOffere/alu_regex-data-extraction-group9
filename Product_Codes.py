#!/usr/bin/python3
import re
Product_Codes_API = "ABC123, JOY010, FAITH112, ACE247,  EYE001, big101..."
Pattern = r"\b[A-Z]{3}\d{3}\b"
matches = re.findall(Pattern,Product_Codes_API)
for i in matches:
    print(i)