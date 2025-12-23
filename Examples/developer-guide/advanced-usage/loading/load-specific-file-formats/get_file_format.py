from groupdocs.parser import Parser
from groupdocs.parser.options import LoadOptions, FileFormat
import os

def get_file_format(file_path):
    """Detect file format based on extension"""
    
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    
    format_map = {
        '.md': FileFormat.MARKUP,
        '.markdown': FileFormat.MARKUP,
        '.mhtml': FileFormat.MHTML,
        '.mht': FileFormat.MHTML,
        '.otp': FileFormat.OTP,
    }
    
    return format_map.get(ext)

def load_document_with_format(file_path):
    """Load document with appropriate format specification"""
    
    file_format = get_file_format(file_path)
    
    if file_format:
        print(f"Loading with explicit format: {file_format}")
        load_options = LoadOptions(file_format)
        parser = Parser(file_path, load_options)
    else:
        print("Loading with auto-detection")
        parser = Parser(file_path)
    
    return parser

# Usage examples
with load_document_with_format("webpage.mhtml") as parser:
    text_reader = parser.get_text()
    if text_reader:
        print(text_reader)