from groupdocs.parser import Parser
from groupdocs.parser.options import TextOptions

# Create an instance of Parser class
with Parser("./sample.pdf") as parser:
    # Create text options for raw mode
    options = TextOptions(False)  # False = Raw mode, True = Accurate mode
    
    # Extract text in raw mode
    text_reader = parser.get_text(options)
    
    # Check if text extraction is supported
    if text_reader is None:
        print("Text extraction isn't supported")
    else:
        # Print the extracted text
        print(text_reader)