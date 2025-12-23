from groupdocs.parser import Parser
from groupdocs.parser.options import LoadOptions, FileFormat

# Create LoadOptions for Markdown format
load_options = LoadOptions(FileFormat.MARKUP)

# Open the file stream
with open("sample.md", "rb") as stream:
    # Create an instance of Parser class with LoadOptions
    with Parser(stream, load_options) as parser:
        # Extract text from the Markdown document
        text_reader = parser.get_text()
        
        if text_reader is not None:
            # Print the extracted text
            # Markdown is detected; text without special symbols is printed
            print(text_reader)
        else:
            print("Text extraction isn't supported")