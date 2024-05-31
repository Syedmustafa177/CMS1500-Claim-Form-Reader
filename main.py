from pathlib import Path
from pypdf import PdfReader
from pypdf import PdfWriter
import re


# Get path to pdfs directory
pdf_path = (Path(__file__).parent/"Health Insurance Claim form.pdf")

# reader and writer perform operations
reader = PdfReader(pdf_path)

number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()


print(text)




# print(text)


# Use regular expression to extract text from Number 2
# matches = re.findall(r"A\.(.*?)B\.", text, re.DOTALL)

# if matches:
#     extracted_text = matches[0].strip()
#     extracted_text = re.sub(r'\s', '', extracted_text)

# # Remove symbols
#     extracted_text = re.sub(r'[\W_]', '', extracted_text)
#     print(extracted_text)
# else:
#     print("Text from Number 2 not found.")