from groupdocs.parser import Parser

def process_document(file_path):
    with Parser(file_path) as parser:
        # Get document information
        doc_info = parser.get_document_info()
        
        print(f"Processing: {file_path}")
        print(f"Type: {doc_info.file_type.file_format}")
        print(f"Pages: {doc_info.page_count}")
        print(f"Size: {doc_info.size / 1024:.2f} KB")
        
        # Process based on page count
        if doc_info.page_count > 0:
            print("Document has pages, proceeding with text extraction...")
            text_reader = parser.get_text()
            if text_reader:
                print(text_reader)
        else:
            print("Document has no pages or page count is not available")

# Process different document types
process_document("sample.pdf")