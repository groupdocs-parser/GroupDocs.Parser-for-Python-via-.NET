from groupdocs.parser import Parser

with Parser("./sample.docx") as parser:
    # Get document info
    doc_info = parser.get_document_info()
    
    print(f"Total pages: {doc_info.page_count}")
    
    # Iterate through pages
    for page_index in range(doc_info.page_count):
        # Extract text from each page
        print(f"
--- Page {page_index + 1} ---")
        text_reader = parser.get_text(page_index)
        if text_reader:
            page_text = text_reader
            print(f"Characters: {len(page_text)}")