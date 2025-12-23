from groupdocs.parser import Parser

try:
    with Parser("./unknown.format") as parser:
        doc_info = parser.get_document_info()
        
        if doc_info:
            print(f"File type: {doc_info.file_type.file_format}")
            
            # Some formats may not have page count
            if doc_info.page_count == 0:
                print("Page count is not available for this format")
        else:
            print("Could not retrieve document information")
            
except Exception as e:
    print(f"Error: {e}")