# CMS1500-Claim-Form-Reader
Description
This script is designed to read and extract text from a CMS-1500 form (Health Insurance Claim Form) PDF file. The extracted text can then be used to integrate the form details into other tools such as Reflection or Facets, which may not capture the form details correctly.

Steps:
Import Required Libraries:

Path from the pathlib module for handling file paths.
PdfReader and PdfWriter from the pypdf module for reading and writing PDF files.
re module for regular expressions (though not used in this snippet, it may be useful for future enhancements).
Define the Path to the PDF File:

The script uses the Path module to define the path to the "Health Insurance Claim form.pdf" file located in the same directory as the script.
Read the PDF File:

An instance of PdfReader is created with the PDF file path.
The script retrieves the total number of pages in the PDF file.
The script extracts text from the first page of the PDF file.
Print the Extracted Text:

The extracted text from the first page is printed to the console.
Usage
This script serves as a foundational step to automate the extraction of information from CMS-1500 forms, facilitating the integration of these details into tools that may not natively support or accurately capture the form's information. Future enhancements could involve parsing the extracted text using regular expressions to extract specific fields and data points for more structured integration.

Future Enhancements
Extend the script to process multiple pages if the form spans more than one page.
Use regular expressions to parse and structure the extracted text into meaningful data fields.
Integrate the parsed data into Reflection, Facets, or other tools to automate form processing and data entry.
This approach ensures the CMS-1500 form details are accurately captured and utilized within your workflow, improving efficiency and reducing the risk of errors associated with manual data entry.
