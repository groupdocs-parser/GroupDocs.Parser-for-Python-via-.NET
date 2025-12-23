from groupdocs.parser import Parser
from groupdocs.parser.options import LoadOptions

def check_if_protected(file_path):
    """Check if a document is password-protected"""
    
    try:
        # Try to get file info without password
        file_info = Parser.get_file_info(file_path)
        
        # Check if the document is encrypted
        if hasattr(file_info, 'is_encrypted') and file_info.is_encrypted:
            print("Document is password-protected")
            return True
        else:
            print("Document is not password-protected")
            return False
            
    except Exception as e:
        print(f"Error checking document: {e}")
        return None

# Check if document is protected
is_protected = check_if_protected("sample.pdf")

if is_protected:
    password = input("Enter password: ")
    load_options = LoadOptions(password)
    with Parser("./sample.pdf", load_options) as parser:
        text_reader = parser.get_text()
        if text_reader:
            print(text_reader)
else:
    with Parser("./sample.pdf") as parser:
        text_reader = parser.get_text()
        if text_reader:
            print(text_reader)