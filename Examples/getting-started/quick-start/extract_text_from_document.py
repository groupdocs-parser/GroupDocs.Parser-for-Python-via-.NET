from groupdocs.parser import Parser

def extract_text_from_document():
    # Create an instance of Parser class
    with Parser("./sample.pdf") as parser:
        # Extract text from the document
        text_reader = parser.get_text()
        
        if text_reader is not None:
            # Print the extracted text
            print(text_reader)
        else:
            print("Text extraction isn't supported for this format")

if __name__ == "__main__":
    extract_text_from_document()