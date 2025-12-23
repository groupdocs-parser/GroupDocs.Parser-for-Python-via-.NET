from groupdocs.parser import Parser
from groupdocs.parser.options import LoadOptions

# Document password
password = "your-password"

# Create LoadOptions with the password
load_options = LoadOptions(password)

# Create an instance of Parser class with the file path and load options
with Parser("protected_document.pdf", load_options) as parser:
    # Extract text from the document
    text_reader = parser.get_text()
    
    if text_reader is not None:
        # Print the extracted text
        print(text_reader)
    else:
        print("Text extraction isn't supported for this format")