from groupdocs.parser import Parser

# Open the file as a binary stream
with open("sample.docx", "rb") as stream:
    # Create an instance of Parser class with the stream
    with Parser(stream) as parser:
        # Extract text from the document
        text_reader = parser.get_text()
        
        if text_reader is not None:
            # Print the extracted text
            print(text_reader)
        else:
            print("Text extraction isn't supported for this format")