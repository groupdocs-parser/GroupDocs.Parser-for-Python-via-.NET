from groupdocs.parser import Parser
from groupdocs.parser.options import LoadOptions, FileFormat

# Create LoadOptions for OTP (OpenDocument Presentation Template) format
load_options = LoadOptions(FileFormat.OTP)

# Load OTP document
with Parser("template.otp", load_options) as parser:
    # Get document info
    doc_info = parser.get_document_info()
    
    print(f"File type: {doc_info.file_type.file_format}")
    print(f"Pages: {doc_info.page_count}")
    
    # Extract text
    text_reader = parser.get_text()
    if text_reader:
        print(text_reader)