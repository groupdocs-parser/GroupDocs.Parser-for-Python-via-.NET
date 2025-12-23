from groupdocs.parser import Parser
from groupdocs.parser.options import TextOptions

# Create an instance of Parser class
with Parser("./sample.pdf") as parser:
    # Get document info
    info = parser.get_document_info()
    
    # Check if document has pages
    if info.raw_page_count == 0:
        print("Document has no pages")
        return
    
    # Create text options for raw mode
    options = TextOptions(False)
    
    # Iterate over pages
    for page_index in range(info.raw_page_count):
        print(f"
Page {page_index + 1}/{info.raw_page_count}")
        
        # Extract text from page in raw mode
        text_reader = parser.get_text(page_index, options)
        
        if text_reader is not None:
            print(text_reader)