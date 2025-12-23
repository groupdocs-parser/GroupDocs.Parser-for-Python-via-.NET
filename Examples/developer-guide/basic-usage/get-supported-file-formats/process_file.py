from groupdocs.parser import Parser
from groupdocs.parser.options import FileType
import os

def process_file(file_path):
    """Process a file if its format is supported"""
    
    # Get file extension
    _, ext = os.path.splitext(file_path)
    
    # Check if format is supported
    supported_file_types = FileType.get_supported_file_types()
    is_supported = any(ft.extension.lower() == ext.lower() for ft in supported_file_types)
    
    if not is_supported:
        print(f"Error: File format '{ext}' is not supported")
        return False
    
    try:
        # Process the file
        with Parser(file_path) as parser:
            doc_info = parser.get_document_info()
            print(f"Processing: {file_path}")
            print(f"Format: {doc_info.file_type.file_format}")
            print(f"Pages: {doc_info.page_count}")
            
            # Extract text
            text_reader = parser.get_text()
            if text_reader:
                print("Text extraction successful")
                return True
    except Exception as e:
        print(f"Error processing file: {e}")
        return False

# Example usage
process_file("sample.pdf")
process_file("sample.docx")