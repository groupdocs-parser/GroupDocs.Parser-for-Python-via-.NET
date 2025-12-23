from groupdocs.parser import Parser
from groupdocs.parser.options import LoadOptions

def safe_load_with_format(file_path, file_format):
    """Safely load a document with specific format and error handling"""
    
    try:
        # Create LoadOptions
        load_options = LoadOptions(file_format)
        
        # Create Parser instance
        with Parser(file_path, load_options) as parser:
            # Verify loading was successful
            doc_info = parser.get_document_info()
            print(f"Document loaded: {doc_info.file_type.file_format}")
            
            # Extract text
            text_reader = parser.get_text()
            if text_reader:
                return text_reader
            else:
                print("Text extraction not supported")
                return None
                
    except Exception as e:
        print(f"Error loading document with format {file_format}: {e}")
        
        # Try loading without format specification
        try:
            print("Attempting to load with auto-detection...")
            with Parser(file_path) as parser:
                text_reader = parser.get_text()
                if text_reader:
                    return text_reader
        except Exception as e2:
            print(f"Auto-detection also failed: {e2}")
            return None

# Example usage
from groupdocs.parser.options import FileFormat
text = safe_load_with_format("document.md", FileFormat.MARKUP)