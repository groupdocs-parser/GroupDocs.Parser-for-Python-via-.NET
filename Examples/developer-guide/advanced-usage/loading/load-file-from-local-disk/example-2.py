from groupdocs.parser import Parser

# Specify an absolute file path
file_path = "sample.pdf"

# Create an instance of Parser class
with Parser(file_path) as parser:
    # Get document info
    doc_info = parser.get_document_info()
    
    print(f"File type: {doc_info.file_type.file_format}")
    print(f"Page count: {doc_info.page_count}")
    print(f"File size: {doc_info.size} bytes")