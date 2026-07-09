# Email Extractor 📧

A simple Python script to extract **email addresses** from a text file using **regular expressions (regex)**.

---

## Features
- Reads text from an input file (`sample.txt` by default).
- Finds all email addresses using regex.
- Saves extracted emails into an output file (`email.txt`).
- Handles missing input file gracefully.

---

## Requirements
- Python 3.x
- No external libraries required (uses built-in `os` and `re` modules).

---

## How to Run
1. Save the script as `extract_emails.py`.
2. Create a text file named `sample.txt` with some text containing email addresses.
3. Run the script:
   ```bash
   python extract_emails.py
