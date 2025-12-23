from groupdocs.parser import Parser
from io import BytesIO

# Read file into memory
with open("sample.pdf", "rb") as file:
    file_data = file.read()

# Create a BytesIO stream
stream = BytesIO(file_data)

# Create an instance of Parser class with the stream
with Parser(stream) as parser:
    # Get document info
    doc_info = parser.get_document_info()
    
    print(f"File type: {doc_info.file_type.file_format}")
    print(f"Page count: {doc_info.page_count}")