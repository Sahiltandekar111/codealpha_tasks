import os
import re

# Input file containing text
input_file = "sample.txt"

# Output file to save extracted emails
output_file = "email.txt"

# Check if input file exists
if os.path.exists(input_file):
    # Read the content of the file
    with open(input_file, 'r', encoding="utf-8") as f:
        text = f.read()

    # Regex pattern to match email addresses
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text)

    # Write extracted emails to output file
    with open(output_file, "w", encoding="utf-8") as f:
        for email in emails:
            f.write(email + "\n")

    # Print success message
    print(f"Extracted {len(emails)} emails and saved to {output_file}")
else:
    # Print error if input file not found
    print("Invalid input file")

