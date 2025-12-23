from groupdocs.parser import Parser
from groupdocs.parser.options import LoadOptions

def load_protected_document(file_path, password):
    """Load a password-protected document with error handling"""
    
    try:
        # Create LoadOptions with password
        load_options = LoadOptions(password)
        
        # Create Parser instance
        with Parser(file_path, load_options) as parser:
            # Get document info to verify successful loading
            doc_info = parser.get_document_info()
            
            print(f"Document loaded successfully!")
            print(f"Type: {doc_info.file_type.file_format}")
            print(f"Pages: {doc_info.page_count}")
            
            # Extract text
            text_reader = parser.get_text()
            if text_reader:
                return text_reader
            
    except Exception as e:
        print(f"Error loading document: {e}")
        return None

# Try loading with password
text = load_protected_document("protected.docx", "correct-password")