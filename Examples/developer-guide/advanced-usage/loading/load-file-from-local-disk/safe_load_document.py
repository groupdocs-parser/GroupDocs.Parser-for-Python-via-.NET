from groupdocs.parser import Parser
import os

def safe_load_document(file_path):
    """Safely load a document with error handling"""
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File not found - {file_path}")
        return None
    
    try:
        # Create parser instance
        parser = Parser(file_path)
        print(f"Document loaded successfully: {file_path}")
        return parser
        
    except Exception as e:
        print(f"Error loading document: {e}")
        return None

# Try to load a document
parser = safe_load_document("sample.pdf")

if parser:
    try:
        # Extract data
        text_reader = parser.get_text()
        if text_reader:
            print(text_reader)