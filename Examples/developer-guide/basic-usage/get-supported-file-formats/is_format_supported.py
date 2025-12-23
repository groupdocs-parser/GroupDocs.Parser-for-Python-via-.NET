from groupdocs.parser.options import FileType

def is_format_supported(extension):
    """Check if a file format is supported by GroupDocs.Parser"""
    supported_file_types = FileType.get_supported_file_types()
    
    for file_type in supported_file_types:
        if file_type.extension.lower() == extension.lower():
            return True
    return False

# Check various formats
formats_to_check = [".pdf", ".docx", ".xlsx", ".txt", ".unknown"]

for ext in formats_to_check:
    if is_format_supported(ext):
        print(f"{ext} - Supported")
    else:
        print(f"{ext} - Not Supported")