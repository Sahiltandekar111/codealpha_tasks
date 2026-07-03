import os
import re

input_file = "sample.txt"
output_file = "email.txt"

if os.path.exists(input_file):
    with open(input_file,'r',encoding="utf-8") as f:
        text = f.read()

    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text)


    with open(output_file,"w",encoding="utf-8") as f:
        for email in emails:
            f.write(email + "\n")
    

    print(f"Extracted {len(emails)} in {output_file}")
else:
    print("invaild input file")


