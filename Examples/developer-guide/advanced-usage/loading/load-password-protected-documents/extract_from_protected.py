from groupdocs.parser import Parser
from groupdocs.parser.options import LoadOptions

def extract_from_protected(file_path, password, extract_type="text"):
    """Extract data from various password-protected formats"""
    
    try:
        # Create LoadOptions with password
        load_options = LoadOptions(password)
        
        # Create Parser instance
        with Parser(file_path, load_options) as parser:
            if extract_type == "text":
                # Extract text
                text_reader = parser.get_text()
                if text_reader:
                    return text_reader
                    
            elif extract_type == "metadata":
                # Extract metadata
                metadata = parser.get_metadata()
                if metadata:
                    result = {}
                    for item in metadata:
                        result[item.name] = item.value
                    return result
                    
            elif extract_type == "images":
                # Extract images
                images = parser.get_images()
                if images:
                    return list(images)
                    
    except Exception as e:
        print(f"Error: {e}")
        return None

# Extract text from protected PDF
text = extract_from_protected("protected.pdf", "password123", "text")