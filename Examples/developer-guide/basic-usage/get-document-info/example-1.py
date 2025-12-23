from groupdocs.parser import Parser

# Create an instance of Parser class
with Parser("./sample.docx") as parser:
    # Get the document info
    doc_info = parser.get_document_info()
    
    # Print document information
    print(f"File type: {doc_info.file_type.file_format}")
    print(f"Page count: {doc_info.page_count}")
    print(f"File size: {doc_info.size} bytes")
    
    # Print file extension
    print(f"File extension: {doc_info.file_type.extension}")