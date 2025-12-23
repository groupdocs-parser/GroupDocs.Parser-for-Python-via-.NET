from groupdocs.parser import Parser

# Specify the file path (absolute or relative)
file_path = "sample.docx"

# Create an instance of Parser class with the file path
with Parser(file_path) as parser:
    # Extract text from the document
    text_reader = parser.get_text()
    
    if text_reader is not None:
        # Print the extracted text
        print(text_reader)
    else:
        print("Text extraction isn't supported for this format")