from groupdocs.parser import Parser
from groupdocs.parser.options import LoadOptions, FileFormat

# Create LoadOptions for MHTML format
load_options = LoadOptions(FileFormat.MHTML)

# Load MHTML document
with Parser("email_page.mhtml", load_options) as parser:
    # Extract text
    text_reader = parser.get_text()
    
    if text_reader:
        print(text_reader)