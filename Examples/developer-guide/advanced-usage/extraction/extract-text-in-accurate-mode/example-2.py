from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("./sample.pdf") as parser:
    # Check if text extraction is supported
    if not parser.features.text:
        print("Document doesn't support text extraction")
        return
    
    # Get document info
    info = parser.get_document_info()
    
    # Check if document has pages
    if info.page_count == 0:
        print("Document has no pages")
        return
    
    # Iterate over pages
    for page_index in range(info.page_count):
        # Print page number
        print(f"
Page {page_index + 1}/{info.page_count}")
        
        # Extract text from the page
        text_reader = parser.get_text(page_index)
        
        # Print the page text
        if text_reader is not None:
            print(text_reader)