from groupdocs.parser import Parser

# Open the file stream
with open("sample.pdf", "rb") as stream:
    # Create an instance of Parser class with the stream
    with Parser(stream) as parser:
        # Extract text into the reader
        text_reader = parser.get_text()
        
        if text_reader is not None:
            # Print the extracted text
            extracted_text = text_reader
            print(extracted_text)
        else:
            print("Text extraction isn't supported for this format")