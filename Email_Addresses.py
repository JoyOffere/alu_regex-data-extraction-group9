import re

# Read text from an external text file
file_path = 'text-doc.txt'

try:
    with open(file_path, 'r') as file:
        text = file.read()
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        email_addresses = re.findall(email_pattern, text)

        # Print the extracted email addresse
        for email in email_addresses:
            print(email)
    
except FileNotFoundError:
    print(f"File not found: {file_path}")