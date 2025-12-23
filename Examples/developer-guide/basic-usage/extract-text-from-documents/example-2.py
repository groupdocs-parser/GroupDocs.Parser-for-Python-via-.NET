from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("./sample.docx") as parser:
    # Extract text into the reader
    text_reader = parser.get_text()
    
    if text_reader is not None:
        # Print the extracted text
        extracted_text = text_reader
        print(extracted_text)
    else:
        print("Text extraction isn't supported for this format")