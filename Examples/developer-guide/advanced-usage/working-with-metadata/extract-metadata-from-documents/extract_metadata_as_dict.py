from groupdocs.parser import Parser

def extract_metadata_as_dict(file_path):
    """
    Extract document metadata as a dictionary.
    """
    with Parser(file_path) as parser:
        metadata = parser.get_metadata()
        
        if metadata is None:
            return None
        
        # Convert to dictionary
        metadata_dict = {}
        for item in metadata:
            metadata_dict[item.name] = item.value
        
        return metadata_dict

# Usage
metadata = extract_metadata_as_dict("report.pdf")

if metadata:
    print("Document Metadata:")
    for key, value in metadata.items():
        print(f"  {key}: {value}")
else:
    print("Metadata extraction not supported")