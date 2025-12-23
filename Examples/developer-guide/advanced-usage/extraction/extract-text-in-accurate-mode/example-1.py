from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("./sample.pdf") as parser:
    # Extract text from the document
    text_reader = parser.get_text()
    
    # Check if text extraction is supported
    if text_reader is None:
        print("Text extraction isn't supported")
    else:
        # Print the extracted text
        print(text_reader)