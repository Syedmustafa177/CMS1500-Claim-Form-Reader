# CMS1500-Claim-Form-Reader
This script reads and extracts text from a CMS-1500 form (Health Insurance Claim Form) PDF file. The extracted text can then be used to integrate the form details into other tools such as Reflection or Facets, which may not capture the form details correctly.

 ### Prerequisites
 * Python 3.x
 * pypdf library


### Description

This script is designed to read and extract text from a CMS-1500 form PDF file. The extracted text can then be used to integrate the form details into tools that may not capture the form details correctly.

### Steps

1. **Import Required Libraries**
   - `Path` from the `pathlib` module for handling file paths.
   - `PdfReader` and `PdfWriter` from the `pypdf` module for reading and writing PDF files.
   - `re` module for regular expressions (though not used in this snippet, it may be useful for future enhancements).

2. **Define the Path to the PDF File**
   - The script uses the `Path` module to define the path to the "Health Insurance Claim form.pdf" file located in the same directory as the script.

3. **Read the PDF File**
   - An instance of `PdfReader` is created with the PDF file path.
   - The script retrieves the total number of pages in the PDF file.
   - The script extracts text from the first page of the PDF file.

4. **Print the Extracted Text**
   - The extracted text from the first page is printed to the console.

### Future Enhancements

- Extend the script to process multiple pages if the form spans more than one page.
- Use regular expressions to parse and structure the extracted text into meaningful data fields.
- Integrate the parsed data into Reflection, Facets, or other tools to automate form processing and data entry.

### License

This project is licensed under the MIT License.



