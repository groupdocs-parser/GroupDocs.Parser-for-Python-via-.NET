from groupdocs.parser import Parser

with Parser("./sample.pdf") as parser:
    # Get document info to check page count
    doc_info = parser.get_document_info()
    
    # Check if the document has pages
    if doc_info.page_count > 0:
        # Extract text from the first page (page index is 0-based)
        text_reader = parser.get_text(0)
        
        if text_reader:
            print(f"Text from page 1:")
            print(text_reader)