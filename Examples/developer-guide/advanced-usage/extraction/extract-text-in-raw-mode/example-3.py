from groupdocs.parser import Parser
from groupdocs.parser.options import TextOptions

# Create an instance of Parser class
with Parser("sample.pdf") as parser:
    # Get document info
    info = parser.get_document_info()
    
    print(f"Accurate mode pages: {info.page_count}")
    print(f"Raw mode pages: {info.raw_page_count}")
    
    # The page count may differ between modes!